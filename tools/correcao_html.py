#!/usr/bin/env python3
"""Gera correcao.html ao lado de correcao.md (qualquer discursiva: curta ou a de prova).

Uso (da raiz do repositório):
    python3 tools/correcao_html.py <pasta em $P/respostas/> [--gerado <pasta do caderno>] [--out arquivo]

- Obrigatório: <pasta>/correcao.md. Opcionais: resposta.md e imagens (manuscrito-*.png/jpg)
  na mesma pasta; enunciado (discursiva.md) e padrão (discursiva-padrao-resposta.md) na
  pasta do caderno.
- Sem --gerado, a pasta do caderno é procurada nos caminhos `…simulados/gerados/…` citados
  no correcao.md; o padrão também é procurado nas pastas-mãe (simulado com q1/ e q2/).
- O correcao.md é renderizado inteiro (títulos, tabelas, listas); NC, NE, TL e NQ viram
  destaques quando forem encontrados. Só stdlib.
"""
import argparse
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


# ---------- Markdown mínimo ----------
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
    s = re.sub(r'(?<!["=>])(https?://[^\s<)]+)', r'<a href="\1" target="_blank" rel="noopener">\1</a>', s)
    return s


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def md(text):
    lines = text.replace("\r\n", "\n").split("\n")
    out, i, para = [], 0, []

    def flush():
        if para:
            out.append("<p>" + "<br>".join(inline(l) for l in para) + "</p>")
            para.clear()

    while i < len(lines):
        l = lines[i]
        s = l.strip()
        if s.startswith("```"):
            flush()
            j = i + 1
            buf = []
            while j < len(lines) and not lines[j].strip().startswith("```"):
                buf.append(lines[j])
                j += 1
            out.append("<pre><code>" + html.escape("\n".join(buf)) + "</code></pre>")
            i = j + 1
            continue
        if not s:
            flush()
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            flush()
            n = min(len(m.group(1)) + 1, 6)
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
            i += 1
            continue
        if re.match(r"^(-{3,}|\*{3,})$", s):
            flush()
            out.append("<hr>")
            i += 1
            continue
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?\s*:?-{2,}", lines[i + 1].strip()):
            flush()
            head = cells(s)
            j = i + 2
            rows = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                rows.append(cells(lines[j]))
                j += 1
            th = "".join(f"<th>{inline(c)}</th>" for c in head)
            tb = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
            out.append(f'<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>')
            i = j
            continue
        if re.match(r"^([-*]|\d+\.)\s+", s):
            flush()
            ordered = bool(re.match(r"^\d+\.", s))
            tag = "ol" if ordered else "ul"
            items = []
            j = i
            while j < len(lines):
                t = lines[j]
                ts = t.strip()
                if re.match(r"^([-*]|\d+\.)\s+", ts) and (len(t) - len(t.lstrip())) < 2:
                    items.append(re.sub(r"^([-*]|\d+\.)\s+", "", ts))
                elif ts and (t.startswith("  ") or t.startswith("\t")) and items:
                    items[-1] += " " + ts
                else:
                    break
                j += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            i = j
            continue
        if s.startswith(">"):
            flush()
            buf = []
            j = i
            while j < len(lines) and lines[j].strip().startswith(">"):
                buf.append(lines[j].strip()[1:].strip())
                j += 1
            out.append("<blockquote>" + md("\n".join(buf)) + "</blockquote>")
            i = j
            continue
        para.append(s)
        i += 1
    flush()
    return "\n".join(out)


# ---------- dados ----------
NUM = r"(\d+(?:,\d+)?)"


def plain(s):
    return re.sub(r"[*`]", "", s)


