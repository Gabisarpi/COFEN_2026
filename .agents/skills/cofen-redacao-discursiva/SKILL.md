---
name: cofen-redacao-discursiva
description: >-
  Gera o editor HTML da discursiva do COFEN 2026 (Cargo 407): texto
  dissertativo de 20 a 30 linhas, folha única, tema escuro, Enter = nova linha
  e wrap por palavra, aviso abaixo do mínimo, autosave, export resposta.md,
  painel de pedidos do enunciado e lista pessoal de erros de língua. Também
  questões discursivas curtas com campos individuais. Use quando a pessoa
  pedir editor de redação, HTML de discursiva, redacao.html, contar linhas, ou
  depois de gerar discursiva.md quando ela for escrever na tela.
---

# COFEN — Redação discursiva (HTML)

Complementa `cofen-simulado-quadrix` (enunciado e padrão em MD) com a **folha interativa**. Depois de exportar, a correção segue o simulado + `cofen-diagnostico-gaps`.

## Quando acionar

1. Pedido de editor / `redacao.html` / contar linhas
2. Depois de gravar `discursiva.md`, se a Gaby for escrever no navegador
3. Não usar para objetiva C/E (isso é `cofen-material-nucleos`)

## Régua da prova (edital COFEN)

| Regra | Valor |
|-------|------:|
| Extensão | **20 a 30 linhas** (`min: 20`, `max: 30`) |
| Valor | 10 pontos · nota = [(CAC × 7) + (OT × 1,5) + (DLP × 1,5)] ÷ 3 |
| Aprovação | ≥ 5,00 |
| Enter (`\n`) | 1 linha na folha |
| Wrap | linha física > `width` (default 60) quebra por palavra e conta o excedente |

O contador fica vermelho abaixo de 20 e acima de 30 linhas.

## Destino

```text
$P/simulados/gerados/YYYY-MM-DD_discursiva_<tema>/
  discursiva.md
  discursiva-padrao-resposta.md
  meta.yaml          # do simulado
  meta-redacao.json  # desta skill
  enunciado.html     # miolo do enunciado
  redacao.html       # saída do build
```

Resposta → `$P/respostas/YYYY-MM-DD_…/resposta.md`. **Não** gravar o editor em `$P/revisao/`.

## Fluxo

1. Ter `discursiva.md` no diretório do gerado.
2. Extrair o miolo para `enunciado.html` (HTML sem `<section>`).
3. Escrever `meta-redacao.json` (ver `references/meta.exemplo.json`), com **`pedidos`**: um texto curto por aspecto/verbo de comando do enunciado. O editor mostra o painel **Pedidos do enunciado** e pede confirmação ao exportar com pedido desmarcado.
4. Build:

```bash
python3 .agents/skills/cofen-redacao-discursiva/scripts/build.py \
  --meta $DIR/meta-redacao.json \
  --enunciado $DIR/enunciado.html \
  --lp-erros pessoal/gaby/revisao/lp-erros.md \
  --out $DIR/redacao.html
```

   `--lp-erros` é opcional: com o arquivo (âncoras `- errado → certo`, mantidas pela `cofen-diagnostico-gaps`), aparece o bloco **Antes de entregar**.

5. Se houver `plano.py` com `MATERIAIS`/`TAREFAS`, ligar o editor no dia (ver `cofen-diagnostico-gaps`).
6. Gaby escreve → Baixar/Copiar `resposta.md` → `$P/respostas/…` → “corrigir discursiva”.

`key` do meta é **único** por editor (localStorage). Ex.: `cofen-gaby-disc-<tema>-YYYY-MM-DD`.

## Discursivas curtas (treino)

Um campo e um contador por questão, autosave e export conjunto em `resposta.md`. O `build.py` atende só à folha única; para curtas, montar a partir do template, com limites conforme o pedido, preservando Enter e wrap.

## Arquivos da skill

| Path | Papel |
|------|-------|
| `assets/redacao.template.html` | Folha escura + contador (mín./máx.) + export MD |
| `scripts/build.py` | Injeta `{{TITLE}}` … `{{ENUNCIADO}}`, `{{MIN}}`, `{{MAX}}` |
| `references/meta.exemplo.json` | Contrato do meta |
| `references/enunciado.exemplo.html` | Miolo de exemplo (fiscalização de contrato de TIC) |

## Anti-padrões

- Entregar só MD quando a Gaby pediu para escrever no HTML
- Contar linhas só por parágrafo e ignorar Enter simples
- Usar limites diferentes de 20–30 na discursiva de prova sem pedido expresso
- Gerar o editor sem extrair os `pedidos`
