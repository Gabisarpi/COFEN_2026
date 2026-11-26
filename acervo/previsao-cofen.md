# Prioridade de estudo — COFEN 2026 · Cargo 407

Gerado por `tools/acervo_previsao.py` em **2026-11-26** · 1399 assertivas oficiais etiquetadas.

Score = mistura da faixa-base do perfil com a frequência no acervo (Quadrix ×2, demais ×1),
o acervo pesa mais à medida que a tag se aproxima de 30 assertivas oficiais.
Faixa = tercil dentro do bloco. **Ranking de estudo, não probabilidade de cair na prova.**

## P1 Básicos

| # | Tag | Faixa | Score | Oficiais | Âncoras | Bancas |
|---|-----|-------|-------|----------|---------|--------|
| 1 | `basicos.lp` | alta | 5.55 | 188 | 0 | quadrix:188 |
| 2 | `basicos.rlm` | média | 5.08 | 99 | 0 | quadrix:99 |
| 3 | `basicos.ingles` | baixa | 5.04 | 110 | 0 | quadrix:110 |

## P2 Complementares

| # | Tag | Faixa | Score | Oficiais | Âncoras | Bancas |
|---|-----|-------|-------|----------|---------|--------|
| 1 | `comp.leg.improbidade` | alta | 4.31 | 54 | 0 | quadrix:54 |
| 2 | `comp.leg.processo` | alta | 4.19 | 39 | 0 | quadrix:39 |
| 3 | `comp.leg.licitacoes` | alta | 3.89 | 2 | 0 | quadrix:2 |
| 4 | `comp.leg.enfermagem` | média | 3.74 | 15 | 0 | quadrix:15 |
| 5 | `comp.leg.lgpd` | média | 3.72 | 27 | 0 | quadrix:27 |
| 6 | `comp.adm` | média | 3.66 | 37 | 0 | quadrix:37 |
| 7 | `comp.leg.cf` | baixa | 2.74 | 8 | 0 | quadrix:8 |
| 8 | `comp.const` | baixa | 2.52 | 7 | 0 | quadrix:7 |
| 9 | `comp.leg.anticorrupcao` | baixa | 2.49 | 16 | 0 | quadrix:16 |

## P3 Específicos

| # | Tag | Faixa | Score | Oficiais | Âncoras | Bancas |
|---|-----|-------|-------|----------|---------|--------|
| 1 | `esp.tic.infra` | alta | 5.32 | 166 | 0 | quadrix:166 |
| 2 | `esp.tic.seguranca` | alta | 5.06 | 106 | 0 | quadrix:106 |
| 3 | `esp.tic.fundamentos` | alta | 5.02 | 85 | 0 | quadrix:85 |
| 4 | `esp.tic.redes` | alta | 4.73 | 82 | 0 | quadrix:82 |
| 5 | `esp.tic.govti` | média | 4.60 | 49 | 0 | quadrix:49 |
| 6 | `esp.tic.engsw` | média | 4.55 | 107 | 0 | quadrix:107 |
| 7 | `esp.tic.bd` | média | 4.46 | 81 | 0 | quadrix:81 |
| 8 | `esp.tic.etica` | média | 4.35 | 45 | 0 | quadrix:45 |
| 9 | `esp.tic.contratos` | baixa | 3.90 | 23 | 0 | quadrix:23 |
| 10 | `esp.tic.auditoria` | baixa | 3.89 | 2 | 0 | quadrix:2 |
| 11 | `esp.tic.gestao` | baixa | 3.83 | 20 | 0 | quadrix:20 |
| 12 | `esp.tic.atendimento` | baixa | 2.43 | 20 | 0 | quadrix:20 |

## Discursiva

| # | Tag | Faixa | Score | Oficiais | Âncoras | Bancas |
|---|-----|-------|-------|----------|---------|--------|
| 1 | `disc.tic` | alta | 3.67 | 11 | 0 | quadrix:11 |

## Como atualizar

```bash
python3 tools/acervo_cobertura.py --write
python3 tools/acervo_previsao.py --write
```
