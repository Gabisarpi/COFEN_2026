#!/usr/bin/env python3
"""Extrai a discursiva Quadrix (enunciado do caderno + padrão definitivo de resposta)
→ acervo/itens/<id>_disc[N].md, com tag disc.tic e as tags do tema.

Uso (raiz do repo):
  python3 tools/acervo_discursiva_quadrix.py --id crefito17_2026_analista_ti \
    --orgao CREFITO-17 --ano 2026 --cargo "Analista de Tecnologia da Informação" \
    --padrao-cargo "ANALISTA DE TECNOLOGIA DA INFORMAÇÃO \\(CÓDIGO 402\\)" \
    --tags esp.tic.govti,esp.tic.gestao [--parte 2] [--sem-prova]

Pasta: acervo/fontes/<id>/prova.pdf (opcional com --sem-prova) e padrao_discursiva.pdf.
O enunciado sai sem a marca d'água "Prova aplicada" (corpo > 20 é descartado).
Não inventa nada: sem caderno, o enunciado fica marcado como não disponível.
"""
import argparse, pathlib, re, subprocess, sys

import pdfplumber

RAIZ = pathlib.Path(__file__).resolve().parents[1]


def enunciado(pdf: pathlib.Path, parte: int | None, cargo: str = "") -> str:
    paginas = []
    with pdfplumber.open(pdf) as doc:
        for p in doc.pages:
            p2 = p.filter(lambda o: o.get("object_type") != "char" or o.get("size", 10) < 20)
            paginas.append(p2.extract_text() or "")
    txt = "\n".join(paginas)
    marcas = [m.start() for m in re.finditer(r"PROVA DISCURSIVA", txt)]
    if not marcas:
        sys.exit("caderno: 'PROVA DISCURSIVA' não encontrado")
    i = marcas[(parte or 1) - 1]
    fim = marcas[parte] if parte and parte < len(marcas) else len(txt)
    s = txt[i:fim]
    j = s.find("não servirá para avaliação.")
    s = s[j + len("não servirá para avaliação."):] if j >= 0 else s
    s = re.split(r"\n\s*RASCUNHO", s)[0]
    linhas = [l.strip() for l in s.splitlines()]
    linhas = [l for l in linhas if l and not re.fullmatch(r"\d{1,2}", l) and not re.search(r"Quadrix \| \d{4}|^CONSELHO ", l)
              and not (cargo and re.fullmatch(re.escape(cargo) + r"\s*\d{1,2}", l))]
    # junta linhas do mesmo parágrafo; quebra antes de a), b), c) e depois de ponto final curto
    out = []
    for l in linhas:
        novo = (not out or re.match(r"^[a-e]\)\s", l) or out[-1].endswith((".", ":", ";")) and l[:1].isupper()
                or l.startswith("Considerando que o texto") or l.startswith("Ao elaborar"))
        if novo:
            out.append(l)
        else:
            out[-1] = (out[-1][:-1] if out[-1].endswith("‑") or out[-1].endswith("-") and not out[-1].endswith(" -") else out[-1] + " ") + l
    return "\n\n".join(out).replace("‑", "-")


