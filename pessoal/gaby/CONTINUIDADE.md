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
- **Skills adaptadas (26/11):** 10 skills `cofen-*` em `.agents/skills/` (Quadrix, +1/−1 em tudo, 120 itens 40/30/50, discursiva única de 20–30 linhas, tags `esp.tic.*`) + scripts em `tools/`. Builds testados (caderno, flashcards, folha, editor de redação, correção). Ranking inicial em `acervo/previsao-cofen.md` vem só do perfil, porque o acervo está vazio.
- Foco atual ainda é a CGU (prova 13/12/2026). Estudo COFEN começa depois, salvo decisão em contrário.

## Pendências

- [ ] Fazer a inscrição (26/11/2026 a 11/01/2027, taxa R$ 100).
- [ ] Colocar o `edital.pdf` oficial (quadrix.org.br) na raiz do repo.
- [ ] Conferir no item 2 do edital se o 407 tem 1 vaga imediata ou só cadastro de reserva.
- [ ] Montar acervo de provas Quadrix de TI (conselhos profissionais de preferência).
- [ ] Na primeira prova Quadrix ingerida, conferir o extrator (`tools/acervo_extract_quadrix.py`) contra o PDF.
- [ ] Montar a amostra de dificuldade em `cargos/tic/amostra/` (~25 itens reais Quadrix).
- [ ] Windows: `git config core.symlinks true` no clone local (symlinks `.claude/skills` e `.cursor/skills`).
- [ ] Montar cronograma 14/12/2026 → 27/02/2027.
