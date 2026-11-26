#!/usr/bin/env python3
"""Sugestão do dia (“o que estudo hoje”) — COFEN 2026 · Gaby · Cargo 407.

Cruza as tags do dia no cronograma (`pessoal/gaby/cronograma/plano.py`, lista DIAS),
as lacunas `aberto`/`em_reforco` de `lacunas.yaml` e o proxy de prioridade
(`acervo_previsao.py`). Não fura a fase: lacuna de tag ainda não vista no plano
vira “slot futuro”, não estudo de hoje.

Uso (raiz do repo):
  python3 tools/acervo_sugestao_hoje.py [--data YYYY-MM-DD] [--write]

`--write` grava `pessoal/gaby/cronograma/sugestao-hoje.md` (local, não versionado).
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import sys

try:
    import yaml
except ImportError:
    print("Precisa de PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import acervo_previsao as prev  # noqa: E402
import cronograma_gerar as cg  # noqa: E402

ROOT = cg.ROOT
P = ROOT / "pessoal" / "gaby"
SEV = {"alta": 3.0, "media": 2.0, "média": 2.0, "baixa": 1.0}
FAIXA = {"alta": 1.3, "média": 1.0, "baixa": 0.7}


def casa(tag: str, tags: list[str]) -> bool:
    """`tag` coberta por alguma tag do plano (igual, ou uma é prefixo da outra)."""
    return any(tag == t or tag.startswith(t + ".") or t.startswith(tag + ".") for t in tags)


def dias_plano() -> list[tuple] | None:
    plano = P / "cronograma" / "plano.py"
    if not plano.exists():
        return None
    return [r for r in cg.ler_dias(plano) if len(r) == 6]


def lacunas() -> list[dict]:
    path = P / "cronograma" / "lacunas.yaml"
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return [e for e in data.get("entradas") or []
            if isinstance(e, dict) and e.get("status") in ("aberto", "em_reforco")
            and not e.get("fora_do_padrao")]


def score(e: dict, proxy: dict[str, dict]) -> float:
    sev = SEV.get(str(e.get("severidade", "media")).lower(), 2.0)
    certeza = int(e.get("erros_com_certeza") or 0)
    oc = int(e.get("ocorrencias") or 1)
    faixa = (proxy.get(e.get("tag", "")) or {}).get("faixa", "média")
    st = 1.0 if e.get("status") == "aberto" else 0.6
    return round(sev * (1 + 0.5 * certeza) * (1 + 0.25 * (oc - 1)) * FAIXA.get(faixa, 1.0) * st, 2)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", help="YYYY-MM-DD (default: hoje)")
    ap.add_argument("--write", action="store_true", help="grava pessoal/gaby/cronograma/sugestao-hoje.md")
    a = ap.parse_args()
    hoje = dt.date.fromisoformat(a.data) if a.data else dt.date.today()

    proxy = prev.proxy_scores()
    dias = dias_plano()
    linhas = [f"# Sugestão do dia — {hoje:%d/%m/%Y}", ""]

    tags_hoje: list[str] = []
    vistas: list[str] = []
    futuras: dict[str, str] = {}
    if dias is None:
        linhas += ["_Sem `plano.py`: não há filtro de fase. Todas as lacunas entram; confira se a matéria já foi estudada._", ""]
    else:
        for d, tipo, titulo, det, tags, curto in dias:
            data = cg.D(d)
            ts = (tags or "").split()
            if data == hoje:
                tags_hoje = ts
                linhas += ["## Plano do dia", "", f"- **{d} · {cg.TIPO.get(tipo, tipo)}** — {titulo}",
                           f"- {det}" if det else "", f"- Tags: {' '.join(f'`{t}`' for t in ts) or '—'}", ""]
            if data <= hoje:
                vistas += ts
            else:
                for t in ts:
                    futuras.setdefault(t, d)
        if not tags_hoje:
            linhas += ["_Hoje não tem linha no plano (folga ou fora do cronograma)._", ""]

    hoje_lac, retencao, futuro = [], [], []
    for e in lacunas():
        tag = e.get("tag", "")
        item = (score(e, proxy), e)
        if dias is None or casa(tag, tags_hoje):
            hoje_lac.append(item)
        elif casa(tag, vistas):
            retencao.append(item)
        else:
            quando = next((d for t, d in futuras.items() if casa(tag, [t])), "sem data no plano")
            futuro.append((quando, e))

    def bloco(titulo: str, itens: list):
        nonlocal linhas
        linhas += [f"## {titulo}", ""]
        if not itens:
            linhas += ["- (nenhuma)", ""]
            return
        for sc, e in sorted(itens, key=lambda x: -x[0])[:7]:
            faixa = (proxy.get(e.get("tag", "")) or {}).get("faixa", "—")
            linhas.append(f"- **{e.get('id')}** · `{e.get('tag')}` · {e.get('tema')} · "
                          f"{e.get('severidade')} · {e.get('status')} · ocorr. {e.get('ocorrencias')} · "
                          f"faixa {faixa} · score {sc}")
        linhas.append("")

    bloco("Lacunas do tema de hoje", hoje_lac)
    bloco("Retenção (matéria já estudada)", retencao)
    if futuro:
        linhas += ["## Não estudar agora — matéria futura no plano", ""]
        for quando, e in futuro:
            linhas.append(f"- **{e.get('id')}** · `{e.get('tag')}` → {quando}")
        linhas.append("")
    linhas += ["---", "Proxy: `python3 tools/acervo_previsao.py --write` · ledger: `pessoal/gaby/cronograma/lacunas.yaml`", ""]

    md = "\n".join(l for l in linhas if l is not None)
    print(md)
    if a.write:
        out = P / "cronograma" / "sugestao-hoje.md"
        out.write_text(md, encoding="utf-8", newline="\n")
        print(f"Escrito {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
