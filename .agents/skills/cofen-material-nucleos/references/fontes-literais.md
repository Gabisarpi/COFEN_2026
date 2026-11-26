# Fontes literais já conferidas

A Quadrix copia definições quase palavra por palavra destas fontes. Antes de citar um trecho
como literal, abra a página (WebFetch ou a leitura web do seu agente) na mesma sessão. As citações abaixo foram conferidas em
24/10/2026 e servem de ponto de partida, mas confira de novo se forem usadas meses depois,
porque a documentação de provedor muda.

## OWASP Top 10 (vigente no treino = **:2025**)

Índice: `https://owasp.org/Top10/2025/`. **Não** usar `…/Top10/2021/…` em item novo.

| Código | Nome 2025 | Nota vs 2021 |
|---|---|---|
| A01 | Broken Access Control | Mantém #1 |
| A02 | Security Misconfiguration | Era A05; inclui stack trace / erro verboso ao cliente |
| A03 | Software Supply Chain Failures | Expande A06:2021 components |
| A04 | Cryptographic Failures | Era A02 |
| **A05** | **Injection** | Era A03 |
| A06 | Insecure Design | Era A04 |
| A07 | Authentication Failures | Era Identification and Authentication Failures |
| A08 | Software or Data Integrity Failures | Mantém #8 (nome leve) |
| A09 | Security Logging and Alerting Failures | Ênfase em alerting |
| A10 | Mishandling of Exceptional Conditions | Novo |

Acervo/provas antigas podem citar A03=Injection ou A05=Misconfig: ao gerar variação, **atualizar** a numeração.

## Fontes brasileiras

| Fonte | Uso | Observação |
|---|---|---|
| Cartilha CERT.br — fascículo Códigos Maliciosos: `https://cartilha.cert.br/fasciculos/codigos-maliciosos/fasciculo-codigos-maliciosos.pdf` | vírus, worm, trojan, backdoor, RAT, bot/botnet, rootkit, spyware, keylogger, screenlogger, ransomware | Baixar com curl e extrair com `pdftotext` (sem `-layout`). As capitulares caem: "orna-se" = "Torna-se". TCE/AC 2024 copiou o keylogger quase literal. |
| Outros fascículos CERT.br (`/fasciculos/<nome>/fasciculo-<nome>.pdf`) | autenticação, backup, golpes, redes, privacidade, vazamento de dados | Índice: `https://cartilha.cert.br/fasciculos/` |
| Justificativas oficiais (TCDF 2024 e outras) | ficam no próprio acervo, abaixo da tabela de assertivas (`- **NNN** — Certo/Errado. ...`) | Cite-as na resolução: mostram como a banca raciocina. |

## NIST

| Documento | Trecho |
|---|---|
| SP 800-207 (Zero Trust) — `https://csrc.nist.gov/pubs/sp/800/207/final` | "no implicit trust granted to assets or user accounts based solely on their physical or network location" · "Zero trust focuses on protecting resources (assets, services, workflows, network accounts, etc.), not network segments" |
| SP 800-94 (IDPS), SP 800-41r1 (firewalls), SP 800-61 (incidentes), SP 800-145 (nuvem), CSF 2.0 | Conceitos. Conferir o texto antes de citar. |

## AWS

| Página | Trecho |
|---|---|
| VPC subnet sizing — `https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html` | "The first four IP addresses and the last IP address in each subnet CIDR block are not available for your use". Sub-rede entre /28 e /16. Broadcast não suportado na VPC. |
| Network ACLs — `https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html` | "NACLs are stateless […] Security groups are stateful" · "We evaluate the rules in order, starting with the lowest numbered rule" |
| ALB — `.../elasticloadbalancing/latest/application/introduction.html` | "functions at the application layer, the seventh layer of the Open Systems Interconnection (OSI) model" |
| NLB — `.../elasticloadbalancing/latest/network/introduction.html` | "functions at the fourth layer of the OSI model" · TCP, UDP, TCP_UDP, TLS, QUIC · "Each individual TCP connection is routed to a single target for the life of the connection." |
| Direct Connect — `.../directconnect/latest/UserGuide/Welcome.html` e `encryption-in-transit.html` | "bypassing internet service providers in your network path" · "does not encrypt your traffic that is in transit by default" (opções: Site-to-Site VPN/IPsec ou MACsec) |
| Site-to-Site VPN — `.../vpn/latest/s2svpn/VPC_VPN.html` | IPsec · "Each VPN connection includes two VPN tunnels which you can simultaneously use for high availability." |
| Shield Standard — `.../waf/latest/developerguide/ddos-standard-summary.html` | "automatic protection of Shield Standard, at no additional charge" · "network and transport layer DDoS attacks" |
| WAF — `.../waf/latest/developerguide/waf-chapter.html` | "monitor the HTTP(S) requests that are forwarded to your protected web application resources". Recursos: CloudFront, API Gateway REST, ALB, AppSync, Cognito, App Runner, Verified Access, Amplify (NLB não está na lista). |

