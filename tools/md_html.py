#!/usr/bin/env python3
"""Gera a versão HTML de leitura de um arquivo Markdown (correção, fonte de áudio, roteiro).

Uso (da raiz do repositório):
    python3 tools/md_html.py <arquivo.md> [--out arquivo.html] [--eyebrow "texto"]

Grava <arquivo>.html ao lado do .md, com o mesmo visual de tools/correcao_html.py (tema
claro e escuro, tabelas, listas, código). O .md continua sendo a fonte: mudou o .md,
rodar de novo. Só stdlib.
"""
import argparse
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from correcao_html import CSS, JS, inline, md  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("arquivo", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--eyebrow")
    a = ap.parse_args()
    src = a.arquivo
    if not src.is_file():
        sys.exit(f"erro: {src} não existe")
    text = src.read_text(encoding="utf-8")
    m = re.search(r"^# (.+)$", text, re.M)
    title = m.group(1).strip() if m else src.stem
    body = text.replace(m.group(0), "", 1) if m else text
    parts = src.resolve().parts
    pessoa = parts[parts.index("pessoal") + 1].capitalize() if "pessoal" in parts else ""
    eyebrow = a.eyebrow or "COFEN 2026" + (f" · {pessoa}" if pessoa else "")
    page = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(re.sub(r"[*`]", "", title))[:80]}</title>
<style>{CSS}</style></head>
<body><main>
<button class="theme" id="th" type="button">Tema</button>
<div class="eyebrow">{html.escape(eyebrow)}</div>
<h1>{inline(title)}</h1>
<section class="card">{md(body)}</section>
<p class="eyebrow">Gerado por <code>tools/md_html.py</code> de <code>{html.escape(src.name)}</code>, que segue como fonte.</p>
</main><script>{JS}</script></body></html>
"""
    out = a.out or src.with_suffix(".html")
    out.write_text(page, encoding="utf-8")
    print("ok", out)


if __name__ == "__main__":
    main()
