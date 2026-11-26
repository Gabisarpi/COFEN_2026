# Formato do `folha.json`

Exemplo completo e conferido: [exemplo-folha-iac.json](exemplo-folha-iac.json). O build com esse spec
reproduz a folha publicada de IaC e CI/CD (mesma estrutura, textos, quizzes, CSS e JS).

Todo campo de texto aceita HTML simples: `<b>`, `<code>`, `<a href="#id">` para outra seção da folha.

## Raiz

| Campo | Obrigatório | Conteúdo |
|---|---|---|
| `titulo` | sim | `"Folha de revisão · <tema>"` (nome estável do artifact; vira `<title>` e `<h1>`) |
| `subtitulo` | sim | eixo e itens do edital · tag · lacunas do ledger na data (abertas, em reforço) · placares dos cadernos |
| `discursiva` | não | rótulo das frases prontas (padrão `"discursiva"`) |
| `key` | sim | chave do localStorage, `folha-<slug>-v1` |
| `arquivo` | não | caminho do HTML a partir da raiz do repo (padrão: ao lado do JSON) |
| `ledger` | não | caminho do `lacunas.yaml`; com ele o build confere os `id` das lacunas |
| `como_usar_titulo` | não | padrão `"Como usar (25 min)"` |
| `como_usar` | sim | lista de passos (HTML). Padrão: pré-teste · mapa · núcleos · teste de saída · agenda |
| `pre` | sim | `{titulo, ed, itens}`; `itens` = 3 a 6 itens de quiz |
| `mapa` | não | `{titulo, ed, svg, legenda}` |
| `prioridade` | sim | lista (HTML) com links `#id` dos núcleos, na ordem de revisão |
| `nucleos` | sim | lista de núcleos (abaixo) |
| `gatilhos` | sim | `{ed, colunas: [[título, html], ...]}`, normalmente 3 colunas |
| `saida` | sim | `{itens}`, 10 a 14 itens de quiz |
| `agenda` | sim | `[[id, rótulo], ...]`, ex.: `["d1","20/11 (D+1)"]` |
| `agenda_ed` | não | texto ao lado do título da agenda |
| `rodape` | sim | fontes (cadernos, ledger, documentação conferida) e caminho do arquivo |

## Item de quiz

`["enunciado", "C" | "E", "porquê em uma frase"]`. Quizzes com 3 ou mais itens precisam ter C e E.

## Núcleo

```json
{"id": "c2", "titulo": "C2 · Ferramentas: ...", "ed": "edital 4.1 · 3 provas · 3 lacunas · 3/6 em 19/11",
 "blocos": [ ... ]}
```

`id` vira a âncora e a chave do quiz (não usar `pre`, `mapa`, `saida`, `gatilhos`, `agenda`).
Obrigatórios: um bloco `fatos` e pelo menos um `inversao` ou `gancho`.

## Blocos

| `tipo` | Campos | Render |
|---|---|---|
| `diagrama` | `svg`, `legenda` | figura com rolagem horizontal própria |
| `fatos` | `itens: [{html, tag?}]` | lista; com `tag`, linha amarela + etiqueta |
| `pares` | `titulo?` (padrão "Não confunda"), `cab: [...]`, `linhas: [[...]]` | tabela; 1ª coluna em negrito |
| `inversao` | `html` | caixa vermelha "Inversão:" |
| `gancho` | `html` | caixa verde-água "Gancho:" |
| `q2` | `html` | caixa tracejada "Frase pronta para a Q2:" |
| `nota` | `html` | parágrafo discreto (ex.: "Sem erro em 19/11") |
| `teste` | `itens` (1 a 4 itens de quiz) | "Teste-se" com botões C/E e resolução após responder |
| `lacunas` | `itens: [{status, hd, errei, certo, id?}]` | caixas Errei/Certo |

`status` = `aberto` | `em_reforco`. `hd` = linha de cabeçalho (ex.: `"2 ocorrências · devops-ferramenta-fase"`);
`errei` = o que ela marcou, com o enunciado real entre aspas e a prova; `certo` = gabarito + porquê.

## Comportamento do template (fixo)

- Respostas e agenda ficam no `localStorage` do navegador (`key`); a página funciona sem ele.
- Placar do pré-teste e do teste de saída: certos, errados, em branco e líquido (+1/−1/0).
- Clicar de novo no botão marcado desfaz a resposta. "Limpar minhas respostas" zera tudo.
- Tema claro e escuro por tokens; largura de celular sem rolagem horizontal da página.
