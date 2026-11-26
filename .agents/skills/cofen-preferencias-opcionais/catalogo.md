# Opções individuais disponíveis

Válidas para este repo, com adesão independente por módulo. **Sem adesão,
manter o fluxo existente.** Parâmetros abaixo são sugestões ajustáveis, não valores
obrigatórios nem uma proporção científica ótima.

| ID | Possibilidade e quando apresentar | Skill executora | Sugestão após adesão |
|---|---|---|---|
| `interface-numerica` | Controles discretos que combinam resposta e confiança; apresentar ao gerar objetivas ou discutir aparência e cliques | `cofen-material-nucleos` e `cofen-simulado-quadrix` | `meta.interface=numerica`; rótulos pelo peso, `0` e `>>>`; fonte e estrutura originais, caixa do trecho decisivo em verde/vermelho suave. Sem adesão: interface clássica. Contrato em `../cofen-material-nucleos/references/formato-dados.md`, seção Interface opcional |
| `resolucao-detalhada` | Resolução que define cada sigla/termo do item e o conceito vizinho da pegadinha, com glossário dos itens corrigidos; apresentar quando a pessoa disser que não sabia o que era um termo ou que faltou explicar o vizinho | `cofen-material-nucleos` (também `cofen-flashcards`) | `meta.resolucao=detalhada`; campos `termos` e `viz` em todo item; aplicar aos cadernos novos e aos ainda não respondidos. Sem adesão: resolução padrão (aula do núcleo + conceito). Contrato em `../cofen-material-nucleos/references/formato-dados.md`, seção Resolução detalhada |
| `flashcards-entrega` | Onde abrir os flashcards: HTML local (painel/disco, sem Claude), artefato (link, celular) ou os dois; apresentar no primeiro flashcard da pessoa | `cofen-flashcards` | `html` · `artefato` · `ambos`. Mesmo `flashcards.html` nos dois modos; marcações não somam entre modos, vale o YAML exportado. Sem adesão: só `.tsv` + `_notebooklm.md` (formato padrão da Gaby), oferecendo o HTML numa linha. Contrato em `../cofen-flashcards/SKILL.md`, §3 |
| `revisao-objetivas` | Retomar conteúdos estudados no caderno cotidiano; apresentar no planejamento ou geração de questões | `cofen-simulado-quadrix` e `cofen-material-nucleos` | 70% tema atual e 30% revisão pela quantidade de itens, arredondando sem aumentar o total |
| `revisao-discursivas` | Revisar por explicação e aplicação; apresentar no planejamento ou geração de enunciados | `cofen-simulado-quadrix`; editor via `cofen-redacao-discursiva` | 70/30 pelo peso dos quesitos ou esforço; preservar coesão, equilibrando na semana se necessário |
| `audio-curto-revisao` | Retomar dificuldades após correção; apresentar quando houver pontos que justifiquem áudio | `cofen-diagnostico-gaps` seleciona pontos e prepara fonte/roteiro NotebookLM em `$P/audio/notebooklm/` | 5–8 min, 100% revisão, 2–3 pontos: pergunta com pausa, explicação, justificativa discursiva e desafio antes da resolução |

## Condições de execução

- Revisar apenas conteúdos já estudados. Priorizar erros com certeza, recorrências
  e erros recentes; depois acertos com dúvida e amostras de temas antigos. Dúvida
  não equivale a erro conceitual. Considerar respostas e ledger da pessoa ativa.
- Usar variações para testar aplicação. Questões reais pertinentes continuam
  permitidas; refação idêntica deve ser intencional e não comprova sozinha consolidação.
- Preservar o escopo pedido e a distribuição dos simulados completos. Não ampliar
  pedidos focados nem acrescentar carga para cumprir percentuais. Retomar temas sem
  conexão com o assunto atual em questões independentes quando necessário.
- D+2/D+7/D+21 orientam seleção sem impor tarefas extras nem alterar o gerador do
  cronograma. Não inferir conclusão pela data planejada.
- Áudio é fonte/roteiro, salvo produção efetiva de arquivo de áudio. A adesão não
  implica produzir um para todo caderno. Seguir tom e horários pessoais; audição
  exige aviso e não resolve lacunas sem evidência posterior nas respostas.
