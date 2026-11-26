---
id: cfn_2024_pae_ti_suporte_disc
orgao: "CFN"
ano: 2024
banca: quadrix
cargo: "Profissional de Atividades Estratégicas (PAE) – Ocupação: Tecnologia da Informação – Suporte Técnico"
prova: discursiva
formato: discursiva_20-30_linhas
tags_edital:
  - disc.tic
  - esp.tic.redes
  - esp.tic.seguranca
temas:
  - "Análise e funcionamento do sistema de nomes de domínios (DNS)"
aderencia: alta
fonte:
  path: acervo/fontes/cfn_2024_pae_ti_suporte/prova.pdf
  padrao: acervo/fontes/cfn_2024_pae_ti_suporte/padrao_discursiva.pdf
  nota: "extração automática (acervo_discursiva_quadrix.py); padrão definitivo de resposta da Quadrix."
---
## Enunciado

O sistema de nomes de domínios (DNS) foi projetado para ser um sistema distribuído e resiliente, facilitando a navegação na web e permitindo a escalabilidade da Internet. Sem o DNS, a experiência de uso da Internet seria muito mais complicada para os usuários finais.

MOCKAPETRIS, P. Domain names – implementation and specification. RFC 1035, 1987.

Considerando que o texto acima tenha caráter exclusivamente motivador, redija um texto dissertativo acerca do tema a seguir.

Análise e funcionamento do sistema de nomes de domínios (DNS)

Ao elaborar seu texto, aborde, necessariamente, os seguintes aspectos:

a) funcionamento básico do DNS, com o destaque para o processo de resolução de nomes de domínio e as interações entre cliente e servidor DNS;

b) diferença dos principais tipos de servidores DNS (DNS recursivo, DNS autoritativo e DNS raiz), com a explicação do papel de cada um no processo de resolução de nomes; e

c) desafios de segurança enfrentados pelo DNS, com a citação de, pelo menos, duas vulnerabilidades conhecidas e a proposição de estratégias para a mitigação desses problemas no contexto de uma rede corporativa.

## Padrão definitivo de resposta (Quadrix)

Quanto ao o funcionamento básico do DNS, destacando o processo de resolução de nomes de domínio e as interações entre cliente e servidor DNS, é preciso mencionar, pelo menos, o seguinte: o DNS funciona como um sistema hierárquico e distribuído que mapeia nomes de domínio legíveis por humanos, como www.exemplo.com, para endereços IP numéricos, como 192.168.1.1. Quando um usuário insere um nome de domínio em seu navegador, uma consulta DNS é iniciada. O cliente (dispositivo do usuário) envia essa solicitação para um servidor DNS recursivo. Esse servidor consulta outros servidores DNS para resolver o nome de domínio e retorna o endereço IP correspondente ao cliente. O processo envolve várias etapas, que podem incluir consultas a servidores de domínio raiz, servidores TLD (Top-Level Domain) e servidores autoritativos, até que o nome seja resolvido. Após o processo, o endereço IP retornado permite que o navegador se conecte ao servidor da web correspondente.

Em relação à diferença dos principais tipos de servidores DNS, espera-se que o candidato mencione o servidor DNS Recursivo – também conhecido como "resolver". Esse servidor atua como intermediário entre o cliente e outros servidores DNS. Ele realiza a maior parte do trabalho de busca por informações, realizando consultas em nome do cliente até encontrar a resposta correta (ou uma mensagem de erro, caso o domínio não exista). Servidor DNS Autoritativo: esse servidor contém as informações definitivas sobre um domínio específico, incluindo os registros DNS (por exemplo, A, MX e CNAME). Ele é responsável por fornecer a resposta final para consultas

relacionadas a um domínio específico. Servidor DNS Raiz: o servidor DNS raiz é o ponto inicial do sistema hierárquico do DNS. Ele não contém registros DNS diretamente, mas redireciona a consulta para os servidores TLD, que, posteriormente, encaminham para servidores autoritativos. Existem 13 conjuntos de servidores raiz distribuídos globalmente.

Com relação aos desafios de segurança enfrentados pelo DNS, o texto deve mencionar, pelo menos, que o DNS enfrenta diversos desafios de segurança, com destaque para as vulnerabilidades que podem ser exploradas por atacantes. Duas das principais ameaças são: 1 - DNS Spoofing (ou Cache Poisoning), vulnerabilidade na qual um invasor insere informações falsas em um cache DNS, fazendo com que futuras consultas retornem endereços IP incorretos. Com isso, os usuários podem ser redirecionados para sites falsos ou maliciosos sem perceber. Uma estratégia eficaz é implementar DNSSEC (Domain Name System Security Extensions), que adiciona autenticação criptográfica às respostas DNS, garantindo que as consultas não sejam adulteradas; e 2 - Ataques DDoS (Distributed Denial of Service) em servidores DNS, nos quais servidores DNS são sobrecarregados com uma quantidade massiva de consultas simultâneas, o que pode derrubá-los e deixar os serviços indisponíveis. Para mitigar esse risco, é recomendado o uso de arquiteturas de alta disponibilidade, como a distribuição de servidores DNS em diferentes geografias e o uso de redes de entrega de conteúdo (CDNs) para absorver o tráfego excessivo.

Brasília/DF, 21 de janeiro de 2025. INSTITUTO QUADRIX
