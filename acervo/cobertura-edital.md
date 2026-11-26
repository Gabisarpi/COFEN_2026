# Cobertura do acervo × edital

Gerado por `tools/acervo_cobertura.py` em **2026-11-26** · 285 arquivos em `acervo/itens/`.

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
| `basicos.lp` | 188 | 158 | 376 | quadrix:188 | 🟢 ok |
| `basicos.rlm` | 99 | 89 | 198 | quadrix:99 | 🟢 ok |
| `basicos.ingles` | 110 | 92 | 220 | quadrix:110 | 🟢 ok |

### Heatmap (top peso)

- `basicos.lp` — peso 376 (188 assertivas)
- `basicos.ingles` — peso 220 (110 assertivas)
- `basicos.rlm` — peso 198 (99 assertivas)

## comp

| Tag | Assertivas | Alta | Peso | Bancas | Gap |
|-----|------------|------|------|--------|-----|
| `comp.leg.enfermagem` | 15 | 15 | 30 | quadrix:15 | 🟢 ok |
| `comp.leg.cf` | 8 | 8 | 16 | quadrix:8 | 🟡 4 |
| `comp.leg.licitacoes` | 2 | 2 | 4 | quadrix:2 | 🟡 10 |
| `comp.leg.improbidade` | 54 | 43 | 108 | quadrix:54 | 🟢 ok |
| `comp.leg.lgpd` | 27 | 24 | 54 | quadrix:27 | 🟢 ok |
| `comp.leg.processo` | 39 | 35 | 78 | quadrix:39 | 🟢 ok |
| `comp.leg.anticorrupcao` | 16 | 16 | 32 | quadrix:16 | 🟢 ok |
| `comp.const` | 7 | 2 | 14 | quadrix:7 | 🟡 5 |
| `comp.adm` | 37 | 23 | 74 | quadrix:37 | 🟢 ok |

### Heatmap (top peso)

- `comp.leg.improbidade` — peso 108 (54 assertivas)
- `comp.leg.processo` — peso 78 (39 assertivas)
- `comp.adm` — peso 74 (37 assertivas)
- `comp.leg.lgpd` — peso 54 (27 assertivas)
- `comp.leg.anticorrupcao` — peso 32 (16 assertivas)
- `comp.leg.enfermagem` — peso 30 (15 assertivas)
- `comp.leg.cf` — peso 16 (8 assertivas)
- `comp.const` — peso 14 (7 assertivas)

## especificos

| Tag | Assertivas | Alta | Peso | Bancas | Gap |
|-----|------------|------|------|--------|-----|
| `esp.tic.fundamentos` | 85 | 80 | 170 | quadrix:85 | 🟢 ok |
| `esp.tic.redes` | 82 | 67 | 164 | quadrix:82 | 🟢 ok |
| `esp.tic.seguranca` | 106 | 91 | 212 | quadrix:106 | 🟢 ok |
| `esp.tic.bd` | 81 | 56 | 162 | quadrix:81 | 🟢 ok |
| `esp.tic.engsw` | 107 | 66 | 214 | quadrix:107 | 🟢 ok |
| `esp.tic.govti` | 49 | 49 | 98 | quadrix:49 | 🟢 ok |
| `esp.tic.etica` | 45 | 41 | 90 | quadrix:45 | 🟢 ok |
| `esp.tic.gestao` | 20 | 20 | 40 | quadrix:20 | 🟢 ok |
| `esp.tic.auditoria` | 2 | 2 | 4 | quadrix:2 | 🟡 8 |
| `esp.tic.contratos` | 23 | 23 | 46 | quadrix:23 | 🟢 ok |
| `esp.tic.atendimento` | 20 | 10 | 40 | quadrix:20 | 🟢 ok |
| `esp.tic.infra` | 166 | 131 | 332 | quadrix:166 | 🟢 ok |

### Heatmap (top peso)

- `esp.tic.infra` — peso 332 (166 assertivas)
- `esp.tic.engsw` — peso 214 (107 assertivas)
- `esp.tic.seguranca` — peso 212 (106 assertivas)
- `esp.tic.fundamentos` — peso 170 (85 assertivas)
- `esp.tic.redes` — peso 164 (82 assertivas)
- `esp.tic.bd` — peso 162 (81 assertivas)
- `esp.tic.govti` — peso 98 (49 assertivas)
- `esp.tic.etica` — peso 90 (45 assertivas)

## disc

| Tag | Assertivas | Alta | Peso | Bancas | Gap |
|-----|------------|------|------|--------|-----|
| `disc.tic` | 11 | 10 | 22 | quadrix:11 | 🟢 ok |

### Heatmap (top peso)

- `disc.tic` — peso 22 (11 assertivas)

## Como atualizar

```bash
python3 tools/acervo_cobertura.py --write
python3 tools/acervo_cobertura.py --write --write-catalogo
```
