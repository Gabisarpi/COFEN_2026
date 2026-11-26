#!/usr/bin/env python3
"""Monta a página do material a partir do template e confere os dados antes.

Uso:
  python3 build.py --data dados.js --meta meta.json --repo /caminho/COFEN_2026 --out pagina.html

dados.js: o bloco JavaScript com `const NUC = [...]` e `const ITENS = [...]`
(ver references/formato-dados.md). Pode definir constantes auxiliares antes (ex.: CERT).
meta.json: {"title","eyebrow","h1","lede","method_html","key","material","pessoa","cargo",
            "eixo","respostas","resp_dir", "peso"?}. "peso" (opcional, default 1) é o
ponto Quadrix por item: P1/P2 → 1, P3 → 2. No "lede", {N}, {REAIS}, {VAR} e {NUC}
são trocados pelas contagens reais.

Conferências (o script para se alguma falhar, exceto as marcadas como aviso):
  - aspas e colchetes/chaves balanceados no dados.js
  - cada item com n, src, real, gab, txt, gat, exp, peg, inv, fonte; gab em C/E
  - todo item aponta para um núcleo existente e todo núcleo tem item
  - nenhuma resolução remete a outro item ("item seguinte", "veja o próximo", "compare com o
    item...") nem cita o gabarito de outra prova sobre o mesmo núcleo: em qualquer ordem
    (blocos ou intercalado) isso entrega a resposta do item ainda não respondido
  - `par` (par mínimo) aponta para um item existente do mesmo núcleo
  - (aviso) texto de item real que não aparece literalmente no acervo
  - (aviso) núcleo sem variação inédita, ou com todos os gabaritos iguais
  - verificador de calibração (scripts/verificar.py): cota de `code` na trilha Dev, proporção
    C/E e sequência do gabarito. Os ERROS dele bloqueiam, exceto com --sem-verificacao ou ao
    regenerar um material já publicado (mesma `key` no --out), em que ordem e itens se mantêm
    e os erros viram aviso. meta.cota_code_livre=true (pedido expresso) afrouxa só a cota.
"""
import argparse, glob, json, os, re, sys

ap = argparse.ArgumentParser()
ap.add_argument("--data", required=True)
ap.add_argument("--meta", required=True)
ap.add_argument("--repo", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--sem-verificacao", action="store_true",
                help="rebaixa a aviso os erros do verificador de calibração (cota de code e sequência C/E)")
a = ap.parse_args()

here = os.path.dirname(os.path.abspath(__file__))
tpl = open(os.path.join(here, "..", "assets", "template.html"), encoding="utf-8").read()
data = open(a.data, encoding="utf-8").read()
meta = json.load(open(a.meta, encoding="utf-8"))
erros, avisos = [], []

STR = r'"(?:[^"\\]|\\.)*"'
sem_str = re.sub(STR, '""', data)
for i, linha in enumerate(data.splitlines(), 1):
    if '"' in re.sub(STR, "", linha):
        erros.append(f"linha {i}: aspas desbalanceadas: {linha.strip()[:80]}")
for x, y in ("[]", "{}", "()"):
    if sem_str.count(x) != sem_str.count(y):
        erros.append(f"'{x}' e '{y}' desbalanceados ({sem_str.count(x)} × {sem_str.count(y)})")

def campo(bloco, k):
    m = re.search(r"\b" + k + r':\s*(' + STR + r'|\d+)', bloco)
    if not m:
        return None
    v = m.group(1)
    return json.loads(v) if v.startswith('"') else int(v)

nucs = re.findall(r'\{id:"([^"]+)"', data.split("const ITENS", 1)[0])
itens = re.split(r"\n\{n:", data.split("const ITENS", 1)[1])[1:]
itens = ["{n:" + b for b in itens]
obrig = ["n", "src", "real", "gab", "txt", "gat", "exp", "peg", "inv"]
# Remissões a outro item: entregam o gabarito do item que a pessoa ainda vai responder.
SPOILER = re.compile(
    r"\b(?:item|itens|assertiva|questão|variação|variações)\s+(?:seguinte|anterior|abaixo|acima|a seguir|ao lado|vizinh[oa])"
    r"|\bpr[óo]xim[oa]s?\s+(?:item|itens|assertiva|questão|variação)"
    r"|\b(?:veja|compare|confira|contraste|cf\.)\b[^.]{0,40}\b(?:item|itens|assertiva|variação)\b"
    r"|\b(?:mesma ideia|mesmo núcleo|mesma frase)\b[^.]{0,60}\b(?:virou|deu|foi)\s+[CE]\b"
    r"|\boutra prova\b[^.]{0,40}\b(?:virou|deu)\s+[CE]\b"
    r"|\b(?:item|itens|variação|variações)\b[^.]{0,40}\b(?:logo abaixo|abaixo|acima|seguinte|anterior)\b"
    r"|\b(?:oposto|inverso|contrário|contraponto|mesmo núcleo)\s+d[oa]\s+(?:item|variação)\b"
    r"|\b[A-Z][A-Za-z/]{2,}(?:\s+\d{4})?\s+[CE]\s*×"
    r"|\bpar mínimo\b[^.]{0,30}\bcom o item\b",
    re.I)
