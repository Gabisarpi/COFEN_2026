#!/usr/bin/env python3
"""Verificador numérico de calibração de um caderno (dados.js + meta.json).

Uso isolado (não grava nada):
  python3 verificar.py --data dados.js --meta meta.json [--cargo tic]

O build.py chama `verificar()` antes de gravar o HTML. Regras (fonte: skills
cofen-calibrar-itens §1 e cofen-simulado-quadrix → "Proibir pista de sequência"):

  (a) Cota de `code` — trilha tic (Cargo 407): item com `code` próprio ou herdado do
      núcleo. > 10% = AVISO; > 20% = ERRO. `meta.cota_code_livre: true` (pedido expresso
      da pessoa naquele caderno) rebaixa o ERRO a AVISO.
  (b) Proporção C/E: AVISO fora de 45–55%, com tolerância de 1 item para blocos pequenos.
  (c) Sequência do gabarito, na ordem do modo "por núcleo" (NUC → itens do núcleo):
      flip rate fora de ~35–70% = AVISO; > 75% = ERRO; janela de 8 itens consecutivos
      com ≥ 7 alternâncias C↔E = ERRO; corrida > 5 iguais = AVISO.

Blocos com menos de 8 itens recebem só avisos. Um simulado de 120 itens em HTML sai
como um caderno por prova (P1, P2, P3), e a checagem vale por caderno, isto é, por prova.
"""
import argparse, json, math, re, sys

STR = r'"(?:[^"\\]|\\.)*"'
TOK = re.compile(STR + r'|\b([A-Za-z_]\w*)\s*:')
VAL = re.compile(r'\s*(' + STR + r'|[A-Za-z_]\w*|\d+)')
MIN_BLOCO = 8


def _objetos(secao, chave_inicio):
    """Lista de dicionários {chave: valor bruto} na ordem, ignorando chaves dentro de strings."""
    objs = []
    for m in TOK.finditer(secao):
        k = m.group(1)
        if not k:
            continue
        v = VAL.match(secao, m.end())
        bruto = v.group(1) if v else ""
        if k == chave_inicio:
            objs.append({})
        if objs:
            objs[-1].setdefault(k, bruto)
    return objs


def _texto(bruto):
    return json.loads(bruto) if bruto.startswith('"') else bruto


def _tem(bruto):
    return bool(bruto) and bruto != '""'


def extrair(data):
    antes, _, depois = data.partition("const ITENS")
    nuc_sec = antes.split("const NUC", 1)[1] if "const NUC" in antes else antes
    nucs = _objetos(nuc_sec, "id")
    itens = _objetos(depois, "n")
    return nucs, itens


def verificar(data, meta, cargo=None):
    """Devolve (erros, avisos, relatorio). Erros bloqueiam o build salvo --sem-verificacao."""
    erros, avisos, rel = [], [], []
    nucs, itens = extrair(data)
    code_nuc = {_texto(n.get("id", '""')): _tem(n.get("code", "")) for n in nucs}
    ordem = []
    for n in nucs:
        nid = _texto(n.get("id", '""'))
        ordem += [i for i in itens if _texto(i.get("n", '""')) == nid]
    ordem += [i for i in itens if i not in ordem]  # núcleo inexistente: o build já acusa
    gabs = [_texto(i.get("gab", '""')) for i in ordem]
    gabs = [g for g in gabs if g in ("C", "E")]
    N = len(gabs)
    if not N:
        return erros, avisos, ["verificação: nenhum item com gab C/E"]
    peq = N < MIN_BLOCO
    sufixo = " (bloco < 8 itens: só aviso)" if peq else ""

    # (a) cota de code
    cargo = (cargo or meta.get("cargo") or "").lower()
    com_code = sum(1 for i in ordem if _tem(i.get("code", "")) or code_nuc.get(_texto(i.get("n", '""'))))
    pc = com_code / N
    linha = f"code: {com_code}/{N} itens ({pc:.0%}, próprio ou herdado do núcleo)"
    if cargo in ("tic", ""):
        livre = bool(meta.get("cota_code_livre"))
        if pc > 0.20 and not peq and not livre:
            erros.append(f"{linha} > teto de 20% da trilha tic (cofen-calibrar-itens §1). Reescreva em prosa, "
                         "ou use meta.cota_code_livre=true só com pedido expresso da pessoa")
        elif pc > 0.10:
            avisos.append(f"{linha} > ~10% da trilha tic" + (" (cota_code_livre)" if livre and pc > 0.20 else sufixo))
        rel.append(linha + " · cota tic ≤ ~10% (teto 20%)")
    else:
        rel.append(linha + (f" · trilha {cargo}: sem cota de código" if cargo else " · trilha desconhecida: sem cota"))

    # (b) proporção C/E, com tolerância de 1 item
    c = gabs.count("C")
    lo, hi = math.ceil(0.45 * N) - 1, math.floor(0.55 * N) + 1
    rel.append(f"C/E: {c} C × {N - c} E ({c / N:.0%} C)")
    if not lo <= c <= hi:
        avisos.append(f"C/E: {c} C × {N - c} E ({c / N:.0%} C) fora de 45–55% (tolerância de 1 item); "
                      "verdade técnica > cota, mas confira se dá para equilibrar")

    # (c) sequência
    flips = [gabs[k] != gabs[k - 1] for k in range(1, N)]
    if N > 1:
        fr = sum(flips) / (N - 1)
        seq = "".join(gabs)
        rel.append(f"sequência: {seq} · flip rate {fr:.0%}")
        if fr > 0.75:
            (avisos if peq else erros).append(f"flip rate {fr:.0%} > 75% (quase alternado): reordene itens/núcleos" + sufixo)
        elif not 0.35 <= fr <= 0.70:
            avisos.append(f"flip rate {fr:.0%} fora de ~35–70%")
        for k in range(0, N - 7):
            alt = sum(flips[k:k + 7])
            if alt >= 7:  # 8 itens têm 7 transições; 7 = CECECECE
                (avisos if peq else erros).append(
                    f"itens {k + 1}–{k + 8} ({seq[k:k + 8]}): ≥ 7 alternâncias na janela de 8" + sufixo)
                break
        for r in re.finditer(r"C{6,}|E{6,}", seq):
            avisos.append(f"corrida de {len(r.group(0))} '{r.group(0)[0]}' seguidos (itens {r.start() + 1}–{r.end()}): "
                          "aceitável só se a verdade técnica cair assim")
    return erros, avisos, rel


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--meta", required=True)
    ap.add_argument("--cargo", choices=["tic"], help="sobrescreve meta.cargo")
    a = ap.parse_args()
    data = open(a.data, encoding="utf-8").read()
    meta = json.load(open(a.meta, encoding="utf-8"))
    erros, avisos, rel = verificar(data, meta, a.cargo)
    for r in rel:
        print("INFO  ", r)
    for e in erros:
        print("ERRO  ", e)
    for w in avisos:
        print("AVISO ", w)
    sys.exit(1 if erros else 0)
