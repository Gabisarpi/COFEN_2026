#!/usr/bin/env python3
"""Extrai provas Quadrix C/E (PDF) + gabarito definitivo → acervo/itens/<id>_bNN.md.

Lê o PDF com pdfplumber (posição de cada palavra), separa as duas colunas da página e
reconhece o número do item pela marca da Quadrix (algarismo em negrito, corpo ≥ 9,
no começo da linha). Os números de linha dos textos (corpo 7) e o rodapé são descartados.
Cada bloco de comando ("julgue os itens a seguir") vira um arquivo, com as próprias tags
(regras em `acervo_tags_407.py`), para o heatmap contar por assunto.

Uso (raiz do repo):
  python3 tools/acervo_extract_quadrix.py --id coren_pr_2024_analista_ti \\
    --orgao COREN-PR --ano 2024 --cargo "Analista de Tecnologia da Informação" \\
    --gab-cargo "ANALISTA DE TECNOLOGIA DA INFORMAÇÃO \\(CÓDIGO 402\\)" [--aderencia alta] [--dry]

Pasta esperada: acervo/fontes/<id>/prova.pdf e gabarito.pdf.
Divisão das partes: lida do gabarito ("Conhecimentos Básicos 1 a 40" …).
"""
from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys

import pdfplumber

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import acervo_tags_407 as tg  # noqa: E402
import yaml  # noqa: E402

AJUSTES = pathlib.Path(__file__).resolve().parent / "acervo_ajustes_quadrix.yaml"

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTES = ROOT / "acervo" / "fontes"
ITENS = ROOT / "acervo" / "itens"


# ------------------------------------------------------------------ gabarito

def ler_gabarito(pdf: pathlib.Path, cargo_re: str) -> tuple[dict[int, str], str, list[tuple[str, int, int]]]:
    txt = subprocess.check_output(["pdftotext", "-layout", str(pdf), "-"]).decode("utf-8", "replace")
    partes = []
    for nome, a, b in re.findall(r"Conhecimentos (Básicos|Complementares|Específicos)\s+(\d+) a (\d+)", txt):
        partes.append((nome.lower(), int(a), int(b)))
    m = re.search(cargo_re, txt)
    if not m:
        sys.exit(f"gabarito: cargo não encontrado ({cargo_re})")
    resto = txt[m.end():]
    prox = re.search(r"\n\s*2\.\d+\s+[A-ZÁÉÍÓÚÂÊÔÃÕÇ]", resto)
    sec = resto[: prox.start()] if prox else resto
    gab: dict[int, str] = {}
    linhas = [l for l in sec.splitlines() if l.strip()]
    for i in range(len(linhas) - 1):
        nums = linhas[i].split()
        if nums and all(x.isdigit() for x in nums):
            letras = linhas[i + 1].split()
            if len(letras) == len(nums) and all(x in "CEX" for x in letras):
                for n, g in zip(nums, letras):
                    gab[int(n)] = g
    notas = " ".join(l.strip() for l in linhas if re.match(r"\s*Ite(m|ns)\s+\d", l))
    return gab, notas, partes


# ------------------------------------------------------------------ prova

