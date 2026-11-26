# Diagramas da folha (SVG inline)

Um diagrama entra quando mostra um **mecanismo** que a prosa obriga a montar de cabeça: fluxo de
dados, quem inicia a conversa, ordem de passos, antes × depois, o que cada comando toca. Lista e
definição não viram diagrama.

Na folha de IaC: pipeline com fases, ferramentas e faixas de cada prática (mapa); Ansible push ×
Puppet pull; cherry-pick criando E′; rotina de IC em 6 passos; Terraform plan/apply/refresh-only/drift;
azul-verde × canário. Copie a estrutura desses SVGs do `exemplo-folha-iac.json`.

## Regras que o build confere

- Começa com `<svg`, tem `viewBox`, `role="img"` e `aria-label` com a afirmação do desenho.
- Sem `<script>`, `<style>` ou `foreignObject` dentro do SVG.
- Ids de `<marker>` **únicos na página inteira** (todos os SVGs dividem o mesmo documento):
  use `ar`, `ar2`, `ar3`... em sequência.

## Classes prontas (CSS do template; não use cor literal)

| Classe | Uso |
|---|---|
| `bx` | caixa neutra |
| `bx-a` · `bx-o` · `bx-w` · `bx-t` | caixa destacada: azul (foco), verde (certo/novo), âmbar (erro dela, portão), verde-água (mecanismo) |
| `ln` · `ln-d` | linha neutra · tracejada discreta (divisória) |
| `ln-a` · `ln-o` · `ln-w` · `ln-t` | linha colorida (2px) |
| `tx` · `tx-s` · `tx-b` · `tx-inv` | texto 12px · secundário 11px · negrito · negrito sobre fundo cheio |
| `tx-a` · `tx-o` · `tx-w` · `tx-t` | rótulo colorido de seta |
| `dot` · `dot-o` | nó de grafo (commit) neutro · destacado |
| `mk` · `mk-a` · `mk-o` · `mk-w` · `mk-t` | preenchimento da ponta de seta no `<marker>` |

Seta: `<marker id="arN" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="mk-a"/></marker>` e `marker-end="url(#arN)"`.

## Composição

- Largura do `viewBox` entre 600 e 770; a figura tem `min-width:560px` e rola dentro da própria caixa no celular.
- Grade regular: caixas de mesma altura, gaps iguais, textos centrados com `text-anchor="middle"`.
- Toda seta tem rótulo curto (`lê`, `apply`, `SSH`, `100%`, `reverter`).
- Cor com significado: âmbar marca o ponto em que a pessoa errou; verde, o resultado certo ou novo.
- Comparação = os dois lados no mesmo desenho, separados por `ln-d`, com o mesmo arranjo.
- A `legenda` diz o que o desenho prova e liga ao erro dela ("O erro com certeza de 19/11 está neste desenho...").
