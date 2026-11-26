#!/usr/bin/env python3
"""Gera a folha de revisão ativa (HTML) a partir de folha.json.

Uso: python3 .agents/skills/cofen-folha-revisao/scripts/build.py <folha.json> [--out caminho.html] [--sem-ledger]

Valida o spec (estrutura, gabaritos, SVG acessível, lacunas existentes no ledger) e grava o HTML
com o template fixo da skill (CSS, motor de quiz e agenda). Erro de validação → corrigir o JSON,
nunca o HTML gerado. Formato: references/formato-folha.md.
"""
import html, json, pathlib, re, sys

SKILL = pathlib.Path(__file__).resolve().parent.parent
REPO = SKILL.parent.parent.parent
TPL = SKILL / "assets" / "template.html"

ERR = []


def err(m):
    ERR.append(m)


def need(d, k, ctx):
    if k not in d or d[k] in (None, "", []):
        err(f"{ctx}: campo obrigatório '{k}' ausente")
        return False
    return True


def check_quiz(items, ctx, nmin=1, nmax=99):
    if not isinstance(items, list) or not (nmin <= len(items) <= nmax):
        err(f"{ctx}: precisa de {nmin} a {nmax} itens (tem {len(items) if isinstance(items, list) else 0})")
        return
    gabs = set()
    for i, it in enumerate(items):
        if not (isinstance(it, list) and len(it) == 3 and it[1] in ("C", "E") and it[0].strip() and it[2].strip()):
            err(f"{ctx} item {i+1}: formato é [enunciado, 'C'|'E', porquê]")
            continue
        gabs.add(it[1])
    if len(items) >= 3 and gabs != {"C", "E"}:
        err(f"{ctx}: com 3 ou mais itens, precisa ter C e E")


def check_svg(svg, ctx):
    if not svg.lstrip().startswith("<svg"):
        err(f"{ctx}: svg deve começar com <svg")
    if 'role="img"' not in svg or "aria-label=" not in svg:
        err(f"{ctx}: svg precisa de role=\"img\" e aria-label")
    if "viewBox=" not in svg:
        err(f"{ctx}: svg precisa de viewBox")
    for bad in ("<script", "<style", "foreignObject"):
        if bad in svg:
            err(f"{ctx}: svg não pode conter {bad}")
    ids = re.findall(r'<marker id="([^"]+)"', svg)
    return ids


def ledger_ids(path):
    try:
        import yaml
    except ImportError:
        return None
    p = REPO / path
    if not p.is_file():
        err(f"ledger não encontrado: {path}")
        return None
    d = yaml.safe_load(p.read_text())
    return {e["id"] for e in d.get("entradas", []) if "id" in e}


# ---------- render ----------

def fig(svg, cap):
    return f'<figure>\n<div class="fig">\n{svg.strip()}\n</div>\n<figcaption>{cap}</figcaption>\n</figure>'


def fatos(items):
    out = ['<ul class="f">']
    for f in items:
        if f.get("tag"):
            out.append(f'<li class="mine">{f["html"]}<span class="tag">{f["tag"]}</span></li>')
        else:
            out.append(f'<li>{f["html"]}</li>')
    out.append("</ul>")
    return "\n".join(out)


def pares(b):
    head = "".join(f"<th>{h}</th>" for h in b["cab"])
    rows = "\n".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in b["linhas"])
    return f'<div class="tbl"><h3>{b.get("titulo", "Não confunda")}</h3>\n<table><tr>{head}</tr>\n{rows}</table></div>'


def lacunas(items):
    out = ['<div class="gaps">']
    for g in items:
        chip = "c-aberto" if g["status"] == "aberto" else "c-reforco"
        rot = "aberto" if g["status"] == "aberto" else "em reforço"
        out.append(f'<div class="gap"><div class="hd"><span class="chip {chip}">{rot}</span>{g["hd"]}</div>\n'
                   f'<div><span class="err">Errei:</span> {g["errei"]}</div>\n'
                   f'<div><span class="ok">Certo:</span> {g["certo"]}</div></div>')
    out.append("</div>")
    return "\n".join(out)


DISC = "discursiva"  # rótulo da frase pronta; o spec pode trocar com "discursiva": "<rótulo>"