def linhas_pagina(page) -> list[dict]:
    """Linhas da página em ordem de leitura: colunas esquerda e direita, faixas de largura total."""
    W, H = page.width, page.height
    mid = W / 2
    todas = [w for w in page.extract_words(extra_attrs=["size", "fontname", "upright"], keep_blank_chars=False)
             if w["upright"] and 7.5 <= w["size"] <= 20 and 20 < w["top"] < H - 40]
    ws = [w for w in todas if w["size"] >= 8.5]
    # frações empilhadas (numerador sobre denominador, mesmo x): viram "n/d" na linha do texto
    dig = [w for w in todas if re.fullmatch(r"\d+", w["text"]) and "Bold" not in w["fontname"]]
    usados = set()
    for a_ in dig:
        for b_ in dig:
            if a_ is b_ or id(a_) in usados or id(b_) in usados:
                continue
            if abs(a_["x0"] - b_["x0"]) <= 3.5 and 8 <= b_["top"] - a_["top"] <= 15:
                lado_ = a_["x0"] >= mid - 3
                viz = [v for v in ws if v is not a_ and v is not b_ and (v["x0"] >= mid - 3) == lado_
                       and -1 <= a_["x0"] - v["x1"] <= 7 and -6 <= a_["top"] - v["top"] <= 20]
                if not viz:
                    continue
                v = min(viz, key=lambda v: (a_["x0"] - v["x1"], abs(a_["top"] - v["top"])))
                frac = dict(a_, text=f"{a_['text']}/{b_['text']}", top=v["top"], bottom=v["bottom"],
                            size=v["size"], fontname=v["fontname"])
                usados.add(id(a_)); usados.add(id(b_))
                ws = [w for w in ws if w is not a_ and w is not b_] + [frac]
    # palavras em fonte de código (Courier etc.) ficam alguns pt fora da linha: alinhar à palavra
    # de texto mais próxima na mesma coluna antes de agrupar
    corpo = [w for w in ws if "Courier" not in w["fontname"] and "Mono" not in w["fontname"]]
    for w in ws:
        if "Courier" in w["fontname"] or "Mono" in w["fontname"]:
            m = (w["top"] + w["bottom"]) / 2
            lado_w = w["x0"] >= mid - 3
            viz = [v for v in corpo if (v["x0"] >= mid - 3) == lado_w and abs((v["top"] + v["bottom"]) / 2 - m) < 5.5]
            if viz:
                v = min(viz, key=lambda v: (abs((v["top"] + v["bottom"]) / 2 - m), abs(v["x0"] - w["x0"])))
                w["top"], w["bottom"] = v["top"], v["bottom"]
    def agrupa(lista):
        lista = sorted(lista, key=lambda w: ((w["top"] + w["bottom"]) / 2, w["x0"]))
        gs, ms = [], []
        for w in lista:
            meio = (w["top"] + w["bottom"]) / 2
            tol = max(2.5, 0.4 * (w["bottom"] - w["top"]))
            if ms and abs(meio - ms[-1]) <= tol:
                gs[-1].append(w)
            else:
                gs.append([w]); ms.append(meio)
        return [(m, sorted(g, key=lambda w: w["x0"])) for m, g in zip(ms, gs)]

    L = agrupa([w for w in ws if w["x1"] <= mid + 3])
    R = agrupa([w for w in ws if w["x0"] >= mid - 3])
    S = agrupa([w for w in ws if not (w["x1"] <= mid + 3 or w["x0"] >= mid - 3)])
    usados_L, usados_R = set(), set()
    pecas = []  # (tipo, meio, words)
    for m, g in S:  # linha que atravessa o meio da página = largura total
        tot = list(g)
        for k, (mL, gL) in enumerate(L):
            if k not in usados_L and abs(mL - m) <= 4:
                tot += gL; usados_L.add(k)
        for k, (mR, gR) in enumerate(R):
            if k not in usados_R and abs(mR - m) <= 4:
                tot += gR; usados_R.add(k)
        pecas.append(("F", m, sorted(tot, key=lambda w: w["x0"])))
    for k, (mL, gL) in enumerate(L):  # linha corrida que só "pula" o meio num espaço entre palavras
        if k in usados_L:
            continue
        for q, (mR, gR) in enumerate(R):
            if q not in usados_R and abs(mL - mR) <= 2.5 and 0 <= gR[0]["x0"] - gL[-1]["x1"] < 8:
                pecas.append(("F", mL, gL + gR)); usados_L.add(k); usados_R.add(q)
                break
    pecas += [("L", m, g) for k, (m, g) in enumerate(L) if k not in usados_L]
    pecas += [("R", m, g) for k, (m, g) in enumerate(R) if k not in usados_R]
    pecas.sort(key=lambda x: x[1])
    out, bufL, bufR = [], [], []

    def flush():
        out.extend(bufL); out.extend(bufR); bufL.clear(); bufR.clear()

    for tipo, top, g in pecas:
        if tipo == "F":
            flush(); out.append(g)
        elif tipo == "L":
            bufL.append(g)
        else:
            bufR.append(g)
    flush()
    # borda de cada coluna = posição mais à esquerda de um candidato a número de item
    cand = []
    for g in out:
        if len(g) > 1 and g[0]["text"].isdigit() and "Bold" in g[0]["fontname"] and g[1]["x0"] - g[0]["x0"] >= 17:
            cand.append(g[0]["x0"])
    bordaL = min((c for c in cand if c < mid - 3), default=0)
    bordaR = min((c for c in cand if c >= mid - 3), default=mid)
    res = []
    for g in out:
        txt = " ".join(w["text"] for w in g)
        borda = bordaR if g[0]["x0"] >= mid - 3 else bordaL
        res.append({"x0": g[0]["x0"], "words": g, "txt": txt, "borda": borda})
    return res


