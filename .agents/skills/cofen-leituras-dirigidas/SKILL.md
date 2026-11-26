---
name: cofen-leituras-dirigidas
description: Prepara leituras técnicas dirigidas para o COFEN 2026 — um trecho curto de fonte que a banca usa (lei e normas do edital, IN SGD/ME 94/2022, guias gov.br de contratação de TIC, ISO 27001/27002, ITIL, COBIT, Microsoft Learn, Red Hat, NIST, CERT.br, RFC) escolhido para preparar o treino discursivo ou a discursiva do dia, com 3 perguntas-guia, termos-âncora, frases literais e uma conferência de quais termos a pessoa usou no texto. Grava os docs no artifact "Leituras Dirigidas" da pessoa e liga cada leitura ao cronograma (plano.py). Use quando a pessoa pedir "leitura dirigida", "leitura técnica", "próximas leituras", "artigo da AWS/Microsoft sobre X", "o que ler antes da discursiva", "melhorar o raciocínio da escrita lendo", "estender as leituras", ou ao avaliar as leituras na correção de uma discursiva.
---

# Leituras técnicas dirigidas (COFEN 2026)

A leitura **não é estudo de conteúdo solto**. Ela serve à escrita do mesmo dia: a pessoa lê
~12–15 min de uma fonte que a banca costuma copiar, responde 3 perguntas, anota 5 termos e monta um
mapa **problema → causa → controle → justificativa**. Depois escreve o treino curto ou a Q2 e, na
conferência, marca quais termos-âncora usou. A conferência mede se a leitura chegou ao texto.

Formato herdado do repo CGU_2026 (validado lá em novembro/2026). O exemplo de doc completo (tema do CGU)
fica em [assets/exemplo-l001.json](assets/exemplo-l001.json): copie a estrutura, não o conteúdo.

## 0. Contexto

1. Identidade e regras comuns (`$P`, `$C`, CONTINUIDADE, preferências, só `$P/`): `AGENTS.md` → Sempre.
   Depois **`$C/perfil.md`** (seção *Discursiva*) e as fontes de `cofen-simulado-quadrix` → Fontes.
2. Leia o cronograma (`$P/cronograma/plano.py`: `DIAS`, `MATERIAIS`) e o ledger
   (`$P/cronograma/lacunas.yaml`). Veja quais dias da janela têm treino curto ou discursiva.
3. Leia `$P/leituras/leituras.json`, se existir: `_sobre` traz a URL do artifact da pessoa,
   `piloto` traz a métrica e as regras combinadas, `leituras` traz o que já foi lido. Não repita fonte
   nem seção.
4. O `plano.py` editado é o da pessoa ativa. Não edite `acervo/` nem `cargos/`.

## 1. Escolher o tema de cada dia

- **Dois tipos de leitura, um tema por dia:**
  - **Preparação:** presa a uma escrita do mesmo dia (ou da Q2 próxima): o treino `tNNN`, o Modelo Q2,
    a folha da discursiva ou um bloco C/E do dia.
  - **Revisão** (`treino.tipo = "revisao"`): leitura estratégica de matéria P3 **já estudada**, fora do
    material do dia (ex.: dia de P1/P2), para ampliar e revisar. Escolha pelas lacunas abertas de maior
    severidade e reincidência, variando o bloco (contratos, auditoria, redes, segurança...). Sem treino escrito: a `nota`
    pede 2 ou 3 linhas no campo do mapa, e a página mostra o passo 4 como "Fixar". Em dia de simulado,
    só aquecimento curto (~8 min).
