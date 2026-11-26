#!/usr/bin/env python3
"""Heatmap de cobertura do acervo × mapa do Cargo 407 (P1–P4).

Lê `acervo/itens/*.md`, conta assertivas por tag e banca, compara com os mapas
e opcionalmente atualiza blocos de cobertura em `catalogo.yaml`.

Uso (raiz do repo):
  python3 tools/acervo_cobertura.py              # imprime resumo
  python3 tools/acervo_cobertura.py --write       # grava acervo/cobertura-edital.md
  python3 tools/acervo_cobertura.py --write --write-catalogo
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("Precisa de PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = pathlib.Path(__file__).resolve().parent.parent
ITENS = ROOT / "acervo" / "itens"
CATALOGO = ROOT / "acervo" / "catalogo.yaml"
OUT_MD = ROOT / "acervo" / "cobertura-edital.md"
MAPA = ROOT / "cargos" / "tic" / "mapa-edital.md"

PESO = {"quadrix": 2.0}  # demais bancas: 1.0
SKIP_NAMES = {"_SCHEMA.exemplo.md"}
SKIP_SUBSTR = ("_GABARITO",)

TAG_RE = re.compile(r"`((?:basicos|comp|disc|esp\.tic)\.[a-z0-9_.]+)`")
ASSERT_RE = re.compile(r"^\|\s*\d+\s*\|")
FM_SPLIT = re.compile(r"^---\s*$", re.M)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    text = text.replace("\r\n", "\n")
    if not text.startswith("---"):
        return {}, text
    parts = FM_SPLIT.split(text, maxsplit=2)
    if len(parts) < 3:
        return {}, text
    data = yaml.safe_load(parts[1]) or {}
    if not isinstance(data, dict):
        data = {}
    return data, parts[2]


def count_assertivas(body: str) -> int:
    return sum(1 for line in body.splitlines() if ASSERT_RE.match(line))


def tags_from_mapa(path: pathlib.Path) -> list[str]:
    if not path.exists():
        return []
    found = TAG_RE.findall(path.read_text(encoding="utf-8"))
    # preserve order, unique
    out, seen = [], set()
    for t in found:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def infer_banca(fm: dict, cat_by_pasta: dict[str, str]) -> str:
    b = (fm.get("banca") or "").strip().lower()
    if b:
        return b
    fonte = fm.get("fonte") or {}
    path = ""
    if isinstance(fonte, dict):
        path = str(fonte.get("path") or "")
    # acervo/fontes/{pasta}/...
    m = re.match(r"acervo/fontes/([^/]+)/", path.replace("\\", "/"))
    if m and m.group(1) in cat_by_pasta:
        return cat_by_pasta[m.group(1)]
    return "quadrix"


def load_catalog_bancas() -> dict[str, str]:
    if not CATALOGO.exists():
        return {}
    cat = yaml.safe_load(CATALOGO.read_text(encoding="utf-8")) or {}
    out = {}
    for f in cat.get("fontes") or []:
        pasta = (f.get("pasta") or "").rstrip("/")
        slug = pasta.split("/")[-1] if pasta else ""
        banca = (f.get("banca") or "quadrix").strip().lower()
        if slug:
            out[slug] = banca
    return out


def iter_itens():
    for p in sorted(ITENS.glob("*.md")):
        if p.name in SKIP_NAMES or any(s in p.name for s in SKIP_SUBSTR):
            continue
        text = p.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        yield p, fm, body


def collect(cat_bancas: dict[str, str]):
    """Returns stats[tag] = {itens, aderencia_alta, peso, por_banca, arquivos}"""
    stats = defaultdict(lambda: {
        "itens": 0,
        "aderencia_alta": 0,
        "peso": 0.0,
        "por_banca": defaultdict(int),
        "arquivos": 0,
    })
    arquivos = 0
    for path, fm, body in iter_itens():
        arquivos += 1
        tags = list(dict.fromkeys(fm.get("tags_edital") or []))
        tags = [t for t in tags if isinstance(t, str)]
        n = count_assertivas(body)
        # discursiva / bloco sem tabela: conta 1 unidade por arquivo
        units = n if n > 0 else 1
        alta = (fm.get("aderencia") or "").strip().lower() == "alta"
        banca = infer_banca(fm, cat_bancas)
        w = PESO.get(banca, 1.0)
        if not tags:
            continue
        for tag in tags:
            s = stats[tag]
            s["itens"] += units
            s["arquivos"] += 1
            if alta:
                s["aderencia_alta"] += units
            s["peso"] += units * w
            s["por_banca"][banca] += units
    return stats, arquivos


def bucket(tag: str) -> str | None:
    if tag.startswith("basicos."):
        return "basicos"
    if tag.startswith("comp."):
        return "comp"
    if tag.startswith("disc."):
        return "disc"
    if tag.startswith("esp.tic."):
        return "especificos"
    return None


def coverage_block(tags: list[str], stats) -> dict:
    block = {}
    for tag in tags:
        s = stats.get(tag) or {"itens": 0, "aderencia_alta": 0}
        block[tag] = {"itens": int(s["itens"]), "aderencia_alta": int(s["aderencia_alta"])}
    return block


def render_md(stats, mapas: dict[str, list[str]], n_arquivos: int) -> str:
    hoje = dt.date.today().isoformat()
    lines = [
        "# Cobertura do acervo × edital",
        "",
        f"Gerado por `tools/acervo_cobertura.py` em **{hoje}** · {n_arquivos} arquivos em `acervo/itens/`.",
        "",
        "Contagem: **assertivas** na tabela do item (ou 1 se discursiva/sem tabela). "
        "Peso heatmap: Quadrix×2, demais bancas×1.",
        "",
        "## Metas (plano)",
        "",
        "| Bloco | Meta assertivas/tag |",
        "|-------|---------------------|",
        "| P1 `basicos.*` | ≥15 |",
        "| P2 `comp.*` | ≥12 |",
        "| P3 `esp.tic.*` | ≥10 |",
        "| Discursiva `disc.*` | ≥8 arquivos/tag |",
        "",
    ]

    metas = {"basicos": 15, "comp": 12, "especificos": 10, "disc": 8}

    for nome, tags in mapas.items():
        meta = metas.get(nome, 10)
        lines += [f"## {nome}", "", "| Tag | Assertivas | Alta | Peso | Bancas | Gap |",
                  "|-----|------------|------|------|--------|-----|"]
        ranking = []
        for tag in tags:
            s = stats.get(tag) or {
                "itens": 0, "aderencia_alta": 0, "peso": 0.0, "por_banca": {},
            }
            gap = max(0, meta - int(s["itens"]))
            bancas = ", ".join(f"{k}:{v}" for k, v in sorted(s["por_banca"].items())) or "—"
            ranking.append((s["peso"], tag, s, gap, bancas))
            flag = "🔴" if gap == meta else ("🟡" if gap else "🟢")
            lines.append(
                f"| `{tag}` | {s['itens']} | {s['aderencia_alta']} | {s['peso']:.0f} | {bancas} | {flag} {gap or 'ok'} |"
            )
        lines.append("")
        top = sorted(ranking, key=lambda x: -x[0])[:8]
        if any(t[0] > 0 for t in top):
            lines += ["### Heatmap (top peso)", ""]
            for peso, tag, s, gap, _ in top:
                if peso <= 0:
                    continue
                lines.append(f"- `{tag}` — peso {peso:.0f} ({s['itens']} assertivas)")
            lines.append("")

    # tags órfãs (no acervo, fora do mapa)
    known = set()
    for tags in mapas.values():
        known.update(tags)
    orphans = sorted(t for t in stats if t not in known)
    if orphans:
        lines += ["## Tags no acervo fora do mapa", ""]
        for t in orphans:
            lines.append(f"- `{t}` ({stats[t]['itens']})")
        lines.append("")

    lines += [
        "## Como atualizar",
        "",
        "```bash",
        "python3 tools/acervo_cobertura.py --write",
        "python3 tools/acervo_cobertura.py --write --write-catalogo",
        "```",
        "",
    ]
    return "\n".join(lines)


def replace_catalogo_blocks(blocks: dict[str, dict]) -> None:
    """Substitui/insere blocos YAML de cobertura antes de `fontes:`."""
    if not CATALOGO.exists():
        CATALOGO.write_text("atualizado: ''\nfontes:\n", encoding="utf-8", newline="\n")
    text = CATALOGO.read_text(encoding="utf-8")
    # Remove existing coverage keys (multi-line until next top-level key)
    keys = ["cobertura", "cobertura_basicos", "cobertura_comp", "cobertura_disc"]
    for key in keys:
        text = re.sub(
            rf"(?m)^{key}:\n(?:(?:[ \t].*|#.*)\n)*",
            "",
            text,
            count=1,
        )

    def dump_block(name: str, data: dict) -> str:
        lines = [f"{name}:"]
        for tag, vals in data.items():
            lines.append(f"  {tag}:")
            lines.append(f"    itens: {vals['itens']}")
            lines.append(f"    aderencia_alta: {vals['aderencia_alta']}")
        return "\n".join(lines) + "\n"

    chunk = "".join(dump_block(k, blocks[k]) for k in keys if k in blocks)
    # Insert before fontes:
    if re.search(r"(?m)^fontes:\s*$", text):
        text = re.sub(r"(?m)^fontes:\s*$", chunk + "fontes:", text, count=1)
    else:
        text = chunk + text

    # atualizado
    hoje = dt.date.today().isoformat()
    if re.search(r"(?m)^atualizado:", text):
        text = re.sub(r"(?m)^atualizado:.*$", f"atualizado: '{hoje}'", text, count=1)
    CATALOGO.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write", action="store_true", help=f"Grava {OUT_MD.relative_to(ROOT)}")
    ap.add_argument(
        "--write-catalogo",
        action="store_true",
        help="Atualiza blocos cobertura* em catalogo.yaml",
    )
    args = ap.parse_args()

    cat_bancas = load_catalog_bancas()
    stats, n_arq = collect(cat_bancas)

    mapa = tags_from_mapa(MAPA)
    mapas = {
        "basicos": [t for t in mapa if t.startswith("basicos.")],
        "comp": [t for t in mapa if t.startswith("comp.")],
        "especificos": [t for t in mapa if t.startswith("esp.tic.")],
        "disc": [t for t in mapa if t.startswith("disc.")],
    }

    md = render_md(stats, mapas, n_arq)
    if args.write:
        OUT_MD.write_text(md, encoding="utf-8", newline="\n")
        print(f"Escrito {OUT_MD.relative_to(ROOT)}")
    else:
        print(md)

    if args.write_catalogo:
        blocks = {
            "cobertura": coverage_block(mapas["especificos"], stats),
            "cobertura_basicos": coverage_block(mapas["basicos"], stats),
            "cobertura_comp": coverage_block(mapas["comp"], stats),
            "cobertura_disc": coverage_block(mapas["disc"], stats),
        }
        replace_catalogo_blocks(blocks)
        print(f"Atualizado {CATALOGO.relative_to(ROOT)} (blocos cobertura*)")

    # resumo gaps
    print("--- gaps (meta) ---")
    for nome, meta in [("basicos", 15), ("comp", 12), ("especificos", 10), ("disc", 8)]:
        zeros = [t for t in mapas[nome] if stats.get(t, {}).get("itens", 0) == 0]
        baixos = [
            t
            for t in mapas[nome]
            if 0 < stats.get(t, {}).get("itens", 0) < meta
        ]
        print(f"{nome}: zero={len(zeros)} abaixo_meta={len(baixos)}")


if __name__ == "__main__":
    main()