def metric(text, key):
    """Valor de NC/NE/TL/NQ: linha de tabela cujo 1º campo começa pela chave, ou 'KEY = x'."""
    keyre = rf"^{key}\d?\b"
    for l in text.splitlines():
        if l.strip().startswith("|"):
            c = [plain(x).strip() for x in cells(l)]
            if c and re.match(keyre, c[0]):
                vals = [x for x in c[1:] if re.search(r"\d", x)]
                if vals:
                    v = vals[-1]
                    m = re.search(rf"≈?\s*{NUM}(\s*/\s*{NUM})?", v)
                    if m:
                        return m.group(0).strip()
    t = plain(text)
    if key in ("NE", "TL"):
        m = re.search(rf"\b{key}\s*(?:=|:)\s*(\d+)(?![\d,])", t) or re.search(rf"\b{key}\s+(\d+)(?![\d,])", t)
        return m.group(1) if m else None
    m = None
    for m in re.finditer(rf"\b{key}\d?\s*(?:=|≈|:)\s*([^\n·|]+)", t):
        pass
    if m:
        seg = m.group(1)
        allm = list(re.finditer(rf"≈?\s*{NUM}(\s*/\s*{NUM})?", seg))
        if allm:
            return allm[-1].group(0).strip()
    return None


def find_gerado(corr, resp_dir):
    for p in re.findall(r"`([^`]*simulados/gerados/[^`]*)`", corr):
        p = p.replace("…", "").strip().lstrip("/")
        cands = [ROOT / p]
        parts = resp_dir.resolve().parts
        if "pessoal" in parts:
            pdir = Path(*parts[: parts.index("pessoal") + 2])
            cands.append(pdir / p)
            m = re.search(r"simulados/gerados/.*", p)
            if m:
                cands.append(pdir / m.group(0))
        for c in cands:
            if c.suffix and c.is_file():
                c = c.parent
            if c.is_dir() and "gerados" in c.parts and c.name != "gerados":
                return c
    return None


def up_find(start, name, levels=2):
    d = start
    for _ in range(levels + 1):
        f = d / name
        if f.is_file():
            return f
        d = d.parent
    return None


def answer_html(text):
    body = []
    for l in text.splitlines():
        if l.startswith("#"):
            body.append(f"<h4>{inline(l.lstrip('#').strip())}</h4>")
        elif l.strip():
            body.append(f"<p>{html.escape(l)}</p>")
    return "\n".join(body)


CSS = """
:root{--bg:#f6f7f9;--surf:#fff;--ink:#1c2430;--muted:#5d6876;--line:#dfe3e8;--acc:#2f5fb3;--code:#eef1f5}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0f141a;--surf:#171e26;--ink:#e3e8ee;--muted:#93a0ae;--line:#2a3440;--acc:#7fa8f0;--code:#1f2832}}
:root[data-theme="dark"]{--bg:#0f141a;--surf:#171e26;--ink:#e3e8ee;--muted:#93a0ae;--line:#2a3440;--acc:#7fa8f0;--code:#1f2832}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:900px;margin:0 auto;padding:24px 16px 64px}
h1{font-size:1.4rem;line-height:1.25;margin:.2rem 0 .6rem}
h2{font-size:1.4rem;line-height:1.25;margin:.2rem 0 .6rem}
h3{font-size:1.12rem;margin:1.6rem 0 .5rem;padding-top:.8rem;border-top:1px solid var(--line)}
h4,h5{font-size:1rem;margin:1.1rem 0 .4rem}
.eyebrow{color:var(--muted);font-size:.85rem}
code{background:var(--code);padding:.05em .35em;border-radius:4px;font-size:.9em;word-break:break-word}
pre{background:var(--code);padding:10px;border-radius:8px;overflow-x:auto}
pre code{background:none;padding:0}
a{color:var(--acc);word-break:break-word}
hr{border:0;border-top:1px solid var(--line);margin:1.2rem 0}
blockquote{margin:.6rem 0;padding:.2rem 12px;border-left:3px solid var(--line);color:var(--muted)}
.tiles{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:14px 0 18px}
.tile{background:var(--surf);border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.tile .k{color:var(--muted);font-size:.78rem;text-transform:uppercase;letter-spacing:.04em}
.tile .v{font-size:1.35rem;font-weight:650;font-variant-numeric:tabular-nums}
.card{background:var(--surf);border:1px solid var(--line);border-radius:12px;padding:16px;margin:0 0 16px}
details.card>summary{cursor:pointer;font-weight:600}
.resp p{margin:.25rem 0;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.92rem;white-space:pre-wrap}
.tbl{overflow-x:auto;margin:.6rem 0}
table{border-collapse:collapse;width:100%;font-size:.93rem}
th,td{border-bottom:1px solid var(--line);padding:7px 8px;text-align:left;vertical-align:top}
th{color:var(--muted);font-weight:600}
li{margin:.3rem 0}
img{max-width:100%;border:1px solid var(--line);border-radius:8px;margin:6px 0}
.theme{float:right;background:var(--surf);color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:4px 10px;cursor:pointer;font:inherit;font-size:.85rem}
@media (max-width:620px){.tiles{grid-template-columns:repeat(2,1fr)}}
"""