## Microsoft Learn

| Página | Trecho |
|---|---|
| ExpressRoute — `https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction` | "ExpressRoute connections don't go over the public internet" · BGP · dois enlaces redundantes até os MSEEs |
| VNet FAQ — `.../azure/virtual-network/virtual-networks-faq` | reserva 5 endereços por sub-rede · menor /29, maior /2 · "Multicast, broadcast, IP-in-IP encapsulated packets, and GRE packets are blocked" |
| Load Balancer — `.../azure/load-balancer/load-balancer-overview` | "operates at layer 4 of the OSI model" · Basic retirado em 30/09/2025 |
| DDoS Protection — `.../azure/ddos-protection/ddos-protection-overview` | "protects at layer 3 and layer 4 […] For web applications protection at layer 7, you need to add protection at the application layer using a WAF offering" |
| Azure Firewall — `.../azure/firewall/overview` | "fully stateful firewall as a service" · Standard L3–L7 com threat intel · IDPS por assinatura só no Premium |
| Zero Trust — `https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview` | "never trust, always verify" · Verify explicitly / Use least privilege access / Assume breach |

## Google Cloud

| Página | Trecho |
|---|---|
| VPC — `https://docs.cloud.google.com/vpc/docs/vpc` (o cloud.google.com redireciona) | "VPC networks, including their associated routes and firewall rules, are global resources." · "Subnets are regional resources." |

## Identidade e criptografia (conferidas em 24/10/2026)

| Fonte | Trecho |
|---|---|
| NIST FIPS 197 (AES) — `https://csrc.nist.gov/pubs/fips/197/final` (PDF; extrair com `pdftotext`) | "The AES algorithm is capable of using cryptographic keys of 128, 192, and 256 bits to encrypt and decrypt data in blocks of 128 bits." |
| RFC 8446 (TLS 1.3) §1.2 | "Static RSA and Diffie-Hellman cipher suites have been removed; all public-key based key exchange mechanisms now provide forward secrecy." |
| NIST SP 800-63B — `https://pages.nist.gov/800-63-4/sp800-63b.html` | "Use of the PSTN for out-of-band verification is restricted as described in this section" · "A multi-factor authenticator requires two factors to execute a single authentication event" |
| MP 2.200-2/2001, art. 5º — `https://www.planalto.gov.br/ccivil_03/mpv/antigas_2001/2200-2.htm` (ISO-8859-1) | AC Raiz "compete emitir, expedir, distribuir, revogar e gerenciar os certificados das AC de nível imediatamente subseqüente ao seu" · "Parágrafo único. É vedado à AC Raiz emitir certificados para o usuário final." |
| ITI — `https://www.gov.br/iti/pt-br/assuntos/icp-brasil/entes-da-icp-brasil` | "A AC-Raiz também é responsável por emitir a Lista de Certificados Revogados (LCR)" · AC "responsável por emitir, distribuir, renovar, revogar e gerenciar certificados digitais" |
| Kubernetes Secrets — `https://kubernetes.io/docs/concepts/configuration/secret/` | "Kubernetes Secrets are, by default, stored unencrypted in the API server's underlying data store (etcd)." · ConfigMap: "An API object used to store non-confidential data in key-value pairs." |
| AWS KMS — `https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html` | "Envelope encryption is the practice of encrypting plaintext data with a data key, and then encrypting the data key under another key." · "You can safely store the encrypted data key alongside the encrypted data." · "The private key never leaves AWS KMS unencrypted." |
| AWS IAM best practices — `https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html` | "Get started with AWS managed policies and move toward least-privilege permissions" · "AWS managed policies might not grant least-privilege permissions for your specific use cases" |
| Microsoft Entra PIM — `https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure` | "Provide just-in-time privileged access" · eligible: "A role assignment that requires a user to perform one or more actions to use the role." · active: "doesn't require a user to perform any action" |
| OpenID Connect Core 1.0 — `https://openid.net/specs/openid-connect-core-1_0.html` | "OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol." (TCE/AC 2024 C7 copiou trocando OAuth por JWT) |
| OWASP Password Storage — `https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html` | "A salt is a unique, randomly generated string that is added to each password as part of the hashing process." · "Unlike a password salt, the pepper should not be public and should not be stored along with the generated hash." |

