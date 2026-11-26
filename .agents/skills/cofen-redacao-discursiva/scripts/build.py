#!/usr/bin/env python3
"""Monta redacao.html a partir do template + meta + enunciado.

Uso (na raiz do repo ou com paths absolutos):
  python3 .agents/skills/cofen-redacao-discursiva/scripts/build.py \\
    --meta meta-redacao.json \\
    --enunciado enunciado.html \\
    --out redacao.html

meta-redacao.json (campos obrigatórios):
  title, h1, subtitle, key, out_path, md_title, caderno
  max (default 30), min (default 20), width (default 60), pessoa, cargo, questao
meta-redacao.json (opcionais):
  pedidos: ["Explicar o risco X", "Indicar duas estratégias", ...]  # pedidos explícitos do enunciado
  lp_erros: ["mal → mau (adjetivo)", ...]                            # âncoras de LP da pessoa
--lp-erros $P/revisao/lp-erros.md (opcional): lê as linhas "- errado → certo" do arquivo, se existir,
  e as soma a lp_erros. Sem pedidos nem LP, o editor se comporta como antes (painel recolhido e vazio).
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
TPL = HERE.parent / "assets" / "redacao.template.html"

ap = argparse.ArgumentParser(description="Build HTML de redação discursiva COFEN")
ap.add_argument("--meta", required=True, help="JSON com metadados da redação")
ap.add_argument("--enunciado", required=True, help="Fragmento HTML do enunciado (sem <section>)")
ap.add_argument("--out", required=True, help="caminho de saída redacao.html")
ap.add_argument("--lp-erros", help="opcional: $P/revisao/lp-erros.md (ignorado se não existir)")
a = ap.parse_args()

meta = json.loads(pathlib.Path(a.meta).read_text(encoding="utf-8"))
enunciado = pathlib.Path(a.enunciado).read_text(encoding="utf-8").strip()
tpl = TPL.read_text(encoding="utf-8")

obrig = ["title", "h1", "subtitle", "key", "out_path", "md_title", "caderno"]
falta = [k for k in obrig if not meta.get(k)]
if falta:
    sys.exit(f"meta incompleto: faltam {falta}")

mx = int(meta.get("max", 30))
mn = int(meta.get("min", 20))
if not (1 <= mn <= mx <= 90):
    sys.exit(f"limites inválidos: min {mn}, max {mx} (COFEN: 20 a 30 linhas)")
width = int(meta.get("width", 60))
if width < 40 or width > 90:
    sys.exit(f"width fora da faixa útil: {width}")

pedidos = meta.get("pedidos") or []
lp_erros = list(meta.get("lp_erros") or [])
if not isinstance(pedidos, list) or not all(isinstance(x, str) and x.strip() for x in pedidos):
    sys.exit("pedidos deve ser lista de textos não vazios")
if a.lp_erros and pathlib.Path(a.lp_erros).is_file():
    for linha in pathlib.Path(a.lp_erros).read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*[-*]\s+(.+\S)", linha)
        if m and ("→" in m.group(1) or "->" in m.group(1)):
            lp_erros.append(m.group(1))
lp_erros = list(dict.fromkeys(x.strip() for x in lp_erros if isinstance(x, str) and x.strip()))


def js_json(v) -> str:
    return json.dumps(v, ensure_ascii=False).replace("</", "<\\/")


# Escape for JS string literals in KEY / OUT_PATH / MD_TITLE / CADERNO
def js_str(s: str) -> str:
    return (
        s.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("</", "<\\/")
    )

rep = {
    "TITLE": str(meta["title"]),
    "H1": str(meta["h1"]),
    "SUBTITLE": str(meta["subtitle"]),
    "ENUNCIADO": enunciado,
    "MAX": str(mx),
    "MIN": str(mn),
    "WIDTH": str(width),
    "KEY": js_str(str(meta["key"])),
    "OUT_PATH": js_str(str(meta["out_path"])),
    "MD_TITLE": js_str(str(meta["md_title"])),
    "CADERNO": js_str(str(meta["caderno"])),
    "PEDIDOS": js_json([x.strip() for x in pedidos]),
    "LP_ERROS": js_json(lp_erros),
}

out = tpl
for k, v in rep.items():
    out = out.replace("{{" + k + "}}", v)

resto = re.findall(r"\{\{[A-Z_]+\}\}", out)
if resto:
    sys.exit(f"marcadores não preenchidos: {sorted(set(resto))}")

path_out = pathlib.Path(a.out)
path_out.parent.mkdir(parents=True, exist_ok=True)
path_out.write_text(out, encoding="utf-8")
print(f"OK: redação · TL {mn}–{mx} · wrap {width} · "
      f"{len(pedidos)} pedidos · {len(lp_erros)} âncoras de LP → {path_out}")
