# Perfil da trilha — Cargo 407 · Analista de TIC (COFEN 2026)

Lido pelas skills de simulado, flashcards e diagnóstico. Tudo que é **específico do cargo** fica aqui; regras comuns ficam nas skills e em `AGENTS.md`.

## Identificação

- Cargo 407 — Analista de Tecnologia da Informação e Comunicação · estudante: Gaby
- `$C = cargos/tic/`

## Mapa e tags

- Mapa: `cargos/tic/mapa-edital.md` · resumo/cortes: `cargos/tic/resumo-edital.md`
- Prefixos: P1 `basicos.*` · P2 `comp.*` · P3 `esp.tic.*` (12 blocos) · discursiva `disc.tic`

## Banca — Instituto Quadrix

- Itens **Certo/Errado**, +1/−1 (uma errada anula uma certa); branco vale 0.
- Estilo Quadrix: enunciados mais curtos que os do Cebraspe, muita cobrança literal de lei e de norma, itens “conceituais de manual” em TI. Calibrar pelo acervo Quadrix (`acervo/`), não pelo Cebraspe.
- Material CGU (Cebraspe) serve como base de conteúdo, mas os itens novos devem imitar a Quadrix.

## Discursiva

- 1 texto de 20–30 linhas, 10 pontos, conteúdo = 70% da nota.
- Cenários prováveis: fiscalização de contrato de TIC com SLA; elaboração de TR; política de backup/continuidade; plano de migração de sistema; auditoria de TIC/controles internos; incidente de segurança + LGPD; gestão de ativos.

## Prioridades do P3

1. Faixa alta (exclusivos do 407 + base forte): **contratos de TIC (14.133 + TR + fiscalização)**, **governança ITIL/COBIT + indicadores/SLA**, **segurança/ISO 27001-27002**, **redes**, **auditoria e controles**.
2. Faixa média: SO Windows/Linux, BD/SQL, infraestrutura (operação, ativos, migração), LGPD/LAI.
3. Faixa baixa: engenharia de software/UML, fundamentos de hardware, atendimento/Ouvidoria.

Reaproveitar do CGU: redes, Linux/Windows, nuvem, segurança, ITIL/COBIT, contratação de TI.

## Escopo dos itens

- Cenários de conselho profissional (Cofen/Corens), autarquia federal, regime CLT.
- Comandos com trecho de norma (ISO, Lei 14.133, resoluções COFEN), tabela de SLA, trecho de config/log, consulta SQL simples.

## Especificidade técnica (anti-dedução)

- Blocos técnicos (1–4, 12): porta, camada, protocolo, comando, nível de RAID, tipo de backup — detalhe concreto e verificável.
- Contratos (10): papéis (gestor, fiscal técnico, administrativo, requisitante), artefatos (DFD, ETP, TR, plano de fiscalização), glosa × sanção, recebimento provisório × definitivo.
- Governança e auditoria (6, 8, 9): práticas ITIL 4 × processos ITIL v3, objetivos COBIT 2019 (EDM/APO/BAI/DSS/MEA), três linhas, controle preventivo × detectivo × corretivo.
- Legislação: prazo, competência, “deverá” × “poderá”, regra × exceção — sempre do texto vigente.

## Fontes técnicas primárias

- Legislação: Planalto (Leis 5.905/1973, 8.429/1992, 9.784/1999, 12.527/2011, 12.846/2013, 13.709/2018, 14.133/2021; Decreto 94.406/1987); resoluções no site do Cofen.
- Contratações de TIC: IN SGD/ME 94/2022 e modelos/guias da SGD (gov.br/governodigital).
- Segurança: ABNT NBR ISO/IEC 27001:2022 e 27002:2022; CERT.br; NIST CSF 2.0.
- Serviços e governança: ITIL 4; COBIT 2019 (ISACA).
- SO, redes e BD: Microsoft Learn (pt-br), documentação Red Hat, RFCs, documentação do PostgreSQL.

## Amostra de dificuldade

- Ainda não existe. Montar em `cargos/tic/amostra/` com ~25 itens reais Quadrix de TI (conselhos profissionais) depois da primeira ingestão do acervo.
- Até lá: calibrar por 2–3 itens reais Quadrix da tag (quando houver) e pela régua de `cofen-calibrar-itens`.

## Acervo mais aderente

- Provas Quadrix de analista de TI em conselhos profissionais (Sistema Cofen/Corens, CFM/CRMs, CFO/CROs, CFMV/CRMVs, CAU, CFF/CRFs).
- Apoio de conteúdo (peso ×1, não molde de estilo): itens Cebraspe de TI do repo CGU_2026.

## Exemplos de pedidos

- “bloco de 15 itens de contratos de TIC” (`esp.tic.contratos`)
- “material de núcleos de governança e auditoria” (`esp.tic.gestao`, `esp.tic.auditoria`)
- “discursiva sobre fiscalização de contrato com SLA”
- “flashcards da Lei 5.905 e do Decreto 94.406” (`comp.leg.enfermagem`)
- “simulado completo”
