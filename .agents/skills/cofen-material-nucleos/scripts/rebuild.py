#!/usr/bin/env python3
"""Extrai dados.js e meta.json de um material já gerado, para remontá-lo com o template atual.

Uso:
  python3 rebuild.py --html pessoal/<quem>/revisao/AAAA-MM-DD_<eixo>-nucleos.html --out <scratch>/<eixo>
  # gera <out>.dados.js e <out>.meta.json; corrija o que precisar e rode build.py com eles

Serve quando o template muda (vale para todos os materiais) ou quando um material antigo precisa
de correção e o dados.js original não existe mais. O `key` é preservado, então as respostas salvas
no navegador continuam valendo depois de republicar no mesmo link.
"""
import argparse, html, json, re, sys

ap = argparse.ArgumentParser()
ap.add_argument("--html", required=True)
ap.add_argument("--out", required=True, help="prefixo dos arquivos de saída")
a = ap.parse_args()
t = open(a.html, encoding="utf-8").read()


def pega(rx, nome, flags=re.S):
    m = re.search(rx, t, flags)
    if not m:
        sys.exit(f"não achei {nome} em {a.html}")
    return m.group(1)


data = pega(r"<script>\n(.*?)\nITENS\.forEach\(\(it,i\)", "bloco de dados")
meta = {
    "title": html.unescape(pega(r"<title>(.*?)</title>", "title")),
    "eyebrow": pega(r'<header class="intro">\s*<div class="label">(.*?)</div>', "eyebrow"),
    "h1": pega(r"<h1>(.*?)</h1>", "h1"),
    # o lede já vem com as contagens; chaves literais precisariam de escape no format do build
    "lede": pega(r'<p class="lede">(.*?)</p>', "lede").replace("{", "{{").replace("}", "}}"),
    "method_html": pega(r'<summary>Como estes núcleos[^<]*</summary>\s*<div class="body">\n(.*?)\n\s*</div>\s*</details>', "método"),
    "key": pega(r'const KEY="([^"]+)"', "key"),
    "material": pega(r"material: (\S+)\\npessoa", "material"),
    "pessoa": pega(r"\\npessoa: (\S+?)\\n", "pessoa"),
    "cargo": pega(r"\\ncargo: (\S+?)\\n", "cargo"),
    "eixo": pega(r"\\neixo: (.*?)\\nitens", "eixo"),
    "respostas": pega(r'(?:Cole|Salve) em <span class="mono">(.*?)</span>', "respostas"),
    "resp_dir": pega(r'copie\)? o resultado para <span class="mono">(.*?)</span>', "resp_dir"),
}
# Materiais antigos podem não declarar esses campos; manter o padrão original.
peso = re.search(r"const PESO\s*=\s*([12])\s*;", t)
interface = re.search(r'const INTERFACE\s*=\s*"(classica|numerica)"\s*;', t)
meta["peso"] = int(peso.group(1)) if peso else 1
meta["interface"] = interface.group(1) if interface else "classica"
# resolução detalhada não fica no HTML como constante: inferir pelos campos do dados
if re.search(r"\btermos:\s*\"", data):
    meta["resolucao"] = "detalhada"
open(a.out + ".dados.js", "w", encoding="utf-8").write(data + "\n")
json.dump(meta, open(a.out + ".meta.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"OK: {a.out}.dados.js ({data.count(chr(10) + '{n:')} itens) e {a.out}.meta.json (key {meta['key']})")