RESOLUCAO = ["gat", "termos", "viz", "exp", "passo", "ex", "lembre", "peg", "inv", "nota", "quote", "fonte"]
por_nuc = {n: [] for n in nucs}
reais = var = 0
acervo = ""
for f in glob.glob(os.path.join(a.repo, "acervo/itens/*.md")):
    acervo += open(f, encoding="utf-8").read()
for k, b in enumerate(itens, 1):
    vals = {c: campo(b, c) for c in obrig}
    falta = [c for c, v in vals.items() if v is None]
    if "fonte:" not in b:
        falta.append("fonte")
    if falta:
        erros.append(f"item {k}: faltam {falta}")
        continue
    if vals["gab"] not in ("C", "E"):
        erros.append(f"item {k}: gab inválido {vals['gab']}")
    for c in RESOLUCAO:
        v = campo(b, c)
        if isinstance(v, str) and (m := SPOILER.search(v)):
            erros.append(f"item {k} ({vals['n']}): '{c}' remete a outro item ou ao gabarito dele: «{m.group(0)}». "
                         "Escreva a reescrita que inverte; o par mínimo vai no campo par")
    if vals["n"] not in por_nuc:
        erros.append(f"item {k}: núcleo {vals['n']} não existe")
        continue
    vals["id"] = f'{vals["n"]}-{len(por_nuc[vals["n"]]) + 1}'
    vals["campos"] = {c: campo(b, c) for c in RESOLUCAO}
    vals["par"] = campo(b, "par")
    vals["k"] = k
    por_nuc[vals["n"]].append(vals)
    if vals["real"]:
        reais += 1
        if vals["txt"] not in acervo:
            avisos.append(f"item {k} ({vals['src'][:50]}): texto não bate literalmente com o acervo")
    else:
        var += 1
# opção individual resolucao-detalhada (meta.resolucao = "detalhada"): todo item define os termos e o vizinho
detalhada = meta.get("resolucao", "padrao") == "detalhada"
if meta.get("resolucao", "padrao") not in ("padrao", "detalhada"):
    erros.append(f"resolucao inválida: {meta.get('resolucao')} (use padrao ou detalhada)")
for _its in por_nuc.values():
    for _i in _its:
        t, v = _i["campos"].get("termos"), _i["campos"].get("viz")
        if detalhada and not t:
            erros.append(f"item {_i['k']} ({_i['id']}): falta 'termos' (resolução detalhada: sigla por extenso :: definição simples)")
        if detalhada and not v:
            erros.append(f"item {_i['k']} ({_i['id']}): falta 'viz' (resolução detalhada: o conceito vizinho e como diferenciar)")
        if t and any(" :: " not in p for p in t.split(" || ")):
            erros.append(f"item {_i['k']} ({_i['id']}): 'termos' fora do formato 'Termo :: definição || Termo :: definição'")
for n, its in por_nuc.items():
    if not its:
        erros.append(f"núcleo {n} sem itens")
    elif not any(not i["real"] for i in its):
        avisos.append(f"núcleo {n} sem variação inédita")
    elif len({i["gab"] for i in its}) == 1:
        avisos.append(f"núcleo {n}: todos os gabaritos são {its[0]['gab']}")
# padrão didático (08/11/2026): mini-aula por núcleo e passo a passo em item numérico
_nucblocos = re.split(r"\n \{id:", data.split("const ITENS", 1)[0])[1:]
for _b in _nucblocos:
    _id = re.match(r'"([^"]+)"', _b)
    if _id and "aula:" not in _b:
        avisos.append(f"núcleo {_id.group(1)} sem 'aula' (mini-aula obrigatória para materiais novos; ver SKILL.md, Explicações que ensinam)")
for _its in por_nuc.values():
    for _i in _its:
        if re.search(r"/\d{2}\b|\b\d+ (?:dias|bits|hosts|bytes|anos)\b", _i["txt"]) and not _i["campos"].get("passo"):
            avisos.append(f"item {_i['k']} ({_i['id']}): parece numérico/procedimental e não tem 'passo'")

ids = {i["id"]: i for its in por_nuc.values() for i in its}

