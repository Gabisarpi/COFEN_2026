---
name: cofen-flashcards
description: Gera flashcards interativos (HTML local, Artifact ou os dois) para a COFEN 2026 a partir das lacunas abertas do ledger (lacunas.yaml) ou de um tema pedido — cartões de conceito (responder de cabeça e virar) e cartões C/E calibrados no estilo Quadrix, com frase-gancho e fonte oficial, refação dos marcados "revisar" e exportação YAML para respostas/ que o diagnóstico de gaps lança no ledger. Liga o material ao dia no cronograma (plano.py). Use quando a pessoa pedir "flashcards", "cartões", "flashcard de X", "revisão rápida das lacunas", "10 minutos antes do material", "o que continua caindo", ou quando o diagnóstico propuser flashcard para uma lacuna reincidente.
---

# Flashcards das lacunas (COFEN 2026)

Herdada do repo CGU_2026 (formato HTML aprovado lá em 11/11/2026).

**Formato padrão da Gaby (sempre):** todo conjunto de flashcards sai em **dois arquivos** em `$P/flashcards/`:

1. `AAAA-MM-DD_<tema>.tsv` — importável no Anki/Quizlet. Cabeçalho `#separator:tab`, `#html:false`,
   `#tags column:3`; uma linha por cartão: `frente<TAB>verso<TAB>COFEN_tic <tema> AAAA-MM-DD`.
2. `AAAA-MM-DD_<tema>_notebooklm.md` — fonte para o NotebookLM gerar os cartões: título, “Como usar no
   NotebookLM” (fonte única marcada → Studio → Flashcards → Personalizar), prompt pedindo *exatamente N
   flashcards em português do Brasil, um por par PERGUNTA/RESPOSTA, sem acrescentar informação,
   dificuldade difícil*, e depois `### Cartão k` com `**PERGUNTA:**` / `**RESPOSTA:**`.

Os dois arquivos têm os **mesmos** cartões. O baralho HTML interativo (abaixo) é **opcional**: gerar só se
a Gaby pedir ou se a opção `flashcards-entrega` estiver registrada em `$P/preferencias-estudo.md`.
Cartões C/E no TSV/NotebookLM: frente = assertiva, verso = `C` ou `E` + motivo.

Flashcard **não substitui** caderno de núcleos nem reforço calibrado: é revisão curta (≈10 min,
15–20 cartões) da regra que a pessoa já estudou e continua errando. O ganho vem de responder de
cabeça antes de virar e de julgar C/E antes de ver o gabarito.

## 0. Contexto

1. Identidade e regras comuns (`$P`, `$C`, CONTINUIDADE, preferências, só `$P/`): `AGENTS.md` → Sempre. Ler `$C/perfil.md`.
2. Ler `$P/cronograma/lacunas.yaml` (detalhes de cada erro) e `$P/cronograma/plano.py` (`DIAS`, `MATERIAIS`).
3. Não editar `acervo/` nem `cargos/`.
4. Sem `plano.py`, ignorar os passos de cronograma e registrar o material na `CONTINUIDADE.md`.

## 1. Escolher o conteúdo

- **Padrão:** 1 a 3 lacunas abertas, na ordem de prioridade do `cofen-diagnostico-gaps` §3. Sem tema pedido, priorizar as que **reincidiram depois de
  reforço** (erro ou branco em material posterior ao estudo).
- **Um baralho por lacuna** (até 4: as cores do template são 4). Cada baralho declara as `lacunas` que cobre.
- **Fase do cronograma:** só matéria já estudada (mesma regra do §4b do `cofen-simulado-quadrix`).
  Lacuna de matéria futura → propor o dia certo, não gerar agora.
- Ler os `detalhes` da lacuna no ledger: **cada erro real vira pelo menos um cartão** (a pegadinha
  exata que a pessoa errou, reescrita; nunca o mesmo enunciado copiado).

## 2. Montar os cartões

Por baralho, 8–10 cartões, mais ou menos metade de cada tipo:

