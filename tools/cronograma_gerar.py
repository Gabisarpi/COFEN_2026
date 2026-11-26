#!/usr/bin/env python3
"""Gerador comum do cronograma pessoal (plano.md + cronograma.html).

Cada pessoa mantém em `pessoal/<quem>/cronograma/plano.py` só os dados
(FASES, DIAS, MATERIAIS, FERIADOS, PERDIDOS, horas(), textos do markdown) e
chama `gerar(...)`. O `template.html` (UI) continua na pasta da pessoa e
recebe o JSON do plano no marcador `__PLANO__`.

As tags de DIAS são validadas contra `cargos/<trilha>/mapa-edital.md`
(cargos/tic): tag desconhecida aborta a geração.
Um prefixo de tags do mapa (ex.: `esp.tic`, `comp`, `basicos`) vale como agrupador.

Também expõe utilitários usados por `validar_estudo.py` e
`acervo_sugestao_hoje.py` (leitura de DIAS sem executar o plano).
"""
from __future__ import annotations

import ast
import datetime as dt
import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
# O plano do COFEN atravessa a virada do ano: jul–dez = 2026, jan–jun = 2027 (prova 28/02/2027).
ANO_INICIO = 2026
DOW = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
TIPO = {
    "nuc": "Núcleos", "ref": "Reforço", "bloco": "Bloco C/E", "disc": "Discursiva",
    "sim": "Simulado", "p2": "P2", "p1": "P1", "rev": "Revisão", "leve": "Leve", "prova": "Prova",
}
# pessoa → trilha (ver REPO.md)
TRILHA_PESSOA = {"gaby": "tic"}

_TAG_RE = re.compile(r"`((?:basicos|comp|disc|esp\.tic)\.[a-z0-9_.]+|disc\.tic|esp\.tic)`")


def D(s: str) -> dt.date:
    """'DD/MM' → date: meses de julho a dezembro em ANO_INICIO, janeiro a junho no ano seguinte."""
    dd, mm = s.split("/")
    ano = ANO_INICIO if int(mm) >= 7 else ANO_INICIO + 1
    return dt.date(ano, int(mm), int(dd))


def mid(nome: str) -> str:
    """Id estável da atividade (chave em dias/<data>.itens no banco do artifact). Mudar o nome muda o id."""
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:48]


# ---------------------------------------------------------------- tags do mapa

def _tags_arquivo(path: pathlib.Path) -> list[str]:
    if not path.exists():
        return []
    return list(dict.fromkeys(_TAG_RE.findall(path.read_text(encoding="utf-8"))))


def tags_trilha(trilha: str) -> set[str]:
    """Tags válidas da trilha: todas as do mapa do cargo (basicos.*, comp.*, esp.tic.*, disc.tic)."""
    if trilha != "tic":
        raise ValueError(f"trilha inválida: {trilha!r} (use tic)")
    return set(_tags_arquivo(ROOT / "cargos" / trilha / "mapa-edital.md"))


def tag_valida(tag: str, mapa: set[str]) -> bool:
    """Tag exata do mapa ou prefixo (agrupador) de alguma tag do mapa."""
    return tag in mapa or any(m.startswith(tag + ".") for m in mapa)


def erros_tags_dias(dias, trilha: str) -> list[str]:
    """Lista de mensagens para tags de DIAS fora do mapa da trilha."""
    mapa = tags_trilha(trilha)
    erros = []
    for row in dias:
        d, tags = row[0], row[4]
        for t in (tags or "").split():
            if not tag_valida(t, mapa):
                erros.append(f"{d}: tag desconhecida `{t}` (não existe em cargos/{trilha}/mapa-edital.md)")
    return erros


def ler_dias(plano: pathlib.Path) -> list[tuple]:
    """Lê a lista DIAS de um plano.py sem executá-lo (ast.literal_eval)."""
    tree = ast.parse(plano.read_text(encoding="utf-8"), filename=str(plano))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "DIAS" for t in node.targets
        ):
            return [tuple(x) for x in ast.literal_eval(node.value)]
    raise ValueError(f"{plano}: atribuição DIAS = [...] não encontrada")


# ---------------------------------------------------------------- geração

def _card(nome, url, destino):
    """Tarefa do dia: url = caminho (gerado se existir), "?" (material a gerar) ou None (sem material)."""
    pend = url == "?"
    if url and not pend and destino and not url.startswith(("http://", "https://")):
        pend = not (pathlib.Path(destino) / url).is_file()
    return {"nome": nome, "url": None if pend else url, "id": mid(nome), "pend": pend}


