# Fonte NotebookLM — {{DATA}} — {{TEMA}}

Concurso: COFEN 2026 · Quadrix C/E · **Cargo 407 Analista de TIC**.
Objetivo: áudio para tempo ocioso (~30–45 min em **2 Audio Overviews**, A + B). Bônus, não substitui o bloco de estudo.

## Como gerar no NotebookLM

1. Crie o notebook `{{BLOCO}} — {{DATA}}` e faça upload **deste arquivo** (se quiser, também do PDF da folha do dia em `pessoal/gaby/revisao/`).
2. Studio → **Audio Overview** → *Personalizar* → cole o **Prompt A** → gerar.
3. Repita com o **Prompt B**.
4. Opcional: Studio → **Flashcards** / **Quiz** com o **Prompt C**.

**Prompt A ({{PARTE_A}}):**
> Em português do Brasil, explique só a PARTE A desta fonte para uma candidata ao concurso do COFEN (banca Quadrix, itens certo/errado). Formato: conceito → exemplo curto → uma pegadinha no estilo Quadrix lida em voz alta → resposta certo/errado com o motivo. Enfatize: {{ENFASES_A}}. Não invente artigo de lei, prazo ou número fora da fonte.

**Prompt B ({{PARTE_B}}):**
> Em português do Brasil, explique só a PARTE B desta fonte, no mesmo formato. Enfatize: {{ENFASES_B}}. Termine com uma rodada rápida de 8 afirmações certo/errado.

**Prompt C (quiz/flashcards):**
> Gere 20 itens certo/errado no estilo Quadrix sobre esta fonte: assertivas curtas, com troca de uma palavra da lei ou da norma (prazo, competência, “deverá” × “poderá”), meia-verdade e alguns itens certos contraintuitivos. Mostre o gabarito com justificativa curta.

---

## Contexto para o modelo

Português do Brasil. Tom: professor de concurso, objetivo e técnico. Formato: definição → exemplo → item C/E → gabarito + motivo.

---

## PARTE A — {{PARTE_A}}

{{CONTEUDO_A}}

## PARTE B — {{PARTE_B}}

{{CONTEUDO_B}}