| Tipo (`k`) | Frente | Verso |
|---|---|---|
| `conceito` | pergunta aberta, tabela a montar, caso curto com números | resposta direta + porquê; tabela quando há eixos (modo × quem × prazo) |
| `ce` | assertiva Quadrix para julgar | gabarito explicado, citando o erro real quando for o caso ("foi o X3-2 do extra") |

Regras:

- **Cartões C/E passam pela `cofen-calibrar-itens`** (obrigatório): meia-verdade ou troca de rótulo
  vizinho nos E, pelo menos 1 C contraintuitivo por baralho, os dois gabaritos presentes, sem pista
  de redação. Densidade conforme `$C/perfil.md`.
- Ordem dentro do baralho: primeiro o mapa (regra/tabela), depois os C/E, por fim o caso aplicado.
- `h` (gancho): uma frase curta que a pessoa repete de cabeça ("Compliance: o prazo só cresce").
  Aparece só no verso e vira a lista "para revisar" no placar.
- `s` (fonte): lei/norma ou documentação oficial que a banca usa (Planalto, resoluções Cofen, IN SGD/ME 94/2022,
  ISO/IEC 27001/27002, ITIL, COBIT, Microsoft Learn, RFC, CERT.br). Declarar uma vez em `fontes` e referenciar pela chave. Conferir a literalidade antes de gravar;
  sem fonte conferida, não afirmar.
- Português claro, sem jargão desnecessário; HTML simples permitido em `f`/`a` (`<b>`, `<code>`, `<table>` dentro de `<div class="tbl">`).
- **Resolução detalhada** (opção `resolucao-detalhada` em `$P/preferencias-estudo.md`): `"resolucao": "detalhada"`
  no deck e, em todo cartão, `termos` (`Termo (sigla por extenso) :: definição simples || ...`) e `viz`
  (o conceito vizinho e como diferenciar). O verso mostra "O que é" antes da resposta e "Vizinho" depois.
- Toda carta tem `lacuna` = id existente no ledger (o build confere).

Formato completo do `deck.json`: [references/formato-deck.md](references/formato-deck.md).

## 3. Gerar e entregar

0. **Sempre:** gravar `$P/flashcards/AAAA-MM-DD_<tema>.tsv` e `$P/flashcards/AAAA-MM-DD_<tema>_notebooklm.md`
   com os mesmos cartões (formato no início desta skill). Os passos 1–3 valem só para o baralho HTML.
1. Pasta: `$P/simulados/gerados/AAAA-MM-DD_flashcards-<tema>/` com `deck.json`.
2. `python3 .agents/skills/cofen-flashcards/scripts/build.py <pasta>` → valida e grava `flashcards.html`.
   Erro de validação → corrigir o deck, nunca o HTML gerado.
3. **Entrega — o mesmo `flashcards.html` serve aos dois modos** (o template detecta onde está aberto):

   | Modo | Como | Exportação YAML | Quando |
   |---|---|---|---|
   | `html` | abrir o arquivo do disco no navegador (ou pelo link relativo no `cronograma.html`) | "Baixar arquivo" salva `.yaml` direto (Blob); mover para `$P/respostas/` | quem estuda pelo painel local, sem Claude aberto, ou com Codex/Cursor |
   | `artefato` | publicar com o Artifact tool: `file_path` = `flashcards.html`, `icon: "cards"`, **`capabilities: {"downloads": true}`**, descrição de uma frase; republicar no mesmo link ao corrigir (mesmo `file_path`, ou `url` em outra sessão) | "Baixar arquivo" via runtime (pode sair `.yaml.txt`) | celular, outro aparelho, link para revisar fora de casa |
   | `ambos` | os dois acima | idem | padrão quando a pessoa não escolheu |

   Escolha individual: opção `flashcards-entrega` (`html` · `artefato` · `ambos`) em
   `$P/preferencias-estudo.md`, apresentada uma vez pela `cofen-preferencias-opcionais`. Sem registro,
   entregar só o `.tsv` e o `_notebooklm.md` e oferecer o HTML numa linha; não ativar por silêncio. Sem Artifact tool
   (Codex/Cursor) → `html`. As marcações ficam no `localStorage` de cada modo/aparelho: não somam;
   vale o YAML exportado.