def montar_dados(fases, dias_src, materiais, horas, feriados, revisao_dia=None, destino=None,
                 tarefas=None):
    tarefas = tarefas or {}
    dias = []
    for d, tipo, titulo, det, tags, curto in dias_src:
        dt_ = D(d)
        dias.append({
            "id": dt_.isoformat(), "dm": d, "dow": DOW[dt_.weekday()], "tipo": tipo,
            "titulo": titulo, "det": det,
            "tags": tags.split() if tags else [], "curto": curto, "h": horas(d, tipo),
            "feriado": feriados.get(d),
            "mat": [_card(n, u, destino) for n, u in (tarefas.get(d) or materiais.get(d, []))],
            "tar": d in tarefas,
        })

    # revisão espaçada: conteúdos novos voltam em D+2, D+7 e D+21;
    # dia sem espaço (prova, simulado, leve) empurra para o próximo dia livre
    idx = {x["id"]: x for x in dias}
    for x in dias:
        x["rev"] = []
    for x in dias:
        if not x["curto"]:
            continue
        for k in (2, 7, 21):
            alvo = dt.date.fromisoformat(x["id"]) + dt.timedelta(days=k)
            adiada = False
            while alvo.isoformat() in idx and idx[alvo.isoformat()]["tipo"] in ("prova", "sim", "leve"):
                alvo += dt.timedelta(days=1)
                adiada = True
            if alvo.isoformat() in idx:
                idx[alvo.isoformat()]["rev"].append({
                    "t": f'{x["curto"]} (D+{k}{", adiada" if adiada else ""})',
                    "mat": x["mat"], "tags": x["tags"], "de": x["dm"],
                })

    # folha de revisão do dia (opcional): um link por dia no lugar da lista espaçada
    for x in dias:
        x["rd"] = None
        if not revisao_dia:
            continue
        mins = revisao_dia["min"](x["dm"], x["tipo"])
        pasta = pathlib.Path(destino) / revisao_dia["pasta"] if destino else None
        arq = f'{x["id"]}.html'
        existe = bool(pasta and (pasta / arq).is_file())
        futuro = x["id"] >= dt.date.today().isoformat()
        if mins and (existe or (x["rev"] and futuro)):
            x["rd"] = {"min": mins, "url": f'{revisao_dia["pasta"]}/{arq}' if existe else None,
                       "n": len(x["rev"])}
            if x["tar"]:
                x["mat"].insert(0, _card(f'Revisão do dia (≤{mins} min)', x["rd"]["url"] or "?", None))

    # semanas seg→dom
    sem = []
    for x in dias:
        d = dt.date.fromisoformat(x["id"])
        seg = d - dt.timedelta(days=d.weekday())
        if not sem or sem[-1]["seg"] != seg.isoformat():
            sem.append({"seg": seg.isoformat(), "dias": []})
        sem[-1]["dias"].append(x["id"])
    for i, s in enumerate(sem):
        s["n"] = i + 1

    return {"fases": fases, "dias": dias, "semanas": sem}, idx


def _celula_rev(x):
    if x.get("tar"):
        return "nos cards"
    if "rd" in x and x["rd"] is not None:
        r = x["rd"]
        return f'[folha do dia, ≤{r["min"]} min]({r["url"]})' if r["url"] else f'a gerar (≤{r["min"]} min)'
    if x.get("rd_modo"):
        return "—"
    return ", ".join(r["t"] for r in x["rev"]) or "—"


def montar_md(data, idx, *, md_cabecalho, md_rodape, md_fase, md_pos_fases,
              md_sep_semana, md_feriado):
    L = list(md_cabecalho)
    for f in data["fases"]:
        L.append(md_fase.format(**f))
    L += list(md_pos_fases)
    for s in data["semanas"]:
        ds = [idx[i] for i in s["dias"]]
        L += [f'## Semana {s["n"]} ({ds[0]["dm"]} → {ds[-1]["dm"]})', "",
              f'| Dia | Data | Tipo | Bloco | {"Revisão do dia" if data.get("rd_modo") else "Revisão espaçada"} |',
              md_sep_semana]
        for x in ds:
            bold = "**" if x["tipo"] == "prova" else ""
            fer = md_feriado.format(x["feriado"]) if x["feriado"] else ""
            if x.get("tar"):
                fer += " · " + " · ".join(
                    f'☐ [{m["nome"]}]({m["url"]})' if m["url"] else f'☐ {m["nome"]}{" (a gerar)" if m["pend"] else ""}'
                    for m in x["mat"])
                bloco = f'**{x["titulo"]}**{fer}'
            else:
                fer += "".join(f' · [material: {m["nome"]}]({m["url"]})' for m in x["mat"] if m["url"])
                bloco = f'**{x["titulo"]}**: {x["det"]}{fer}'
            L.append(
                f'| {x["dow"]} | {bold}{x["dm"]}{bold} | {TIPO[x["tipo"]]} | '
                f'{bloco} | {_celula_rev(x)} |'
            )
        L.append("")
    L += list(md_rodape)
    return "\n".join(L) + "\n"


