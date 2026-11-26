#!/usr/bin/env bash
# Reextrai as discursivas Quadrix do acervo (enunciado + padrão). Rodar da raiz.
set -e
d(){ python3 tools/acervo_discursiva_quadrix.py "$@"; }
d --id cfn_2024_pae_ti_suporte --orgao CFN --ano 2024 --cargo "Profissional de Atividades Estratégicas (PAE) – Ocupação: Tecnologia da Informação – Suporte Técnico" --padrao-cargo "TECNOLOGIA DA INFORMAÇÃO – SUPORTE TÉCNICO" --tags esp.tic.redes,esp.tic.seguranca
d --id cfo_2024_analista_infraestrutura --orgao CFO --ano 2024 --cargo "Analista de Infraestrutura" --padrao-cargo "ANALISTA DE INFRAESTRUTURA \(CÓDIGO 401\)" --tags esp.tic.seguranca,esp.tic.govti
d --id crf_pr_2025_analista_sistemas --orgao CRF-PR --ano 2025 --cargo "Analista de Sistemas" --padrao-cargo "ANALISTA DE SISTEMAS \(CÓDIGO 400\)" --tags esp.tic.infra,esp.tic.seguranca,esp.tic.atendimento
d --id crefito17_2026_analista_ti --orgao CREFITO-17 --ano 2026 --cargo "Analista de Tecnologia da Informação" --padrao-cargo "ANALISTA DE TECNOLOGIA DA INFORMAÇÃO \(CÓDIGO 402\)" --tags esp.tic.govti,esp.tic.gestao
d --id core_sp_2025_analista_ti --orgao CORE-SP --ano 2025 --cargo "Analista de Tecnologia da Informação" --padrao-cargo "ANALISTA DE TECNOLOGIA DA INFORMAÇÃO \(CÓDIGO 400\)" --tags esp.tic.engsw --aderencia media
d --id crq_rs_2026_analista_informatica --orgao CRQ-RS --ano 2026 --cargo "Analista de Informática" --padrao-cargo "ANALISTA DE INFORMÁTICA \(CÓDIGO 401\)" --parte 2 --tema "Estudo de caso: backup e recovery após corrupção de dados e falha de armazenamento" --tags esp.tic.seguranca,esp.tic.infra,esp.tic.bd
d --id cfp_2024_analista_ti_suporte --orgao CFP --ano 2024 --cargo "Analista Técnico/TI/Suporte" --padrao-cargo "ANALISTA TÉCNICO/TI/SUPORTE \(CÓDIGO 408\)" --tags esp.tic.redes,esp.tic.seguranca --sem-prova --tema "Segmentação de redes com VLANs: conceito, tipos e boas práticas"
d --id coren_pr_2024_analista_ti --orgao COREN-PR --ano 2024 --cargo "Analista de Tecnologia da Informação" --padrao-cargo "ANALISTA DE TECNOLOGIA DA INFORMAÇÃO \(CÓDIGO 402\)" --tags esp.tic.bd,esp.tic.gestao
d --id cro_sp_2025_analista_suporte_ti --orgao CRO-SP --ano 2025 --cargo "Analista de Suporte de Tecnologia de Informação" --padrao-cargo "ANALISTA DE SUPORTE DE TECNOLOGIA DE INFORMAÇÃO \(CÓDIGO 407\)" --tags esp.tic.seguranca,esp.tic.infra
d --id crp_sp_2025_especialista_gestao_tic --orgao CRP-SP --ano 2025 --cargo "Especialista em Gestão – Tecnologia da Informação e Comunicação" --padrao-cargo "TECNOLOGIA DA INFORMAÇÃO E COMUNICAÇÃO \(CÓDIGO 408\)" --tags esp.tic.bd
d --id crmv_go_2025_analista_adm_ti --orgao CRMV-GO --ano 2025 --cargo "Analista Administrativo - Área de Tecnologia da Informação" --padrao-cargo "ÁREA DE TECNOLOGIA DA INFORMAÇÃO \(CÓDIGO 400\)" --tags esp.tic.redes,esp.tic.infra,esp.tic.gestao
# COREN-PR: a Quadrix só publicou o padrão preliminar; a nota do arquivo diz isso.
sed -i 's/padrão definitivo de resposta da Quadrix./padrão PRELIMINAR de resposta da Quadrix (o definitivo não foi publicado)./' acervo/itens/coren_pr_2024_analista_ti_disc.md
sed -i 's/^## Padrão definitivo de resposta (Quadrix)$/## Padrão preliminar de resposta (Quadrix)/' acervo/itens/coren_pr_2024_analista_ti_disc.md
