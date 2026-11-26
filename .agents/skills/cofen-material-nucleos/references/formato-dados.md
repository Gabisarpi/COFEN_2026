# Formato do dados.js e do meta.json

## dados.js

JavaScript puro, sem `import`. Strings sempre entre aspas duplas; aspas internas como `\"` ou `'`.
Pode-se declarar constantes auxiliares antes (ex.: `const CERT="<a href=...>Cartilha CERT.br</a>";`)
e usá-las em `fonte:` (`fonte:CERT` ou `fonte:"Justificativa oficial; "+CERT`).

```js
const NUC = [
 {id:"S1", t:"Firewall: tipos, camadas e limites", ed:"1.3", provas:7, itens:10,
  card:["Âncora 1 (frase curta, com o número/termo exato).","Âncora 2.","Âncora 3."],
  inv:"Como a banca costuma inverter este núcleo, em uma frase.",
  aula:"<p>Mini-aula do tema (120–250 palavras): o que é, como funciona, onde a banca pega.</p><table>...</table>",
  cmd:"(opcional) Comando do bloco — cenário do órgão/sistema.",
  code:"(opcional) Trecho sql/config/log compartilhado; use \\n nas quebras.",
  lang:"java"},
];
const ITENS = [
{n:"S1", src:"TCDF 2024 · Auditor de Controle Externo – Infra (Esp. 3) · item 132", real:1, gab:"C",
 txt:"Texto LITERAL do acervo (real:1) ou o item inédito (real:0).",
 gat:"o trecho que decide o gabarito",
 termos:"(opção resolucao-detalhada) SLI (Service Level Indicator) :: o que se mede; ex.: % de requisições em menos de 300 ms || SLO (Service Level Objective) :: a meta para o SLI; ex.: 99% no mês",
 viz:"(opção resolucao-detalhada) SLA (Service Level Agreement): o contrato com o cliente, com consequência se a meta não for cumprida. Diferença: SLO é meta interna; SLA é compromisso contratual, em geral mais folgado.",
 exp:"3–6 frases: ideia central simples → mecanismo → por que o item é C/E. Cite a justificativa oficial quando houver.",
 passo:"(obrigatório em item numérico/procedimental) Passo 1 | Passo 2 | Passo 3",
 ex:"(opcional) Exemplo concreto de órgão público/infra.",
 lembre:"(opcional) Regra de bolso de uma linha.",
 peg:"Tipo de pegadinha (ver SKILL.md) e por que engana.",
 inv:"'...reescrita que inverte o gabarito' (C|E).",
 par:"(opcional) S1-3",
 nota:"(opcional) aviso quando o gabarito oficial é discutível.",
 quote:"(opcional) trecho literal do provedor/norma, em inglês se a fonte for em inglês.",
 cmd:"(opcional) sobrescreve o cmd do núcleo neste item (modo intercalado).",
 code:"(opcional) sobrescreve o code do núcleo.",
 lang:"sql",
 fonte:"RFC/NIST/documentação; links como <a href=\"...\">título</a>."},
];
```

