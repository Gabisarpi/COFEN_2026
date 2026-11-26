---
id: crp_sp_2025_especialista_gestao_tic_disc
orgao: "CRP-SP"
ano: 2025
banca: quadrix
cargo: "Especialista em Gestão – Tecnologia da Informação e Comunicação"
prova: discursiva
formato: discursiva_20-30_linhas
tags_edital:
  - disc.tic
  - esp.tic.bd
temas:
  - "Técnicas de otimização de consultas em bancos de dados relacionais"
aderencia: alta
fonte:
  path: acervo/fontes/crp_sp_2025_especialista_gestao_tic/prova.pdf
  padrao: acervo/fontes/crp_sp_2025_especialista_gestao_tic/padrao_discursiva.pdf
  nota: "extração automática (acervo_discursiva_quadrix.py); padrão definitivo de resposta da Quadrix."
---
## Enunciado

À medida que o volume de dados cresce exponencialmente, a eficiência das consultas torna-se um fator crítico para o desempenho dos sistemas de informação. Consultas mal formuladas podem degradar significativamente a performance de aplicações e gerar gargalos em ambientes corporativos.

ELMASRI, R.; NAVATHE, S. B. Fundamentos de Sistemas de Banco de Dados. 6. ed. São Paulo: Pearson, 2011. (com adaptações).

Considerando que o texto acima tenha caráter exclusivamente motivador, redija um texto dissertativo acerca do tema a seguir.

Técnicas de otimização de consultas em bancos de dados relacionais

Ao elaborar seu texto, aborde, necessariamente, os seguintes aspectos:

a) importância da otimização de consultas em ambientes de grande volume de dados;

b) técnicas ou estratégias que podem ser utilizadas para otimizar consultas SQL; e

c) exemplo prático (real ou hipotético) em que a falta de otimização de consultas resultaria em impacto negativo para uma organização.

## Padrão definitivo de resposta (Quadrix)

Quanto à importância da otimização de consultas em ambientes de grande volume de dados, é preciso mencionar, pelo menos, o seguinte: a otimização de consultas é fundamental em ambientes com grandes volumes de dados porque influencia diretamente o desempenho dos sistemas e a experiência dos usuários. Consultas mal otimizadas podem consumir muitos recursos do banco de dados, como CPU, memória e I/O, causando lentidão nas respostas, bloqueios, e até mesmo indisponibilidade do sistema. Em aplicações críticas, como sistemas bancários, de e-commerce ou saúde, a demora na execução de uma simples consulta pode comprometer a tomada de decisões em tempo real e a satisfação dos clientes.

Quanto às técnicas ou estratégias para otimizar consultas SQL, espera-se que o candidato mencione: a) Uso de índices: criar índices em colunas frequentemente utilizadas em cláusulas WHERE, JOIN, ORDER BY e GROUP BY acelera a localização dos dados, evitando varreduras completas na tabela (full table scan). No entanto, é importante avaliar o impacto nos comandos de escrita ( INSERT, UPDATE, DELETE), que podem ser afetados negativamente pelo excesso de índices; b) Evitar o uso de coringas no início do LIKE: consultas como WHERE nome LIKE '%silva' impedem o uso de índices e forçam a varredura completa da tabela. Utilizar LIKE 'silva%' permite a utilização de índices com melhor desempenho; e c) Utilização de EXPLAIN (ou EXPLAIN PLAN): comando que permite analisar como o otimizador de consultas do banco planeja executar uma query. A partir dessas informações, o desenvolvedor pode reescrever a consulta, adicionar índices ou criar visões materializadas, conforme o caso.

Com relação ao exemplo prático (real ou hipotético) em que a falta de otimização de consultas resultaria em impacto negativo para uma organização, o texto deve mencionar, pelo menos, que, imagine uma empresa de comércio eletrônico que possui uma tabela de pedidos com milhões de registros. O setor de logística relata lentidão ao consultar pedidos dos últimos três dias para expedição. A consulta utiliza a cláusula WHERE data_pedido >= CURRENT_DATE - 3, mas não há índice na coluna data_pedido. Essa falta de índice faz com que a consulta analise todos os registros da tabela, consumindo tempo e recursos excessivos. A solução seria criar um índice na coluna data_pedido, permitindo que o banco de dados acesse diretamente os registros mais recentes, otimizando a consulta e garantindo respostas rápidas à equipe logística.

Brasília/DF, 3 de novembro de 2025. INSTITUTO QUADRIX
