# Cobertura do acervo × edital

Gerado por `tools/acervo_cobertura.py` em **2026-11-26** · 0 arquivos em `acervo/itens/`.

Contagem: **assertivas** na tabela do item (ou 1 se discursiva/sem tabela). Peso heatmap: Quadrix×2, demais bancas×1.

## Metas (plano)

| Bloco | Meta assertivas/tag |
|-------|---------------------|
| P1 `basicos.*` | ≥15 |
| P2 `comp.*` | ≥12 |
| P3 `esp.tic.*` | ≥10 |
| Discursiva `disc.*` | ≥8 arquivos/tag |

## basicos

| Tag | Assertivas | Alta | Peso | Bancas | Gap |
|-----|------------|------|------|--------|-----|
| `basicos.lp` | 0 | 0 | 0 | — | 🔴 15 |
| `basicos.rlm` | 0 | 0 | 0 | — | 🔴 15 |
| `basicos.ingles` | 0 | 0 | 0 | — | 🔴 15 |

## comp

| Tag | Assertivas | Alta | Peso | Bancas | Gap |
|-----|------------|------|------|--------|-----|
| `comp.leg.enfermagem` | 0 | 0 | 0 | — | 🔴 12 |
| `comp.leg.cf` | 0 | 0 | 0 | — | 🔴 12 |
| `comp.leg.licitacoes` | 0 | 0 | 0 | — | 🔴 12 |
| `comp.leg.improbidade` | 0 | 0 | 0 | — | 🔴 12 |
| `comp.leg.lgpd` | 0 | 0 | 0 | — | 🔴 12 |
| `comp.leg.processo` | 0 | 0 | 0 | — | 🔴 12 |
| `comp.leg.anticorrupcao` | 0 | 0 | 0 | — | 🔴 12 |
| `comp.const` | 0 | 0 | 0 | — | 🔴 12 |
| `comp.adm` | 0 | 0 | 0 | — | 🔴 12 |

## especificos

| Tag | Assertivas | Alta | Peso | Bancas | Gap |
|-----|------------|------|------|--------|-----|
| `esp.tic.fundamentos` | 0 | 0 | 0 | — | 🔴 10 |
| `esp.tic.redes` | 0 | 0 | 0 | — | 🔴 10 |
| `esp.tic.seguranca` | 0 | 0 | 0 | — | 🔴 10 |
| `esp.tic.bd` | 0 | 0 | 0 | — | 🔴 10 |
| `esp.tic.engsw` | 0 | 0 | 0 | — | 🔴 10 |
| `esp.tic.govti` | 0 | 0 | 0 | — | 🔴 10 |
| `esp.tic.etica` | 0 | 0 | 0 | — | 🔴 10 |
| `esp.tic.gestao` | 0 | 0 | 0 | — | 🔴 10 |
| `esp.tic.auditoria` | 0 | 0 | 0 | — | 🔴 10 |
| `esp.tic.contratos` | 0 | 0 | 0 | — | 🔴 10 |
| `esp.tic.atendimento` | 0 | 0 | 0 | — | 🔴 10 |
| `esp.tic.infra` | 0 | 0 | 0 | — | 🔴 10 |

## disc

| Tag | Assertivas | Alta | Peso | Bancas | Gap |
|-----|------------|------|------|--------|-----|
| `disc.tic` | 0 | 0 | 0 | — | 🔴 8 |

## Como atualizar

```bash
python3 tools/acervo_cobertura.py --write
python3 tools/acervo_cobertura.py --write --write-catalogo
```