def padrao(pdf: pathlib.Path, cargo_re: str, parte: int | None) -> str:
    txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    L = [re.sub(r"[ \t]{2,}", " ", l).strip() for l in txt.splitlines()]
    def cab(k):  # cabeçalho de cargo na linha k (ou quebrado em k, k+1)
        dois = L[k] + " " + (L[k + 1] if k + 1 < len(L) else "")
        return bool(re.search(r"\(C[ÓO]DIGO\s*\d*", L[k]) or re.search(r"\(C[ÓO]DIGO$", L[k])) and L[k][:1].isalnum() and L[k].upper() == L[k], dois
    ini = None
    for k in range(len(L)):
        e, dois = cab(k)
        if e and re.search(cargo_re, dois):
            ini = k + (2 if not re.search(r"\)\s*$", L[k]) else 1)
            break
    if ini is None:
        sys.exit(f"padrão: cargo não encontrado ({cargo_re})")
    fim = next((k for k in range(ini, len(L)) if cab(k)[0]), len(L))
    paras, cur = [], []
    for l in L[ini:fim] + [""]:
        if not l or re.fullmatch(r"\d{1,2}", l):
            if not l and cur:
                paras.append(" ".join(cur)); cur = []
            continue
        if re.fullmatch(r"PARTE \d", l) or re.match(r"PARTE \d\b", l):
            if cur:
                paras.append(" ".join(cur)); cur = []
            paras.append(l[:7]); l = l[7:].strip()
            if not l:
                continue
        cur.append(l)
    if parte:
        k = [n for n, p in enumerate(paras) if p == f"PARTE {parte}"]
        if k:
            paras = paras[k[0] + 1:]
            k2 = [n for n, p in enumerate(paras) if re.fullmatch(r"PARTE \d", p)]
            paras = paras[: k2[0]] if k2 else paras
    return "\n\n".join(paras).replace("\u2011", "-")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True)
    ap.add_argument("--orgao", required=True)
    ap.add_argument("--ano", type=int, required=True)
    ap.add_argument("--cargo", required=True)
    ap.add_argument("--padrao-cargo", required=True, help="regex do cabeçalho do cargo no padrão")
    ap.add_argument("--tags", default="", help="tags do tema, separadas por vírgula")
    ap.add_argument("--parte", type=int, help="nº da parte, quando a discursiva tem mais de uma")
    ap.add_argument("--aderencia", default="alta")
    ap.add_argument("--tema", help="tema, quando o enunciado não traz a linha de tema")
    ap.add_argument("--sem-prova", action="store_true", help="o caderno não foi publicado")
    a = ap.parse_args()
    pasta = RAIZ / "acervo/fontes" / a.id
    enun = ("_Enunciado não disponível: o caderno de prova deste cargo não está no ZIP oficial. "
            "Os aspectos cobrados aparecem no padrão de resposta abaixo._") if a.sem_prova else enunciado(pasta / "prova.pdf", a.parte, a.cargo)
    pad = padrao(pasta / "padrao_discursiva.pdf", a.padrao_cargo, a.parte)
    tema = re.search(r"acerca do tema a seguir\.\s*\n\n(.+?)\n\nAo elaborar", enun, re.S)
    tags = ["disc.tic"] + [t for t in a.tags.split(",") if t]
    suf = f"_disc{a.parte}" if a.parte else "_disc"
    rel = lambda p: str(p.relative_to(RAIZ))
    fm = [
        "---", f"id: {a.id}{suf}", f'orgao: "{a.orgao}"', f"ano: {a.ano}", "banca: quadrix",
        f'cargo: "{a.cargo}"', "prova: discursiva", "formato: discursiva_20-30_linhas",
        "tags_edital:", *[f"  - {t}" for t in tags],
        "temas:", f'  - "{(a.tema or (tema.group(1).replace(chr(10), " ").strip() if tema else "ver padrão")).replace(chr(34), chr(39))}"',
        f"aderencia: {a.aderencia}", "fonte:",
        f"  path: {rel(pasta / 'prova.pdf') if not a.sem_prova else 'não publicado'}",
        f"  padrao: {rel(pasta / 'padrao_discursiva.pdf')}",
        '  nota: "extração automática (acervo_discursiva_quadrix.py); padrão definitivo de resposta da Quadrix."',
        "---", "",
    ]
    corpo = "## Enunciado\n\n" + enun + "\n\n## Padrão definitivo de resposta (Quadrix)\n\n" + pad + "\n"
    dest = RAIZ / "acervo/itens" / f"{a.id}{suf}.md"
    dest.write_text("\n".join(fm) + corpo, encoding="utf-8")
    print(f"{dest.name}: enunciado {len(enun)} car. · padrão {len(pad)} car. · tema: {tema.group(1)[:70] if tema else '-'}")


if __name__ == "__main__":
    main()