def bloco(b, nid, quiz):
    t = b["tipo"]
    if t == "diagrama":
        return fig(b["svg"], b["legenda"])
    if t == "fatos":
        return fatos(b["itens"])
    if t == "pares":
        return pares(b)
    if t == "inversao":
        return f'<div class="trap"><b>Inversão:</b> {b["html"]}</div>'
    if t == "gancho":
        return f'<div class="hook"><b>Gancho:</b> {b["html"]}</div>'
    if t == "q2":
        return f'<div class="q2"><b>Frase pronta para a {DISC}:</b> {b["html"]}</div>'
    if t == "nota":
        return f'<p class="sub">{b["html"]}</p>'
    if t == "teste":
        quiz[nid] = b["itens"]
        return f'<h3>Teste-se</h3>\n<div class="quiz" data-quiz="{nid}"></div>'
    if t == "lacunas":
        return "<h3>Suas lacunas</h3>\n" + lacunas(b["itens"])
    raise ValueError(t)


def render(s):
    global DISC
    DISC = s.get("discursiva", "discursiva")
    quiz = {}
    parts = []
    parts.append(f'<header>\n<h1>{s["titulo"]}</h1>\n<p class="sub">{s["subtitulo"]}</p>\n</header>')
    li = "\n".join(f"<li>{x}</li>" for x in s["como_usar"])
    parts.append(f'<div class="panel how">\n<h2>{s.get("como_usar_titulo", "Como usar (25 min)")}</h2>\n<ol>\n{li}\n</ol>\n</div>')
    parts.append('<div class="legend">\n<span><i class="sw" style="background:var(--warn)"></i>amarelo = ponto em que você já errou</span>\n'
                 '<span><i class="sw" style="background:var(--bad)"></i>vermelho = como a banca inverte</span>\n'
                 '<span><i class="sw" style="background:var(--teal)"></i>verde-água = gancho de memória</span>\n'
                 '<span><i class="sw" style="border:1px dashed var(--accent)"></i>tracejado = frase pronta para a ' + DISC + '</span>\n</div>')
    p = s["pre"]
    quiz["pre"] = p["itens"]
    parts.append(f'<section id="pre">\n<header><h2>{p["titulo"]}</h2><span class="ed">{p["ed"]}</span></header>\n'
                 '<div class="quiz" data-quiz="pre"></div>\n<div class="score" data-score="pre"></div>\n</section>')
    if s.get("mapa"):
        m = s["mapa"]
        parts.append(f'<section id="mapa">\n<header><h2>{m["titulo"]}</h2><span class="ed">{m["ed"]}</span></header>\n{fig(m["svg"], m["legenda"])}\n</section>')
    li = "\n".join(f"<li>{x}</li>" for x in s["prioridade"])
    parts.append(f'<nav class="panel prio" aria-label="Prioridade">\n<h2>Revise nesta ordem (pelas suas lacunas)</h2>\n<ol>\n{li}\n</ol>\n</nav>')
    for n in s["nucleos"]:
        body = "\n".join(bloco(b, n["id"], quiz) for b in n["blocos"])
        parts.append(f'<section id="{n["id"]}">\n<header><h2>{n["titulo"]}</h2><span class="ed">{n["ed"]}</span></header>\n{body}\n</section>')
    g = s["gatilhos"]
    cols = "\n".join(f"<div><h3>{h}</h3><span>{t}</span></div>" for h, t in g["colunas"])
    parts.append(f'<section id="gatilhos">\n<header><h2>Gatilhos da banca neste tema</h2><span class="ed">{g["ed"]}</span></header>\n<div class="trig">\n{cols}\n</div>\n</section>')
    sd = s["saida"]
    quiz["saida"] = sd["itens"]
    parts.append(f'<section id="saida">\n<header><h2>Teste de saída · {len(sd["itens"])} itens misturados</h2><span class="ed">nota líquida Quadrix · refaça nas datas da agenda</span></header>\n'
                 '<div class="quiz" data-quiz="saida"></div>\n<div class="score" data-score="saida"></div>\n</section>')
    parts.append('<section id="agenda">\n<header><h2>Agenda de revisão espaçada</h2><span class="ed">'
                 + s.get("agenda_ed", "refaça só o teste de saída; com líquido de 10 ou mais, pule para a data seguinte")
                 + '</span></header>\n<div class="sched" id="sched"></div>\n<div><button type="button" class="btn" id="reset">Limpar minhas respostas desta folha</button></div>\n</section>')
    parts.append(f'<footer>{s["rodape"]}</footer>')
    tpl = TPL.read_text()
    out = (tpl.replace("__TITLE__", html.escape(s["titulo"], quote=False))
              .replace("__MAIN__", "\n\n".join(parts))
              .replace("__QUIZ__", json.dumps(quiz, ensure_ascii=False))
              .replace("__KEY__", json.dumps(s["key"]))
              .replace("__AGENDA__", json.dumps(s["agenda"], ensure_ascii=False)))
    return out


