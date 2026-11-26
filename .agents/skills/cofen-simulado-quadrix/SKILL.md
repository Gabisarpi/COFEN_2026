---
name: cofen-simulado-quadrix
description: >-
  Monta e corrige simulados Quadrix (C/E + discursiva) para o COFEN 2026,
  Cargo 407 Analista de TIC, usando o acervo local, o mapa e o perfil da
  trilha; calibração via cofen-calibrar-itens antes de gravar. Use quando a
  pessoa pedir simulado, itens Quadrix, gabarito C/E, bloco de N itens,
  correção de caderno ou de discursiva, ou questões no estilo da banca.
---

# COFEN — Simulado Quadrix

Projeto: raiz do repo `COFEN_2026`. `$P = pessoal/gaby/` · `$C = cargos/tic/`. O que é do cargo vem de **`$C/perfil.md`**.

## Âncoras (ler antes de gerar)

1. `AGENTS.md` → Sempre (destinos em `$P`, “feito” só com aviso, push só com autorização)
2. **`$C/perfil.md`** — banca, prioridades do P3, discursiva, escopo dos itens
3. **`cofen-calibrar-itens`** — densidade + anti-dedução **antes de gravar**
4. `$C/mapa-edital.md` — tags · `$C/resumo-edital.md` — cortes e notas
5. `acervo/catalogo.yaml` + `acervo/itens/` — corpus de estilo (Quadrix primeiro)
6. `simulados/templates/objetiva-quadrix.md` e `discursiva-quadrix.md`

## Regras gerais

- **Formato da banca:** comando (texto ou cenário, opcional) + itens **Certo/Errado**. Quadrix costuma usar enunciado curto e afirmação direta; muita cobrança literal de lei, norma e definição de manual.
- **Pontuação:** todas as partes valem **+1 / −1 / 0** (certo/errado/branco). Não há peso 2.
- **Composição das questões diárias:** misturar (1) tema atual do cronograma, (2) lacunas `aberto`/`em_reforco` de `$P/cronograma/lacunas.yaml`, (3) temas já estudados (retenção). Só entram temas já estudados (filtro de fase, §4b). Proporção conforme `$P/preferencias-estudo.md`, se existir. Não vale para pedido focado nem para simulado completo. Registrar no meta os temas retomados.
- **Questões reais sempre que pertinente:** buscar no acervo antes de montar; critérios em `cofen-material-nucleos` → §2. Não inventar gabarito para item ingerido sem gabarito oficial.
- **Preferências e opções individuais:** seguir [cofen-preferencias-opcionais](../cofen-preferencias-opcionais/SKILL.md), sem bloquear o pedido.
- **Formato do caderno: HTML (padrão) ou MD.** Perguntar numa linha, salvo se o pedido já disser; sem resposta, HTML.
  - **HTML:** molde de `cofen-material-nucleos` (`dados.js` + `meta.json` + `scripts/build.py` → `caderno.html`). `peso: 1` sempre. O build roda o verificador de calibração.
  - **MD:** `caderno.md` (sem gabarito) + `gabarito.md` (justificativas) + `meta.yaml`.
  - Discursiva: `discursiva.md` + `discursiva-padrao-resposta.md`; se for escrever na tela, também `redacao.html` via **`cofen-redacao-discursiva`**.
- **Gabarito sempre separado** do enunciado (no HTML, oculto até responder).
- **Destino:** `$P/simulados/gerados/YYYY-MM-DD_tema/`.

## 1) Ingestão / tagging

Usar a skill **`cofen-acervo`**. Atalho: `acervo/fontes/{orgao}_{ano}_{slug}/` com prova + gabarito definitivo; normalizar em `acervo/itens/*.md` com `banca:`, `formato:` e `tags_edital` do mapa; rodar `python3 tools/acervo_cobertura.py --write --write-catalogo`.

## 2) Priorização por heatmap