## IaC e CI/CD (conferidas em 24/10/2026)

Para conferir texto exato, baixe com curl e tire as tags com Python; o resumo da WebFetch corta as frases.

| Fonte | Trecho |
|---|---|
| AWS What is IaC — `https://aws.amazon.com/what-is/iac/` | "Infrastructure as code (IaC) is the ability to provision and support your computing infrastructure using code instead of manual processes and settings." · declarativa = "end state of a desired system"; imperativa = "describe all the steps", "becomes necessary in complex infrastructure deployments. This is especially true when the order of events is critical." · "roll back environments using previous versions of IaC configuration files" |
| AWS Configuration Management — `https://aws.amazon.com/what-is/configuration-management/` | "tracks, updates, and maintains these configurations so that the system performs at a predetermined baseline and remains secure despite any changes" (CNJ 2024 C2, item 81, traduziu) |
| AWS Continuous Delivery — `https://aws.amazon.com/devops/continuous-delivery/` | "The difference between continuous delivery and continuous deployment is the presence of a manual approval to update to production." · "deployment-ready build artifact" |
| Microsoft Learn What is IaC — `https://learn.microsoft.com/en-us/devops/deliver/what-is-infrastructure-as-code` | "networks, virtual machines, load balancers, and connection topologies" · "environment drift" · "the team edits the source, not the target" · idempotência: "regardless of the environment's starting state", "either automatically configuring the existing target, or by discarding the existing target and recreating a fresh environment" |
| Red Hat What is IaC — `https://www.redhat.com/en/topics/automation/what-is-infrastructure-as-code-iac` | imperativa: "defines the specific commands needed to achieve the desired configuration. Those commands then need to be executed in the correct order." (MPO 2024 C5, item 62, colou como "declarativa") · infraestrutura imutável reduz drift |
| Wikipedia IaC | "managing and provisioning computer data center resources through machine-readable definition files" (MPO 2024 C5, item 61) |
| IBM Continuous deployment — `https://www.ibm.com/think/topics/continuous-deployment` | "code changes to an application are released automatically into the production environment" (TCDF 2024, item 104 e justificativa) |
| Martin Fowler — CI, BlueGreenDeployment, CanaryRelease | CI: "at least daily" · blue-green: "switch the router back to your blue environment" · canary: "slowly rolling out the change to a small subset of users" |
| HashiCorp Terraform — `/terraform/language`, `/cli/commands/plan`, `/language/state/sensitive-data` | "The Terraform language is declarative, describing an intended goal rather than the steps" · plan: "lets you preview the changes", lê os objetos remotos por padrão · "Terraform stores your state in a plaintext file, which includes any secret values" |
| Ansible Glossary + Red Hat Learning Ansible | idempotência: "the result of performing it once is exactly the same as the result of performing it repeatedly without any intervening actions" (CPNU-JE 2024, item 70, no enunciado) · "Push mode is the default mode of Ansible" · "Ansible is agentless" · playbook YAML · Windows usa WinRM |
| Pro Git 3.1 e 2.5 | "A branch in Git is simply a lightweight movable pointer" (CNJ 2024 C2, item 82) · "git push <remote> <branch>" |
| Atlassian Gitflow | "The main branch stores the official release history, and the develop branch serves as an integration branch" |
| GitHub Docs — secure-use e OIDC | "automatic redaction is not guaranteed" · OIDC: "request a short-lived access token from the cloud provider" |

## Ainda não conferidas (boas candidatas)

IBM Topics (`https://www.ibm.com/think/topics/...`: zero trust, IAM, PAM, SIEM, DLP), Cloudflare Learning
(DDoS, DNS, TLS), Kubernetes docs (Pod, Service, Deployment), AWS Shared Responsibility Model,
Azure RBAC e Entra ID (MFA, acesso condicional), Google Cloud IAM, OASIS SAML 2.0 Technical Overview.

## Nuvem, SO e privacidade/incidentes (conferidas em 28/10/2026)

