# Continuidade — Gaby (COFEN 2026 · Cargo 407 Analista de TIC)

Prova: **28/02/2027, tarde** · Banca: Quadrix C/E · `$P = pessoal/gaby/` · `$C = cargos/tic/`

## Ler nesta ordem

1. `REPO.md` + `AGENTS.md`
2. Este arquivo
3. `$C/perfil.md` → `$C/mapa-edital.md` + `$C/resumo-edital.md`
4. Cronograma: `$P/cronograma/` · ledger `$P/cronograma/lacunas.yaml`

## Material do dia (formato fixo, herdado do CGU)

| Peça | Onde |
|------|------|
| Folha de estudo `.md` + `.pdf` e gabarito comentado separado | `revisao/YYYY-MM-DD_tema.*` |
| Itens C/E novos (estilo Quadrix) + reais da banca, gabarito separado, `meta.yaml` | `simulados/gerados/YYYY-MM-DD_tema/` |
| Fonte NotebookLM | `audio/notebooklm/YYYY-MM-DD_tema.md` |
| Flashcards `.tsv` **e** `_notebooklm.md` | `flashcards/` |

## Estado (2026-11-26) — ONDE PARAMOS

- Repo criado com a estrutura espelhada do CGU_2026.
- Edital resumido em `cargos/tic/resumo-edital.md`; tags em `mapa-edital.md`.
- **Skills adaptadas (26/11):** 10 skills `cofen-*` em `.agents/skills/` (Quadrix, +1/−1 em tudo, 120 itens 40/30/50, discursiva única de 20–30 linhas, tags `esp.tic.*`) + scripts em `tools/`. Builds testados (caderno, flashcards, folha, editor de redação, correção). 
- **27/11: foco só no COFEN** (a inscrição da CGU foi perdida).

- **Acervo montado (26/11):** 7 provas Quadrix C/E de TI (840 assertivas, gabarito definitivo, conferidas contra o PDF) em `acervo/`; heatmap e ranking regenerados; amostra de dificuldade em `cargos/tic/amostra/2026-11-26_amostra_quadrix/`. Prova mais aderente: CREF-11 2026 (blocos iguais aos exclusivos do 407).

- **Acervo ampliado (26/11):** busca no site oficial da Quadrix (23 editais de conselhos triados). Entraram CREFITO-17 2026 (edital no molde do 407, agora a prova mais aderente), CFN 2024 (código 407), CFO 2024 e CRF-PR 2025: 1.320 assertivas em 11 provas. Discursivas: 11 temas reais de TI com o padrão de resposta da banca (`disc.tic` saiu do zero). Detalhes e fontes em `acervo/README.md`.

- **Cronograma (27/11):** `cronograma/plano.py` → `plano.md` + `cronograma.html`, de 27/11 a 27/02, todos os dias: 2 h até 14/12, 5 h de 15/12 a 03/01, 2 h depois (~245 h). Fase 1: P2 e exclusivos do 407; fase 2: simulado diagnóstico em 15/12 e todo o P3 técnico + P1; fase 3: rotação semanal com simulados em dois dias.

## Pendências

- [ ] Fazer a inscrição (26/11/2026 a 11/01/2027, taxa R$ 100).
- [ ] Colocar o `edital.pdf` oficial (quadrix.org.br) na raiz do repo.
- [ ] Conferir no item 2 do edital se o 407 tem 1 vaga imediata ou só cadastro de reserva.
- [ ] Acervo: `esp.tic.auditoria` segue com 2 itens; procurar provas Quadrix de 2026 que saírem com o molde do 407 (CREFITO-17 e CREF-11 foram as primeiras).
- [ ] Próximas provas a buscar no site oficial (vistas no PCI e no Gran, lista em `acervo/README.md`): CREFITO-18 2024, CFP 2024 TI (cadernos 407/408), CRQ-IV 2023, CREF-3 2023, CFO 2022, CRMV-SP 2022, CORE-PR 2021.
- [ ] Usar as 11 discursivas reais no treino (editor `cofen-redacao-discursiva`), começando pela do CREFITO-17.
- [ ] Windows: `git config core.symlinks true` no clone local (symlinks `.claude/skills` e `.cursor/skills`).
