---
name: cofen-folha-revisao
description: Gera a folha de revisão ativa (artifact HTML) de um tópico do edital ou assunto pedido, para a COFEN 2026, no formato aprovado em 19/11/2026 — pré-teste das lacunas abertas, mapa visual em SVG, núcleos com diagrama, fatos (um por linha, erro da pessoa em amarelo), pares que a banca troca, inversão, gancho de memória, frase pronta para a discursiva, "Teste-se" C/E, caixas Errei/Certo do ledger, gatilhos da banca, teste de saída com nota líquida Quadrix e agenda espaçada. Liga a folha na Central de Revisão (hub-revisao.html) e no cronograma. Use quando a pessoa pedir "folha de revisão de X", "material de revisão do tópico/bloco Y", "revisão do que errei no caderno Z", "próxima folha da Central", "revisão do dia", "folha de amanhã", ou quando a Central apontar o próximo tópico sem folha ou o painel mostrar "Revisão do dia: a gerar".
---

# Folha de revisão ativa (COFEN 2026)

Formato herdado do repo CGU_2026 (aprovado lá em 19/11/2026). O spec de exemplo (folha de IaC e CI/CD do
CGU) está em [references/exemplo-folha-iac.json](references/exemplo-folha-iac.json): **leia-o antes de
escrever um spec novo** e copie o tom, a densidade e a ordem dos blocos — não o conteúdo, que é do CGU.

Diferença do COFEN: há **uma** discursiva (20–30 linhas, tag `disc.tic`); use o bloco `q2` como
“frase pronta para a discursiva” e, na raiz do spec, `"discursiva": "Discursiva"` se o rótulo precisar mudar.

A folha não substitui caderno de núcleos: é a revisão de 25 min de um tópico já estudado, montada a
partir dos cadernos respondidos e das lacunas. O ganho vem de **testar antes de reler** (pré-teste),
**ver o mecanismo** (diagrama), **testar logo depois** (Teste-se), **misturar** (teste de saída) e
**espaçar** (agenda D+1, D+3, D+7, D+14, véspera).

O HTML sai sempre do template fixo da skill (CSS, motor de quiz, agenda). Escreva só o `folha.json`;
nunca edite o HTML gerado.

## 0. Contexto

1. Identidade e regras comuns (`$P`, `$C`, CONTINUIDADE, preferências, só `$P/`): `AGENTS.md` → Sempre. Ler `$C/perfil.md` e `$C/mapa-edital.md`.
2. Ler `$P/revisao/hub-revisao.html` se existir (Central: `BLOCOS`, tópicos com `folha:null`, `lac:[abertas, em reforço]`). Sem Central, pular os passos dela.
3. Ler `$P/cronograma/lacunas.yaml` e os YAML de `$P/respostas/` do tópico.
4. Não editar `acervo/` nem `cargos/`.

## 1. Escolher o tópico

- **Pedido explícito** (tópico do edital, bloco de um caderno, assunto): usar esse.
- **Sem pedido**: o primeiro da lista "Próximas folhas" da Central, ordenada pela regra de prioridade
  por pontos (`cofen-diagnostico-gaps` §4: pontos em jogo, medidos sem estudo na véspera). Tag de prioridade
  baixa na banca não ganha folha: vale flashcard dos erros.
- Um tópico da Central = uma folha. Se o pedido for um bloco de caderno, a folha cobre o **tópico do
  edital** desse bloco, organizada pelos núcleos do caderno.
- Só matéria já estudada (há caderno respondido). Tópico ainda não estudado → dizer em uma linha e
  propor o dia.

## 2. Levantar o material (antes de escrever)

Monte uma tabela de trabalho, por núcleo do(s) caderno(s) do tópico:

| Núcleo | edital | provas no acervo | acertos/itens no último caderno | lacunas (id · status · ocorrências) | itens errados (id, enunciado, gabarito, confiança) |

Fontes: `dados.js`/`meta.json` dos cadernos (`NUC`: título, `ed`, `provas`, `card`, `inv`; `ITENS`:
enunciado, gabarito, `peg`, `exp`), os YAML de respostas e o ledger (`detalhes`, `acertos_pos`).