| Página | Trecho |
|---|---|
| NIST SP 800-145 — `https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf` | IaaS: "has control over operating systems, storage, and deployed applications; and possibly limited control of select networking components (e.g., host firewalls)" · PaaS: "possibly configuration settings for the application-hosting environment" · SaaS: "or even individual application capabilities" · Public: "It exists on the premises of the cloud provider." · Resource pooling: "may be able to specify location at a higher level of abstraction (e.g., country, state, or datacenter)" · Rapid elasticity: "in some cases automatically" |
| AWS Regions — `https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/regions.html` | "All Regions currently have three or more Availability Zones." · recursos "do not exist in any other Region unless you explicitly use a replication or copy feature" |
| AWS Lambda — `https://docs.aws.amazon.com/lambda/latest/dg/welcome.html` | "Lambda automatically manages the underlying infrastructure – including server maintenance, capacity provisioning, scaling, and patching" |
| Amazon SQS queue types — `https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html` | Standard: "at-least-once delivery", "best-effort ordering", consumidor idempotente · FIFO: ordem "within each message group", "Exactly-once processing" |
| Microsoft Learn Global Catalog — `https://learn.microsoft.com/en-us/windows/win32/ad/global-catalog` | "a partial replica of every naming context in the directory […] every object […] but with only a small number of their attributes" |
| Microsoft Learn Group Policy Hierarchy — `https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-hierarchy` | ordem Local, site, domínio, OU · "it overwrites policy that was applied earlier" |
| Windows Firewall overview — `https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/` | "block all incoming traffic, unless solicited or matching a rule" · "allow all outgoing traffic, unless matching a rule" |
| kill(1) — `https://man7.org/linux/man-pages/man1/kill.1.html` | "If no signal is specified, the TERM signal is sent." |
| nginx proxy_pass — `https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass` | "Sets the protocol and address of a proxied server and an optional URI to which a location should be mapped." |
| LGPD — `https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm` | art. 6º III (necessidade) · art. 12 (anonimizado não é pessoal, salvo reversão) · art. 13 § 4º (pseudonimização) · art. 16 (eliminação e quatro exceções) · art. 48 (comunicação de incidente) |
| NIST SP 800-61 Rev. 3 — `https://csrc.nist.gov/pubs/sp/800/61/r3/final` | abril/2025, substitui a Rev. 2 (2012); "A CSF 2.0 Community Profile" |
| RFC 3227 — `https://www.rfc-editor.org/rfc/rfc3227` | ordem de volatilidade (2.1) · "Don't shutdown until you've completed evidence collection." · cadeia de custódia (4.1) |
| Resolução CD/ANPD 15/2024 | prazo de 3 dias úteis para o controlador comunicar incidente (conferido só em fontes secundárias; não citar o artigo) |

## Operação de segurança, observabilidade, continuidade e K8s (conferidas em 28/10/2026)

