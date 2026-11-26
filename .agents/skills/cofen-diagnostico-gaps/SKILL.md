---
name: cofen-diagnostico-gaps
description: >-
  Diagnostica desempenho e lacunas de estudo do COFEN 2026 (Cargo 407) a partir
  de revisões, correções C/E, discursivas e do ledger cronograma/lacunas.yaml;
  propõe reforços e ajustes no cronograma (inclusive painel HTML via plano.py).
  Use ao corrigir gabarito ou discursiva, depois de um simulado, ou quando a
  pessoa pedir o que estudo hoje, ajustar cronograma, lacunas, pontos fracos,
  triagem de erros ou desempenho.
---

# COFEN — Diagnóstico de lacunas

Repo individual da Gaby (`Gabisarpi/COFEN_2026`). `$P = pessoal/gaby/` · `$C = cargos/tic/`.

Complementa `cofen-simulado-quadrix`. Esta skill **fecha o ciclo**: evidência → ledger → proposta de estudo/cronograma.

## Quando acionar (obrigatório)

1. Corrigir objetiva ou discursiva
2. Fechar simulado/bloco com correção
3. Pedido de: o que estudo hoje · ajustar cronograma · lacunas · pontos fracos · triagem
4. Início de sessão em que a `CONTINUIDADE.md` indique foco em planejamento

Depois de uma correção, o diagnóstico (mesmo curto) faz parte da entrega. Opções individuais: [cofen-preferencias-opcionais](../cofen-preferencias-opcionais/SKILL.md).

## Fontes (nesta ordem)

1. `$P/cronograma/lacunas.yaml` — ledger canônico ([lacunas-schema.md](lacunas-schema.md))
2. Cronograma: `$P/cronograma/plano.py` se existir; senão o `.md` do plano em `$P/cronograma/`
3. `$P/revisao/` — folhas recentes (§3 “Meus erros”)
4. `$P/respostas/**/correcao.md` + metas em `$P/simulados/gerados/` · `$P/respostas/*_flashcards-*.yaml` (regras no §4 da `cofen-flashcards`)
5. `$C/mapa-edital.md` — tags oficiais (nunca inventar tag)
6. `acervo/cobertura-edital.md` e `acervo/previsao-cofen.md` (quando existirem) — `python3 tools/acervo_cobertura.py --write` / `python3 tools/acervo_previsao.py --write`
7. Sugestão do dia: `python3 tools/acervo_sugestao_hoje.py [--data YYYY-MM-DD]` (não fura a fase). `--write` grava `$P/cronograma/sugestao-hoje.md`, **local, não versionado**.

## Fluxo

### 1) Coletar evidências

Para cada gap: `tag` do mapa (a mais específica) · `tema` (1 linha) · `severidade` (`alta`: conceito/literalidade cobrada errada; `media`; `baixa`: imprecisão leve, LP isolada) · `fonte` `{tipo, path, data}` · `detalhe` (errou → certo) · `confianca` (erro **com certeza** incrementa `erros_com_certeza`).

**Lacunas de processo** (pedido do enunciado não respondido, estrutura, língua) não são conteúdo: ação de processo. Pedido omitido → painel “Pedidos do enunciado” no próximo editor. Língua → `$P/revisao/lp-erros.md`, uma âncora `errado → certo` por linha, sem repetir (marcar reincidência com data). LP recorrente (≥ 3 do mesmo tipo) vira entrada com tag `disc.tic`.

### 2) Atualizar o ledger

- Mesma `tag` + mesmo `tema` = mesma entrada: `ocorrencias += 1`, `ultima_data`, append em `fontes`/`detalhes`.
- Gap novo: `status: aberto`.
- **Transição de status:**
  - Erro novo → zera `acertos_pos` e volta a `aberto`.
  - Acerto em **variação distinta** (não refação do mesmo item) → append `{data, confianca, fonte}` em `acertos_pos`, status `em_reforco`.
  - **`resolvido`** exige ≥ 2 acertos com `confianca: certeza` em **dias diferentes**. Lacuna de discursiva: pelo menos um deles em resposta escrita, quando houver.
  - Acerto com dúvida → só `em_reforco`. Refação idêntica não conta. Flashcard leva no máximo a `em_reforco`.
- `notas` da raiz: só ~10 linhas recentes. Atualizar `atualizado:`.

### 3) Diagnosticar

Ordem de prioridade dos abertos: **severidade alta** → mais `erros_com_certeza` → mais `ocorrencias` → mais recente → proximidade no cronograma. Esta ordem vale para as outras skills.

Score opcional: `score(tag) ≈ prioridade_proxy(tag) × severidade_lacuna(tag)` (proxy = faixa em `acervo/previsao-cofen.md`; sem acervo, faixa do `$C/perfil.md` → Prioridades do P3). Ordena propostas; não fura a fase do cronograma.