4. Cronograma (dia com `TAREFAS` no `plano.py`: trocar o `"?"` da tarefa pelo link, ver `cofen-diagnostico-gaps` → Tarefas do dia): em `MATERIAIS` do `plano.py`, acrescentar no dia combinado (padrão: o próximo dia de
   estudo, como primeiro item) `("Flashcards · <tema> (10 min) — HTML local", "../simulados/gerados/<pasta>/flashcards.html")`
   e/ou `("Flashcards · <tema> — artefato", "<url>")`, conforme o modo. Rodar `python3 $P/cronograma/plano.py`
   e republicar o `cronograma.html` no artifact da pessoa (ler o artifact antes; as marcações ficam no
   banco dele). As revisões D+2/D+7/D+21 daquele dia passam a repetir os flashcards automaticamente.
5. `$P/CONTINUIDADE.md`: uma linha com link, pasta e dia.

## 4. Exportação e lançamento no ledger

A página grava as marcações só no navegador; o registro vem do YAML que a pessoa salva em
`$P/respostas/AAAA-MM-DD_flashcards-<tema>.yaml` (caminho em `export` no deck). Formato:

```yaml
material: "pessoal/gaby/simulados/gerados/2026-12-15_flashcards-contratos/flashcards.html"
tipo: flashcards
pessoa: gaby
cargo: tic
gerado: "2026-12-15"
data: "2026-12-15"          # dia da exportação
itens:
  - id: ol3
    baralho: ol
    lacuna: retencao-object-lock-ilm
    tipo: ce
    resposta: E              # primeira resposta; na = não respondeu
    gabarito: E
    resultado: acerto        # acerto | erro | na
    autoavaliacao: sei       # sei | revisar | sem_marcar
    gatilho: "Bypass tem \"Governance\" no nome: só vale no governance."
  - id: ol1
    baralho: ol
    lacuna: retencao-object-lock-ilm
    tipo: conceito
    autoavaliacao: revisar
    gatilho: "Trava versão, não o nome do objeto."
```

Ao receber o arquivo (renomear `.yaml.txt` se vier assim), seguir o `cofen-diagnostico-gaps` com estas regras:

- Validar: ids e gabaritos batem com o `deck.json`; `resultado` coerente com `resposta`.
- Na entrada do ledger, a fonte do deck usa **`tipo: revisao`**, com `path` do YAML exportado. O
  `tools/validar_estudo.py` só aceita `objetiva`, `discursiva`, `revisao` ou `simulado`; `tipo: flashcards`
  reprova a validação.
- **C/E com erro** → `ocorrencias += 1` na `lacuna`, detalhe com o id do cartão e a regra (como em cadernos).
- **Conceito marcado `revisar`** → só detalhe (autoavaliação não é evidência de erro).
- **C/E em branco (`na`)** não conta.
- Lacuna com **todos os C/E certos (mínimo 2) e nenhum `revisar`** → pode ir para `em_reforco`.
  Flashcard **nunca** marca `resolvido`: isso exige acerto em caderno/simulado calibrado.
- Nota curta em `notas:` do ledger (data, acertos C/E, revisar por baralho; `notas` guarda só ~10 linhas, ver `cofen-diagnostico-gaps` §2) e linha na tabela "Feito" do CONTINUIDADE.

## Anti-padrões

- Copiar o enunciado que a pessoa errou (ela decora a resposta, não a regra).
- Baralho só de conceito, sem C/E (o diagnóstico fica sem medida), ou só com um gabarito.
- Gancho que entrega o gabarito na frente do cartão.
- Editar `flashcards.html` à mão em vez do `deck.json` + build.
- Entregar só o HTML e esquecer o `.tsv` e o `_notebooklm.md`.
- Publicar sem `capabilities: {"downloads": true}` (no artefato o botão de baixar some; resta só copiar).
- Editar o template para um modo só: o mesmo HTML precisa funcionar do disco e como artefato.
- Marcar lacuna como `resolvido` por causa de flashcard.
