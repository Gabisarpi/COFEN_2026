# Revisão — {{DATA}} ({{DIA_SEMANA}}) — {{TEMA}} + P3 do dia: {{TEMA_P3}}

**Tags:** {{TAGS}}  
**PDF:** `pessoal/gaby/revisao/{{ARQUIVO}}/folha-de-estudo.pdf` (gabarito do "Teste-se": `gabarito-do-teste-se.pdf`, na mesma pasta)  
**Áudio:** `pessoal/gaby/audio/notebooklm/{{ARQUIVO}}.md`  
**Flashcards:** `pessoal/gaby/flashcards/{{ARQUIVO}}_anki.tsv` (Anki/Quizlet) e `{{ARQUIVO}}_notebooklm.md`  
**Caderno C/E ({{N_ITENS}} itens):** `pessoal/gaby/simulados/gerados/{{ARQUIVO}}/` · [abrir]({{LINK_CADERNO}})  
**Fonte oficial:** {{LINK_FONTE}}

## Roteiro do dia ({{HORAS}} h)

| Tempo | O quê |
|-------|-------|
| {{T0}} | **Revisão espaçada:** flashcards de ontem (comece pelas âncoras) |
| {{T1}} | Ler as seções e os quadros desta folha, com a fonte aberta ao lado |
| {{T2}} | Caderno: núcleos do tema principal, sem consultar |
| {{T3}} | **P3 do dia:** a seção do P3 + o núcleo correspondente do caderno |
| {{T4}} | "Teste-se" · conferir o gabarito separado · preencher "Meus erros do dia" · baixar o YAML do caderno |

Na dúvida real, deixe em branco: na Quadrix, cada erro anula um acerto.

## Passo a passo do dia (o que fazer, em ordem, e onde)

**Antes (fora das {{HORAS}} h, quando puder):** no **NotebookLM**, crie o notebook "{{TITULO_CURTO}} — {{DATA_CURTA}}", adicione a fonte `{{ARQUIVO}}.md` (pasta `audio/notebooklm/`) e gere os áudios em **Studio → Resumo em áudio → Personalizar**, colando o Prompt A e depois o Prompt B. Ouça no deslocamento ou na academia: é reforço, não substitui os passos abaixo.

| # | Passo | Onde | Como |
|---|-------|------|------|
| 1 | **Flashcards de ontem** (10 min) | Anki ou NotebookLM | Responda de cabeça antes de virar; comece pelas âncoras e pelos cartões marcados "revisar" |
| 2 | **Ler a folha** (seções do tema) | Este PDF | Leitura ativa: sublinhe o que é número, prazo ou "quem faz o quê" |
| 3 | **Caderno: tema principal** | [Painel](https://claude.ai/artifact/8dVvHQNixZauPtCZm7Ta1a) → card de hoje → link do caderno | Marque C, E ou branco **e** a confiança; leia a resolução de cada item logo depois |
| 4 | **P3 do dia** | Este PDF (seção do P3) + núcleo do P3 no caderno | Mesmo procedimento do passo 3 |
| 5 | **Teste-se** | Fim deste PDF + `gabarito-do-teste-se.pdf` | Responda num papel, sem olhar a folha; depois confira |
| 6 | **Baixar o resultado do caderno** | Caderno → botão **Baixar arquivo** | Sai `…yaml.txt` em Downloads; **não precisa renomear**: me diga "salve meu resultado" que eu busco e lanço no controle de lacunas |
| 7 | **Âncoras dos erros** | Painel → card de hoje → campo de nota | Uma frase por erro; ou me mande no chat |
| 8 | **Marcar o dia como feito** | Painel → card de hoje → **Feito** | Corrija as horas se precisar |
| 9 | **Importar os flashcards de hoje** (para amanhã) | Anki: *Arquivo → Importar* `{{ARQUIVO}}_anki.tsv` · NotebookLM: fonte `{{ARQUIVO}}_notebooklm.md` → Studio → Flashcards → Personalizar (prompt no topo do arquivo) | Só importar; a revisão é amanhã no passo 1 |


## 1. {{SECAO_1}}

- 

## 2. {{SECAO_2}}

| | | |
|---|---|---|
| | | |

## 3. {{SECAO_3}}

- 

### Pares que a banca troca

| A banca escreve | A fonte diz |
|---|---|
| | |

### Ganchos de memória

- 

## {{N}}. P3 do dia — {{TEMA_P3}}

| | | |
|---|---|---|
| | | |

**Gancho:** 

## Teste-se (C/E em uma linha) — gabarito no PDF separado

| # | Afirmação |
|---|---|
| 1 | |
| 2 | |
| 3 | |

<!-- O gabarito NUNCA entra nesta folha: vai em revisao/{{ARQUIVO}}/gabarito-do-teste-se.md (colunas # | C/E | Por quê) e no PDF correspondente. -->

## Meus erros do dia

| Item/tema | Eu marquei | Certo | Âncora (1 frase) |
|-----------|------------|-------|------------------|
| | | | |

## Amanhã

**{{DATA_AMANHA}} ({{DIA_AMANHA}}):** {{TEMA_AMANHA}} · P3 do dia: {{P3_AMANHA}}

<!--
Material do dia completo (formato fixo, ver CONTINUIDADE.md):
Nome do dia ({{ARQUIVO}}): AAAA-MM-DD_tema-1_tema-2, minúsculas, hífen dentro do tema, sublinhado entre temas (ex.: 2026-11-28_decreto-94406_res-507_backup).
1. revisao/{{ARQUIVO}}/folha-de-estudo.md + .pdf (python3 tools/md_html.py <md> → wkhtmltopdf; sem listas aninhadas, que não renderizam)
2. revisao/{{ARQUIVO}}/gabarito-do-teste-se.md + .pdf
3. caderno C/E em simulados/gerados/{{ARQUIVO}}/ (skill cofen-material-nucleos) + link em MATERIAIS do plano.py
4. fonte de áudio em audio/notebooklm/{{ARQUIVO}}.md (a partir de audio/notebooklm/_MODELO.md)
5. flashcards/{{ARQUIVO}}_anki.tsv + flashcards/{{ARQUIVO}}_notebooklm.md
6. respostas/{{ARQUIVO}}.yaml (resultado do caderno, quando a pessoa enviar)
-->