JS = """(function(){var r=document.documentElement,k="cofen-correcao-tema";try{var t=localStorage.getItem(k);if(t)r.dataset.theme=t}catch(e){}
document.getElementById("th").onclick=function(){var d=r.dataset.theme||(matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light");r.dataset.theme=d==="dark"?"light":"dark";try{localStorage.setItem(k,r.dataset.theme)}catch(e){}};})();"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("respostas", type=Path)
    ap.add_argument("--gerado", type=Path)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()

    rd = a.respostas
    cf = rd / "correcao.md"
    if not cf.is_file():
        sys.exit(f"erro: {cf} não existe")
    corr = cf.read_text(encoding="utf-8")
    title_m = re.search(r"^# (.+)$", corr, re.M)
    title = title_m.group(1).strip() if title_m else rd.name
    body_md = corr.replace(title_m.group(0), "", 1) if title_m else corr

    parts = rd.resolve().parts
    pessoa = parts[parts.index("pessoal") + 1].capitalize() if "pessoal" in parts else ""

    gen = a.gerado or find_gerado(corr, rd)
    enun = padr = None
    if gen and gen.is_dir():
        enun = up_find(gen, "discursiva.md", 0) or up_find(gen, "enunciado.md", 0)
        padr = up_find(gen, "discursiva-padrao-resposta.md", 2)
    resp = rd / "resposta.md"
    imgs = sorted(p for p in rd.iterdir() if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"))

    tiles = []
    for key, lab in (("NQ", "Nota (NQ)"), ("NC", "NC"), ("NE", "NE"), ("TL", "TL")):
        v = metric(corr, key)
        if v:
            tiles.append(f'<div class="tile"><div class="k">{lab}</div><div class="v">{html.escape(v)}</div></div>')

    extras = []
    if enun:
        extras.append(f'<details class="card"><summary>Enunciado</summary>{md(enun.read_text(encoding="utf-8"))}</details>')
    if resp.is_file():
        extras.append(f'<details class="card"><summary>Sua resposta</summary><div class="resp">{answer_html(resp.read_text(encoding="utf-8"))}</div></details>')
    if imgs:
        extras.append('<details class="card"><summary>Folhas manuscritas</summary>'
                      + "".join(f'<img src="{html.escape(p.name)}" alt="{html.escape(p.stem)}" loading="lazy">' for p in imgs)
                      + "</details>")
    if padr:
        extras.append(f'<details class="card"><summary>Padrão de resposta</summary>{md(padr.read_text(encoding="utf-8"))}</details>')

    fontes = ["correcao.md"] + (["resposta.md"] if resp.is_file() else [])
    for f in (enun, padr):
        if f:
            try:
                fontes.append(str(f.resolve().relative_to(ROOT)))
            except ValueError:
                fontes.append(f.name)

    page = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Correção de discursiva</title>
<style>{CSS}</style></head>
<body><main>
<button class="theme" id="th" type="button">Tema</button>
<div class="eyebrow">COFEN 2026{' · ' + html.escape(pessoa) if pessoa else ''} · correção de discursiva</div>
<h1>{inline(title.replace('Correção — ', ''))}</h1>
{'<div class="tiles">' + ''.join(tiles) + '</div>' if tiles else ''}
<section class="card">{md(body_md)}</section>
{''.join(extras)}
<p class="eyebrow">Gerado por <code>tools/correcao_html.py</code> de {', '.join(f'<code>{html.escape(x)}</code>' for x in fontes)}. Fonte da verdade: <code>correcao.md</code>.</p>
</main><script>{JS}</script></body></html>
"""
    out = a.out or (rd / "correcao.html")
    out.write_text(page, encoding="utf-8")
    print("ok", out, "· destaques:", len(tiles), "· enunciado:", bool(enun), "· padrão:", bool(padr),
          "· resposta:", resp.is_file(), "· imagens:", len(imgs))


if __name__ == "__main__":
    main()