CAB_RE = re.compile(r"(Quadrix\s*\|\s*\d{4}|INSTITUTO QUADRIX|APLICAÇÃO:|^CONSELHO |^INSTITUTO BRASILEIRO|RASCUNHO$|^ANOTAÇÕES$|^PROVA APLIC|^Prova$|^ap$|^lica$|^da$)")


def ler_prova(pdf: pathlib.Path, cargo_titulo: str) -> list[dict]:
    """Eventos em ordem: {'tipo':'ctx','txt':…} ou {'tipo':'item','n':…,'txt':…,'secao':…}."""
    ev, esperado, secao = [], 1, "basicos"
    atual = None
    with pdfplumber.open(str(pdf)) as doc:
        for page in doc.pages:
            for ln in linhas_pagina(page):
                t = ln["txt"].strip()
                if not t or CAB_RE.search(t) or (cargo_titulo and t.replace(" ", "") == cargo_titulo.replace(" ", "")):
                    continue
                up = t.upper()
                if "CONHECIMENTOS BÁSICOS" in up or "CONHECIMENTOS GERAIS" in up:
                    secao = "basicos"; atual = None; continue
                if "CONHECIMENTOS COMPLEMENTARES" in up:
                    secao = "complementares"; atual = None; continue
                if "CONHECIMENTOS ESPECÍFICOS" in up:
                    secao = "especificos"; atual = None; continue
                if up in ("PROVA OBJETIVA",):
                    continue
                w0 = ln["words"][0]
                gap = (ln["words"][1]["x0"] - w0["x0"]) if len(ln["words"]) > 1 else 99
                eh_num = (w0["text"].isdigit() and "Bold" in w0["fontname"] and w0["size"] >= 9
                          and int(w0["text"]) == esperado and gap >= 17 and w0["x0"] <= ln["borda"] + 5)
                if eh_num:
                    corpo = " ".join(w["text"] for w in ln["words"][1:])
                    x_txt = ln["words"][1]["x0"] if len(ln["words"]) > 1 else w0["x1"] + 12
                    atual = {"tipo": "item", "n": esperado, "txt": corpo, "secao": secao,
                             "x_num": w0["x0"], "x_txt": x_txt}
                    ev.append(atual); esperado += 1
                    continue
                recuo = ln["x0"] - ln["borda"]
                if atual is not None and 12 <= recuo <= 40 and ln["borda"] > 0:
                    atual["txt"] = (atual["txt"] + " " + t).strip() if atual["txt"] else t
                    continue
                if atual is not None and not atual["txt"]:  # número sozinho na linha: texto vem embaixo
                    atual["txt"] = t; atual["x_txt"] = ln["x0"]; continue
                atual = None
                if ev and ev[-1]["tipo"] == "ctx":
                    ev[-1]["txt"] += "\n" + t
                else:
                    ev.append({"tipo": "ctx", "txt": t, "secao": secao})
    return ev


def limpa(s: str) -> str:
    s = s.replace("‑", "-").replace("­", "")
    s = re.sub(r"(\w)- (\w)", r"\1-\2", s)
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s+([,.;:!?)\]”])", r"\1", s)
    s = re.sub(r"([(\[“])\s+", r"\1", s)
    return s.replace("|", "\\|")


def blocos(ev: list[dict]) -> list[dict]:
    """Agrupa itens por comando. Contexto seguido de contexto se junta; texto-base vale para a faixa citada."""
    out: list[dict] = []
    ref = None
    for e in ev:
        if e["tipo"] == "ctx":
            m = re.search(r"Te(?:xto|xt) (?:para|for) (?:os |as )?(?:ite(?:ns|ms)|questões) (?:de |from )?(\d+) (?:a|to|and|e) (\d+)", e["txt"])
            if m:
                ref = (int(m.group(1)), int(m.group(2)))
            if out and not out[-1]["itens"]:
                out[-1]["ctx"] += "\n" + e["txt"]
            else:
                out.append({"ctx": e["txt"], "secao": e["secao"], "itens": []})
            continue
        if not out:
            out.append({"ctx": "", "secao": e["secao"], "itens": []})
        b = out[-1]
        if not b["itens"] and ref and ref[0] <= e["n"] <= ref[1]:
            b["texto_de"] = ref
        b["itens"].append(e)
    return [b for b in out if b["itens"]]


def secao_por_numero(n: int, partes: list[tuple[str, int, int]], default: str) -> str:
    for nome, a, b in partes:
        if a <= n <= b:
            return {"básicos": "basicos", "complementares": "complementares", "específicos": "especificos"}[nome]
    return default