| Página | Trecho |
|---|---|
| NIST CSF 2.0 (CSWP 29) — `https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf` | GV "strategy, expectations, and policy are established, communicated, and monitored" · ID "current cybersecurity risks are understood" · PR "Safeguards […] are used" · DE "attacks and compromises are found and analyzed" · RS "supports the ability to contain the effects" · RC "Assets and operations affected […] are restored" |
| CIS Implementation Groups — `https://www.cisecurity.org/controls/implementation-groups` | IG1: "the foundational set of cyber defense Safeguards that every enterprise should apply" · "IG3 is comprised of all the Controls and Safeguards" |
| CIS Control 18 — `https://www.cisecurity.org/controls/penetration-testing` | "Test the effectiveness and resiliency of enterprise assets through identifying and exploiting weaknesses in controls" |
| CIS Control 11 — `https://www.cisecurity.org/controls/data-recovery` | "Establish and maintain data recovery practices sufficient to restore in-scope enterprise assets to a pre-incident and trusted state." |
| FIRST CVSS v4.0 User Guide — `https://www.first.org/cvss/v4.0/user-guide` | "designed to measure the severity of a vulnerability and should not be used alone to assess risk" |
| MITRE ATT&CK — `https://attack.mitre.org/` | "a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations" |
| pam.conf(5) — `https://man7.org/linux/man-pages/man5/pam.conf.5.html` | account: "non-authentication based account management […] time of day, currently available system resources […] location" · auth: "establishes that the user is who they claim to be" (MPO 2024 C5, item 86, trocou auth por account) |
| Google SRE Book, SLOs — `https://sre.google/sre-book/service-level-objectives/` | SLI "a carefully defined quantitative measure of some aspect of the level of service" · SLO "a target value or range of values for a service level that is measured by an SLI" · SLA "includes consequences of meeting (or missing) the SLOs" · "unrealistic and undesirable to insist that SLOs will be met 100% of the time" |
| Google SRE Book, Monitoring — `https://sre.google/sre-book/monitoring-distributed-systems/` | "The four golden signals of monitoring are latency, traffic, errors, and saturation." · p99 de um backend vira a mediana do frontend |
| Prometheus overview — `https://prometheus.io/docs/introduction/overview/` | "time series collection happens via a pull model over HTTP" · Pushgateway "for short-lived jobs" |
| Grafana configuration — `https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/` | http_port "defaults to 3000" · http_addr vazio "equivalent to setting the value to 0.0.0.0" (TCU 2025, item 134, disse 127.0.0.1 e 8080) |
| NIST glossary (SP 800-34) — `https://csrc.nist.gov/glossary/term/recovery_point_objective` | RPO "The point in time to which data must be recovered after an outage." · RTO "length of time an information system’s components can be in the recovery phase before negatively impacting" · hot site "fully operational offsite data processing facility equipped with hardware and software" |
| Uptime Institute Tiers — `https://uptimeinstitute.com/tiers` | Tier III "concurrently maintainable" · Tier IV "add fault tolerance to the Tier III topology" |
| Kubernetes components — `https://kubernetes.io/docs/concepts/overview/components/` | kube-scheduler "Looks for Pods not yet bound to a node, and assigns each Pod to a suitable node." · kubelet "Ensures that Pods are running, including their containers." |
| Kubernetes Secrets / ConfigMaps — `https://kubernetes.io/docs/concepts/configuration/secret/` | Secrets "by default, stored unencrypted in the API server's underlying data store (etcd)" · ConfigMap "non-confidential data", "does not provide secrecy or encryption" (TCDF 2024, item 107) |
| Kubernetes StatefulSet / HPA | StatefulSet "maintains a sticky identity for each of those Pods" · HPA "Horizontal scaling means that the response to increased load is to deploy more Pods" |
| OpenTelemetry — `https://opentelemetry.io/` | não abriu pelo WebFetch em 28/10/2026; não citar literal |

## Armazenamento (conferidas em 07/11/2026)

| Página | Trecho |
|---|---|
| AWS EBS volumes — `https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html` | "The volume and instance must be in the same Availability Zone." · "EBS volumes persist independently from the running life of an EC2 instance." (o volume raiz tem DeleteOnTermination por padrão) |
| AWS EFS — `https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html` | "supports the Network File System version 4 (NFSv4.1 and NFSv4.0) protocol" · "Using Amazon EFS with Microsoft Windows–based Amazon EC2 instances is not supported." · Regional = várias AZs; One Zone = uma AZ |
| S3 storage classes — `https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html` | One Zone-IA "is as durable as S3 Standard-IA, but it is less available and less resilient" · durabilidade 99.999999999% em todas as classes (exceto RRS) · Glacier Flexible/Deep Archive "not available for real-time access" · mínimo 30/90/180 dias (Standard-IA / Glacier IR e Flexible / Deep Archive) |
| S3 Object Lock — `https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html` | WORM · compliance: "can't be overwritten or deleted by any user, including the root user" · governance: "unless they have special permissions" (s3:BypassGovernanceRetention) · legal hold "has no expiration date" · "works only in buckets that have S3 Versioning enabled" · não impede novas versões |
| Azure Blob access tiers — `https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview` | hot / cool (30 dias) / cold (90) / archive (180) · archive é offline: "can't be read or modified" até reidratar, "up to 15 hours" · archive não pode ser o tier padrão da conta · archive só em LRS/GRS/RA-GRS |
| NIST SP 800-88 Rev. 2 (set/2025, substituiu a Rev. 1) — glossário `https://csrc.nist.gov/glossary/term/clear` e `/purge` | Clear: "logical techniques to sanitize data in all user-addressable storage locations for protection against simple, non-invasive data recovery techniques using the same interface that is available to the user" · Purge: "physical or logical techniques to render target data recovery infeasible using state-of-the-art laboratory techniques" |

## Bancos de dados (conferidas em 07/11/2026)

