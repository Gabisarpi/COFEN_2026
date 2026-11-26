#!/usr/bin/env python3
"""Extrai as assertivas do acervo que têm uma tag do mapa, já sem as fontes sabidamente ruins.

Uso:
  python3 extract.py --repo /caminho/COFEN_2026 --tag esp.tic.seguranca \
      --out /scratch/pool [--campo tags_edital] [--incluir-completas]

Gera <out>.txt (uma linha por assertiva: arquivo#n|gab|texto) e <out>.json, e imprime
a contagem por prova. Use --grep para buscar também, por regex, itens de outras tags
cujo texto toque o assunto.
"""
import argparse, collections, glob, json, os, re, sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML ausente: pip install pyyaml")

# Provas sabidamente ruins (texto embaralhado, tag de atacado): acrescentar ids aqui.
RUINS: tuple = ()

ap = argparse.ArgumentParser()
ap.add_argument("--repo", required=True)
ap.add_argument("--tag", required=True, help="tag do mapa, ex.: esp.tic.redes")
ap.add_argument("--campo", default="tags_edital",
                help="campo de tags no frontmatter (padrão: tags_edital, mapa do Cargo 407).")
ap.add_argument("--out", required=True, help="prefixo dos arquivos de saída")
ap.add_argument("--grep", help="regex extra: inclui itens de QUALQUER tag cujo texto case")
ap.add_argument("--incluir-completas", action="store_true",
                help="inclui arquivos *_completa (em geral embaralhados)")
a = ap.parse_args()

rows, por_prova = [], collections.Counter()
rx = re.compile(a.grep) if a.grep else None
for f in sorted(glob.glob(os.path.join(a.repo, "acervo/itens/*.md"))):
    t = open(f, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n(.*)", t, re.S)
    if not m:
        continue
    try:
        h = yaml.safe_load(m.group(1)) or {}
    except Exception:
        continue
    iid = h.get("id", os.path.basename(f)[:-3])
    if iid.startswith(RUINS) or iid.startswith(("ancora", "_SCHEMA")):
        continue
    # extrato_retag_infra_* = itens reais de provas completas de TI, classificados item a item;
    # outros extratos (aderência, retag Java do Dev) continuam fora
    if iid.startswith("extrato") and not iid.startswith("extrato_retag_infra"):
        continue
    if "completa" in iid and not a.incluir_completas:
        continue
    tags = h.get(a.campo) or []
    tem_tag = a.tag in tags
    for n, txt, gab in re.findall(r"^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*([CEX])\s*\|", m.group(2), re.M):
        arq = iid
        orig = re.match(r"\[([\w.]+?)(?:\.md)?#(\d+)\]\s*(.*)", txt)
        if orig:  # linha de extrato: aponta para a prova e o item de origem
            arq, n, txt = orig.group(1), orig.group(2), orig.group(3)
        if tem_tag or (rx and rx.search(txt)):
            rows.append(dict(arquivo=arq, n=n, gab=gab, txt=txt, orgao=h.get("orgao"),
                             ano=h.get("ano"), cargo=h.get("cargo"), aderencia=h.get("aderencia"),
                             tem_tag=tem_tag))
            por_prova[arq.rsplit("_", 2)[0]] += 1

with open(a.out + ".txt", "w", encoding="utf-8") as fo:
    for r in rows:
        fo.write(f"{r['arquivo']}#{r['n']}|{r['gab']}|{'' if r['tem_tag'] else '[grep] '}{r['txt']}\n")
json.dump(rows, open(a.out + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(f"{len(rows)} assertivas em {len(por_prova)} provas")
for p, c in por_prova.most_common():
    print(f"  {c:4d}  {p}")
