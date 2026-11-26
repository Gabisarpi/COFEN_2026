---
id: crefito17_2026_analista_ti_b19
orgao: "CREFITO-17"
ano: 2026
banca: quadrix
cargo: "Analista de Tecnologia da Informação"
prova: P3
formato: certo_errado
tags_edital:
  - esp.tic.bd
itens: 91-94
aderencia: alta
fonte:
  path: acervo/fontes/crefito17_2026_analista_ti/prova.pdf
  gabarito: acervo/fontes/crefito17_2026_analista_ti/gabarito.pdf
  nota: "extração automática (acervo_extract_quadrix.py); gabarito definitivo. Itens 55, 60 e 61: alterados para “E” (errado). / Item 114: alterado para “C” (certo)."
---

## Comando

Durante uma análise das rotinas do sistema, o analista deparou-se com o script SQL a seguir, utilizado diariamente para gerar relatórios financeiros de fisioterapeutas cadastrados. SELECT p.nome, c.cidade, COUNT(a.id) AS total_atendimentos, SUM(a.valor) AS receita_total FROM Profissional p INNER JOIN Atendimento a ON p.id = a.id_profissional LEFT JOIN Clinica c ON a.id_clinica = c.id WHERE p.especialidade = ‘Fisioterapia’ GROUP BY p.nome, c.cidade HAVING COUNT(a.id) > 10 ORDER BY receita_total DESC; Com base nessa situação hipotética e a partir da análise estrutural dessa query e dos conceitos fundamentais de banco de dados, julgue os itens seguintes.

## Assertivas

| id | texto | gabarito |
|----|-------|----------|
| 91 | Na ordem lógica de processamento da consulta, a cláusula HAVING atua antes de WHERE, filtrando linhas individuais que só depois serão submetidas ao GROUP BY. | E |
| 92 | No contexto apresentado, a tabela Atendimento funciona como tabela de relacionamento ao vincular profissionais e clínicas por meio de chaves estrangeiras. | C |
| 93 | Caso haja lentidão na geração do relatório, a criação de índice sobre a coluna especialidade pode constituir medida de otimização voltada a acelerar a filtragem de registros realizada na cláusula WHERE. | C |
| 94 | O comando SELECT integra a DDL, por ser o mecanismo responsável por definir a estrutura lógica dos dados que serão exibidos ao usuário. | E |
