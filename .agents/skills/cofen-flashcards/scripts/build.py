#!/usr/bin/env python3
"""Monta flashcards.html a partir de deck.json (skill cofen-flashcards).

Uso:  python3 .agents/skills/cofen-flashcards/scripts/build.py <pasta-ou-deck.json> [--ledger <lacunas.yaml>]

Valida o deck (ids únicos, tipos, gabaritos, fontes, baralhos, lacunas do ledger) e grava
flashcards.html na mesma pasta do deck.json. Sai com código 1 se houver erro.
"""
import json, re, sys, html
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "assets" / "template.html"
CAMPOS = ["titulo", "eyebrow", "h1", "lede", "pessoa", "cargo", "data", "material", "export", "key", "baralhos", "cartoes"]


def ids_ledger(path):
    if not path or not Path(path).exists():
        return None
    return set(re.findall(r"(?m)^  - id: (\S+)", Path(path).read_text(encoding="utf-8")))


def validar(d, ledger):
    erros, avisos = [], []
    for k in CAMPOS:
        if k not in d:
            erros.append(f"campo obrigatório ausente: {k}")
    if erros:
        return erros, avisos
    bids = [b["id"] for b in d["baralhos"]]
    if len(bids) != len(set(bids)):
        erros.append("baralhos com id repetido")
    if len(bids) > 4:
        avisos.append("mais de 4 baralhos: as cores se repetem")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d["data"]):
        erros.append("data deve ser AAAA-MM-DD")
    if not d["export"].startswith(f"pessoal/{d['pessoa']}/respostas/") or not d["export"].endswith(".yaml"):
        erros.append("export deve ficar em pessoal/<pessoa>/respostas/ e terminar em .yaml")
    vistos, fontes = set(), d.get("fontes", {})
    por_baralho = {b: {"conceito": 0, "ce": 0, "C": 0, "E": 0} for b in bids}
    for c in d["cartoes"]:
        cid = c.get("id", "?")
        for k in ("id", "d", "k", "f", "a", "h", "s"):
            if not c.get(k):
                erros.append(f"{cid}: campo '{k}' vazio")
        if cid in vistos:
            erros.append(f"{cid}: id repetido")
        vistos.add(cid)
        if c.get("d") not in bids:
            erros.append(f"{cid}: baralho '{c.get('d')}' não existe")
            continue
        if c.get("k") not in ("conceito", "ce"):
            erros.append(f"{cid}: tipo deve ser 'conceito' ou 'ce'")
            continue
        pb = por_baralho[c["d"]]
        pb[c["k"]] += 1
        if c["k"] == "ce":
            if c.get("g") not in ("C", "E"):
                erros.append(f"{cid}: cartão C/E sem gabarito C ou E")
            else:
                pb[c["g"]] += 1
        s = c.get("s", "")
        if s and s not in fontes and "<a " not in s and len(s) < 12:
            erros.append(f"{cid}: fonte '{s}' não está em 'fontes' (use a chave ou o texto/HTML da fonte)")
        if d.get("resolucao") == "detalhada":
            for k in ("termos", "viz"):
                if not c.get(k):
                    erros.append(f"{cid}: falta '{k}' (resolução detalhada)")
        if c.get("termos") and any(" :: " not in p for p in c["termos"].split(" || ")):
            erros.append(f"{cid}: 'termos' fora do formato 'Termo :: definição || Termo :: definição'")
        if not c.get("lacuna"):
            avisos.append(f"{cid}: sem 'lacuna' (o diagnóstico não terá onde lançar)")
        elif ledger is not None and c["lacuna"] not in ledger:
            erros.append(f"{cid}: lacuna '{c['lacuna']}' não existe no ledger")
    for b, pb in por_baralho.items():
        n = pb["conceito"] + pb["ce"]
        if n == 0:
            erros.append(f"baralho {b}: vazio")
            continue
        if pb["ce"] and (pb["C"] == 0 or pb["E"] == 0):
            avisos.append(f"baralho {b}: C/E só com um gabarito ({pb['C']} C, {pb['E']} E)")
        if pb["ce"] < 2:
            avisos.append(f"baralho {b}: menos de 2 cartões C/E (o diagnóstico precisa deles para medir)")
    return erros, avisos


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(1)
    alvo = Path(args[0])
    deck = alvo / "deck.json" if alvo.is_dir() else alvo
    ledger = args[args.index("--ledger") + 1] if "--ledger" in args else None
    d = json.loads(deck.read_text(encoding="utf-8"))
    if ledger is None:
        guess = Path("pessoal") / d.get("pessoa", "") / "cronograma" / "lacunas.yaml"
        ledger = str(guess) if guess.exists() else None
    erros, avisos = validar(d, ids_ledger(ledger))
    for a in avisos:
        print("aviso:", a)
    if erros:
        for e in erros:
            print("ERRO:", e)
        sys.exit(1)
    payload = json.dumps(d, ensure_ascii=False).replace("</", "<\\/")
    out = TEMPLATE.read_text(encoding="utf-8").replace("__TITULO__", html.escape(d["titulo"])).replace("__DECK__", payload)
    dest = deck.parent / "flashcards.html"
    dest.write_text(out, encoding="utf-8")
    ce = sum(1 for c in d["cartoes"] if c["k"] == "ce")
    print(f"ok: {dest} · {len(d['cartoes'])} cartões ({ce} C/E) em {len(d['baralhos'])} baralho(s) · ledger {'conferido' if ledger else 'não encontrado'}")


if __name__ == "__main__":
    main()