# Remissão indireta: "item 55 da mesma prova", "(C, item 78)", "TCE/AC 2024 C7, item 67" quando esse item
# está NESTA página; ou "Como inverte" que reproduz o texto de outro item (entrega o gabarito dele).
norm = lambda s: re.sub(r"\W+", " ", s.lower()).strip()
srcs = [(i, re.match(r"(.*) · item (\d+)$", i["src"])) for i in ids.values()]
for i in ids.values():
    pref_i = re.match(r"(.*) · item \d+$", i["src"])
    for c in RESOLUCAO:
        v = i["campos"].get(c) or ""
        for o, m in srcs:
            if o is i or not m:
                continue
            if not re.search(r"\bitem " + m.group(2) + r"\b", v):
                continue
            org = m.group(1).split(" ")[0]
            mesma = pref_i and pref_i.group(1) == m.group(1)
            if org in v or mesma:
                erros.append(f"item {i['k']} ({i['id']}): '{c}' cita o item {m.group(2)} ({o['id']}), que está nesta página")
    # "'impede a ocorrência' é E": cita o gatilho ou o texto de outro item junto com o gabarito dele
    for c in RESOLUCAO:
        for trecho in re.findall(r"'([^']{6,}?)'\s*(?:é|foi|vira|virou|dá|deu|ficou)\s+[CE]\b", i["campos"].get(c) or ""):
            for o in ids.values():
                if o is not i and (norm(trecho) in norm(o["txt"]) or norm(trecho) == norm(o["gat"])):
                    erros.append(f"item {i['k']} ({i['id']}): '{c}' cita «{trecho}» com o gabarito, e isso é de {o['id']}")
    for trecho in re.findall(r"'\.{0,3}([^']{25,}?)\.{0,3}'", i["campos"].get("inv") or ""):
        for o in ids.values():
            if o is not i and len(norm(trecho)) > 25 and norm(trecho) in norm(o["txt"]):
                erros.append(f"item {i['k']} ({i['id']}): 'inv' reproduz o texto de {o['id']}; escreva outra inversão e ligue os dois por par")
for i in ids.values():
    if i["par"] is None:
        continue
    o = ids.get(i["par"])
    if not o:
        erros.append(f"item {i['k']} ({i['id']}): par {i['par']} não existe")
    elif o["n"] != i["n"] or o["id"] == i["id"]:
        erros.append(f"item {i['k']} ({i['id']}): par {i['par']} precisa ser outro item do mesmo núcleo")
    elif o["gab"] == i["gab"]:
        avisos.append(f"item {i['k']} ({i['id']}): par {i['par']} tem o mesmo gabarito; par mínimo costuma inverter")

# verificador numérico de calibração (cofen-calibrar-itens §1 e cofen-simulado-quadrix, pista de sequência)
sys.path.insert(0, here)
from verificar import verificar
v_erros, v_avisos, v_rel = verificar(data, meta)
for r in v_rel:
    print("INFO  ", r)
regerar = os.path.exists(a.out) and f'const KEY="{meta.get("key")}"' in open(a.out, encoding="utf-8").read()
if v_erros and (a.sem_verificacao or regerar):
    motivo = "--sem-verificacao" if a.sem_verificacao else "regeneração de material existente (mesma key; ordem preservada)"
    v_avisos = [f"{e} [rebaixado: {motivo}]" for e in v_erros] + v_avisos
    v_erros = []
erros += [f"calibração: {e}" for e in v_erros]
avisos += [f"calibração: {w}" for w in v_avisos]

for e in erros:
    print("ERRO  ", e)
for w in avisos:
    print("AVISO ", w)
if erros:
    sys.exit(1)

N = reais + var
peso = int(meta.get("peso", 1))
if peso != 1:
    sys.exit(f"peso inválido: {peso} (COFEN/Quadrix: todos os itens valem 1)")
interface = meta.get("interface", "classica")
if interface not in ("classica", "numerica"):
    sys.exit(f"interface inválida: {interface} (use classica ou numerica)")
# modo "prova" (simulado): correção, mini-aulas e cartões só depois de "Entregar prova"
modo = meta.get("modo", "estudo")
if modo not in ("estudo", "prova"):
    sys.exit(f"modo inválido: {modo} (use estudo ou prova)")
# número do primeiro item na folha (numeração contínua do simulado: P1 1, P2 41, P3 81)
inicio = meta.get("numero_inicial", 1)
if not isinstance(inicio, int) or isinstance(inicio, bool) or inicio < 1:
    sys.exit(f"numero_inicial inválido: {inicio} (use um inteiro ≥ 1)")
lede = meta["lede"].format(N=N, REAIS=reais, VAR=var, NUC=len(nucs))
rep = {"TITLE": meta["title"], "EYEBROW": meta["eyebrow"], "H1": meta["h1"], "LEDE": lede,
       "METHOD": meta["method_html"], "KEY": meta["key"], "MATERIAL": meta["material"],
       "PESSOA": meta["pessoa"], "CARGO": meta["cargo"], "EIXO": meta["eixo"],
       "RESPOSTAS": meta["respostas"], "RESP_DIR": meta["resp_dir"], "PESO": str(peso),
       "INTERFACE": interface, "MODO": modo, "INICIO": str(inicio)}
out = tpl.replace("/*{{DATA}}*/", data)
for k, v in rep.items():
    out = out.replace("{{" + k + "}}", v)
resto = re.findall(r"\{\{[A-Z_]+\}\}", out)
if resto:
    sys.exit(f"marcadores não preenchidos: {resto}")
os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
open(a.out, "w", encoding="utf-8").write(out)
print(f"OK: {N} itens ({reais} reais, {var} variações) em {len(nucs)} núcleos → {a.out}")
