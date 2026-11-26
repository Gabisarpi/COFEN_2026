# Cobertura do acervo × edital

Gerado por `tools/acervo_cobertura.py` em **2026-11-26** · 182 arquivos em `acervo/itens/`.

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
| `basicos.lp` | 126 | 116 | 252 | quadrix:126 | 🟢 ok |
| `basicos.rlm` | 59 | 59 | 118 | quadrix:59 | 🟢 ok |
| `basicos.ingles` | 70 | 62 | 140 | quadrix:70 | 🟢 ok |

### Heatmap (top peso)

- `basicos.lp` — peso 252 (126 assertivas)
- `basicos.ingles` — peso 140 (70 assertivas)
- `basicos.rlm` — peso 118 (59 assertivas)

## comp

| Tag | Assertivas | Alta | Peso | Bancas | Gap |
|-----|------------|------|------|--------|-----|
| `comp.leg.enfermagem` | 15 | 15 | 30 | quadrix:15 | 🟢 ok |
| `comp.leg.cf` | 8 | 8 | 16 | quadrix:8 | 🟡 4 |
| `comp.leg.licitacoes` | 2 | 2 | 4 | quadrix:2 | 🟡 10 |
| `comp.leg.improbidade` | 29 | 29 | 58 | quadrix:29 | 🟢 ok |
| `comp.leg.lgpd` | 8 | 8 | 16 | quadrix:8 | 🟡 4 |
| `comp.leg.processo` | 17 | 17 | 34 | quadrix:17 | 🟢 ok |
| `comp.leg.anticorrupcao` | 16 | 16 | 32 | quadrix:16 | 🟢 ok |
| `comp.const` | 2 | 2 | 4 | quadrix:2 | 🟡 10 |
| `comp.adm` | 16 | 13 | 32 | quadrix:16 | 🟢 ok |

### Heatmap (top peso)

- `comp.leg.improbidade` — peso 58 (29 assertivas)
- `comp.leg.processo` — peso 34 (17 assertivas)
- `comp.leg.anticorrupcao` — peso 32 (16 assertivas)
- `comp.adm` — peso 32 (16 assertivas)
- `comp.leg.enfermagem` — peso 30 (15 assertivas)
- `comp.leg.cf` — peso 16 (8 assertivas)
- `comp.leg.lgpd` — peso 16 (8 assertivas)
- `comp.leg.licitacoes` — peso 4 (2 assertivas)

## especificos

| Tag | Assertivas | Alta | Peso | Bancas | Gap |
|-----|------------|------|------|--------|-----|
| `esp.tic.fundamentos` | 66 | 66 | 132 | quadrix:66 | 🟢 ok |
| `esp.tic.redes` | 32 | 32 | 64 | quadrix:32 | 🟢 ok |
| `esp.tic.seguranca` | 33 | 33 | 66 | quadrix:33 | 🟢 ok |
| `esp.tic.bd` | 55 | 35 | 110 | quadrix:55 | 🟢 ok |
| `esp.tic.engsw` | 88 | 58 | 176 | quadrix:88 | 🟢 ok |
| `esp.tic.govti` | 33 | 33 | 66 | quadrix:33 | 🟢 ok |
| `esp.tic.etica` | 24 | 24 | 48 | quadrix:24 | 🟢 ok |
| `esp.tic.gestao` | 8 | 8 | 16 | quadrix:8 | 🟡 2 |
| `esp.tic.auditoria` | 2 | 2 | 4 | quadrix:2 | 🟡 8 |
| `esp.tic.contratos` | 12 | 12 | 24 | quadrix:12 | 🟢 ok |
| `esp.tic.atendimento` | 4 | 4 | 8 | quadrix:4 | 🟡 6 |
| `esp.tic.infra` | 53 | 48 | 106 | quadrix:53 | 🟢 ok |

### Heatmap (top peso)

- `esp.tic.engsw` — peso 176 (88 assertivas)
- `esp.tic.fundamentos` — peso 132 (66 assertivas)
- `esp.tic.bd` — peso 110 (55 assertivas)
- `esp.tic.infra` — peso 106 (53 assertivas)
- `esp.tic.seguranca` — peso 66 (33 assertivas)
- `esp.tic.govti` — peso 66 (33 assertivas)
- `esp.tic.redes` — peso 64 (32 assertivas)
- `esp.tic.etica` — peso 48 (24 assertivas)

## disc

| Tag | Assertivas | Alta | Peso | Bancas | Gap |
|-----|------------|------|------|--------|-----|
| `disc.tic` | 0 | 0 | 0 | — | 🔴 8 |

## Como atualizar

```bash
python3 tools/acervo_cobertura.py --write
python3 tools/acervo_cobertura.py --write --write-catalogo
```
