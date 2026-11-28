# Revisão — {{DATA}} ({{DIA_SEMANA}}) — {{TEMA}} + P3 do dia: {{TEMA_P3}}

**Tags:** {{TAGS}}  
**PDF:** `pessoal/gaby/revisao/{{ARQUIVO}}.pdf` (gabarito do "Teste-se": `{{ARQUIVO}}_gabarito.pdf`)  
**Áudio:** `pessoal/gaby/audio/notebooklm/{{ARQUIVO}}.md`  
**Flashcards:** `pessoal/gaby/flashcards/{{ARQUIVO}}.tsv` (Anki/Quizlet) e `_notebooklm.md`  
**Caderno C/E ({{N_ITENS}} itens):** `pessoal/gaby/simulados/gerados/{{ARQUIVO}}/` · [abrir]({{LINK_CADERNO}})  
**Fonte oficial:** {{LINK_FONTE}}

## Roteiro do dia ({{HORAS}} h)

| Tempo | O quê |
|-------|-------|
| {{T1}} | Ler as seções e os quadros desta folha, com a fonte aberta ao lado |
| {{T2}} | Caderno: núcleos do tema principal, sem consultar |
| {{T3}} | **P3 do dia:** a seção do P3 + o núcleo correspondente do caderno |
| {{T4}} | "Teste-se" · conferir o gabarito separado · preencher "Meus erros do dia" · baixar o YAML do caderno |

Na dúvida real, deixe em branco: na Quadrix, cada erro anula um acerto.

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

<!-- O gabarito NUNCA entra nesta folha: vai em {{ARQUIVO}}_gabarito.md (colunas # | C/E | Por quê) e no PDF correspondente. -->

## Meus erros do dia

| Item/tema | Eu marquei | Certo | Âncora (1 frase) |
|-----------|------------|-------|------------------|
| | | | |

## Amanhã

**{{DATA_AMANHA}} ({{DIA_AMANHA}}):** {{TEMA_AMANHA}} · P3 do dia: {{P3_AMANHA}}

<!--
Material do dia completo (formato fixo, ver CONTINUIDADE.md):
1. esta folha .md + .pdf (python3 tools/md_html.py <md> → wkhtmltopdf; sem listas aninhadas, que não renderizam)
2. {{ARQUIVO}}_gabarito.md + .pdf
3. caderno C/E em simulados/gerados/{{ARQUIVO}}/ (skill cofen-material-nucleos) + link em MATERIAIS do plano.py
4. fonte de áudio em audio/notebooklm/{{ARQUIVO}}.md (a partir de audio/notebooklm/_MODELO.md)
5. flashcards {{ARQUIVO}}.tsv + {{ARQUIVO}}_notebooklm.md
-->