Ordem dos núcleos na folha = **prioridade de revisão**: primeiro os que têm lacuna `aberto` (mais
ocorrências e erro com certeza antes), depois os só `em_reforco`, por fim os sem erro. O núcleo de
conceito sem erro vai para o fim.

## 3. Escrever o `folha.json`

Formato completo: [references/formato-folha.md](references/formato-folha.md). Regras de conteúdo:

- **Pré-teste (3 a 6 itens):** um item por lacuna aberta, com a **mesma pegadinha** que derrubou a
  pessoa, reescrita (nunca o enunciado original).
- **Mapa (opcional, recomendado):** um SVG que mostre o tópico inteiro de uma vez (fases, camadas,
  fluxo) e onde caem os erros dela. Ver [references/diagramas.md](references/diagramas.md).
- **Núcleo**, nesta ordem de blocos:
  1. `diagrama` quando o conteúdo é mecanismo (fluxo, quem fala com quem, antes × depois, ordem de
     passos). Não desenhe lista nem definição.
  2. `fatos`: um fato por linha, em prosa curta, termo-chave em `<b>`. O que ela errou leva `tag`
     ("você errou", "você errou com certeza", "você deixou em branco").
  3. `pares` (Não confunda) quando há rótulos vizinhos.
  4. `inversao`: como a banca transforma o fato em E (tirar dos `inv`/`peg` dos cadernos e dos erros reais).
  5. `gancho`: uma imagem concreta e curta que a pessoa repete de cabeça. Não pode entregar gabarito de item do teste.
  6. `q2` quando o núcleo cai em discursiva (cenários em `$C/perfil.md` → Discursiva): uma frase técnica
     pronta, no registro da prova.
  7. `teste` (Teste-se, 1 a 4 itens): **inéditos**, sobre os fatos do núcleo, com C e E na folha.
  8. `lacunas`: uma caixa por entrada do ledger tocada no tópico (id, status, ocorrências, o enunciado
     real em "Errei", o gabarito e o porquê em "Certo").
- **Gatilhos da banca:** três colunas: "Cheira a E" (palavras que sinalizaram E nos itens dela),
  "Parece E, mas é C" e "Seu padrão" (o tipo de erro que domina: E aceito × C marcado E, com contagem).
- **Teste de saída (10 a 14 itens):** inéditos, misturados entre os núcleos, metade C e metade E
  (±2), sem repetir enunciado do pré-teste nem do Teste-se.
- **Agenda:** datas reais a partir de hoje: D+1, D+3, D+7, D+14 e a véspera da prova (27/02/2027, "só os gatilhos").
- **Itens C/E** (pré, Teste-se, saída) passam pela **`cofen-calibrar-itens`** (obrigatório): meia-verdade
  ou troca de rótulo vizinho nos E, C contraintuitivo presente, sem pista de redação. Cada item traz o
  porquê em uma frase.
- **Fonte conferida:** fato novo que não esteja nos cadernos só entra com documentação oficial
  conferida (a mesma regra dos cadernos). Listar as fontes no `rodape`.
- Texto: português claro e direto, frases curtas, sem travessão de aparte nem "não é X, é Y" de efeito.
- `key` do localStorage: `folha-<slug>-v1` (mude o sufixo só se a estrutura dos quizzes mudar).

## 4. Gerar, publicar e ligar

1. Gravar `$P/revisao/folha-<slug>.json` (o `arquivo` dentro dele aponta para `$P/revisao/folha-<slug>.html`).
2. `python3 .agents/skills/cofen-folha-revisao/scripts/build.py $P/revisao/folha-<slug>.json`
   valida (estrutura, gabaritos C/E, SVG com `role="img"`/`aria-label`/`viewBox`, ids de `<marker>`
   únicos na página, âncoras internas, lacunas existentes no ledger) e grava o HTML. Erro → corrigir o JSON.
3. Publicar com o Artifact tool: `icon: "book"` na primeira vez, descrição de uma frase. Se o publish
   recusar o caminho do repo (`blockReadsOutsideWorkingDirectories`), copiar o HTML para o scratchpad e
   publicar de lá; nas republicações, usar o **mesmo** caminho do scratchpad (ou `url`).
4. Central: no `BLOCOS` de `$P/revisao/hub-revisao.html`, trocar `folha:null` do tópico pelo link
   (`A+"<id>"`) e atualizar `lac:[abertas, em reforço]` pelo ledger. Republicar a Central no artifact
   dela (ler antes; o publish com `url` exige leitura).
