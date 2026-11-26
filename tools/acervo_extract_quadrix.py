#!/usr/bin/env python3
"""Extrai itens C/E Quadrix (prova + gabarito) → Markdown do schema do acervo.

Uso (raiz do repo):
  python3 tools/acervo_extract_quadrix.py \\
    --prova acervo/fontes/.../prova.pdf \\
    --gabarito acervo/fontes/.../gabarito.pdf \\
    --out acervo/itens/orgao_ano_slug.md \\
    --id orgao_ano_slug --orgao ORGAO --ano 2024 --cargo '...' \\
    --tags esp.tic.contratos,comp.leg.licitacoes \\
    [--prova-num P2|P3] [--aderencia media]

Requer pdftotext (poppler). Herdado do extrator Cebraspe do CGU: conferir o resultado na primeira prova Quadrix (numeração e gabarito) e ajustar o parse se preciso. Layout de 2 colunas: tenta separar e ordenar por nº do item.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys
import textwrap

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore


def pdftotext(path: pathlib.Path, layout: bool = True) -> str:
    cmd = ["pdftotext"]
    if layout:
        cmd.append("-layout")
    cmd += [str(path), "-"]
    out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
    return out.decode("utf-8", errors="replace")


def parse_gabarito(text: str) -> dict[int, str]:
    """Aceita padrões Item\\nGabarito e linhas 'N\\nC|E|X'."""
    gab: dict[int, str] = {}
    pairs = re.findall(r"(?m)^(\d{1,3})\s*\n([CEX])\s*$", text)
    for n, g in pairs:
        gab[int(n)] = g
    if len(gab) >= 10:
        return gab
    for m in re.finditer(r"(?m)\b(\d{1,3})\s+([CEX])\b", text):
        gab[int(m.group(1))] = m.group(2)
    return gab


def split_columns(page: str) -> tuple[str, str]:
    """Split a layout page into left/right streams.

    Right-only lines (first glyph past mid) must keep the item number intact:
    cutting the gap after ``93`` used to drop IDs and leave placeholders.
    """
    lines = page.splitlines()
    if not lines:
        return "", ""
    widths = [len(l.rstrip()) for l in lines if l.strip()]
    if not widths:
        return page, ""
    mid = max(40, max(widths) // 2)
    left, right = [], []
    for line in lines:
        first = next((i for i, c in enumerate(line) if c != " "), None)
        if first is None:
            left.append("")
            right.append("")
            continue
        # Content starts on the right half → whole line is right column
        if first >= mid - 10:
            left.append("")
            right.append(line.strip())
            continue
        # Prefer longest gap whose center is near mid (true 2-col lines)
        candidates = []
        for m in re.finditer(r" {3,}", line):
            center = (m.start() + m.end()) / 2
            if abs(center - mid) <= max(25, mid * 0.3):
                candidates.append((m.end() - m.start(), m.start(), m.end()))
        if candidates:
            candidates.sort(reverse=True)
            _, a, b = candidates[0]
            lpart, rpart = line[:a].rstrip(), line[b:].strip()
            # Orphaned bare number on left belongs with the right body
            if re.fullmatch(r"\d{1,3}", lpart.strip()) and rpart:
                left.append("")
                right.append(f"{lpart.strip()}   {rpart}")
            else:
                left.append(lpart)
                right.append(rpart)
        elif len(line) > mid and line[mid:].strip():
            left.append(line[:mid].rstrip())
            right.append(line[mid:].strip())
        else:
            left.append(line.rstrip())
            right.append("")
    return "\n".join(left), "\n".join(right)


def extract_items_from_stream(stream: str) -> dict[int, str]:
    stream = stream.replace("\r\n", "\n")
    parts = re.split(r"(?m)(?=^\d{1,3}(?:\s|$))", stream)
    items: dict[int, str] = {}
    for part in parts:
        part = part.strip()
        if not part:
            continue
        m = re.match(r"^(\d{1,3})(?:\s+|$)(.*)$", part, re.S)
        if not m:
            continue
        n = int(m.group(1))
        if n < 1 or n > 200:
            continue
        body = m.group(2)
        body = re.split(r"(?m)^(?:CEBRASPE|Espaço livre|--\s*PROVA)", body)[0]
        body = re.sub(r"\s+", " ", body).strip()
        if len(body) < 8:
            continue
        if n not in items or len(body) > len(items[n]):
            items[n] = body
    return items


def extract_items_layout(text: str) -> dict[int, str]:
    pages = text.split("\f")
    merged: dict[int, str] = {}
    for page in pages:
        left, right = split_columns(page)
        for stream in (left, right, page):
            for n, body in extract_items_from_stream(stream).items():
                if n not in merged or len(body) > len(merged[n]):
                    merged[n] = body
    return merged


def extract_items_raw(text: str) -> dict[int, str]:
    return extract_items_from_stream(text)


def render_md(
    *,
    item_id: str,
    orgao: str,
    ano: int,
    cargo: str,
    prova: str,
    banca: str,
    tags: list[str],
    tags_infra: list[str],
    aderencia: str,
    prova_path: str,
    gab_path: str,
    items: dict[int, str],
    gab: dict[int, str],
    nota: str,
) -> str:
    fm: dict = {
        "id": item_id,
        "orgao": orgao,
        "ano": ano,
        "banca": banca,
        "cargo": cargo,
        "prova": prova,
        "formato": "certo_errado",
        "tags_edital": tags,
        "aderencia": aderencia,
        "fonte": {
            "path": prova_path,
            "gabarito": gab_path,
            "nota": nota,
        },
    }
    if tags_infra:
        fm["tags_edital"] = tags_infra
    if yaml:
        front = yaml.dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False)
    else:
        front = textwrap.dedent(
            f"""\
            id: {item_id}
            orgao: {orgao}
            ano: {ano}
            banca: {banca}
            cargo: {cargo}
            prova: {prova}
            formato: certo_errado
            tags_edital: {tags}
            aderencia: {aderencia}
            fonte:
              path: {prova_path}
              gabarito: {gab_path}
              nota: {nota!r}
            """
        )
    rows = []
    missing = []
    for n in sorted(set(gab.keys()) | set(items.keys())):
        if n not in gab:
            continue
        g = gab[n]
        texto = items.get(n, f"[texto não extraído automaticamente — ver PDF item {n}]")
        texto = texto.replace("|", "/").replace("\n", " ")
        rows.append(f"| {n} | {texto} | {g} |")
        if n not in items:
            missing.append(n)
    body = "\n".join(
        [
            "## Comando",
            "",
            "Itens extraídos automaticamente do caderno Quadrix (revisar redação junto ao PDF se necessário).",
            "",
            "## Assertivas",
            "",
            "| id | texto | gabarito |",
            "|----|-------|----------|",
            *rows,
            "",
        ]
    )
    if missing:
        body += f"\n<!-- extração incompleta: itens sem texto {missing} -->\n"
    return f"---\n{front}---\n\n{body}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prova", type=pathlib.Path, required=True)
    ap.add_argument("--gabarito", type=pathlib.Path, required=True)
    ap.add_argument("--out", type=pathlib.Path, required=True)
    ap.add_argument("--id", required=True)
    ap.add_argument("--orgao", required=True)
    ap.add_argument("--ano", type=int, required=True)
    ap.add_argument("--cargo", required=True)
    ap.add_argument("--tags", default="", help="tags_edital separadas por vírgula")
    ap.add_argument("--tags-infra", default="", dest="tags_infra")
    ap.add_argument("--prova-num", default="P3", dest="prova_num")
    ap.add_argument("--aderencia", default="media")
    ap.add_argument("--banca", default="quadrix")
    ap.add_argument("--nota", default="Extração automática Quadrix; validar contra PDF.")
    args = ap.parse_args()

    gab_text = pdftotext(args.gabarito, layout=False)
    gab = parse_gabarito(gab_text)
    if len(gab) < 5:
        print(f"Gabarito fraco: {len(gab)} itens", file=sys.stderr)
        return 1

    layout = pdftotext(args.prova, layout=True)
    raw = pdftotext(args.prova, layout=False)
    items = extract_items_layout(layout)
    raw_items = extract_items_raw(raw)
    for n, body in raw_items.items():
        if n not in items or len(body) > len(items[n]):
            items[n] = body

    items = {n: t for n, t in items.items() if n in gab}

    tags = [t.strip() for t in args.tags.split(",") if t.strip()]
    tags_infra = [t.strip() for t in args.tags_infra.split(",") if t.strip()]
    root = pathlib.Path(__file__).resolve().parent.parent

    def rel(p: pathlib.Path) -> str:
        try:
            return str(p.resolve().relative_to(root))
        except ValueError:
            return str(p)

    md = render_md(
        item_id=args.id,
        orgao=args.orgao,
        ano=args.ano,
        cargo=args.cargo,
        prova=args.prova_num,
        banca=args.banca,
        tags=tags,
        tags_infra=tags_infra,
        aderencia=args.aderencia,
        prova_path=rel(args.prova),
        gab_path=rel(args.gabarito),
        items=items,
        gab=gab,
        nota=args.nota,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(md, encoding="utf-8")
    cov = len(items)
    missing = sorted(set(gab) - set(items))
    print(f"OK {args.out}: gabarito={len(gab)} texto={cov} faltando_texto={missing[:30]}")
    return 0 if cov >= len(gab) * 0.7 else 2


if __name__ == "__main__":
    sys.exit(main())