| Página | Trecho |
|---|---|
| PostgreSQL, Log-Shipping Standby — `https://www.postgresql.org/docs/current/warm-standby.html` | "Streaming replication is asynchronous by default" (atraso "typically under one second") · cascata: standby "acting as a relay [...] reduce the number of direct connections to the primary" · "Cascading replication is currently asynchronous." (CNJ 2024 C2, item 66, disse "simultâneas") |
| PostgreSQL, WAL — `https://www.postgresql.org/docs/current/wal-intro.html` | "changes to data files [...] must be written only after those changes have been logged" · "we do not need to flush data pages to disk on every transaction commit" · "roll-forward recovery, also known as REDO" |
| PostgreSQL, MVCC — `https://www.postgresql.org/docs/current/mvcc-intro.html` | "reading never blocks writing and writing never blocks reading" |
| PostgreSQL, Transaction Isolation — `https://www.postgresql.org/docs/current/transaction-iso.html` | "Read Committed is the default isolation level in PostgreSQL" · "PostgreSQL's Read Uncommitted mode behaves like Read Committed" · Repeatable Read: phantom "Allowed, but not in PG" |
| PostgreSQL, Using EXPLAIN — `https://www.postgresql.org/docs/current/using-explain.html` | EXPLAIN ANALYZE "actually executes the query" · "any side-effects will happen as usual" (usar BEGIN/ROLLBACK) |
| PostgreSQL, Transactions (tutorial) — `https://www.postgresql.org/docs/current/tutorial-transactions.html` | "each individual statement has an implicit BEGIN and (if successful) COMMIT wrapped around it" · ROLLBACK TO: "changes earlier than the savepoint are kept" · "After rolling back to a savepoint, it continues to be defined" |
| Oracle Database Concepts, Transactions — `https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/transactions.html` | "The database issues an implicit COMMIT statement before and after every DDL statement." (contraste: DDL transacional do PostgreSQL, wiki "Transactional DDL") |
| PostgreSQL, Comparison / Table Expressions / SELECT / Aggregates | "Ordinary comparison operators yield null [...] when either input is null" · BETWEEN = ">= x AND <= y" · NATURAL "forms a USING list consisting of all column names that appear in both input tables" · "WHERE filters individual rows before the application of GROUP BY, while HAVING filters group rows" · dependência funcional pela PK no GROUP BY · count("any") "not null" · avg "non-null input values" |
| PostgreSQL, REVOKE / CREATE VIEW / PG 15 release | dependentes revogados "if CASCADE is specified; if it is not, the revoke action will fail" · "sum of privileges granted directly [...] and privileges granted to PUBLIC" · visão: "determined by the permissions of the view owner" (security_invoker) · "Remove PUBLIC creation permission on the public schema" |
| PostgreSQL, Explicit Locking / CREATE INDEX / TRUNCATE | "Only an ACCESS EXCLUSIVE lock blocks a SELECT (without FOR UPDATE/SHARE)" · TRUNCATE → ACCESS EXCLUSIVE · CREATE INDEX: "Other transactions can still read the table" · CONCURRENTLY não roda em bloco de transação · FOR UPDATE "prevents them from being locked, modified or deleted" · TRUNCATE "same effect as an unqualified DELETE" |
| PostgreSQL postgres_fdw · Microsoft PolyBase · AWS RDS Multi-AZ failover | postgres_fdw "access data stored in external PostgreSQL servers" · PolyBase "query data with Transact-SQL (T-SQL) directly from SQL Server, Oracle, Teradata, MongoDB [...]" (TCU 2025, item 116) · failover "changes the Domain Name System (DNS) record of the DB instance to point to the standby" |
| AWS RDS Multi-AZ DB instance — `https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html` | "synchronous standby replica in a different Availability Zone" · "You can't use a standby replica to serve read traffic" |
| Redis persistence — `https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/` | RDB "point-in-time snapshots of your dataset at specified intervals" · AOF "logs every write operation received by the server" · "You can disable persistence completely. This is sometimes used when caching." · fsync padrão everysec |
| Elastic, clusters/nodes/shards — `https://www.elastic.co/docs/deploy-manage/distributed-architecture/clusters-nodes-shards` | "each shard is a self-contained Lucene index containing a subset of the documents" · primários e réplicas (TCE/RS 2025, item 38) |
| Apache Cassandra, Dynamo — `https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html` | "per-operation tradeoff between consistency and availability through Consistency Levels" · QUORUM "A majority (n/2 + 1) of the replicas must respond" · W + R > RF (Telebras 2025, item 86) |

## Serviços, Scrum e Kanban (conferidas em 07/11/2026)