def validate(s, use_ledger=True):
    for k in ("titulo", "subtitulo", "key", "como_usar", "pre", "prioridade", "nucleos", "gatilhos", "saida", "agenda", "rodape"):
        need(s, k, "folha")
    if ERR:
        return
    if not s["titulo"].startswith("Folha de revisão · "):
        err("titulo deve ser 'Folha de revisão · <tema>' (nome estável do artifact)")
    check_quiz(s["pre"].get("itens", []), "pre", 3, 6)
    check_quiz(s["saida"].get("itens", []), "saida", 10, 14)
    markers = []
    if s.get("mapa"):
        markers += check_svg(s["mapa"]["svg"], "mapa")
    ids_n = set()
    known = ledger_ids(s["ledger"]) if (use_ledger and s.get("ledger")) else None
    for n in s["nucleos"]:
        ctx = f"núcleo {n.get('id')}"
        for k in ("id", "titulo", "ed", "blocos"):
            need(n, k, ctx)
        if n.get("id") in ids_n or n.get("id") in ("pre", "mapa", "saida", "gatilhos", "agenda"):
            err(f"{ctx}: id repetido ou reservado")
        ids_n.add(n.get("id"))
        tipos = [b.get("tipo") for b in n.get("blocos", [])]
        if "fatos" not in tipos:
            err(f"{ctx}: falta bloco 'fatos'")
        if "inversao" not in tipos and "gancho" not in tipos:
            err(f"{ctx}: falta bloco 'inversao' ou 'gancho'")
        for b in n.get("blocos", []):
            t = b.get("tipo")
            if t not in ("diagrama", "fatos", "pares", "inversao", "gancho", "q2", "nota", "teste", "lacunas"):
                err(f"{ctx}: tipo de bloco desconhecido '{t}'")
            elif t == "diagrama":
                markers += check_svg(b.get("svg", ""), ctx)
                need(b, "legenda", ctx)
            elif t == "teste":
                check_quiz(b.get("itens", []), f"{ctx} teste-se", 1, 4)
            elif t == "lacunas":
                for g in b.get("itens", []):
                    if g.get("status") not in ("aberto", "em_reforco"):
                        err(f"{ctx}: status de lacuna deve ser aberto|em_reforco")
                    for k in ("hd", "errei", "certo"):
                        need(g, k, ctx + " lacuna")
                    if known is not None and g.get("id") and g["id"] not in known:
                        err(f"{ctx}: lacuna '{g['id']}' não existe no ledger")
            elif t == "pares":
                for r in b.get("linhas", []):
                    if len(r) != len(b.get("cab", [])):
                        err(f"{ctx}: linha da tabela com nº de colunas diferente do cabeçalho")
    dup = {m for m in markers if markers.count(m) > 1}
    if dup:
        err(f"ids de <marker> repetidos entre diagramas (colidem na página): {sorted(dup)}")
    anchors = set(re.findall(r'href="#([\w-]+)"', json.dumps(s, ensure_ascii=False).replace('\\"', '"')))
    valid = ids_n | {"pre", "mapa", "saida", "gatilhos", "agenda"}
    for a in anchors - valid:
        if not a.startswith("ar"):
            err(f"link interno #{a} não aponta para nenhuma seção")


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        sys.exit(2)
    spec = pathlib.Path(a[0])
    out = None
    if "--out" in a:
        out = pathlib.Path(a[a.index("--out") + 1])
    s = json.loads(spec.read_text())
    validate(s, use_ledger="--sem-ledger" not in a)
    if ERR:
        print("Folha inválida:")
        for e in ERR:
            print(" -", e)
        sys.exit(1)
    out = out or (REPO / s["arquivo"] if s.get("arquivo") else spec.with_suffix(".html"))
    out.write_text(render(s))
    nq = sum(len(b["itens"]) for n in s["nucleos"] for b in n["blocos"] if b["tipo"] == "teste")
    nd = sum(1 for n in s["nucleos"] for b in n["blocos"] if b["tipo"] == "diagrama") + (1 if s.get("mapa") else 0)
    print(f"ok: {out} · {len(s['nucleos'])} núcleos · {nd} diagramas · pré {len(s['pre']['itens'])} · teste-se {nq} · saída {len(s['saida']['itens'])}")


if __name__ == "__main__":
    main()