Em simulado completo, bloco ≥ 20 ou “o que a banca mais cobra”: ler `acervo/cobertura-edital.md` e `acervo/previsao-cofen.md` (quando existirem), cruzar com **Prioridades do P3** do perfil e com a fase do cronograma. Anotar no meta `heatmap_ref`, `previsao_ref` e as tags priorizadas. Sem acervo ainda: seguir só o perfil e dizer isso no meta.

## 3) Simulado completo

| Prova | Itens | Mínimo |
|-------|-------|--------|
| P1 Básicos (LP, RLM, Inglês) | 40 C/E | 10 |
| P2 Complementares (legislação, Constitucional, Administrativo) | 30 C/E | 8 |
| P3 Específicos (`esp.tic.*`) | 50 C/E | 12 |
| Objetiva total | 120 | 34 |
| P4 Discursiva | 1 texto, 20–30 linhas, 10 pts | 5 |

Passos:

1. Distribuir tags conforme mapa. Referência para P1: LP ~16, RLM ~12, Inglês ~12. P2: legislação específica ~14, Administrativo ~9, Constitucional ~7. P3: cobrir os 12 blocos, com peso maior nos exclusivos do 407 (8–12) e na faixa alta do perfil. Anotar no meta a distribuição usada (o edital não fixa a divisão interna).
2. **Discursiva = tema mais provável**, não lacuna do ledger: recorrência no edital (blocos 8–12), discursivas Quadrix do acervo para cargos de TI e cenários do perfil. Registrar no meta os sinais da escolha.
3. **Rascunhos no repositório:** gravar dados por partes em `$P/simulados/gerados/<simulado>/_rascunho/`; no fim montar os `dados.js` e apagar o rascunho.
4. Salvar em `$P/simulados/gerados/YYYY-MM-DD_HHMM_simulado/`:
   - **HTML:** um caderno por prova (`p1/`, `p2/`, `p3/`), `"modo": "prova"` e `"numero_inicial"` (1, 41, 71) no `meta.json`.
   - **MD:** `caderno.md` + `gabarito.md` + `meta.yaml`.
   - Nos dois: `discursiva.md` + `discursiva-padrao-resposta.md`.
5. **Padrão de resposta da discursiva:**
   - Pontuar **cada pedido explícito** do enunciado (um aspecto por verbo de comando; integração entre pedidos não pontua). O padrão só pontua o que o pedido cobra.
   - Distribuir os 3 pontos de **CAC** entre os aspectos; OT e DLP ficam como critérios à parte (0–3 cada).
   - Conferir que o conteúdo pontuado **cabe em 30 linhas** (≈ 30 × 60 caracteres). Se não couber, reduzir pedidos.
6. **Ensaio de prova:** 4 h cronometradas para objetiva + discursiva juntas (sugestão: ~3h10 objetiva, ~50 min discursiva). Sem abrir gabarito durante. Checagem de sequência C/E **por prova**.

**Bloco reduzido:** pedido de N itens ou só uma prova → respeitar e anotar o desvio.

## 4) Bloco temático

1. Filtrar as tags pedidas (ex.: `esp.tic.contratos`).
2. Gerar N itens (default 10–20) no formato escolhido; `peso: 1`; `respostas` → `$P/respostas/…yaml`.
3. Incluir reais pertinentes (`real:1`, origem completa) e registrar contagem reais/inéditos no meta; sem reais, registrar o motivo.

### 4b) Reforço de lacunas

Cruzar três filtros: (1) entradas `aberto`/`em_reforco` do ledger (ordem: `cofen-diagnostico-gaps` §3); (2) **fase já estudada** no cronograma (não antecipar matéria futura); (3) pedido explícito. Dizer em uma linha o que ficou de fora. No meta: `escopo`, `excluido`, `lacunas_alvo`.

## 5) Correção

**Objetiva:** certo +1, errado −1, branco 0 em todas as partes. Eliminação: P1 < 10, P2 < 8, P3 < 12 ou total < 34. Informar a nota por parte e o líquido (%).