5. Cronograma (dia com `TAREFAS` no `plano.py`: trocar o `"?"` da tarefa pelo link, ver `cofen-diagnostico-gaps` → Tarefas do dia): acrescentar `("Folha de revisão · <tema>", "<url>")` em `MATERIAIS` do dia
   (padrão: hoje), rodar `python3 $P/cronograma/plano.py` e republicar o painel (ler o artifact antes).
6. `$P/CONTINUIDADE.md`: uma linha com link, arquivo, núcleos e a data em que as lacunas foram congeladas.
7. Commit só dos arquivos da tarefa (`.json`, `.html`, hub, plano, painel, CONTINUIDADE); push só com autorização da Gaby.

## 5. Atualizar depois de nova correção

A folha congela as lacunas na data do `subtitulo`. Quando o ledger mudar no tópico (novo caderno,
simulado), atualizar `fatos`/`tag`, `lacunas`, `prioridade`, `gatilhos` e o pré-teste no JSON,
rodar o build e republicar no mesmo link. Não reaproveitar itens de teste que a pessoa já viu como
se fossem medida nova: o teste de saída mede retenção, não substitui caderno calibrado. A folha
**nunca** muda status no ledger.

## 6. Folha de revisão do dia (cronograma com `revisao_dia`)

Quando o `plano.py` passa `revisao_dia` ao gerador, o painel
não lista mais a revisão espaçada: cada dia em que vence algo mostra **"Revisão do dia (≤N min)"**,
com link para `$P/revisao/dia/AAAA-MM-DD.html` ou "a gerar". O limite vem de `rev_min` no `plano.py`
(sugestão: 25 min; 15 no domingo e em dia leve; nenhum no dia da prova).

1. **Quando:** na véspera ou no próprio dia, a pedido. Não gerar dias futuros em lote: as lacunas
   congelariam na data da geração.
2. **O que entra:** `python3 $P/cronograma/plano.py --revisao DD/MM` lista os temas que vencem
   (D+2/D+7/D+21), as tags, os materiais e as lacunas `aberto`/`em_reforco` dessas tags. Um núcleo
   por tema, na ordem: lacuna aberta, depois em reforço, depois sem lacuna (manutenção, com `nota`).
   Tema que já tem folha própria: o núcleo vira só o pré-teste e o teste de saída dela, com link.
3. **Caber no limite:** `como_usar_titulo` = `"Como usar (≤N min)"`, e os passos de `como_usar` com
   minutos que somam N, terminando em "parou o relógio, parou a folha". Pré-teste 3–4 itens, até
   2 itens no Teste-se de cada núcleo, saída de 10 itens (metade C, metade E). Sem `mapa` nem
   diagrama, salvo quando o tema for mecanismo e couber no tempo.
4. **Spec:** `$P/revisao/dia/AAAA-MM-DD.json`, `titulo` = `"Folha de revisão · dia DD/MM (<temas>)"`,
   `key` = `folha-dia-AAAA-MM-DD-v1`, `agenda` = as próximas datas desses temas no cronograma e a
   véspera. Itens passam pela `cofen-calibrar-itens`, como nas folhas de tópico.
5. **Gerar e ligar:** `build.py` no JSON e depois `plano.py` (o link troca "a gerar" pelo arquivo
   sozinho). Não entra na Central nem em `MATERIAIS`. Publicar como artifact só se a pessoa pedir.
6. Lacuna em reforço que só fecha por escrito: pedir no `como_usar` 2 ou 3 linhas de cabeça com a
   frase pronta. A folha continua sem mudar status no ledger.

## Anti-padrões

- Editar o HTML gerado ou o template para uma folha só.
- Folha só de leitura (sem pré-teste, Teste-se e saída) ou com os erros da pessoa só no fim.
- Diagrama decorativo (caixas soltas sem setas rotuladas) ou que repete a lista de fatos.
- Copiar enunciado real nos testes (ela decora a resposta, não a regra).
- Gancho que entrega a resposta de um item do teste.
- Teste de saída só com C ou só com E, ou concentrado num núcleo.
- Usar a folha para marcar lacuna como resolvida.
