#!/usr/bin/env python3
"""Proxy de prioridade de estudo do COFEN 2026 (Cargo 407) — não é previsão binária.

Combina a frequência oficial no acervo (Quadrix ×2, demais bancas ×1), a aderência
alta e uma penalidade para âncoras geradas (COFEN_ANCORA / ancora_*). Enquanto o
acervo for pequeno, o score é misturado com a faixa-base do perfil
(`cargos/tic/perfil.md` → Prioridades do P3). Saída: ranking + faixa (alta/média/baixa).

Uso (raiz do repo):
  python3 tools/acervo_previsao.py            # imprime
  python3 tools/acervo_previsao.py --write    # grava acervo/previsao-cofen.md
"""
from __future__ import annotations

import argparse
import datetime as dt
import math
import pathlib
import re
import sys
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import acervo_cobertura as ac  # noqa: E402

ROOT = ac.ROOT
OUT = ROOT / "acervo" / "previsao-cofen.md"
ANCORA_RE = re.compile(r"(?i)ancora_|COFEN_ANCORA")
PESO_BANCA = {"quadrix": 2.0}

# Faixa-base pelo perfil (usada sozinha sem acervo; misturada quando há acervo).
BASE = {
    "esp.tic.contratos": 3, "esp.tic.govti": 3, "esp.tic.gestao": 3, "esp.tic.seguranca": 3,
    "esp.tic.redes": 3, "esp.tic.auditoria": 3,
    "esp.tic.fundamentos": 2, "esp.tic.bd": 2, "esp.tic.infra": 2, "esp.tic.etica": 2,
    "esp.tic.engsw": 1, "esp.tic.atendimento": 1,
    "basicos.lp": 3, "basicos.rlm": 2, "basicos.ingles": 2,
    "comp.leg.enfermagem": 3, "comp.leg.licitacoes": 3, "comp.adm": 3,
    "comp.leg.lgpd": 2, "comp.const": 2, "comp.leg.cf": 2, "comp.leg.improbidade": 2,
    "comp.leg.processo": 2, "comp.leg.anticorrupcao": 1,
    "disc.tic": 3,
}
# Quantas assertivas oficiais por tag para o acervo pesar tanto quanto a faixa-base.
ACERVO_PLENO = 30


def is_ancora(path: pathlib.Path, fm: dict) -> bool:
    return bool(ANCORA_RE.search(path.name)) or str(fm.get("orgao") or "") == "COFEN_ANCORA"


def collect(cat_bancas: dict[str, str]):
    stats = defaultdict(lambda: {"oficial": 0, "ancora": 0, "peso": 0.0, "alta": 0,
                                 "por_banca": defaultdict(int)})
    for path, fm, body in ac.iter_itens():
        tags = [t for t in dict.fromkeys(fm.get("tags_edital") or []) if isinstance(t, str)]
        if not tags:
            continue
        n = ac.count_assertivas(body)
        units = n if n > 0 else 1
        banca = ac.infer_banca(fm, cat_bancas)
        w = PESO_BANCA.get(banca, 1.0)
        alta = (fm.get("aderencia") or "").strip().lower() == "alta"
        anc = is_ancora(path, fm)
        for tag in tags:
            s = stats[tag]
            if anc:
                s["ancora"] += units
            else:
                s["oficial"] += units
                s["peso"] += units * w
                s["por_banca"][banca] += units
                if alta:
                    s["alta"] += units
    return stats


def base_de(tag: str) -> int:
    for pref, v in BASE.items():
        if tag == pref or tag.startswith(pref + "."):
            return v
    return 2


def score_tag(tag: str, s: dict) -> float:
    oficial = s["oficial"]
    alta_ratio = s["alta"] / oficial if oficial else 0.0
    acervo = math.log1p(s["peso"]) * (0.6 + 0.4 * alta_ratio) + 0.2 * math.log1p(s["ancora"])
    peso_acervo = min(1.0, oficial / ACERVO_PLENO)
    base = base_de(tag)
    # base 1..3 → mesma escala aproximada de log1p(peso) com acervo pleno (~4)
    return round((1 - peso_acervo) * base * 1.35 + peso_acervo * acervo, 4)


def rows_bloco(tags: list[str], stats) -> list[dict]:
    rows = [{"tag": t, "score": score_tag(t, stats[t]), "oficial": stats[t]["oficial"],
             "ancora": stats[t]["ancora"],
             "bancas": ", ".join(f"{k}:{v}" for k, v in sorted(stats[t]["por_banca"].items())) or "—"}
            for t in tags]
    ordered = sorted(rows, key=lambda r: (-r["score"], r["tag"]))
    n = len(ordered)
    i_alta, i_media = max(1, (n + 2) // 3), max(2, (2 * n + 2) // 3)
    for i, r in enumerate(ordered):
        r["faixa"] = "alta" if i < i_alta else "média" if i < i_media else "baixa"
        if i and r["score"] == ordered[i - 1]["score"]:
            r["faixa"] = ordered[i - 1]["faixa"]  # empate: mesma faixa
        r["rank"] = i + 1
    return ordered


def proxy_scores() -> dict[str, dict]:
    """tag → {score, faixa, oficial}. Usado por acervo_sugestao_hoje.py."""
    stats = collect(ac.load_catalog_bancas())
    mapa = ac.tags_from_mapa(ac.MAPA)
    out = {}
    for pref in ("basicos.", "comp.", "esp.tic.", "disc."):
        for r in rows_bloco([t for t in mapa if t.startswith(pref)], stats):
            out[r["tag"]] = r
    return out


def render(stats, mapa: list[str]) -> str:
    hoje = dt.date.today().isoformat()
    total = sum(s["oficial"] for s in stats.values())
    lines = [
        "# Prioridade de estudo — COFEN 2026 · Cargo 407",
        "",
        f"Gerado por `tools/acervo_previsao.py` em **{hoje}** · {total} assertivas oficiais etiquetadas.",
        "",
        "Score = mistura da faixa-base do perfil com a frequência no acervo (Quadrix ×2, demais ×1),",
        f"o acervo pesa mais à medida que a tag se aproxima de {ACERVO_PLENO} assertivas oficiais.",
        "Faixa = tercil dentro do bloco. **Ranking de estudo, não probabilidade de cair na prova.**",
        "",
    ]
    for nome, pref in (("P1 Básicos", "basicos."), ("P2 Complementares", "comp."),
                       ("P3 Específicos", "esp.tic."), ("Discursiva", "disc.")):
        rows = rows_bloco([t for t in mapa if t.startswith(pref)], stats)
        if not rows:
            continue
        lines += [f"## {nome}", "", "| # | Tag | Faixa | Score | Oficiais | Âncoras | Bancas |",
                  "|---|-----|-------|-------|----------|---------|--------|"]
        for r in rows:
            lines.append(f"| {r['rank']} | `{r['tag']}` | {r['faixa']} | {r['score']:.2f} | "
                         f"{r['oficial']} | {r['ancora']} | {r['bancas']} |")
        lines.append("")
    lines += ["## Como atualizar", "", "```bash", "python3 tools/acervo_cobertura.py --write",
              "python3 tools/acervo_previsao.py --write", "```", ""]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="grava acervo/previsao-cofen.md")
    a = ap.parse_args()
    stats = collect(ac.load_catalog_bancas())
    md = render(stats, ac.tags_from_mapa(ac.MAPA))
    if a.write:
        OUT.write_text(md, encoding="utf-8", newline="\n")
        print(f"Escrito {OUT.relative_to(ROOT)}")
    else:
        print(md)


if __name__ == "__main__":
    main()
