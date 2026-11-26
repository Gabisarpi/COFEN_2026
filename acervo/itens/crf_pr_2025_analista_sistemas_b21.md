---
id: crf_pr_2025_analista_sistemas_b21
orgao: "CRF-PR"
ano: 2025
banca: quadrix
cargo: "Analista de Sistemas"
prova: P3
formato: certo_errado
tags_edital:
  - esp.tic.seguranca
  - esp.tic.bd
itens: 106-110
aderencia: media
fonte:
  path: acervo/fontes/crf_pr_2025_analista_sistemas/prova.pdf
  gabarito: acervo/fontes/crf_pr_2025_analista_sistemas/gabarito.pdf
  nota: "extração automática (acervo_extract_quadrix.py); gabarito definitivo. Item 11: alterado para “C” (certo). / Itens 12, 60 e 68: anulados."
---

## Comando

O Conselho Regional de Farmácia do Estado do Paraná (CRF-PR) mantém um sistema corporativo que armazena dados cadastrais de profissionais, registros de empresas farmacêuticas, processos administrativos, multas e informações financeiras. O ambiente utilizou PostgreSQL em servidores Linux, com exigência de alta disponibilidade, controle de acesso com base em papéis, auditoria de operações sensíveis, rotinas de backup automatizadas e otimização de desempenho para relatórios estatísticos enviados ao Conselho Federal. A equipe de TI precisou garantir a continuidade dos serviços, conformidade com normas de proteção de dados e integridade das informações institucionais. Com base nessa situação hipotética, julgue os itens a seguir.

## Assertivas

| id | texto | gabarito |
|----|-------|----------|
| 106 | A ativação do parâmetro log_statement = ‘all’ no arquivo postgresql.conf é indicada para ambientes de produção do CRF, pois não impacta desempenho e melhora a auditoria sem gerar sobrecarga significativa. | E |
| 107 | A execução do comando pg_ctl promote no servidor principal do CRF realiza a promoção automática da réplica em modo streaming para nó primário, mantendo a sincronização bidirecional entre os dois servidores. | E |
| 108 | Utiliza-se o comando pg_dumpall -U postgres > backup_crf.sql para realizar um backup lógico completo (global) do banco do CRF, incluindo funções, permissões e estruturas. | C |
| 109 | O comando psql -U crf_admin -d crf_db < backup_crf.sq l permite restaurar um backup lógico específico para um banco de dados já existente no PostgreSQL. | C |
| 110 | A habilitação do parâmetro synchronous_commit = off no ambiente do CRF garante que todas as transações sejam confirmadas somente após a gravação dos dados no servidor primário e em todas as réplicas síncronas, aumentando a consistência dos registros financeiros. | E |
