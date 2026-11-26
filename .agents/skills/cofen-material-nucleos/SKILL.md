---
name: cofen-material-nucleos
description: Gera materiais de estudo interativos (Artifact HTML) para a COFEN 2026 com os núcleos que a Quadrix mais repete num bloco do edital. Junta itens C/E reais do acervo e variações inéditas que invertem o gabarito, esconde a resolução até a pessoa responder e marcar a confiança, explica o que decide cada item, como a banca inverte e o texto literal da fonte (AWS, Microsoft, Google, NIST, CERT.br, RFC), e exporta o resultado em YAML para o diagnóstico de gaps. Use sempre que a pessoa pedir "material de estudo", "faz outro material", "próximo bloco", "núcleos mais cobrados", "questões que mais se repetem", "assuntos recorrentes da banca", "artifact de questões", "material como o de Redes", ou quiser estudar um eixo/matéria do edital a partir do que a banca mais cobra, mesmo sem dizer "núcleo".
---

# Material por núcleos recorrentes (COFEN 2026)

O objetivo é ensinar **como a banca cobra**, não só o conteúdo. A Quadrix repete o mesmo
núcleo (a mesma afirmação técnica ou o mesmo trecho de lei/norma) em provas diferentes e muda um
detalhe para inverter o gabarito, e muitas vezes copia a definição de uma lei, norma ou manual.
O material treina exatamente isso: reconhecer o núcleo, achar a palavra que decide o item
e saber a frase-fonte.

Formato herdado do repo CGU_2026 (validado lá em 24/10/2026). Não copie remissões "veja o item
seguinte" em `inv` (ver §3, resolução sem spoiler); para ligar pares, use o campo `par`.

## 0. Contexto

1. Identidade e regras comuns (`$P`, `$C`, CONTINUIDADE, preferências, pastas): `AGENTS.md` → Sempre.
   Depois **`$C/perfil.md`** (obrigatório), **`cofen-calibrar-itens`** (obrigatório antes de gravar) e
   `$C/mapa-edital.md`.
2. Destino do caderno e das respostas: `AGENTS.md` → Simulados Quadrix (`$P/simulados/gerados/…`;
   nunca `$P/revisao/`). Materiais antigos em `revisao/` podem permanecer; **novos** vão para
   `simulados/gerados/`. Não edite `acervo/`; se achar erro nele, avise e ofereça a correção.
3. Se a pessoa não disser qual bloco, siga o cronograma dela (`$P/cronograma/`) e veja em
   `$P/simulados/gerados/` o que já foi feito. Sem cronograma, sugira o próximo bloco ainda sem
   material pela prioridade do acervo (`acervo/previsao-cofen.md`, `acervo/cobertura-edital.md`) ou,
   sem acervo, pelas **Prioridades do P3** do perfil.
4. Esta skill vale para Claude Code e Cursor. Onde o texto citar uma ferramenta que o seu agente não
   tem (WebFetch, Artifact), use o equivalente: busca/leitura web para conferir fontes, arquivo HTML
   local para publicar (ver §5).

## 1. Validar o escopo pelo edital **e pelo perfil** (não pule)

Para apresentar opções ainda desconhecidas ou gerenciar adesão à revisão, seguir
[cofen-preferencias-opcionais](../cofen-preferencias-opcionais/SKILL.md). A oferta é
opcional para a pessoa e não bloqueia a geração do material solicitado.

Preferências individuais (leitura e limites: `AGENTS.md` → Sempre): aplicar eventual revisão
integrada antes de selecionar itens, respeitando o escopo solicitado. Registrar em meta a
distribuição atual/revisão e os temas retomados quando habilitada. Preferências pessoais não
mudam a calibração da trilha.

Extraia o texto do edital: `pdftotext -layout edital.pdf <scratch>/edital.txt`. Copie o subitem
exato do **Cargo 407** (item 19.2.4 e seguintes). Depois procure o mesmo assunto nos **outros cargos de TI**
(404 Analista de Sistemas, 405 Analista de Suporte Técnico) e nos complementares, para traçar a fronteira:

