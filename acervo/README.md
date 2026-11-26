# Acervo — provas Quadrix (COFEN 2026 · Cargo 407)

- `catalogo.yaml` — provas ingeridas (órgão, cargo, código, URLs, aderência, notas) + blocos `cobertura*`.
- `fontes/<id>/` — `prova.pdf` + `gabarito.pdf` (gabarito definitivo, com todos os cargos do concurso) + `padrao_discursiva.pdf` quando houver.
- `itens/<id>_bNN.md` — um arquivo por **bloco de comando**, com as tags do mapa do 407 (`tags_edital`).
- `itens/<id>_disc.md` — discursiva: enunciado do caderno + padrão de resposta da Quadrix (tag `disc.tic` + tags do tema).
- `cobertura-edital.md` — heatmap (assertivas por tag × meta) · `previsao-cofen.md` — ranking de estudo.

## Situação (26/11/2026)

**11 provas Quadrix C/E** de TI, nível superior: **1.320 assertivas** com gabarito definitivo, em 274 blocos, todas conferidas contra o PDF (texto de cada item reencontrado no caderno). Mais **11 discursivas** de TI com o padrão de resposta da banca.

| Prova | Cargo | Por que importa |
|-------|-------|-----------------|
| `crefito17_2026_analista_ti` | Analista de TI (402) | **Mais aderente:** o edital usa o mesmo molde do 407 (Sistema Cofen/Corens, governança, auditorias, contratos, atendimento estratégico, gestão de ativos, implantação e migração). Discursiva: indicadores, riscos, ITIL e COBIT |
| `cref11_2026_analista_suporte_ti` | Analista de Suporte em TI (402) | P3 com os mesmos blocos exclusivos do 407 |
| `cfn_2024_pae_ti_suporte` | PAE – TI – Suporte Técnico (407) | ITIL, mudanças, base de conhecimento, fiscalização de contratos, backup, manutenção. Discursiva: DNS |
| `coren_pr_2024_analista_ti` | Analista de TI (402) | Sistema Cofen/Corens: Lei 5.905, Regimento do Coren, Res. COFEN 507/2016 e 564/2017. Discursiva: análise de dados (padrão preliminar) |
| `cfo_2024_analista_infraestrutura` | Analista de Infraestrutura (401) | Infraestrutura em blocos de 10 itens com situação-problema. Discursiva: segurança + ITIL + riscos |
| `crp_sp_2025_especialista_gestao_tic` | Especialista em Gestão de TIC (408) | ITIL 4, COBIT 2019, ISO 27001/27002, indicadores. Discursiva: otimização de consultas |
| `crmv_go_2025_analista_adm_ti` | Analista Adm. – TI (400) | Constitucional, Administrativo, ITIL 4/COBIT, Lei 14.133. Discursiva: monitoramento de redes |
| `cro_sp_2025_analista_suporte_ti` | Analista de Suporte de TI (407) | Improbidade, anticorrupção, contratos de TI, SLA/OLA. Discursiva: segurança em nuvem |
| `crf_pr_2025_analista_sistemas` | Analista de Sistemas (400) | Suporte e infraestrutura (Samba, Apache, VoIP, CFTV, AD, GLPI, Zabbix). Discursiva: acesso remoto |
| `coffito_2023_analista_ti` | Analista de TI (403) | LAI, LGPD, processo administrativo (discursiva de atualidades, fora do perfil) |
| `ibict_2024_tecnologista_ti` | Tecnologista – TI (404) | Aderência média (desenvolvimento, ciência da informação) |

Só a discursiva (objetiva de múltipla escolha ou caderno não publicado):

| Fonte | Discursiva |
|-------|------------|
| `core_sp_2025_analista_ti` (400) | Testes de software |
| `crq_rs_2026_analista_informatica` (401) | Parte 2: estudo de caso de backup e recovery (a parte 1 é de atualidades) |
| `cfp_2024_analista_ti_suporte` (408) | VLANs (só o padrão; o caderno não está no ZIP oficial) |

Blocos com `tags_edital: []` = fora do edital do 407 (atualidades, leis e regimentos de outros conselhos, metodologia científica). Ficam no acervo como exemplo de estilo, mas não entram no heatmap.

## Lacunas do acervo

- **Exclusivos do 407:** `esp.tic.auditoria` continua quase vazio (2 itens); `gestao`, `contratos` e `atendimento` melhoraram, mas seguem abaixo das matérias técnicas.
- `comp.const`, `comp.leg.licitacoes`: abaixo da meta.
- Discursivas ainda sem padrão: CREF-11 2026 e IBICT 2024 (caderno sem a discursiva).

## Fontes verificadas em 26/11/2026

- **Quadrix (oficial):** 776 concursos encerrados; triados os editais de 23 conselhos de 2024–2026. Entraram os 4 cargos de TI com objetiva C/E (CREFITO-17, CFN, CFO, CRF-PR) e 3 discursivas extras. O site também deu o padrão das discursivas de 5 provas que já estavam no acervo.
- **qconcursos:** origem dos 7 cadernos iniciais.
- **PCI Concursos e Gran Questões:** só repetem os PDFs da Quadrix (sem padrão de discursiva). Mas listam outras provas Quadrix de TI que **ainda não estão aqui**. São as próximas a buscar no site oficial: CFP 2024 Analista Técnico – TI/Suporte (408; o Gran tem o caderno que falta no ZIP oficial), CFP 2024 TI/Desenvolvimento (407), CREFITO-18 2024 Analista de TI, CRQ-IV/SP 2023 PAS Analista de Sistemas (Rede), CREF-3/SC 2023 Analista TI, CFO 2022 e CRMV-SP 2022 Analista de Suporte de TI, CORE-PR 2021 Analista TI.
- **Estratégia e veprovas:** a busca não trouxe provas Quadrix de TI além das já listadas; não foram baixados itens de lá. O banco do Estratégia exige assinatura.

## Como ingerir outra prova

1. Criar `acervo/fontes/<orgao>_<ano>_<cargo>/` com `prova.pdf` e `gabarito.pdf`.
2. `python3 tools/acervo_extract_quadrix.py --id <id> --orgao … --ano … --cargo "<título do cabeçalho da prova>" --gab-cargo "<regex do cargo no gabarito>" --dry` (relatório) e, se 120/120, sem `--dry`.
3. Rever as tags dos blocos; correções manuais em `tools/acervo_ajustes_quadrix.yaml`.
4. Acrescentar a prova em `catalogo.yaml` → `fontes` e rodar `python3 tools/acervo_cobertura.py --write --write-catalogo` e `python3 tools/acervo_previsao.py --write`.

5. Discursiva: pôr `padrao_discursiva.pdf` na pasta, acrescentar uma linha em `tools/acervo_discursivas_quadrix.sh` (usa `tools/acervo_discursiva_quadrix.py`) e rodar o script.

Requer `pdftotext` (poppler) e `pip install pdfplumber pyyaml`.