| Campo | Regras |
|---|---|
| `id` do núcleo | Prefixo curto do bloco + número (`R1` redes, `S1` segurança, `K1` contratos, `A1` auditoria...). |
| `ed` | Subitem do edital do cargo (ex.: `"1.3"`). |
| `provas` / `itens` | Provas distintas e assertivas do acervo no núcleo (da contagem feita na seleção). |
| `src` | Real: `Órgão Ano · Cargo (código) · item N`. Inédito: `"Variação inédita"`, com `" · literalidade AWS"` etc. quando reproduz fonte de provedor. |
| `real` | `1` = item do acervo, `0` = variação inédita. |
| `txt` | Real: copiado sem alterar nada, nem os erros de digitação (o build confere com o acervo). Inédito: assertiva no estilo Quadrix (régua de `cofen-calibrar-itens`). |
| `cmd` / `code` / `lang` | `cmd` no núcleo (cenário). `code`/`lang`: **só** se alguma assertiva do núcleo/item julgar o trecho — sem comentário/pista de gabarito no anexo (régua **`cofen-calibrar-itens`**). Não anexar código decorativo (ágil, DevOps conceitual, etc.). No modo “por núcleo”, o template mostra o do `NUC` uma vez; no intercalado, herda o do núcleo se o item não tiver o seu. O HTML tem botão **Código** (mostrar/ocultar todos) e cada trecho em `<details>` (abrir/fechar só aquele). |
| `gat` | Curto, ele é destacado. Use `·` para separar duas âncoras. |
| `fonte` | Pode conter HTML de link. Nunca cite um texto como literal sem tê-lo conferido. |
| `aula` (núcleo) | Obrigatória desde 08/11/2026. HTML simples. Explica o tema do zero (analogia, mecanismo, tabela de vizinhos, onde a banca pega), sem citar itens nem antecipar gabaritos. Aparece fechada no topo do núcleo e junto do cartão na revisão. |
| `exp` | 3 a 6 frases: ideia central → mecanismo → veredito ligado ao gatilho. Escreva para quem não estudou o assunto. |
| `passo` | Passos separados por ` \| ` (vira `<ol>`). Obrigatório em item numérico ou procedimental, com os números do próprio item. Passa pela checagem de remissão. |
| `ex` | Exemplo concreto (órgão público, rede, contrato), diferente dos enunciados da página. |
| `lembre` | Uma linha de regra de bolso para não confundir de novo. |
| `inv` | A reescrita em si, autossuficiente. Nunca "veja o item seguinte/anterior", "compare com o item X" nem o gabarito de outra prova sobre o mesmo núcleo: isso entrega a resposta de um item ainda não respondido. O build trata como ERRO. Vale também para `gat`, `exp`, `peg`, `nota` e `quote`. |
| `fonte` | Também passa pela checagem de remissão: nada de "Mesma prova, item 78 (C)" quando o item 78 está na página. |
| `termos` | Opção individual `resolucao-detalhada`. Cada sigla ou termo técnico do enunciado: `Termo (sigla por extenso) :: definição simples em português + exemplo curto`, separados por ` \|\| `. Fonte em inglês → traduzir. Não pode entregar o gabarito por remissão (passa pela checagem). Alimenta a aba Glossário, que só mostra termos de itens já corrigidos. |
| `viz` | Opção individual `resolucao-detalhada`. O conceito vizinho que a banca troca neste item (ou o mais próximo, se a pegadinha não for troca), definido do mesmo jeito, e como diferenciar os dois numa frase. |
| `par` | Id (`S1-3`) do outro item do par mínimo, no mesmo núcleo. Basta declarar num dos dois. A linha "Par mínimo" só aparece na resolução quando ambos já foram corrigidos. |

O id de cada item (`S1-1`, `S1-2`...) é gerado na página na ordem do array.

## meta.json

```json
{
 "title": "Núcleos de Contratos de TIC",
 "eyebrow": "COFEN 2026 · Cargo 407 Analista de TIC · Gestão e fiscalização de contratos de TIC",
 "h1": "Núcleos de contratos de TIC mais cobrados pela Quadrix",
 "lede": "{N} itens em {NUC} núcleos: {REAIS} reais do acervo e {VAR} variações inéditas que mudam um detalhe e invertem o gabarito. A resolução de cada item só abre depois que você marca a resposta e a confiança.",
 "method_html": "<p><b>Edital.</b> ...</p>\n<p><b>Fronteira com outros cargos.</b> ...</p>\n<p><b>Calibração (perfil).</b> Maioria dos reais: Quadrix (de preferência conselhos profissionais). Itens de outras bancas: só par de inversão (listar quantos).</p>\n<p><b>Acervo.</b> ...</p>\n<p><b>Recorrência.</b> ...</p>\n<div class=\"tbl\"><table><thead><tr><th>Núcleo</th><th>Edital</th><th class=\"n\">Provas</th><th class=\"n\">Itens no acervo</th></tr></thead><tbody id=\"rank\"></tbody></table></div>\n<p><b>Ficaram de fora.</b> ...</p>\n<p><b>Literalidade.</b> ...</p>\n<p><b>Gabaritos.</b> ...</p>",
 "key": "cofen-contratos-nucleos-v1",
 "material": "pessoal/gaby/simulados/gerados/2026-12-15_contratos-nucleos/caderno.html",
 "pessoa": "gaby",
 "cargo": "tic",
 "eixo": "esp.tic.contratos",
 "peso": 1,
 "respostas": "pessoal/gaby/respostas/2026-12-15_contratos-nucleos.yaml",
 "resp_dir": "pessoal/gaby/respostas/"
}
```