- Blocos 1–7 são comuns aos três cargos de TI; blocos 8–12 são exclusivos do 407. Conteúdo que só
  existe no 404 (desenvolvimento web, arquitetura de software) ou no 405 (atendimento ao usuário,
  manutenção de BD) não vira núcleo do 407, salvo se também estiver nos blocos 1–7.
- Assunto que cai muito no acervo mas o edital não lista (ex.: cabeamento estruturado, VoIP, MPLS)
  fica fora e é mencionado em "Ficaram de fora".
- Itens de outro bloco vão para o material daquele bloco. Não repita itens já usados em material
  anterior.

**Calibração de fonte = `$C/perfil.md`.** O miolo dos itens reais tem de soar como a Quadrix cobra:

1. Prefira no pool provas **Quadrix** (peso ×2), de preferência de conselhos profissionais.
2. Itens Cebraspe ou de outra banca (inclusive os herdados do CGU) entram como frequência de conteúdo
   ou **par de inversão pontual** (1–2 por núcleo), nunca como maioria dos `real:1`.
3. Variações inéditas seguem o **Escopo dos itens** do perfil e a régua de `cofen-calibrar-itens`
   (assertiva curta, literalidade de lei/norma).
4. Antes de gravar, conte os `real:1` por banca: a **maioria** deve ser Quadrix. Sem Quadrix suficiente
   no tema, diga isso na entrega e no `method_html`.

Registre no `method_html`: (a) subitem do edital do 407; (b) fronteira com 404/405;
(c) **mistura de fontes** (quantos reais Quadrix × de outras bancas e por quê).

## 2. Levantar os itens

**Questões reais por padrão:** em todo material ou bloco, inclusive curto e pós-áudio,
buscar no acervo e incluir questões reais sempre que houver itens pertinentes ao tema,
ao edital e ao perfil da pessoa, com enunciado e gabarito oficial verificáveis. Não esperar
pedido explícito nem limitar os reais a exemplos fora do caderno. Complementar com inéditos
sem impor cota fixa de reais. Se não houver reais adequados, entregar inéditos e registrar
brevemente o motivo no `meta.json` e na entrega.

Identificar cada real com órgão, ano, cargo e número, preservando texto e gabarito oficial
(`real:1`). Âncoras geradas (`COFEN_ANCORA`), adaptações e conversões de múltipla escolha para
C/E são inéditos (`real:0`), com a inspiração identificada quando cabível. Não forçar item
desatualizado, fora do escopo ou já usado pela pessoa apenas para cumprir a preferência;
repetição intencional cabe em revisão/refação. Esta preferência substitui a orientação
genérica de usar o acervo apenas como estilo, salvo pedido explícito de somente inéditos.

```bash
python3 <skill>/scripts/extract.py --repo <raiz> --tag esp.tic.<bloco> --out <scratch>/pool
# opcional: --grep 'regex' para achar itens do assunto marcados com outra tag
```

O script descarta provas `*_completa` (texto em geral embaralhado; `--incluir-completas` para conferir algo
pontual) e os ids de `RUINS`. Leia o `pool.txt` inteiro: a tag não garante o assunto. Depois do extract,
filtre de novo pela régua do `perfil.md`.

Para cada núcleo candidato, conte **em quantas provas distintas** ele aparece. Muitos itens de
uma única prova pesam menos que o mesmo núcleo em seis provas. Ranqueie por provas × peso no
edital. Reserve um ou dois núcleos para tópicos que o edital cita explicitamente mas o acervo
quase não tem: eles levam mais variações inéditas.

Busque também as justificativas oficiais no acervo (respostas a recursos, quando a banca publica):
elas entram na resolução.

## 3. Montar os núcleos