Produzir (conciso): **top gaps** (3–7) · **hipótese** do que está frágil · **1–3 ações** concretas:

- `N itens <tag>` (calibrados, só tags já estudadas; matéria futura → slot na semana certa)
- flashcard (`cofen-flashcards`) para lacuna reincidente · folha de revisão (`cofen-folha-revisao`) · áudio NotebookLM
- discursiva focada (tema do perfil + ledger)
- ação de processo (pedido omitido, língua)
- mudança de linha no cronograma

### 4) Cronograma — propor, não aplicar às cegas

**Prioridade por pontos (obrigatória em todo ajuste).** Ordenar o tempo pelo ganho na nota final:

1. **Valor do ponto (COFEN):** todos os itens objetivos valem ±1. Item de errado para certo = **+2**; de branco para certo = **+1**; 1 ponto de discursiva = **+1** (máximo 10). A objetiva vale 120 de 140 pontos possíveis (objetiva + discursiva + títulos).
2. **Barreira das objetivas:** só são corrigidas as discursivas dos melhores colocados na objetiva (Cargo 407: 81 no total, 27 na ampla concorrência). Ponto de objetiva vale para a barreira e para a nota final; discursiva só conta depois dela.
3. **Pontos em jogo de um tema** = itens esperados do tema × (1 − líquido sem estudo na véspera). Itens esperados: distribuição do último simulado completo. P1 (40) e P2 (30) têm muitos itens por tema (LP, RLM, Inglês, legislação), então podem render mais que um bloco do P3 com 4–5 itens.
4. **Frequência na banca:** tag de faixa baixa com erros → flashcard ou só os itens errados (≤ 15 min), nunca dia próprio.
5. **Corte acima de tudo:** parte com margem pequena sobre o mínimo (P1 10, P2 8, P3 12, total 34) recebe estudo dirigido até a projeção chegar a ~mínimo + 10.
6. **Discursiva:** manter 1 por semana até a prova; começar pela lista de pedidos.
7. **Medida sem estudo na véspera:** caderno do tema estudado no dia não mede domínio; usar simulado ou itens de temas não estudados na véspera.

- Sempre **propor** o diff em 2–5 bullets; **só editar** com confirmação (“sim”, “aplica”, “pode”).
- Com `plano.py`: editar `DIAS`/`MATERIAIS`/`TAREFAS` no gerador e rodar `python3 $P/cronograma/plano.py` (usa `tools/cronograma_gerar.py`). Sem `plano.py`: editar o `.md` do plano.
- Atualizar `$P/CONTINUIDADE.md` se o próximo passo mudou (~7 dias; o resto em `$P/historico/AAAA-MM.md`).

### Cronograma HTML (`plano.py` + painel)

| Arquivo | Papel |
|---------|-------|
| `$P/cronograma/plano.py` | Fonte única — `FASES`, `DIAS`, `MATERIAIS`, `TAREFAS`, feriados, horas |
| `$P/cronograma/template.html` | UI do painel |
| `$P/cronograma/cronograma.html` | Painel gerado |
| `$P/cronograma/plano.md` | Espelho Markdown gerado |

**Materiais no dia:** `MATERIAIS["DD/MM"] = [("<nome>", "<url>")]`. Com `TAREFAS`, cada tarefa é um card de check `("<turno · tarefa>", url)`, com `url` = caminho, `"?"` (a gerar, pontilhado) ou `None`; ao gerar o material, trocar o `"?"` pelo caminho.

Tipos de dia (`tipo` em `DIAS`): `nuc` · `ref` · `bloco` · `disc` · `sim` · `p1` · `p2` · `rev` · `leve` · `prova`.

### 5) Espelho leve

- `$P/revisao/YYYY-MM-DD_*.md` §3 só com âncoras.
- Em discursiva: `correcao.md` e `meta.gaps` alinhados ao ledger; erros de língua em `lp-erros.md`; gerar `correcao.html` com `python3 tools/correcao_html.py $P/respostas/<pasta>` (o `.md` continua sendo a fonte).

## Formato de saída

```markdown
## Diagnóstico de lacunas
- …

## Propostas
1. …
2. … (ajuste de cronograma: dia X ← tema Y)

## Ledger
Atualizei `pessoal/gaby/cronograma/lacunas.yaml` (N entradas).
Aplico o cronograma? (sim/não)
```

Pós-correção rápida: 5–10 linhas bastam.

## Feito só com aviso explícito

Não inferir conclusão pelo horário ou pelo plano; não marcar reforço/resolvido sem evidência + aviso; pendências declaradas prevalecem.

## Anti-padrões

- Inventar desempenho ou conclusão
- Propor estudo fora do edital
- Reescrever semanas sem evidência
- Marcar `resolvido` sem 2 acertos com certeza em dias diferentes
- Tratar lacuna de processo como conteúdo
- Copiar texto longo da resposta para o ledger
