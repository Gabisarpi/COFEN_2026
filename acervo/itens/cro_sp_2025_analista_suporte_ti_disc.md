---
id: cro_sp_2025_analista_suporte_ti_disc
orgao: "CRO-SP"
ano: 2025
banca: quadrix
cargo: "Analista de Suporte de Tecnologia de Informação"
prova: discursiva
formato: discursiva_20-30_linhas
tags_edital:
  - disc.tic
  - esp.tic.seguranca
  - esp.tic.infra
temas:
  - "Segurança em ambientes de nuvem"
aderencia: alta
fonte:
  path: acervo/fontes/cro_sp_2025_analista_suporte_ti/prova.pdf
  padrao: acervo/fontes/cro_sp_2025_analista_suporte_ti/padrao_discursiva.pdf
  nota: "extração automática (acervo_discursiva_quadrix.py); padrão definitivo de resposta da Quadrix."
---
## Enunciado

A computação em nuvem oferece benefícios inegáveis em termos de escalabilidade, flexibilidade e custo. No entanto, esses mesmos benefícios impõem novos desafios de segurança que exigem abordagem compartilhada entre provedores e clientes.

ZISSIS, Dimitrios & LEKKAS, Dimitrios. Addressing cloud computing security issues. Future Generation Computer Systems, 2012.

Considerando que o texto acima tenha caráter exclusivamente motivador, redija um texto dissertativo acerca do tema a seguir.

Segurança em ambientes de nuvem

Ao elaborar seu texto, aborde, necessariamente, os seguintes aspectos:

a) modelo de responsabilidade compartilhada na segurança da computação em nuvem;

b) identificação de três riscos comuns de segurança em ambientes de nuvem e aponte práticas recomendadas para mitigá-los; e

c) importância da criptografia e da autenticação multifator (MFA) na proteção de dados e acessos em serviços baseados em nuvem.

## Padrão definitivo de resposta (Quadrix)

A segurança em ambientes de computação em nuvem é um tema crítico, considerando a crescente dependência das organizações dessa tecnologia. Nesse contexto, o modelo de responsabilidade compartilhada é um princípio fundamental. Ele define que tanto provedores quanto clientes possuem responsabilidades distintas e complementares na proteção de dados e serviços. O provedor é responsável pela segurança da nuvem, abrangendo a infraestrutura física, o hipervisor, os serviços de rede e o armazenamento. Já o cliente é responsável pela segurança na nuvem, o que inclui a configuração adequada dos serviços contratados, gestão de identidade e acesso, proteção de dados e políticas internas de segurança. Por exemplo, em serviços do tipo IaaS (Infraestrutura como Serviço), cabe ao cliente configurar o sistema operacional, aplicar patches de segurança e definir políticas de firewall. Já em SaaS (Software como Serviço), o cliente deve gerenciar credenciais de acesso e configurar níveis apropriados de autorização para os usuários.

Entre os riscos mais comuns de segurança em nuvem, destacam-se: a configuração incorreta, o acesso não autorizado e o vazamento de dados sensíveis. Primeiro, configurações inadequadas de buckets de armazenamento ou grupos de segurança frequentemente resultam em vazamentos de dados. Esse risco pode ser mitigado utilizando ferramentas de análise contínua, como scanners de conformidade, e seguindo frameworks de melhores práticas, como o CIS Benchmark. Segundo, o acesso não autorizado é resultante da falta de mecanismos robustos de autenticação. Para mitigar esse problema, recomenda-se a implementação de autenticação multifator (MFA), políticas de senha fortes e o uso de controle de acesso baseado em função (RBAC). Por fim, o vazamento de dados sensíveis, que abrange informações não criptografadas em trânsito ou em repouso, pode ser mitigado com o uso de criptografia ponta a ponta (TLS/SSL) e políticas de prevenção de perda de dados (DLP).

Ainda no contexto da segurança, a criptografia e a autenticação multifator (MFA) desempenham papéis imprescindíveis. A criptografia protege os dados armazenados e transmitidos, garantindo confidencialidade e integridade, mesmo em caso de interceptação. Desse modo, é essencial criptografar informações sensíveis tanto em repouso quanto em trânsito, principalmente em ambientes sujeitos a múltiplos pontos de acesso. Por outro lado, a MFA adiciona uma camada extra de segurança no login, combinando algo que o usuário sabe (senha) e algo que ele possui (token, biometria ou aplicativo de autenticação). Seu uso é indispensável para proteger contas administrativas e painéis de gerenciamento de ambientes baseados em nuvem, prevenindo ataques de credenciais comprometidas.

Em conclusão, a computação em nuvem traz avanços significativos, mas exige atenção rigorosa à segurança. O modelo de responsabilidade compartilhada, combinado com práticas robustas de configuração, autenticação e proteção de dados, fornece uma base sólida para mitigar riscos. Dessa forma, provedores e clientes devem trabalhar em conjunto para assegurar que a nuvem seja, ao mesmo tempo, uma tecnologia poderosa e confiável.