- **Tamanho**: 6 a 9 núcleos, de 4 a 6 itens cada (35 a 45 itens no total). Mais do que isso cansa e a pessoa não termina.
- **Pares mínimos**: procure, entre provas, o mesmo núcleo com gabaritos opostos (TCP: "dois FIN" E × "FIN e ACK" C; fiscal técnico "atesta o recebimento definitivo" E × "acompanha a execução e avalia a qualidade" C). São os itens mais valiosos.
- **Resolução sem spoiler**: a resolução de um item nunca pode entregar o gabarito de outro. Nada de "veja o item seguinte, que traz a definição certa", "compare com o próximo", "a mesma ideia virou C em outra prova". A pessoa lê a resolução antes de responder o item seguinte, e no modo intercalado a ordem nem é a mesma. Em `inv`, escreva a própria reescrita que inverte o gabarito (entre aspas, com o C/E resultante). Para ligar dois itens de um par mínimo, use o campo `par` (ver `references/formato-dados.md`): a página só mostra a ligação quando os dois já foram corrigidos. O build recusa remissões a outro item.
- **Variações inéditas**: pelo menos uma por núcleo, mudando um único detalhe (número, camada, verbo, quem faz o quê). Nada de E gritante ou C de cartilha. Siga as regras de anti-dedução do `AGENTS.md` e do **`$C/perfil.md`** (protocolo/porta/camada nos blocos técnicos; prazo, papel e artefato em contratos, normas e auditoria).
- **Calibração:** antes de gravar, cumprir **`cofen-calibrar-itens`** (estilo Quadrix, `code` ≲10%, sem pista, anti-dedução; invariante — não remover o ponteiro sem pedido expresso).
- **Literalidade**: quando o assunto tem documentação de provedor ou norma, crie variações que reproduzam ou invertam a frase-fonte. Confira cada trecho na página original (WebFetch ou a leitura web do seu agente) **antes** de escrever e coloque-o em `quote`. Veja `references/fontes-literais.md` (fontes já conferidas e candidatas) e acrescente lá as que você conferir.
- **Gabarito discutível**: se o oficial contraria a norma técnica, mantenha o oficial e explique em `nota` o que a norma diz e por que a banca foi tolerante.
- **Equilíbrio**: evite núcleo com todos os gabaritos iguais.

### Explicações que ensinam (padrão obrigatório)

A resolução é onde a pessoa aprende. Escreva para quem **ainda não estudou o assunto** e errou o item:
explicar só o resultado ("são 30 hosts") não basta, é preciso mostrar o caminho.

**Por núcleo: `aula` (obrigatória).** Mini-aula de 120 a 250 palavras em HTML simples (`<p>`, `<ul>`,
`<ol>`, `<table>`, `<b>`), que aparece fechada no topo do núcleo ("Entenda o assunto") e junto do cartão
na revisão. Estrutura:
1. **O que é e para que serve**, em linguagem de conversa, com uma analogia concreta.
2. **Como funciona**: o mecanismo em 3 a 5 passos ou uma tabelinha comparativa dos conceitos vizinhos
   que a banca troca (ex.: TCP × UDP; anulação × revogação; PAD × PAR com comissão e prazo).
3. **Onde a banca pega**: os 2 ou 3 detalhes que viram pegadinha (números, quem faz o quê, absolutos).

A `aula` explica o tema, **não** os itens: nada de "no item 3..." nem de antecipar o gabarito de um item
específico. Use exemplos próprios, diferentes dos enunciados.

**Por item: `exp` (obrigatório) em 3 a 6 frases**, nesta ordem:
1. a ideia central em palavras simples;
2. o mecanismo (por que é assim);
3. o veredito ligado ao gatilho: "por isso o item é C/E: [o trecho] está certo/errado porque...".

**Por item, quando couber:**
- `passo` (passos separados por ` | `, viram lista numerada) — **obrigatório** em item numérico ou
  procedimental (sub-rede, prazos encadeados, cálculo de RAID, ordem de fases, DORA, three-way handshake):
  a conta ou a sequência completa, um passo por linha, com os números do próprio item.
- `ex` — exemplo concreto do dia a dia de um órgão público ou de infraestrutura, com números ou nomes
  plausíveis (um servidor, um contrato, uma rede 192.168.10.0/24).
