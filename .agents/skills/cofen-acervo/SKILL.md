---
name: cofen-acervo
description: >-
  Ingere e indexa o acervo de provas do COFEN 2026 (Quadrix primeiro, outras
  bancas C/E como apoio): download de provas públicas, normalização
  objetiva/discursiva, tags do mapa do Cargo 407, heatmap de cobrança × edital.
  Use quando a pessoa pedir ingerir prova, baixar prova Quadrix, montar acervo,
  atualizar heatmap, cobertura do edital, lacunas de acervo P1/P2/P3,
  discursiva no acervo ou o que a banca mais cobra.
---

# COFEN — Acervo (ingestão + heatmap)

Projeto: raiz `COFEN_2026`. Geração/correção → `cofen-simulado-quadrix`. Lacunas/cronograma → `cofen-diagnostico-gaps`.

## Âncoras

1. `REPO.md` + `AGENTS.md`
2. `acervo/README.md` + `acervo/catalogo.yaml` (criar na primeira ingestão) + `acervo/itens/_SCHEMA.exemplo.md`
3. Mapa: `cargos/tic/mapa-edital.md` · perfil: `cargos/tic/perfil.md`
4. Script: `python3 tools/acervo_cobertura.py` → `acervo/cobertura-edital.md`

## Bancas

| Banca | Campo | Uso |
|-------|-------|-----|
| Quadrix | `banca: quadrix` | Estilo dos simulados; peso ×2 no heatmap |
| Cebraspe e outras C/E | `banca: cebraspe` etc. | Frequência de conteúdo; peso ×1; **não** modelo de estilo |

**Prioridade de provas Quadrix:** cargos de TI em conselhos profissionais (Sistema Cofen/Corens, CFM/CRMs, CFO/CROs, CFMV/CRMVs, CAU, CFN, CFF, CRF), depois outros órgãos com Quadrix C/E em TI. Provas de nível superior com legislação de conselhos também servem ao P2 (`comp.adm`, conselhos de fiscalização).

Fontes públicas apenas: site da Quadrix (concursos encerrados → provas e gabaritos) ou divulgação oficial do órgão. Sem material pago de cursinho.

## Ingestão

1. Criar `acervo/fontes/{orgao}_{ano}_{slug}/` (ex.: `coren_sp_2024_analista_ti`).
2. Baixar: prova objetiva, **gabarito definitivo**, discursiva + padrão (se houver).
3. Registrar em `acervo/catalogo.yaml` → `fontes` (`banca`, `cargo`, `status`, URLs; `discursiva: nao_aplicavel` quando não houver).
4. Extrair: `python3 tools/acervo_extract_quadrix.py --id <id> --orgao … --ano … --cargo "<título no cabeçalho da prova>" --gab-cargo "<regex do cargo no gabarito>" --dry`. Só gravar (sem `--dry`) com 120/120 itens lidos. Gera um arquivo por bloco de comando (`<id>_bNN.md`), já etiquetado pelas regras de `tools/acervo_tags_407.py`.
5. Rever as tags e o comando de cada bloco; o que a regra errar vai para `tools/acervo_ajustes_quadrix.yaml` (vale em toda nova extração). Conferir alguns itens contra o PDF.
6. Rodar `python3 tools/acervo_cobertura.py --write --write-catalogo` e `python3 tools/acervo_previsao.py --write`.
7. Conferir buracos (`[texto não extraído]`, `[ver PDF]`); não inventar enunciado.

Layout Quadrix tratado pelo extrator: duas colunas, marca d'água "Prova aplicada", números de linha dos textos (corpo 7), trechos de código em Courier e frações empilhadas (viram `n/d`). Anulados ficam com gabarito `X`.

### Schema do item

```yaml
---
id: orgao_ano_slug
orgao: ORGAO
ano: 2024
banca: quadrix
cargo: ...
prova: P1|P2|P3|P4|mista
formato: certo_errado   # ou multipla_escolha_A-E
tags_edital: []         # basicos.* / comp.* / esp.tic.* / disc.tic
temas: []               # especialmente discursiva
aderencia: alta|media|baixa
fonte:
  path: acervo/fontes/.../prova.pdf
---
```

- Múltipla escolha da Quadrix entra como `formato: multipla_escolha_A-E` (vale para frequência de conteúdo; convertida para C/E vira item inédito, `real:0`).
- **Não inventar gabarito** sem gabarito oficial.

### Reaproveitar o acervo do CGU

O repo `MarcosExing/CGU_2026` tem centenas de itens Cebraspe de TI (redes, segurança, ITIL/COBIT, contratação). Podem entrar com `banca: cebraspe`, peso ×1, retag para `esp.tic.*`, **só como frequência de conteúdo** e par de inversão — não como molde de estilo.

## Heatmap / prioridade

1. `python3 tools/acervo_cobertura.py --write` → ranking por tag × banca e buracos vs mapa.
2. `python3 tools/acervo_previsao.py --write` → `acervo/previsao-cofen.md` (faixas de estudo, não previsão binária).
3. As outras skills cruzam esse ranking com `pessoal/gaby/cronograma/lacunas.yaml`.

## O que esta skill não faz

- Gerar caderno / corrigir → `cofen-simulado-quadrix`
- Mexer no cronograma → `cofen-diagnostico-gaps`

Editar só `.agents/skills/cofen-acervo/`. Conferir: `python3 tools/sync_skills.py --check`.