| Página | Trecho |
|---|---|
| Scrum Guide 2020 — `https://scrumguides.org/scrum-guide.html` | "The Daily Scrum is a 15-minute event for the Developers of the Scrum Team." · "The Sprint Backlog is a plan by and for the Developers." · "No one else tells them how to turn Product Backlog items into Increments of value." · "Within a Scrum Team, there are no sub-teams or hierarchies." · PO "may delegate the responsibility to others. Regardless, the Product Owner remains accountable." · Sprint Review "inspect the outcome of the Sprint and determine future adaptations" |
| The Kanban Guide — `https://kanbanguides.org/english/` | WIP "started but not finished" · Throughput "finished per unit of time" · Cycle Time "between when a work item started and when a work item finished" · "controlling WIP [...] should create a pull system" · sem papéis nem iterações; não define lead time |
| ITIL 4 (AXELOS) | Texto proprietário: usar só como conceito, sem citação literal |

## Capacidade, custos e IA (conferidas em 07/11/2026)

| Página | Trecho |
|---|---|
| AWS Spot interruptions — `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html` | "launch Spot Instances on spare EC2 capacity for steep discounts in exchange for returning them when Amazon EC2 needs the capacity back" |
| AWS Savings Plans — `https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html` | "commitment of using a specified amount of compute power (measured per hour) for a one or three year period" · Compute SP "regardless of instance family, instance size, OS, tenancy, or AWS Region" (+ Fargate e Lambda) |
| AWS Budgets — `https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html` | ação a 80%: "automatically apply a custom IAM policy that denies you the ability to provision additional resources" · "updated up to three times a day" · custo pode passar do limite antes do aviso |
| AWS service quotas — `https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html` | "default quotas, formerly referred to as limits" · "each quota is Region-specific" · "not all quotas can be increased" |
| RFC 6585 §4 — `https://www.rfc-editor.org/rfc/rfc6585#section-4` | 429 "too many requests in a given amount of time (\"rate limiting\")" · "MAY include a Retry-After header" |
| Kubernetes, Resource Management — `https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/` | "cpu limits are enforced by CPU throttling" · "memory limits are enforced by the kernel with out of memory (OOM) kills" · kube-scheduler usa o request |
| AWS Builders' Library, retries — `https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter` | "retries can make the overload worse instead of better" · "exponential backoff" · "Jitter adds some amount of randomness to the backoff to spread the retries around in time" |
| OWASP LLM01:2025 — `https://genai.owasp.org/llmrisk/llm01-prompt-injection/` | direta × indireta ("input from external sources, such as websites or files") · "Restrict the model's access privileges to the minimum necessary" |
| FinOps Foundation (`finops.org`) | 403 para WebFetch e curl em 07/11/2026: usar só como conceito (fases Informar/Otimizar/Operar, princípios) |

## P2 e contratação (conferidas em 08/11/2026)

| Fonte | Trechos conferidos |
|---|---|
| IN SGD/ME n.º 94/2022 — `https://www.gov.br/governodigital/pt-br/contratacoes-de-tic/legislacao/instrucao-normativa-sgd-me-no-94-de-23-de-dezembro-de-2022` | fases (art. 8.º) e riscos em todas as fases (§ 1.º) · requisitante e técnico acumulam só em caso excepcional (art. 10, § 3.º) · TCO (art. 11, III, a) · TRP = fiscal técnico; TRD = gestor; ocorrências no histórico = fiscal técnico (art. 33) · reunião inicial dispensável para bens (art. 31) · publicação de ETP/TR até edital/extrato/assinatura (art. 34) · homem-hora e postos vedados salvo justificativa (art. 5.º, VIII e IX) · mapa de riscos: fim do TR, fim da seleção, anual, eventos relevantes (art. 38, § 4.º) · Anexo I: nuvem na renovação de data center (4.1), portabilidade (4.2.2), dependência tecnológica (1.4.1) |
| IN SEGES/ME n.º 65/2021 | priorizar incisos I e II (art. 5.º) · média, mediana ou menor valor sobre 3+ preços (art. 6.º) |
| IN SFC/CGU n.º 3/2017 (Referencial Técnico) | definição (item 1) · três linhas e AECI na 2.ª (itens 8 a 14) · consultoria sem assumir responsabilidade da gestão (item 18) · apuração como competência do SCI (item 23) · 24 meses (item 52) · consultoria/avaliação sobre o mesmo objeto (item 53) · recomendações nas causas (item 164) · risco aceito inaceitável (item 180) · glossário: ceticismo, atributos das informações |
| Lei 12.846/2013 · LINDB · Lei 9.784/1999 · Lei 8.112/1990 · CF arts. 71 e 74 · Lei 14.600/2023 art. 49 | ver method_html do material `2026-11-13_p2-controle-responsabilizacao` |
| Decreto 9.203/2017 · Decreto 11.529/2023 · Decreto 11.129/2022 arts. 56–57 | ver material `2026-11-17_p2-governanca-riscos-integridade` |
| LAI · Decreto 7.724/2012 · LGPD · Lei 13.460/2017 · Lei 13.608/2018 | ver material `2026-11-20_p2-lai-ouvidoria-transparencia` |

