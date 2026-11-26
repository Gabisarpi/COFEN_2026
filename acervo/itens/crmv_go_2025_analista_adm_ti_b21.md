---
id: crmv_go_2025_analista_adm_ti_b21
orgao: "CRMV-GO"
ano: 2025
banca: quadrix
cargo: "Analista Administrativo - Área de Tecnologia da Informação"
prova: P3
formato: certo_errado
tags_edital:
  - esp.tic.fundamentos
  - esp.tic.infra
itens: 81-85
aderencia: alta
fonte:
  path: acervo/fontes/crmv_go_2025_analista_adm_ti/prova.pdf
  gabarito: acervo/fontes/crmv_go_2025_analista_adm_ti/gabarito.pdf
  nota: "extração automática (acervo_extract_quadrix.py); gabarito definitivo. Item 15: anulado."
---

## Comando

Acerca dos bancos de dados relacionais e NoSQL, do gerenciamento de usuários e das permissões e dos conceitos de virtualização, julgue os itens a seguir.

## Assertivas

| id | texto | gabarito |
|----|-------|----------|
| 81 | No SQL Server, o Transaction Log é responsável por garantir a atomicidade e a durabilidade das transações, permitindo a recuperação ponto a ponto (detalhada) de dados em caso de falhas, inclusive no modo Simple Recovery Model. | E |
| 82 | Os bancos de dados NoSQL do tipo Document Store, como o MongoDB, armazenam os dados em estruturas JSON (ou BSON) e permitem consultas complexas e indexação em campos aninhados. | C |
| 83 | No MySQL 8.0, quando um usuário recebe privilégios por meio de uma role (função) que é ativada automaticamente no login (SET DEFAULT ROLE ALL), os privilégios herdados não são aplicáveis a procedimentos armazenados criados antes da associação da role, exigindo reatribuição explícita via GRANT OPTION para refletir o novo contexto de execução. | E |
| 84 | Em soluções de virtualização, o conceito de snapshots permite registrar o estado completo de uma máquina virtual em um determinado momento, incluindo memória, disco e configurações, possibilitando o retorno ao estado anterior após falhas ou atualizações mal sucedidas. | C |
| 85 | Em ambientes VMware vSphere e Hyper-V, a ativação de NUMA (Non-Uniform Memory Access) é opcional e raramente afeta o desempenho de VMs com múltiplos vCPUs, pois o hypervisor aloca a memória de forma uniforme em todos os nós físicos, evitando automaticamente o acesso remoto à memória de outros processadores. | E |