PROVA_DE = {"basicos": "P1", "complementares": "P2", "especificos": "P3"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--id", required=True)
    ap.add_argument("--orgao", required=True)
    ap.add_argument("--ano", type=int, required=True)
    ap.add_argument("--cargo", required=True, help="título do cargo como no cabeçalho da prova")
    ap.add_argument("--gab-cargo", required=True, help="regex do cabeçalho do cargo no gabarito")
    ap.add_argument("--aderencia", default="alta")
    ap.add_argument("--dry", action="store_true", help="só relatório, sem gravar")
    a = ap.parse_args()

    aj = yaml.safe_load(AJUSTES.read_text(encoding="utf-8")) if AJUSTES.exists() else {}
    aj_tags, aj_cmd, aj_txt = aj.get("tags") or {}, aj.get("comando") or {}, aj.get("texto") or {}
    pasta = FONTES / a.id
    gab, notas, partes = ler_gabarito(pasta / "gabarito.pdf", a.gab_cargo)
    ev = ler_prova(pasta / "prova.pdf", a.cargo)
    nums = [e["n"] for e in ev if e["tipo"] == "item"]
    bl = blocos(ev)
    faltam = sorted(set(gab) - set(nums))
    vazios = [e["n"] for e in ev if e["tipo"] == "item" and len(e["txt"]) < 15]
    print(f"{a.id}: {len(nums)} itens lidos · gabarito {len(gab)} · blocos {len(bl)} · "
          f"faltam {faltam[:10]}{'…' if len(faltam) > 10 else ''} · curtos {vazios[:10]}")
    if a.dry:
        for b in bl:
            ns = [i["n"] for i in b["itens"]]
            print(f"  [{ns[0]}–{ns[-1]}] {limpa(b['ctx'])[-110:]}")
        return 0

    for f in ITENS.glob(f"{a.id}_b*.md"):
        f.unlink()
    for k, b in enumerate(bl, 1):
        ns = [i["n"] for i in b["itens"]]
        secao = secao_por_numero(ns[0], partes, b["itens"][0]["secao"])
        ctx = limpa(re.sub(r"Nos itens que avaliem conhecimentos de inform[áa]tica.*?equipamentos mencionados\.", "", b["ctx"], flags=re.S))
        corpo_itens = " ".join(limpa(i["txt"]) for i in b["itens"])
        chave = f"{a.id}#{ns[0]}"
        if chave in aj_cmd:
            ctx = aj_cmd[chave]
        tags = aj_tags[chave] if chave in aj_tags else tg.tags_bloco(secao, ctx, corpo_itens)
        fm = [
            "---",
            f"id: {a.id}_b{k:02d}",
            f"orgao: \"{a.orgao}\"",
            f"ano: {a.ano}",
            "banca: quadrix",
            f"cargo: \"{a.cargo}\"",
            f"prova: {PROVA_DE[secao]}",
            "formato: certo_errado",
            "tags_edital:" + ("" if tags else " []"),
            *[f"  - {t}" for t in tags],
            f"itens: {ns[0]}-{ns[-1]}",
            f"aderencia: {a.aderencia}",
            "fonte:",
            f"  path: acervo/fontes/{a.id}/prova.pdf",
            f"  gabarito: acervo/fontes/{a.id}/gabarito.pdf",
            f"  nota: \"extração automática (acervo_extract_quadrix.py); gabarito definitivo. {notas}\"".rstrip(),
            "---",
            "",
            "## Comando",
            "",
            ctx if ctx else "(sem comando próprio: continuação do bloco anterior)",
            "",
        ]
        if "texto_de" in b and not re.search(r"Te(?:xto|xt) (?:para|for)", b["ctx"]):
            fm += [f"_Itens do texto dos itens {b['texto_de'][0]} a {b['texto_de'][1]} (ver bloco anterior)._", ""]
        fm += ["## Assertivas", "", "| id | texto | gabarito |", "|----|-------|----------|"]
        for i in b["itens"]:
            g = gab.get(i["n"], "?")
            txt_i = aj_txt.get(f"{a.id}#{i['n']}", limpa(i["txt"]))
            fm.append(f"| {i['n']} | {txt_i} | {g} |")
        (ITENS / f"{a.id}_b{k:02d}.md").write_text("\n".join(fm) + "\n", encoding="utf-8")
    print(f"gravados {len(bl)} arquivos acervo/itens/{a.id}_bNN.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