## Redes (conferidas em 17/11/2026)

| Fonte | Trechos |
|---|---|
| RFC 2453 §3.4.3 e §3.6 | "The \"simple split horizon\" scheme omits routes learned from one neighbor in updates sent to that neighbor." · "Split horizon with poisoned reverse\" includes such routes in updates, but sets their metrics to infinity." · RIP na UDP 520 · infinito = 16 |
| RFC 8200 §3, §4.5, §8.1 | Hop Limit "Decremented by 1 by each node that forwards the packet." · "fragmentation in IPv6 is performed only by source nodes" · "the UDP checksum is not optional" |
| RFC 4271 | "BGP listens on TCP port 179." · LOCAL_PREF "SHALL be included in all UPDATE messages [...] to other internal peers" e "MUST NOT include this attribute in UPDATE messages it sends to external peers" (a RFC não o chama de discretionary) |
| RFC 7766 §5 | "All general-purpose DNS implementations MUST support both UDP and TCP transport." |
| Cisco 15986 (Administrative Distance) | "AD is a value used to rank the trustworthiness of routing information sources." · conectada 0, estática 1, eBGP 20, EIGRP 90, OSPF 110, IS-IS 115, RIP 120, iBGP 200 · "AD does not override longest prefix match." |
| AWS, How Elastic Load Balancing works | NLB: "Routes each individual TCP connection to a single target for the life of the connection." · cross-zone desligado: 25% × 6,25% (2 + 8 destinos) · ICMP "Fragmentation Needed and Don't Fragment was Set (Type 3, Code 4)" · ALB exige 2 ou mais AZs |

## SO e diretórios (conferidas em 17/11/2026)

| Fonte | Trechos |
|---|---|
| Microsoft Learn, KMS activation planning | "Clients activate if the count is 25 or higher. Servers and volume editions of Microsoft Office products activate if the count is five or greater." · "KMS activations are valid for 180 days" · "attempt to renew their activation every seven days" · DNS dinâmico publica o host · TCP 1688 · conta conexões únicas dos últimos 30 dias |
| Microsoft Learn, Group Policy Hierarchy | ordem local → sites → domains → OUs (OU pai antes da filha) · "when policy is applied, it overwrites policy that was applied earlier" |
| Microsoft Learn, WSUS Overview | "The WSUS server that acts as an update source is called an upstream server." · ao menos um servidor conecta ao Microsoft Update · "WSUS is deprecated and is no longer adding new features. However, it continues to be supported" |
| chmod(1) | sticky bit: "prevents unprivileged users from removing or renaming a file in the directory unless they own the file or the directory" |
| systemctl(1) | enable: "does not have the effect of also starting any of the units being enabled" · --now · mask liga a unidade a /dev/null |

## IaC e CI/CD (conferidas em 17/11/2026)

| Fonte | Trechos |
|---|---|
| Ansible, Ansible concepts | Control node: "The machine from which you run the Ansible CLI tools" · "Ansible is not normally installed on managed nodes" · Inventory: "A list of managed nodes" |
| HashiCorp, Manage resource drift | state "out of sync, or \"drift,\" from the real infrastructure" · "Terraform compares your state file to real infrastructure whenever you invoke terraform plan or terraform apply" · "A refresh-only operation does not attempt to modify your infrastructure" |
| GitHub Docs, OpenID Connect | "You won't need to duplicate your cloud credentials as long-lived GitHub secrets." · "short-lived access token that is only valid for a single job" |
| GitHub Docs, Removing sensitive data | "as a first step you need to revoke and/or rotate that secret" |
| gitignore (git-scm) | "specifies intentionally untracked files [...] Files already tracked by Git are not affected" |
| Microsoft Learn, DevSecOps on AKS | Deploy phase: "developers, application operators, and cluster operator teams work together to establish the right security controls for the CD pipelines" · Build phase: SAST, SCA, secrets scanning · OIDC sem credencial de longa duração |
| Martin Fowler, BlueGreenDeployment / CanaryRelease | "two production environments, as identical as possible" · "switch the router" · canário: "slowly rolling out the change to a small subset of users before rolling it out to the entire infrastructure" |