- `lembre` — regra de bolso de uma linha para não confundir de novo ("servidor 67, cliente 68: o servidor
  chegou primeiro"; "anula o ilegal, revoga o inconveniente").

**Resolução detalhada (opção individual `resolucao-detalhada`):** com adesão registrada em
`$P/preferencias-estudo.md`, `"resolucao": "detalhada"` no `meta.json` e, em **todo** item, `termos`
(cada sigla/termo técnico do enunciado por extenso, definição simples e exemplo; fonte em inglês traduzida)
e `viz` (o conceito vizinho da pegadinha e como diferenciar). Não presumir que a `aula` já cobriu o termo.
Sem adesão, seguir o padrão. Contrato em [formato-dados.md](references/formato-dados.md).

**Teste antes de gravar:** alguém que nunca viu o assunto, lendo só `aula` + `exp` + `passo`, consegue
resolver um item parecido com outros números ou outras palavras? Se não, reescreva. Prefira uma frase a
mais que um salto de raciocínio. Sem jargão sem tradução na primeira vez que aparece.

### Tipos de pegadinha (use os nomes no campo `peg`)

Troca de conceito vizinho · inversão (quem faz o quê) · absolutização ("somente", "suficiente", "impede", "elimina", "apenas") · detalhe numérico (porta, bits, camada, prefixo) · generalização (regra do IPv4 aplicada ao IPv6, de um SKU a todos) · meia-verdade (começo certo, fim errado) · justificativa falsa ("uma vez que...") · literalidade de provedor/norma · C contraintuitivo.

## 4. Escrever os dados e gerar a página

**Interface individual:** consultar `$P/preferencias-estudo.md`. Com adesão à opção
`interface-numerica`, definir `"interface": "numerica"` no `meta.json`; sem adesão,
omitir o campo ou usar `"classica"`. Com adesão à opção `resolucao-detalhada`, definir também
`"resolucao": "detalhada"` (o build exige `termos` e `viz` em todo item). Contrato em
[formato-dados.md](references/formato-dados.md), seção Interface opcional.
Usar o template canônico: não copiar o protótipo nem redesenhar o caderno. A opção
preserva fonte, núcleos, mini-aulas, conceito, conceito-chave/cartões, inversões e
demais campos; altera somente controles de resposta e o destaque de “Decide o item”.

Escreva `dados.js` e `meta.json` no scratchpad seguindo `references/formato-dados.md`. Depois:

```bash
python3 <skill>/scripts/build.py --data <scratch>/dados.js --meta <scratch>/meta.json \
  --repo <raiz do repo> \
  --out <repo>/pessoal/<quem>/simulados/gerados/AAAA-MM-DD_<tema>/caderno.html
```

Persista também `dados.js` e `meta.json` na mesma pasta do `caderno.html`.
No `meta.json`, **`peso` = `1`** em todos os blocos (Quadrix COFEN: acerto +1, erro −1, branco 0).
Sem o campo, o build assume `1`; outro valor é recusado.
Campo `material` deve apontar para o path sob `simulados/gerados/…`.

O build confere aspas, campos obrigatórios e núcleos vazios, e avisa quando o texto de um item
real não bate com o acervo. Resolva todo ERRO. Para cada AVISO, decida: texto divergente quase
sempre é cópia errada e deve ser recopiado do acervo.

**Verificador de calibração** (`scripts/verificar.py`, chamado pelo build; isolado: `--data --meta`):
conta itens com `code` (próprio ou herdado do núcleo), a proporção C/E e a sequência do gabarito na ordem
"por núcleo", com as regras de `cofen-calibrar-itens` §1 e de `cofen-simulado-quadrix` ("Sem pista de
sequência"). ERRO: `code` > 20%, flip rate > 75% ou
janela de 8 com ≥ 7 alternâncias; o resto é AVISO, e bloco < 8 itens só recebe aviso. `meta.cota_code_livre: true`
(só com pedido expresso) afrouxa a cota; `--sem-verificacao` rebaixa os erros, e regenerar material com a
mesma `key` também (a ordem não pode mudar). Erro em caderno novo → reordenar ou reescrever, não silenciar.

O template (`assets/template.html`) já tem o design, os dois temas, as bolhas C/E, a confiança, o destaque do
"Decide o item" em verde (acertou), vermelho (errou) ou neutro (branco), a mini-aula por núcleo e os blocos
Passo a passo, Exemplo e Para lembrar,
o modo intercalado, o resumo, a calibração, o export YAML e o painel **Revisar**: filtro pelo resultado
da última tentativa (errei com certeza, errei na dúvida, acertei na dúvida, branco, não respondidos, ou
"Para revisar", que junta os quatro primeiros nessa ordem de prioridade), filtro por núcleo e **Refazer**,
que devolve os itens filtrados sem resposta e sem resolução e guarda a tentativa anterior. Desempenho e
calibração contam só a primeira tentativa; a refação aparece à parte. Não reescreva o HTML: mude só os dados.
Se a pessoa pedir uma mudança de layout, mude o template, para que valha para todos os materiais.

**Template mudou ou material antigo precisa de correção?** Se o `dados.js` não estiver na pasta, extraia-o
da página publicada e remonte com o template atual:

```bash
python3 <skill>/scripts/rebuild.py --html $P/simulados/gerados/<pasta>/caderno.html --out <scratch>/<eixo>
# corrija <scratch>/<eixo>.dados.js se precisar e rode o build.py com ele e com <eixo>.meta.json
```

O `key` se mantém, então as respostas salvas no navegador continuam valendo ao republicar no mesmo link
(desde que a ordem dos itens não mude). Publicado em outra sessão: leia o artifact antes de republicar.

## 5. Publicar e reportar

O HTML gerado é autossuficiente: guarda as respostas no `localStorage` do navegador e só busca fontes
do Google (sem internet, usa as do sistema). Funciona aberto direto do disco.

- **Com a ferramenta Artifact (Claude Code / claude.ai):** publique (`file_path` = o HTML gerado,
  `icon` = uma palavra genérica do assunto, `description` em uma frase, `capabilities: {downloads: true}`)
  e entregue o link. A capacidade liga o botão **Baixar arquivo**, que salva o YAML como
  `<respostas>.yaml.txt` (o `downloads` não aceita `.yaml`). Ao lançar, renomeie para `.yaml`.
  Material publicado antes desse botão: republicar no mesmo link com `capabilities: {downloads: true}`.
- **Sem ela (Cursor e outros agentes):** não tente publicar. Entregue o caminho do arquivo e diga para
  abrir no navegador (duplo clique ou "Open in Browser"). As respostas ficam naquele navegador; o YAML
  exportado e colado em `$P/respostas/` é o que segue pelo git.

**Cronograma interativo:** se existir `$P/cronograma/plano.py` com o dicionário `MATERIAIS`, acrescente
`"DD/MM": [("<nome>", "<link>")]` no dia do material (dia com `TAREFAS` no `plano.py`: trocar o `"?"` da tarefa pelo link, ver `cofen-diagnostico-gaps` → Tarefas do dia), rode `python3 $P/cronograma/plano.py` e republique
`$P/cronograma/cronograma.html` no mesmo link. A revisão espaçada passa a apontar para o material sozinha.

Na resposta à pessoa, de forma curta:

- o link ou o caminho do arquivo;
- a tabela de núcleos com o número de provas;
- o que a validação pelo edital excluiu e por quê;
- **calibração:** quantos `real:1` vieram do acervo aderente do `perfil.md` vs. do outro cargo (e se algum entrou só como par de inversão);
- os achados de literalidade (que fonte a banca copiou);
- os gabaritos discutíveis;
- a sugestão do próximo bloco.

Não faça commit sem pedido. Lembre que o resultado copiado vai para `$P/respostas/` e que, com ele,
a skill `cofen-diagnostico-gaps` alimenta o `lacunas.yaml`. No YAML, `resposta`/`confianca`/`resultado` são
sempre da primeira tentativa; refações vêm em `refacao: [{resposta, confianca, resultado}]`. Um item errado
que a pessoa acertou com certeza na refação pode baixar a severidade da lacuna, mas não fechá-la sozinho. Quando a pessoa colar o resultado, use os
erros com "certeza" e os núcleos com saldo negativo para escolher o próximo material ou o reforço.
