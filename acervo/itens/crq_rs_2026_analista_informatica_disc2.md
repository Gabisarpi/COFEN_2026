---
id: crq_rs_2026_analista_informatica_disc2
orgao: "CRQ-RS"
ano: 2026
banca: quadrix
cargo: "Analista de Informática"
prova: discursiva
formato: discursiva_20-30_linhas
tags_edital:
  - disc.tic
  - esp.tic.seguranca
  - esp.tic.infra
  - esp.tic.bd
temas:
  - "Estudo de caso: backup e recovery após corrupção de dados e falha de armazenamento"
aderencia: alta
fonte:
  path: acervo/fontes/crq_rs_2026_analista_informatica/prova.pdf
  padrao: acervo/fontes/crq_rs_2026_analista_informatica/padrao_discursiva.pdf
  nota: "extração automática (acervo_discursiva_quadrix.py); padrão definitivo de resposta da Quadrix."
---
## Enunciado

O Conselho Regional de Química da 5ª Região (CRQ-V) utiliza um sistema informatizado para gerenciar o cadastro de profissionais e empresas registradas, emitir certidões, controlar processos de fiscalização, registrar anuidades e armazenar documentos digitais relacionados às atividades finalísticas e administrativas da autarquia. Recentemente, após uma atualização realizada em um servidor de banco de dados, foi identificado um problema que resultou na corrupção de parte das informações referentes aos registros de fiscalização dos últimos dias. Paralelamente, constatou-se que um equipamento de armazenamento apresentou falha física, comprometendo o acesso a arquivos institucionais importantes. Durante a análise do incidente, a equipe de tecnologia da informação verificou que existiam rotinas de backup configuradas, porém havia dúvidas quanto à periodicidade adotada, à validação das cópias realizadas e à efetividade dos procedimentos de recuperação dos dados.

Considerando esse cenário, a diretoria do CRQ-V determinou a elaboração de um plano de ação para assegurar a continuidade dos serviços prestados aos profissionais da área química, minimizar riscos de perda de informações e garantir a recuperação adequada dos dados em situações de falha ou desastre.

Com base na situação hipotética apresentada, redija um estudo de caso, com foco na aplicação prática do conteúdo profissional, atendendo, necessariamente, os seguintes aspectos:

a) importância dos procedimentos de backup para a proteção das informações institucionais do CRQ-V, indicando, pelo menos, três práticas recomendadas para a realização e o gerenciamento das cópias de segurança;

b) procedimentos de recovery que poderiam ser adotados para restaurar os dados e os serviços afetados pelo incidente, destacando as etapas necessárias para garantir a integridade e a consistência das informações recuperadas; e

c) medidas técnicas e administrativas que o CRQ-V pode implementar para aumentar a confiabilidade do ambiente de backup e recovery, reduzindo a probabilidade de indisponibilidade ou perda de dados no futuro.

## Padrão definitivo de resposta (Quadrix)

Os procedimentos de backup são essenciais para preservar a disponibilidade, a integridade e a recuperabilidade das informações do CRQ-V, cuja perda pode interromper atividades de registro, fiscalização, arrecadação e emissão de certidões. As cópias devem seguir periodicidade definida conforme a criticidade dos sistemas e o limite aceitável de perda de dados. Entre as práticas recomendadas estão a estratégia 3-2-1, com três cópias em duas mídias e uma fora do ambiente principal; a manutenção de cópia isolada, offline ou imutável; a definição de retenção e versionamento; e a validação periódica da integridade e da efetiva restauração dos backups. As cópias também devem ser criptografadas e protegidas por controle de acesso.

Diante do incidente, a equipe deve inicialmente conter a falha, interromper alterações no ambiente afetado e identificar a extensão da corrupção e os serviços comprometidos. Em seguida, deve selecionar o ponto de recuperação íntegro mais recente e restaurar, em ambiente controlado, o banco de dados, os arquivos e as dependências necessárias. Quando disponíveis, backups incrementais e registros de transações podem ser aplicados na ordem correta para reduzir a perda de informações. Antes do retorno à produção, devem ser executadas verificações de integridade, consistência referencial e conciliação dos registros, além de testes funcionais e de acesso. A liberação deve ocorrer de forma controlada, com monitoramento e documentação das etapas executadas.

Para aumentar a confiabilidade do ambiente, o CRQ-V deve instituir política formal de backup, retenção e recuperação, com responsabilidades, prioridades, objetivos de tempo de recuperação e de perda aceitável de dados. Também deve adotar monitoramento automatizado, alertas de falha, segregação de credenciais, autenticação forte, redundância de equipamentos e repositórios e proteção física e lógica das cópias. A redundância melhora a disponibilidade, mas não substitui o backup, pois pode reproduzir dados corrompidos. Testes periódicos de restauração, exercícios do plano de recuperação de desastres, gestão de mudanças e capacitação da equipe completam as medidas necessárias para reduzir indisponibilidades e assegurar a continuidade dos serviços.
