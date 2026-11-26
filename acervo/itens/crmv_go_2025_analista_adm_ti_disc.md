---
id: crmv_go_2025_analista_adm_ti_disc
orgao: "CRMV-GO"
ano: 2025
banca: quadrix
cargo: "Analista Administrativo - Área de Tecnologia da Informação"
prova: discursiva
formato: discursiva_20-30_linhas
tags_edital:
  - disc.tic
  - esp.tic.redes
  - esp.tic.infra
  - esp.tic.gestao
temas:
  - "Monitoramento e gerenciamento de redes e sistemas de TI: práticas, ferramentas e desafios operacionais"
aderencia: alta
fonte:
  path: acervo/fontes/crmv_go_2025_analista_adm_ti/prova.pdf
  padrao: acervo/fontes/crmv_go_2025_analista_adm_ti/padrao_discursiva.pdf
  nota: "extração automática (acervo_discursiva_quadrix.py); padrão definitivo de resposta da Quadrix."
---
## Enunciado

Em ambientes corporativos cada vez mais dependentes de infraestrutura digital, o monitoramento e o gerenciamento proativo de redes e sistemas tornaram-se atividades estratégicas. Detectar falhas antes que impactem os usuários, manter níveis de desempenho aceitáveis e garantir a disponibilidade dos serviços são responsabilidades fundamentais das equipes de TI. Nesse contexto, ferramentas como Zabbix, Nagios, PRTG e SolarWinds possibilitam a coleta contínua de métricas e a automação de respostas a incidentes, permitindo uma visão integrada de toda a infraestrutura tecnológica.

Referência: TURNBULL, James. The Art of Monitoring. Turnbull Press, 2018.

Considerando que o texto acima tenha caráter exclusivamente motivador, redija um texto dissertativo acerca do tema a seguir.

Monitoramento e gerenciamento de redes e sistemas de TI: práticas, ferramentas e desafios operacionais

Ao elaborar seu texto, aborde, necessariamente, os seguintes aspectos:

a) diferença entre monitoramento reativo e monitoramento proativo, destacando os impactos de cada abordagem na gestão da disponibilidade de serviços;

b) descrição de duas métricas essenciais que devem ser acompanhadas em um sistema de monitoramento de redes, justificando a importância de cada uma para a continuidade operacional; e

c) apresentação de duas boas práticas de gerenciamento de redes e sistemas que contribuem para a eficiência do monitoramento e a prevenção de incidentes, relacionando-as a conceitos de gestão de TI como ITIL ou ISO/IEC 20000.

## Padrão definitivo de resposta (Quadrix)

Quanto à diferença entre monitoramento reativo e proativo e os seus impactos, é preciso mencionar, pelo menos, o seguinte: o monitoramento reativo caracteriza-se pela atuação após a ocorrência de falhas ou degradação de desempenho, sendo comum em ambientes que não possuem mecanismos automatizados de alerta ou análise preditiva. Nesse modelo, as ações são tomadas apenas quando o problema já afeta o usuário final — por exemplo, quando um servidor fica inacessível e o administrador é notificado tardiamente. Embora simples, essa abordagem aumenta o tempo médio de resolução (MTTR) e reduz a disponibilidade dos serviços. Já o monitoramento proativo busca identificar anomalias antes que causem impacto perceptível, utilizando métricas, logs e alertas predefinidos para antecipar incidentes. Ferramentas como Zabbix, Nagios e PRTG Network Monitor permitem criar gatilhos e limiares de desempenho (thresholds) que automatizam respostas a eventos, como o aumento de uso de CPU ou latência de rede. Essa abordagem reduz o tempo médio entre falhas (MTBF) e favorece a gestão da disponibilidade e confiabilidade dos serviços de TI. Em suma, o modelo proativo está alinhado à cultura de observabilidade e à gestão contínua preconizada pelo ITIL 4, que privilegia a antecipação de falhas em vez da simples reação a elas.

Em relação às duas métricas essenciais no monitoramento de redes e à sua importância, espera-se que o candidato mencione, latência (delay): mede o tempo que um pacote leva para ir de um ponto a outro na rede. Altas latências podem indicar congestionamento, perda de pacotes ou problemas de roteamento. Essa métrica é crítica para aplicações em tempo real (como VoIP e videoconferência), sendo um dos indicadores principais na gestão de desempenho (Performance Management). Disponibilidade (Uptime): representa o percentual de tempo em que um serviço ou dispositivo está operacional. É uma métrica fundamental no monitoramento de

servidores e aplicações críticas, diretamente relacionada aos acordos de nível de serviço (SLAs). O acompanhamento do uptime permite identificar padrões de falhas e avaliar a eficácia da manutenção preventiva. Essas métricas são coletadas por protocolos como SNMP (Simple Network Management Protocol) e complementadas por logs de eventos de sistemas operacionais e serviços.

Com relação às duas boas práticas de gerenciamento de redes e sistemas e sua relação com ITIL, o texto deve mencionar, pelo menos, a implantação de um processo de gerenciamento de incidentes (ITIL 4): essa prática define procedimentos padronizados para registrar, classificar, priorizar e resolver incidentes, garantindo resposta rápida e comunicação transparente entre equipes. O alinhamento com o processo ITIL permite reduzir o impacto operacional e aumentar a satisfação dos usuários, transformando o monitoramento em um componente estratégico do ciclo de melhoria contínua (Continual Improvement Model); e automação de scripts de correção e alertas inteligentes: a utilização de scripts (como Bash, Python ou PowerShell) para reiniciar serviços, limpar caches ou ajustar configurações automaticamente reduz o tempo de resposta e elimina intervenções manuais repetitivas. Essa prática reforça o princípio da melhoria contínua (PDCA) previsto na ISO/IEC 20000-1:2018, otimizando a gestão de recursos e garantindo maior estabilidade do ambiente de TI.
