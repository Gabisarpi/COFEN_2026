#!/usr/bin/env python3
"""Valida os dados de estudo de cada pessoa (ledger de lacunas + tags do cronograma).

Para cada `pessoal/<quem>/`:
- `cronograma/lacunas.yaml`: esquema de `.agents/skills/cofen-diagnostico-gaps/lacunas-schema.md`
  (campos obrigatórios, status, severidade, ids únicos, datas ISO, tag do mapa da trilha)
  e os campos opcionais `acertos_pos`, `erros_com_certeza` e `fora_do_padrao`;
- `cronograma/plano.py` (se existir): tags de DIAS no mapa da trilha (lido sem executar).

Trilha: gaby = tic (Cargo 407).
Por padrão todas as pessoas são estritas; `--aviso QUEM` rebaixa os problemas dela a aviso
(sem corrigir dados alheios).

Uso (raiz do repo):
  python3 tools/validar_estudo.py            # relatório
  python3 tools/validar_estudo.py --check    # exit 1 se houver erro (CI)
  python3 tools/validar_estudo.py --check --aviso gaby
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys

try:
    import yaml
except ImportError:
    print("Precisa de PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cronograma_gerar as cg  # noqa: E402

ROOT = cg.ROOT

OBRIGATORIOS = ("id", "tag", "tema", "severidade", "ocorrencias", "primeira_data",
                "ultima_data", "status", "detalhes", "fontes")
OPCIONAIS = ("acertos_pos", "erros_com_certeza", "fora_do_padrao")
STATUS = {"aberto", "em_reforco", "resolvido"}
SEVERIDADE = {"alta", "media", "baixa"}
FONTE_TIPO = {"objetiva", "discursiva", "revisao", "simulado"}
CONFIANCA = {"certeza", "duvida"}
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def data_iso(v) -> dt.date | None:
    """Aceita 'YYYY-MM-DD' (string) ou date do YAML; None se inválida."""
    if isinstance(v, dt.datetime):
        return None
    if isinstance(v, dt.date):
        return v
    if isinstance(v, str) and ISO_RE.match(v):
        try:
            return dt.date.fromisoformat(v)
        except ValueError:
            return None
    return None


def validar_ledger(path: pathlib.Path, trilha: str) -> tuple[list[str], list[str]]:
    erros: list[str] = []
    avisos: list[str] = []
    try:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        return [f"YAML inválido: {e}"], []
    if not isinstance(doc, dict):
        return ["raiz do YAML deve ser um mapa"], []
    for k in ("atualizado", "prova"):
        if k not in doc:
            erros.append(f"campo de topo `{k}` ausente")
        elif data_iso(doc[k]) is None:
            erros.append(f"`{k}` não é data ISO: {doc[k]!r}")
    ents = doc.get("entradas")
    if ents is None:
        ents = []
        erros.append("campo de topo `entradas` ausente")
    if not isinstance(ents, list):
        return erros + ["`entradas` deve ser lista"], avisos

    mapa = cg.tags_trilha(trilha)
    vistos: dict[str, int] = {}
    for i, e in enumerate(ents):
        ref = f"entrada #{i + 1}"
        if not isinstance(e, dict):
            erros.append(f"{ref}: deve ser mapa")
            continue
        eid = e.get("id")
        if isinstance(eid, str) and eid:
            ref = f"`{eid}`"
            if eid in vistos:
                erros.append(f"{ref}: id duplicado (entradas #{vistos[eid]} e #{i + 1})")
            else:
                vistos[eid] = i + 1
        for k in OBRIGATORIOS:
            if k not in e or e[k] is None or e[k] == "":
                erros.append(f"{ref}: campo obrigatório `{k}` ausente ou vazio")
        extras = set(e) - set(OBRIGATORIOS) - set(OPCIONAIS)
        if extras:
            avisos.append(f"{ref}: campos fora do esquema: {', '.join(sorted(extras))}")

        if "status" in e and e["status"] not in STATUS:
            erros.append(f"{ref}: status {e['status']!r} ∉ {{{', '.join(sorted(STATUS))}}}")
        if "severidade" in e and e["severidade"] not in SEVERIDADE:
            erros.append(f"{ref}: severidade {e['severidade']!r} ∉ {{{', '.join(sorted(SEVERIDADE))}}}")
        tag = e.get("tag")
        if tag and tag not in mapa:
            erros.append(f"{ref}: tag `{tag}` não existe no mapa da trilha {trilha}")
        oc = e.get("ocorrencias")
        if "ocorrencias" in e and (isinstance(oc, bool) or not isinstance(oc, int) or oc < 1):
            erros.append(f"{ref}: `ocorrencias` deve ser inteiro ≥ 1 ({oc!r})")
        d1 = d2 = None
        for k in ("primeira_data", "ultima_data"):
            if k in e:
                d = data_iso(e[k])
                if d is None:
                    erros.append(f"{ref}: `{k}` não é data ISO: {e[k]!r}")
                elif k == "primeira_data":
                    d1 = d
                else:
                    d2 = d
        if d1 and d2 and d1 > d2:
            erros.append(f"{ref}: primeira_data {d1} posterior a ultima_data {d2}")
        if "detalhes" in e and not (isinstance(e["detalhes"], list)
                                    and all(isinstance(x, str) for x in e["detalhes"])):
            erros.append(f"{ref}: `detalhes` deve ser lista de textos")
        fontes = e.get("fontes")
        if "fontes" in e:
            if not isinstance(fontes, list):
                erros.append(f"{ref}: `fontes` deve ser lista")
            else:
                for j, f in enumerate(fontes, 1):
                    if not isinstance(f, dict):
                        erros.append(f"{ref}: fonte {j} deve ser mapa")
                        continue
                    if f.get("tipo") not in FONTE_TIPO:
                        erros.append(f"{ref}: fonte {j} tipo {f.get('tipo')!r} ∉ {{{', '.join(sorted(FONTE_TIPO))}}}")
                    if not isinstance(f.get("path"), str) or not f.get("path"):
                        erros.append(f"{ref}: fonte {j} sem `path`")
                    if data_iso(f.get("data")) is None:
                        erros.append(f"{ref}: fonte {j} `data` não é ISO: {f.get('data')!r}")

        # opcionais (pós-correção)
        if "acertos_pos" in e:
            ap = e["acertos_pos"]
            if not isinstance(ap, list):
                erros.append(f"{ref}: `acertos_pos` deve ser lista")
            else:
                for j, a in enumerate(ap, 1):
                    if not isinstance(a, dict):
                        erros.append(f"{ref}: acertos_pos {j} deve ser mapa")
                        continue
                    if data_iso(a.get("data")) is None:
                        erros.append(f"{ref}: acertos_pos {j} `data` não é ISO: {a.get('data')!r}")
                    if a.get("confianca") not in CONFIANCA:
                        erros.append(f"{ref}: acertos_pos {j} confianca {a.get('confianca')!r} ∉ {{certeza, duvida}}")
                    if "fonte" in a and not isinstance(a["fonte"], str):
                        erros.append(f"{ref}: acertos_pos {j} `fonte` deve ser texto")
                    extra = set(a) - {"data", "confianca", "fonte"}
                    if extra:
                        avisos.append(f"{ref}: acertos_pos {j} campos fora do esquema: {', '.join(sorted(extra))}")
                # regra do esquema: resolvido exige ≥ 2 acertos com certeza em datas diferentes
                # (só aviso, e só quando a entrada já usa acertos_pos; entradas antigas seguem válidas)
                datas_certeza = {str(a.get("data")) for a in ap
                                 if isinstance(a, dict) and a.get("confianca") == "certeza"}
                if e.get("status") == "resolvido" and len(datas_certeza) < 2:
                    avisos.append(f"{ref}: resolvido com menos de 2 acertos_pos com certeza em datas diferentes")
        if "erros_com_certeza" in e:
            ec = e["erros_com_certeza"]
            if isinstance(ec, bool) or not isinstance(ec, int) or ec < 0:
                erros.append(f"{ref}: `erros_com_certeza` deve ser inteiro ≥ 0 ({ec!r})")
        if "fora_do_padrao" in e and not isinstance(e["fora_do_padrao"], bool):
            erros.append(f"{ref}: `fora_do_padrao` deve ser true ou false ({e['fora_do_padrao']!r})")
    return erros, avisos


def validar_plano(path: pathlib.Path, trilha: str) -> list[str]:
    try:
        dias = cg.ler_dias(path)
    except (ValueError, SyntaxError) as e:
        return [f"não foi possível ler DIAS: {e}"]
    erros = []
    for row in dias:
        if len(row) != 6:
            erros.append(f"{row[0] if row else '?'}: linha de DIAS deve ter 6 campos")
    return erros + cg.erros_tags_dias([r for r in dias if len(r) == 6], trilha)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 se houver erro")
    ap.add_argument("--aviso", action="append", default=[], metavar="QUEM",
                    help="relatar os problemas desta pessoa só como aviso (repetível)")
    args = ap.parse_args()
    so_aviso = {q.lower() for q in args.aviso}

    total_erros = total_avisos = 0
    for pdir in sorted(p for p in (ROOT / "pessoal").iterdir() if p.is_dir()):
        quem = pdir.name
        lac = pdir / "cronograma" / "lacunas.yaml"
        plano = pdir / "cronograma" / "plano.py"
        if not lac.exists() and not plano.exists():
            continue
        trilha = cg.TRILHA_PESSOA.get(quem)
        if trilha is None:
            print(f"AVISO {quem}: pessoa sem trilha conhecida (REPO.md); pulando")
            total_avisos += 1
            continue
        probs: list[tuple[str, str]] = []
        avisos: list[tuple[str, str]] = []
        if lac.exists():
            e, a = validar_ledger(lac, trilha)
            probs += [("lacunas.yaml", x) for x in e]
            avisos += [("lacunas.yaml", x) for x in a]
        if plano.exists():
            probs += [("plano.py", x) for x in validar_plano(plano, trilha)]
        estrita = quem not in so_aviso
        nivel = "ERRO" if estrita else "AVISO"
        for arq, msg in probs:
            print(f"{nivel} {quem}/{arq}: {msg}")
        for arq, msg in avisos:
            print(f"AVISO {quem}/{arq}: {msg}")
        if estrita:
            total_erros += len(probs)
        else:
            total_avisos += len(probs)
        total_avisos += len(avisos)
        print(f"{'OK  ' if not probs else 'FALHA' if estrita else 'aviso'} {quem} ({trilha}): "
              f"{len(probs)} problema(s){'' if estrita else ' [só aviso]'}, {len(avisos)} aviso(s) extra")

    print(f"\nTotal: {total_erros} erro(s), {total_avisos} aviso(s)")
    return 1 if (args.check and total_erros) else 0


if __name__ == "__main__":
    sys.exit(main())
