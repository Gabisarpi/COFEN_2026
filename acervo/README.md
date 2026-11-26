# Acervo — provas Quadrix (COFEN 2026 · Cargo 407)

- `catalogo.yaml` — provas ingeridas (órgão, cargo, código, URLs, aderência, notas) + blocos `cobertura*`.
- `fontes/<id>/` — `prova.pdf` + `gabarito.pdf` (gabarito definitivo, com todos os cargos do concurso).
- `itens/<id>_bNN.md` — um arquivo por **bloco de comando**, com as tags do mapa do 407 (`tags_edital`).
- `cobertura-edital.md` — heatmap (assertivas por tag × meta) · `previsao-cofen.md` — ranking de estudo.

## Situação (26/11/2026)

7 provas Quadrix C/E de TI, nível superior, **840 assertivas** com gabarito definitivo, em 182 blocos. Todas conferidas automaticamente contra o PDF (texto de cada item reencontrado no caderno).

| Prova | Cargo | Por que importa |
|-------|-------|-----------------|
| `cref11_2026_analista_suporte_ti` | Analista de Suporte em TI (402) | **Mais aderente:** o P3 tem os mesmos blocos exclusivos do 407 (governança e gestão, normas e auditorias, contratos, atendimento estratégico, implantação e migração) |
| `coren_pr_2024_analista_ti` | Analista de TI (402) | Sistema Cofen/Corens: Lei 5.905, Regimento do Coren, Res. COFEN 507/2016 e 564/2017 |
| `crp_sp_2025_especialista_gestao_tic` | Especialista em Gestão de TIC (408) | ITIL 4, COBIT 2019, ISO 27001/27002, indicadores |
| `crmv_go_2025_analista_adm_ti` | Analista Adm. – TI (400) | Constitucional, Administrativo, ITIL 4/COBIT, Lei 14.133 |
| `cro_sp_2025_analista_suporte_ti` | Analista de Suporte de TI (407) | Improbidade, anticorrupção, contratos de TI, SLA/OLA |
| `coffito_2023_analista_ti` | Analista de TI (403) | LAI, LGPD, processo administrativo |
| `ibict_2024_tecnologista_ti` | Tecnologista – TI (404) | Aderência média (desenvolvimento, ciência da informação) |

Blocos com `tags_edital: []` = fora do edital do 407 (atualidades, leis e resoluções de outros conselhos, metodologia científica). Ficam no acervo como exemplo de estilo, mas não entram no heatmap.

## Lacunas do acervo

- **Exclusivos do 407** (`esp.tic.gestao`, `auditoria`, `contratos`, `atendimento`): poucos itens; só o CREF-11 2026 cobra os blocos com esse nome.
- **Discursivas:** não coletadas (os cadernos são só da objetiva). `disc.tic` está vazio.
- `comp.const`, `comp.leg.licitacoes`: abaixo da meta.

## Como ingerir outra prova

1. Criar `acervo/fontes/<orgao>_<ano>_<cargo>/` com `prova.pdf` e `gabarito.pdf`.
2. `python3 tools/acervo_extract_quadrix.py --id <id> --orgao … --ano … --cargo "<título do cabeçalho da prova>" --gab-cargo "<regex do cargo no gabarito>" --dry` (relatório) e, se 120/120, sem `--dry`.
3. Rever as tags dos blocos; correções manuais em `tools/acervo_ajustes_quadrix.yaml`.
4. Acrescentar a prova em `catalogo.yaml` → `fontes` e rodar `python3 tools/acervo_cobertura.py --write --write-catalogo` e `python3 tools/acervo_previsao.py --write`.

Requer `pdftotext` (poppler) e `pip install pdfplumber pyyaml`.
