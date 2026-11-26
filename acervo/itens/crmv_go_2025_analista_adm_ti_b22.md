---
id: crmv_go_2025_analista_adm_ti_b22
orgao: "CRMV-GO"
ano: 2025
banca: quadrix
cargo: "Analista Administrativo - Área de Tecnologia da Informação"
prova: P3
formato: certo_errado
tags_edital:
  - esp.tic.bd
itens: 86-90
aderencia: alta
fonte:
  path: acervo/fontes/crmv_go_2025_analista_adm_ti/prova.pdf
  gabarito: acervo/fontes/crmv_go_2025_analista_adm_ti/gabarito.pdf
  nota: "extração automática (acervo_extract_quadrix.py); gabarito definitivo. Item 15: anulado."
---

## Comando

O Conselho Regional de Medicina Veterinária do Estado de Goiás (CRMV-GO) mantinha um banco de dados relacional denominado CRMV_GO, que registrava veterinários, especialidades, clínicas e atendimentos. As principais tabelas estão dispostas a seguir. VETERINARIO (id_vet, nome, crmv, data_inscricao, id_especialidade, ativo) ESPECIALIDADE (id_especialidade, descricao) CLINICA (id_clinica, nome_clinica, cidade) ATENDIMENTO (id_atendimento, id_vet, id_clinica, data_atendimento, status) Com base nessa situação hipotética e no uso do comando SELECT no banco de dados CRMV_GO, julgue os itens seguintes.

## Assertivas

| id | texto | gabarito |
|----|-------|----------|
| 86 | O comando a seguir apresenta o nome do veterinário, a sua especialidade e o número total de atendimentos concluídos, incluindo apenas veterinários com pelo menos cinco atendimentos concluídos. SELECT v.nome, e.descricao, COUNT(a.id_atendimento) AS total FROM VETERINARIO v INNER JOIN ESPECIALIDADE e ON v.id_especialidade = e.id_especialidade INNER JOIN ATENDIMENTO a ON v.id_vet = a.id_vet WHERE a.status = 'Concluído' GROUP BY v.id_vet, v.nome, e.descricao HAVING COUNT(a.id_atendimento) >= 5; | C |
| 87 | O comando a seguir apresenta os veterinários que não têm especialidade cadastrada, considerando que o campo id_especialidade pode ser NULL. SELECT nome FROM VETERINARIO WHERE id_especialidade = NULL; | E |
| 88 | O comando a seguir apresenta corretamente os veterinários que realizaram atendimentos em todas as cidades cadastradas na tabela CLINICA. SELECT nome FROM VETERINARIO v WHERE id_vet IN (SELECT id_vet FROM ATENDIMENTO a INNER JOIN CLINICA c ON a.id_clinica = c.id_clinica); | E |
| 89 | O comando a seguir apresenta apenas veterinários ativos cujo CRMV termina com “1234” e que realizaram atendimentos na cidade de Goiânia, utilizando subconsulta correlacionada. SELECT nome FROM VETERINARIO v WHERE ativo = 1 AND crmv LIKE '%1234' AND EXISTS (SELECT 1 FROM ATENDIMENTO a INNER JOIN CLINICA c ON a.id_clinica = c.id_clinica WHERE a.id_vet = v.id_vet AND c.cidade = 'Goiânia'); | C |
| 90 | O comando a seguir apresenta corretamente os veterinários que possuem mais atendimentos em clínicas de Brasília do que em Goiânia. SELECT v.nome FROM VETERINARIO v INNER JOIN ATENDIMENTO a ON v.id_vet = a.id_vet INNER JOIN CLINICA c ON a.id_clinica = c.id_clinica WHERE c.cidade = 'Brasília' GROUP BY v.id_vet HAVING COUNT(a.id_atendimento) > (SELECT COUNT(a2.id_atendimento) FROM ATENDIMENTO a2 INNER JOIN CLINICA c2 ON a2.id_clinica = c2.id_clinica WHERE c2.cidade = 'Goiânia'); | E |
