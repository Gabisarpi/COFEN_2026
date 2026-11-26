#!/usr/bin/env bash
# Reextrai todas as provas Quadrix do acervo (rodar da raiz). X=--dry para só relatório.
set -e
run(){ python3 tools/acervo_extract_quadrix.py "$@"; }
run --id coren_pr_2024_analista_ti --orgao COREN-PR --ano 2024 --cargo "Analista de Tecnologia da Informação" --gab-cargo "ANALISTA DE TECNOLOGIA DA INFORMAÇÃO \(CÓDIGO 402\)" $X
run --id cref11_2026_analista_suporte_ti --orgao CREF-11 --ano 2026 --cargo "Analista de Suporte em Tecnologia da Informação" --gab-cargo "ANALISTA DE SUPORTE EM TECNOLOGIA DA INFORMAÇÃO" $X
run --id cro_sp_2025_analista_suporte_ti --orgao CRO-SP --ano 2025 --cargo "Analista de Suporte de Tecnologia de Informação" --gab-cargo "ANALISTA DE SUPORTE DE TECNOLOGIA DE INFORMAÇÃO \(CÓDIGO 407\)" $X
run --id coffito_2023_analista_ti --orgao COFFITO --ano 2023 --cargo "ANALISTA DE TECNOLOGIA DA INFORMAÇÃO" --gab-cargo "ANALISTA DE TECNOLOGIA DA INFORMAÇÃO \(CÓDIGO 403\)" $X
run --id crp_sp_2025_especialista_gestao_tic --orgao CRP-SP --ano 2025 --cargo "Especialista em Gestão – Tecnologia da Informação e Comunicação" --gab-cargo "ESPECIALISTA EM GESTÃO – TECNOLOGIA DA INFORMAÇÃO E COMUNICAÇÃO \(CÓDIGO 408\)" $X
run --id crmv_go_2025_analista_adm_ti --orgao CRMV-GO --ano 2025 --cargo "Analista Administrativo - Área de Tecnologia da Informação" --gab-cargo "ANALISTA ADMINISTRATIVO - ÁREA DE TECNOLOGIA DA INFORMAÇÃO \(CÓDIGO 400\)" $X
run --id ibict_2024_tecnologista_ti --orgao IBICT --ano 2024 --cargo "CARGO TECNOLOGISTA – PERFIL: TECNOLOGIA DA INFORMAÇÃO" --gab-cargo "TECNOLOGISTA - TECNOLOGIA DA INFORMAÇÃO \(CÓDIGO 404\)" --aderencia media $X