**Discursiva (edital, item da prova discursiva):**

- CAC (conteúdo e atendimento ao comando), OT (organização textual) e DLP (domínio da modalidade escrita), cada um de 0 a 3,00.
- Nota = [(CAC × 7) + (OT × 1,5) + (DLP × 1,5)] ÷ 3 (máximo 10). Aprovação ≥ 5,00.
- Fora do tema, em branco ou abaixo de 20 linhas → registrar o risco (o edital pode zerar ou penalizar; conferir a regra exata no `edital.pdf` antes de aplicar).
- Entregar: CAC desdobrado por pedido do padrão, OT e DLP com justificativa, lista de erros de língua, nota final.

**Nota de referência do concurso:** objetiva (120) + discursiva (10) + títulos (10).

**Persistir em `$P`:**

| Papel | Onde |
|-------|------|
| Enunciado / padrão / caderno / gabarito | `$P/simulados/gerados/.../` |
| Texto da candidata | `$P/respostas/{id}/resposta.md` |
| Correção | `$P/respostas/{id}/correcao.md` (+ `correcao.html` via `tools/correcao_html.py`) |

Atualizar o meta com paths + `correcao: {…, gaps}`; erros de língua → `$P/revisao/lp-erros.md`. Depois, acionar **`cofen-diagnostico-gaps`**.

## Estilo dos itens gerados

- Uma ideia por item; julgamento unívoco.
- Cenários de conselho profissional (Cofen/Corens), autarquia federal, contrato de TIC, regime CLT.
- Escopo do P3: seção **Escopo dos itens** do perfil; nada fora do mapa sem pedido.

### Calibração (obrigatório)

**Antes de gravar** qualquer caderno: cumprir **`.agents/skills/cofen-calibrar-itens/SKILL.md`**. Ponteiro permanente — não remover sem pedido expresso.

### Elaboração C/E (checklist)

**Mecanismos:** conceito/termo; distinção de conceitos próximos; regra × exceção; aplicação; condição necessária × suficiente; competência/responsabilidade; literalidade de lei ou norma (prazo, número, quem faz); generalização indevida.

**Erros nos itens E** (plausíveis): troca de conceito vizinho; competência trocada; prazo/número alterado; regra ↔ exceção; absolutização (“sempre”, “somente”, “vedado”); regra certa no contexto errado.

**Distribuição:** C/E ~45–55%; verdade técnica > cota.

**Sem pista de sequência (checar antes de gravar):** rejeitar janela de 8 com ≥ 7 alternâncias; flip rate entre ~35% e ~70% (acima de 75% = reembaralhar); evitar > 5 iguais seguidos só para cota.

**Independência:** um item não revela outro.

**Evitar:** ambiguidade; C+E na mesma assertiva; erro só por imprecisão de redação; inventar artigo, resolução ou norma.

**Auditoria por item:** gabarito sustentável · univocidade · condições suficientes · erro real se E · sem pista de redação · relevância · originalidade · no edital · dificuldade · justificativa em `gabarito.md` ou `exp`.

### Fontes (verdade do gabarito)

1. **Legislação e normas do edital** (texto vigente no Planalto/DOU; resoluções no site do Cofen; ISO/IEC 27001/27002; ITIL 4; COBIT 2019).
2. **Documentação oficial** (Microsoft Learn, Red Hat, RFC, NIST, CERT.br, gov.br/SGD para contratações de TIC — IN SGD/ME 94/2022).
3. **Acervo local** = estilo e pegadinha, **não** fonte factual.

Indicar no gabarito uma âncora curta (artigo, item da norma, URL).

## Pedidos típicos

- “simulado completo” · “bloco de 15 itens de contratos de TIC” · “reforço das minhas lacunas”
- “corrigir meu gabarito” · “corrigir discursiva”
- “ingerir prova …” → `cofen-acervo`