def listar_revisao(data, dm, destino):
    """Imprime o que vence em `dm` (DD/MM) e as lacunas abertas/em reforço das tags (PyYAML)."""
    x = next((d for d in data["dias"] if d["dm"] == dm), None)
    if not x:
        sys.exit(f"{dm} fora do plano")
    rd = x.get("rd") or {}
    print(f'{x["dow"]} {dm} · {x["titulo"]} · limite {rd.get("min", "—")} min')
    if not x["rev"]:
        print("nada vence neste dia")
        return x
    try:
        import yaml
        ent = yaml.safe_load((pathlib.Path(destino) / "lacunas.yaml").read_text(encoding="utf-8"))["entradas"]
    except Exception:
        ent = []
    for r in x["rev"]:
        print(f'- {r["t"]} · estudado em {r["de"]} · tags: {" ".join(r["tags"]) or "—"}')
        for m in r["mat"]:
            print(f'    material: {m["nome"]} → {m["url"]}')
        for e in ent:
            if e.get("status") in ("aberto", "em_reforco") and set(str(e.get("tag", "")).split()) & set(r["tags"]):
                print(f'    lacuna [{e["status"]}] {e["id"]}: {str(e.get("tema", ""))[:110]}')
    return x


def gerar(destino, *, trilha, fases, dias, horas, md_cabecalho, md_rodape,
          materiais=None, feriados=None,
          md_fase="| **{id} — {nome}** | {ini} → {fim} | {obj} |",
          md_pos_fases=("",),
          md_sep_semana="|-----|------|------|-------|------------------|",
          md_feriado=" · feriado ({})",
          template="template.html", revisao_dia=None, tarefas=None):
    """Valida as tags e grava `plano.md` e `cronograma.html` em `destino`.

    - `destino`: pasta do plano (normalmente `pathlib.Path(__file__).resolve().parent`).
    - `trilha`: tic (mapa usado na validação das tags).
    - `horas(d, tipo)`: horas planejadas do dia (regra pessoal).
    - `md_cabecalho`: linhas antes das linhas da tabela de fases (incluindo o cabeçalho dela).
    - `md_fase`: formato de cada linha de fase (chaves de FASES).
    - `md_pos_fases`, `md_rodape`: linhas depois das fases e no fim do arquivo.
    - `revisao_dia` (opcional): `{"pasta": "../revisao/dia", "min": f(dm, tipo) -> minutos|None}`.
      Troca a lista de revisão espaçada por um link à folha do dia (`<pasta>/AAAA-MM-DD.html`,
      relativa a `destino`), com limite de tempo; sem a folha, mostra "a gerar".
      `python3 plano.py --revisao DD/MM` lista o que vence no dia e as lacunas das tags, sem gravar.
    - `tarefas` (opcional): `{"DD/MM": [(rótulo, url), ...]}`, tudo o que a pessoa faz no dia, um card de
      check por tarefa (substitui `materiais` e o texto do dia no painel). `url` = caminho relativo a
      `destino` (card pontilhado "a gerar" se o arquivo não existir), `"?"` (material ainda a gerar) ou
      `None` (tarefa sem material). Com `revisao_dia`, a folha do dia entra como primeiro card.
    """
    destino = pathlib.Path(destino)
    erros = erros_tags_dias(dias, trilha)
    if erros:
        print("ERRO: tags de DIAS fora do mapa — nada foi gerado:", file=sys.stderr)
        for e in erros:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(2)

    data, idx = montar_dados(fases, dias, materiais or {}, horas, feriados or {},
                             revisao_dia=revisao_dia, destino=destino, tarefas=tarefas)
    if revisao_dia:
        data["rd_modo"] = True
        for x in data["dias"]:
            x["rd_modo"] = True
    if "--revisao" in sys.argv:
        dm = sys.argv[sys.argv.index("--revisao") + 1]
        return listar_revisao(data, dm, destino)
    md = montar_md(data, idx, md_cabecalho=md_cabecalho, md_rodape=md_rodape,
                   md_fase=md_fase, md_pos_fases=md_pos_fases,
                   md_sep_semana=md_sep_semana, md_feriado=md_feriado)
    (destino / "plano.md").write_text(md, encoding="utf-8")
    plano = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = (destino / template).read_text(encoding="utf-8").replace("__PLANO__", plano)
    (destino / "cronograma.html").write_text(html, encoding="utf-8")
    print("gerados: plano.md, cronograma.html")
    print(f'dias={len(data["dias"])} semanas={len(data["semanas"])}')
    return data
