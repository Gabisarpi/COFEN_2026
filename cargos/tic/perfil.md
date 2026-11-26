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

- `cargos/tic/amostra/2026-11-26_amostra_quadrix/` — 25 itens reais do P3 (CREF-11 2026, CRP-SP 2025, CRMV-GO 2025) nos blocos exclusivos do 407 e em ITIL/COBIT; gabarito em arquivo separado (13 C × 12 E).
- Para as demais tags: 2–3 itens reais Quadrix da mesma tag no acervo (`acervo/itens/`).

## Acervo mais aderente

- **Topo:** `crefito17_2026_analista_ti` (edital no mesmo molde do 407), `cref11_2026_analista_suporte_ti` (P3 com os mesmos blocos do 407), `cfn_2024_pae_ti_suporte` (código 407, suporte) e `coren_pr_2024_analista_ti` (Sistema Cofen/Corens).
- Infraestrutura e suporte: `cfo_2024_analista_infraestrutura`, `crf_pr_2025_analista_sistemas`, `cro_sp_2025_analista_suporte_ti`.
- Gestão e governança: `crp_sp_2025_especialista_gestao_tic`, `crmv_go_2025_analista_adm_ti`.
- Legislação (P2): `cro_sp_2025_analista_suporte_ti`, `coffito_2023_analista_ti`, `crmv_go_2025_analista_adm_ti`, `crefito17_2026_analista_ti`.
- **Discursiva:** 11 temas reais com padrão da banca em `acervo/itens/*_disc*.md` (DNS, VLANs, acesso remoto, backup e recovery, segurança em nuvem, monitoramento, indicadores e riscos com ITIL/COBIT, segurança + ITIL + riscos, análise de dados, otimização de consultas, testes de software). O mais próximo do 407: CREFITO-17 2026.
- Aderência média: `ibict_2024_tecnologista_ti`.
- Apoio de conteúdo (peso ×1, não molde de estilo): itens Cebraspe de TI do repo CGU_2026.

## Exemplos de pedidos

- “bloco de 15 itens de contratos de TIC” (`esp.tic.contratos`)
- “material de núcleos de governança e auditoria” (`esp.tic.gestao`, `esp.tic.auditoria`)
- “discursiva sobre fiscalização de contrato com SLA”
- “flashcards da Lei 5.905 e do Decreto 94.406” (`comp.leg.enfermagem`)
- “simulado completo”