- Priorize o que a pessoa **escreveu mal**: zeros num aspecto do padrão, mecanismo não dito ("falou
  em glosa sem dizer o que a dispara"), lacunas abertas em `lacunas.yaml` com tag `disc.tic`. O campo
  `porque` cita esse erro real (treino/Q2 e o que faltou), não um elogio genérico ao tema.
- Se o treino do dia **já traz o comando** do caso, a leitura só prepara esse treino: não crie
  parágrafo próprio.

## 2. Escolher e conferir a fonte

- Prefira **pt-BR** e fonte oficial: texto da lei no Planalto, resoluções no site do Cofen, IN SGD/ME
  94/2022 e modelos/guias de contratação de TIC do gov.br, guias do PPSI, CERT.br, Microsoft Learn
  `learn.microsoft.com/pt-br`, documentação Red Hat.
- **Só entra link que você abriu agora** (WebFetch): a página existe, a seção indicada cobre as
  perguntas e as frases literais estão lá. PDF que devolve erro ou JSON → troque de fonte.
- Recorte o trecho: `secao` diz exatamente o que ler e o que pular. Item de portaria ou páginas de
  PDF vão numerados (ex.: "Anexo I, itens 5.1–5.4"; "pp. 47–51"). `minutos` ≤ 15 (aquecimento antes
  da discursiva: ~6).
- `extra` é opcional: uma segunda leitura curta para o bloco C/E do dia, com `nota` dizendo o que
  ler.

## 3. Montar o doc

Campos de cada leitura `lNNN` (ver o exemplo):

| Campo | Regra |
|---|---|
| `ordem`, `dia` | `dia` no formato do cronograma ("Qua 11/11") |
| `tema`, `porque` | `porque` = qual escrita a leitura prepara e qual erro real ela ataca |
| `fonte`, `titulo`, `url`, `secao`, `minutos` | conferidos no passo 2 |
| `perguntas` | 3 perguntas que, respondidas, montam o mapa problema → causa → controle → justificativa |
| `ancoras` | 5–7 `{termo, sentido}`. Termos que o padrão de resposta premia. `sentido` em 1 linha, com o mecanismo. Se um termo não está no texto lido, diga "(conceito, não está neste artigo)" |
| `frases` | 2–4 `{texto, onde}` **copiadas literalmente** da página, com a seção onde estão |
| `na_q2` | como usar os termos na discursiva/treino: em qual aspecto do padrão eles entram |
| `treino` | `{nome, url, nota}`: a escrita do dia (artifact do treino/discursiva) e o que escrever com a leitura. Treino curto: `nome` = `"Treino curto tNNN · <tema do treino>"` (o mesmo título que a página mostra) e `url` com âncora `#tNNN`, que abre a página direto nele |
| `extra` | opcional, `{titulo, url, nota}` |

Grave `$P/leituras/leituras/lNNN.json` (um arquivo por doc) e acrescente a entrada em
`$P/leituras/leituras.json` (campo `leituras`). Os ids continuam a numeração existente.

## 4. Gravar no artifact

- **A pessoa já tem a página** (`_sobre` traz a URL): grave os docs com `ArtifactData` `batch`
  (`set` em `leituras/lNNN`), sem republicar a página. Para corrigir um doc existente, use `set` com
  `if_version`. Não toque na coleção `respostas`, que é da pessoa.
- **Primeira vez da pessoa:** copie [assets/pagina.html](assets/pagina.html) para
  `$P/leituras/pagina.html` (já vem com a chave `cofen-gaby-leituras:` e o cabeçalho “Cargo 407 · Gaby”) e
  publique com `capabilities: {db: {}, user: {}}`, ícone `book`. Depois semeie os docs e grave a URL
  em `_sobre`.
- A página lê `leituras` (ordenada por `ordem`) e grava em `respostas/{id}`: `termos`, `mapa`,
  `status` (`lida` / `escrita`), `marcados` (termos-âncora que a pessoa marcou como usados no texto),
  `concluido`, `atualizado`.

## 5. Ligar ao cronograma

No `plano.py` da pessoa, para cada dia com leitura:

1. No `det` do dia, antes do treino/discursiva: `Leitura técnica (15 min): <fonte curta>, <recorte> → <para
   qual escrita>.` (no aquecimento: `Aquecimento (6 min, antes da discursiva): …`). O nome é sempre **"Leitura
   técnica"**, para não confundir com a "Leitura de discursiva" (provas do acervo).
2. Em `MATERIAIS["DD/MM"]`: `("Leitura técnica · <tema curto>", "<URL do artifact>")` (dia com `TAREFAS` no `plano.py`: trocar o `"?"` da tarefa pelo link, ver `cofen-diagnostico-gaps` → Tarefas do dia).
3. Rode `python3 $P/cronograma/plano.py` e republique o painel do cronograma, se houver artifact.
   Antes de republicar, faça `git pull --rebase`.
4. Acrescente ou atualize em `$P/CONTINUIDADE.md` o bullet "Leituras técnicas" (janela, docs,
   métrica).
5. Faça commit; push só com autorização da Gaby.

## 6. Avaliar (na correção da discursiva ou do treino)

- Leia `respostas` com `ArtifactData` `list`: veja `status`, `marcados` e `mapa` da leitura ligada.
- Na correção, conte os termos-âncora que **de fato** aparecem no texto (não só os marcados) e veja se
  entraram no aspecto certo do padrão. Compare com a escrita anterior equivalente (a métrica fica em
  `piloto.metrica`).
- Registre o resultado em `leituras.json` (`piloto.resultado`) e na CONTINUIDADE. Se melhorou,
  proponha estender a leitura às próximas discursivas. Se não melhorou, proponha cortar e devolver o tempo aos
  itens C/E. A mudança no cronograma segue a regra da `cofen-diagnostico-gaps`: propor primeiro.

## Anti-padrões

- Link não aberto, ou frase "literal" parafraseada.
- Leitura longa (>15 min) ou artigo inteiro sem recorte.
- Revisão de matéria ainda não estudada (fura a fase do cronograma).
- Parágrafo próprio quando o treino já cobre o caso.
- `porque` genérico ("tema importante"), sem o erro real que motivou a leitura.
- Republicar a página só para trocar conteúdo: conteúdo novo vai como doc no banco.