O `method_html` precisa conter `<tbody id="rank"></tbody>`: a página preenche a tabela de ranking a partir de `NUC`.
O `key` precisa ser único por material, porque é a chave do progresso salvo no navegador.
O `peso` (opcional, default `1`) é o ponto por item no placar: **sempre 1** no COFEN. Acerto `+1`, erro `−1`, branco `0`.
O `cargo` (`tic`) diz ao verificador a cota de `code` (aviso > 10%, erro > 20%).
`cota_code_livre` (opcional, `true` só com pedido expresso da pessoa naquele caderno) rebaixa a aviso o estouro da cota.

## Resolução detalhada (opcional)

`resolucao` no `meta.json`: `"padrao"` (default, inclusive campo ausente) ou `"detalhada"`
(somente com adesão da pessoa ativa à opção `resolucao-detalhada`). Com `"detalhada"`, o build
recusa item sem `termos` e `viz`. Sem a opção, os campos podem existir e aparecem se preenchidos.
A página mostra "O que é" antes do Conceito, "Vizinho" depois dele e a seção Glossário no fim.

## Modo prova (simulado)

`modo` no `meta.json`: `"estudo"` (default, inclusive campo ausente) ou `"prova"`, para o simulado
cronometrado. No modo prova não há correção item a item: ficam fechados o botão de corrigir (`>>>` ou
Corrigir), as mini-aulas, os cartões, os filtros de revisão e o modo intercalado. A pessoa marca as
respostas (pode mudá-las) e o botão **Entregar prova**, no placar, confirma tudo de uma vez, com uma
confirmação que mostra quantos itens ficaram sem resposta. Sem resposta conta como branco; C/E sem
confiança marcada (interface clássica) fica registrado como dúvida. Depois da entrega, o caderno volta
ao comportamento normal (resolução, revisão, refação e export da primeira tentativa). "Recomeçar do zero"
volta ao estado anterior à entrega.

`numero_inicial` (opcional, inteiro, default `1`): número do primeiro item na folha, na ordem "por
núcleo", para a numeração contínua do simulado completo (P1 `1`, P2 `41`, P3 `81`). Vale nos cadernos em
modo prova; no modo estudo a numeração continua posicional.

## Interface opcional

`interface` no `meta.json`: `"classica"` (default, inclusive campo ausente) ou
`"numerica"` (somente com escolha explícita da pessoa ativa, registrada em suas
preferências). O build valida o campo; não lê nem adota preferências de colegas.

Na numérica, resposta e confiança são uma seleção: `${peso}++` = C com certeza,
`${peso}+` = C com dúvida, `${peso}--` = E com certeza, `${peso}-` = E com dúvida,
`0` = branco. `>>>` confirma e só então abre a correção. Os sinais não são a nota
recebida nem revelam o gabarito: o saldo só é calculado após confirmar. Valores
exportados continuam C/E/B e certeza/dúvida/na, com o peso original do caderno.

Preservar fonte e estrutura do modelo atual. “Decide o item” mantém caixa, padding,
cantos arredondados e texto verde/vermelho: fundo com 12% da cor do resultado sobre
a superfície e contorno com 30% da cor sobre a linha do tema. Não substituir a
caixa por sublinhado nem neutralizar o texto; branco mantém estilo neutro. O
template implementa esses detalhes para temas claro e escuro.

## Teclado (todas as pessoas, as duas interfaces)

O template traz atalhos desde 14/11/2026: `↓`/`j` e `↑`/`k` navegam entre os itens (o item
ativo recebe contorno), `1` `2` `3` `4` = C certeza, C dúvida, E certeza, E dúvida, `0` =
branco, `Enter` confirma e abre a correção sem sair do item (para lê-la antes de seguir),
`n` pula para o próximo não respondido, `?` mostra o quadro de atalhos e `Esc` o fecha. Os atalhos não agem em campos de
texto, com Ctrl/Alt/Meta, nem em item já corrigido; `Enter` sobre um botão focado mantém o
clique nativo. Não alterar o mapa sem pedido; caderno antigo só ganha os atalhos se for
reconstruído (mesma `key`, progresso preservado).

Ao regenerar material existente, manter `key`, ordem, IDs e conteúdo; não descartar
tentativas salvas. Não migrar todo o acervo por inferência. Mudanças de aparência
devem ser pequenas e validadas antes de adotar novas alterações.
