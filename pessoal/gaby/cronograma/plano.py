# Dados do cronograma da Gaby (COFEN 2026 · Cargo 407); a geração (plano.md + cronograma.html) fica em tools/cronograma_gerar.py.
# Uso (raiz do repo): python3 pessoal/gaby/cronograma/plano.py
# Tags de DIAS: só valores (ou prefixos) de cargos/tic/mapa-edital.md; tag desconhecida aborta a geração.
# Montado em 27/11/2026, quando o foco passou a ser só o COFEN (inscrição da CGU perdida).
import pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "tools"))
import cronograma_gerar as cg  # noqa: E402

D = cg.D

FASES = [
  {"id": 1, "nome": "Base nova (2 h/dia)", "ini": "27/11", "fim": "14/12",
   "obj": "O que a CGU não cobriu: Sistema Cofen/Corens e P2; os exclusivos do 407 (contratos, governança, gestão, auditoria, atendimento)"},
  {"id": 2, "nome": "Intensiva (5 h/dia)", "ini": "15/12", "fim": "03/01",
   "obj": "Simulado diagnóstico; todo o P3 técnico; P1 (LP, RLM, Inglês) e o resto do P2; 4 discursivas; simulado 2"},
  {"id": 3, "nome": "Manutenção e simulados (2 h/dia)", "ini": "04/01", "fim": "27/02",
   "obj": "Rotação semanal (reforço, LP, discursiva, bloco P3, P2, RLM/Inglês, revisão); 4 simulados em dois dias; última semana só revisão"},
]

# tipo: nuc | ref | bloco | disc | sim | p2 | p1 | rev | leve | prova
# curto: nome na revisão espaçada (só dias com conteúdo novo)
DIAS = [
 ('27/11', 'nuc', 'Lei 5.905/1973 + inscrição', 'Sistema Cofen/Corens: natureza autárquica, composição, competências do Cofen e dos Corens, eleições, anuidades · 15 C/E reais do COREN-PR · fazer a inscrição (até 11/01)', 'comp.leg.enfermagem', 'Lei 5.905'),
 ('28/11', 'nuc', 'Decreto 94.406/1987 + Res. COFEN 507/2016', 'Exercício da enfermagem (categorias, atribuições privativas) e fiscalização · 15 C/E', 'comp.leg.enfermagem', 'Decreto 94.406 / Res. 507'),
 ('29/11', 'nuc', 'Res. COFEN 726/2023 e 751/2024', 'Leitura dirigida das duas resoluções do edital · 15 C/E calibrados · flashcards do Sistema Cofen/Corens', 'comp.leg.enfermagem', 'Res. 726 e 751'),
 ('30/11', 'p2', 'Improbidade (Lei 8.429 + 14.230)', 'Dolo, tipos (arts. 9º, 10 e 11), sanções, prescrição, acordo de não persecução · 20 C/E reais', 'comp.leg.improbidade', 'Improbidade'),
 ('01/12', 'p2', 'Processo administrativo (Lei 9.784)', 'Princípios, competência e delegação, impedimento/suspeição, prazos, recursos, anulação × revogação · 20 C/E reais', 'comp.leg.processo', 'Lei 9.784'),
 ('02/12', 'p2', 'LGPD (Lei 13.709)', 'Bases legais, dados sensíveis, direitos do titular, controlador × operador × encarregado, ANPD, poder público · 20 C/E', 'comp.leg.lgpd', 'LGPD'),
 ('03/12', 'bloco', 'Bloco C/E P2 (30 itens reais)', 'Misto: enfermagem + improbidade + 9.784 + LGPD · modo prova, sem consulta · correção e ledger', 'comp.leg.enfermagem comp.leg.improbidade comp.leg.processo comp.leg.lgpd', None),
 ('04/12', 'nuc', 'Lei 14.133 para contratações de TIC', 'Fases, ETP, TR, modalidades, critérios de julgamento, gestão e fiscalização do contrato · 15 C/E', 'comp.leg.licitacoes esp.tic.contratos', 'Lei 14.133'),
 ('05/12', 'nuc', 'IN SGD/ME 94/2022', 'Planejamento da contratação de TIC (ETP, análise de riscos, TR), papéis da equipe, fiscalização técnica × administrativa × requisitante, SLA/IMR · 15 C/E', 'esp.tic.contratos', 'IN SGD 94/2022'),
 ('06/12', 'disc', '1ª discursiva real: DNS (CFN 2024)', 'Tema conhecido para aprender o formato: 20–30 linhas, 3 aspectos · corrigir pelo padrão da Quadrix · lista de erros de língua', 'disc.tic esp.tic.redes', None),
 ('07/12', 'nuc', 'ITIL 4', 'Cadeia de valor, práticas (incidente, problema, mudança, requisição, nível de serviço, catálogo), SLA × OLA × UC · 15 C/E reais', 'esp.tic.govti', 'ITIL 4'),
 ('08/12', 'nuc', 'COBIT 2019 + riscos de TIC', 'Governança × gestão, objetivos EDM/APO/BAI/DSS/MEA, fatores de desenho; riscos (identificar, analisar, tratar) · 15 C/E', 'esp.tic.govti esp.tic.gestao', 'COBIT / riscos'),
 ('09/12', 'nuc', 'Planejamento e controle de TIC', 'PDTIC, indicadores (KPI/KGI), relatórios gerenciais, ITIL/COBIT no nível gerencial · 15 C/E (CREFITO-17, CREF-11)', 'esp.tic.gestao', 'Gestão de TIC'),
 ('10/12', 'nuc', 'Políticas, normas e auditoria de TIC', 'PSI e normas internas, auditoria de TIC, controles internos e conformidade, SI nos processos · 15 C/E (bloco mais fraco do acervo)', 'esp.tic.auditoria', 'Auditoria de TIC'),
 ('11/12', 'nuc', 'Atendimento técnico estratégico', 'Suporte ao Sistema Cofen/Corens, pareceres e notas técnicas, Ouvidoria, treinamentos · 15 C/E', 'esp.tic.atendimento', 'Atendimento estratégico'),
 ('12/12', 'bloco', 'Bloco C/E dos exclusivos do 407 (30 itens)', 'Contratos, governança, gestão, auditoria e atendimento · reais do CREFITO-17, CREF-11 e CFN · correção e ledger', 'esp.tic.contratos esp.tic.govti esp.tic.gestao esp.tic.auditoria esp.tic.atendimento', None),
 ('13/12', 'disc', 'Discursiva real: indicadores e riscos (CREFITO-17)', 'A discursiva mais parecida com a do 407 · corrigir pelo padrão (CAC, OT, DLP)', 'disc.tic esp.tic.govti esp.tic.gestao', None),
 ('14/12', 'rev', 'Revisão da fase 1', 'Flashcards de P2 e dos exclusivos · reler as lacunas abertas · preparar o simulado de amanhã (sem estudo novo)', 'comp esp.tic', None),
 ('15/12', 'sim', 'Simulado 1 completo (diagnóstico)', '120 itens + discursiva no tempo oficial da prova, modo prova · 30 min: anotar dúvidas (correção amanhã)', 'basicos comp esp.tic disc.tic', None),
 ('16/12', 'ref', 'Correção do simulado 1 + Língua Portuguesa', '3 h: correção item a item, ledger de lacunas, ajuste do plano · 2 h: LP Quadrix (sintaxe, pontuação, reescrita) com itens reais', 'basicos.lp', 'LP'),
 ('17/12', 'nuc', 'Infraestrutura 1: servidores e gestão de ativos', 'Operação de servidores Windows/Linux, AD, serviços de rede; gestão de ativos (inventário, CMDB, ciclo de vida) · 30 C/E reais', 'esp.tic.infra esp.tic.fundamentos', 'Servidores e ativos'),
 ('18/12', 'nuc', 'Infraestrutura 2: implantação, migração e continuidade', 'Implantação e migração de sistemas, integridade, backup (tipos, 3-2-1, RPO/RTO), continuidade · 30 C/E', 'esp.tic.infra esp.tic.seguranca', 'Migração e backup'),
 ('19/12', 'nuc', 'Redes + LP', '3 h: OSI/TCP-IP, IPv4/IPv6 e sub-redes, TCP×UDP, DNS/HTTP(S)/SMTP/FTP, VLAN, VPN, Wi-Fi · 30 C/E · 2 h: LP', 'esp.tic.redes basicos.lp', 'Redes'),
 ('20/12', 'nuc', 'Segurança da informação', 'CIDA, criptografia simétrica/assimétrica, hash, certificados e assinatura digital, ameaças e ataques, ISO 27001/27002 · 30 C/E', 'esp.tic.seguranca', 'Segurança'),
 ('21/12', 'disc', 'Discursiva (backup e recovery) + bloco técnico', '1h30: discursiva real do CRQ-RS · 3 h: 40 C/E de infra, redes e segurança em modo prova + correção', 'disc.tic esp.tic.infra esp.tic.redes esp.tic.seguranca', None),
 ('22/12', 'nuc', 'Banco de dados', 'Modelo relacional, chaves, normalização (1FN–3FN, FNBC), SQL (DDL/DML, joins, agregação), administração de SGBD · 30 C/E', 'esp.tic.bd', 'Banco de dados'),
 ('23/12', 'nuc', 'Engenharia de software + RLM', '3 h: ciclo de vida, Scrum/Kanban, UML, testes · 2 h: raciocínio lógico (proposições, equivalências, negação)', 'esp.tic.engsw basicos.rlm', 'Eng. de software'),
 ('24/12', 'p1', 'LP + Inglês técnico', '3 h: LP (concordância, regência, crase, coesão) · 2 h: Inglês técnico (textos de TI, itens reais)', 'basicos.lp basicos.ingles', 'Inglês técnico'),
 ('25/12', 'rev', 'Revisão leve (Natal)', 'Flashcards de P2 e dos exclusivos · revisão espaçada · sem tema novo', 'comp esp.tic', None),
 ('26/12', 'nuc', 'Fundamentos + RLM', '3 h: arquitetura, hardware/software, SO, internet/intranet, nuvem e virtualização (aproveitar o material do CGU) · 2 h: RLM (problemas, porcentagem, contagem)', 'esp.tic.fundamentos basicos.rlm', 'Fundamentos'),
 ('27/12', 'bloco', 'Bloco técnico + discursiva', '3 h: 40 C/E de BD, eng. de software e fundamentos · 1h30: discursiva real do CRP-SP (otimização de consultas)', 'esp.tic.bd esp.tic.engsw esp.tic.fundamentos disc.tic', None),
 ('28/12', 'p2', 'Ética, LAI e anticorrupção', 'Ética no serviço público, LAI (Lei 12.527), Lei Anticorrupção (12.846) · 30 C/E', 'esp.tic.etica comp.leg.anticorrupcao', 'Ética, LAI, anticorrupção'),
 ('29/12', 'p2', 'Constitucional + Administrativo', 'CF art. 5º e 196–200; Administrativo: conselhos profissionais, empregado público, PAD, atos e poderes · 30 C/E', 'comp.const comp.leg.cf comp.adm', 'Const. + Adm.'),
 ('30/12', 'p1', 'RLM + LP em itens reais', '40 itens de P1 reais do acervo, por partes, com correção comentada', 'basicos.rlm basicos.lp', None),
 ('31/12', 'rev', 'Revisão dos exclusivos + reforço', 'Reforço das lacunas abertas no ledger (exclusivos do 407) · flashcards', 'esp.tic', None),
 ('01/01', 'rev', 'Revisão leve (Ano-Novo)', 'Flashcards e revisão espaçada · sem tema novo', 'comp esp.tic', None),
 ('02/01', 'disc', 'Discursiva (segurança em nuvem) + reforço', '1h30: discursiva real do CRO-SP · 3 h: reforço das lacunas com mais erros desde o simulado 1', 'disc.tic esp.tic.seguranca', None),
 ('03/01', 'sim', 'Simulado 2 completo', '120 itens + discursiva no tempo oficial da prova, modo prova · comparar com o simulado 1', 'basicos comp esp.tic disc.tic', None),
 ('04/01', 'ref', 'Correção do simulado 2', 'Correção item a item, ledger, comparar com o simulado 1 · ajustar a fase 3 se preciso', 'basicos comp esp.tic', None),
 ('05/01', 'p1', 'Língua Portuguesa', '20–25 itens reais de LP + revisão da lista de erros de língua', 'basicos.lp', None),
 ('06/01', 'disc', 'Discursiva: CFO 2024: segurança, ITIL e riscos', '20–30 linhas em até 1 h · corrigir pelo padrão (CAC, OT, DLP) e lançar no ledger', 'disc.tic esp.tic.seguranca esp.tic.govti', None),
 ('07/01', 'bloco', 'Bloco P3 — exclusivos: contratos + governança', '30 itens C/E em 1h15 (reais primeiro) + correção', 'esp.tic.contratos esp.tic.govti', None),
 ('08/01', 'p2', 'P2 — Sistema Cofen/Corens (rodada 2)', 'Revisão rápida da lei + 25 C/E reais', 'comp.leg.enfermagem', None),
 ('09/01', 'p1', 'RLM + Inglês técnico', '1 h: RLM · 1 h: Inglês técnico (itens reais)', 'basicos.rlm basicos.ingles', None),
 ('10/01', 'rev', 'Revisão da semana', 'Revisão espaçada, flashcards e lacunas em reforço', 'comp esp.tic', None),
 ('11/01', 'rev', 'Revisão + conferir a inscrição', 'Último dia da inscrição: conferir se foi paga · revisão espaçada e flashcards', 'comp esp.tic', None),
 ('12/01', 'p1', 'Língua Portuguesa', '20–25 itens reais de LP + revisão da lista de erros de língua', 'basicos.lp', None),
 ('13/01', 'disc', 'Discursiva: CRF-PR 2025: acesso remoto', '20–30 linhas em até 1 h · corrigir pelo padrão (CAC, OT, DLP) e lançar no ledger', 'disc.tic esp.tic.infra esp.tic.seguranca', None),
 ('14/01', 'bloco', 'Bloco P3 — técnico: infra + redes', '30 itens C/E em 1h15 (reais primeiro) + correção', 'esp.tic.infra esp.tic.redes', None),
 ('15/01', 'p2', 'P2 — Improbidade + Lei 9.784', 'Revisão rápida da lei + 25 C/E reais', 'comp.leg.improbidade comp.leg.processo', None),
 ('16/01', 'p1', 'RLM + Inglês técnico', '1 h: RLM · 1 h: Inglês técnico (itens reais)', 'basicos.rlm basicos.ingles', None),
 ('17/01', 'sim', 'Simulado 3 · parte A: P1 + P2', '70 itens (P1 40 + P2 30) em 2 h, modo prova · sem gabarito até a parte B', 'basicos comp', None),
 ('18/01', 'sim', 'Simulado 3 · parte B: P3 + discursiva', '50 itens de P3 (1h15) + discursiva (45 min) · correção no dia seguinte', 'esp.tic disc.tic', None),
 ('19/01', 'p1', 'Língua Portuguesa', '20–25 itens reais de LP + revisão da lista de erros de língua', 'basicos.lp', None),
 ('20/01', 'disc', 'Discursiva: CRMV-GO 2025: monitoramento de redes', '20–30 linhas em até 1 h · corrigir pelo padrão (CAC, OT, DLP) e lançar no ledger', 'disc.tic esp.tic.redes esp.tic.infra', None),
 ('21/01', 'bloco', 'Bloco P3 — exclusivos: gestão + auditoria + atendimento', '30 itens C/E em 1h15 (reais primeiro) + correção', 'esp.tic.gestao esp.tic.auditoria esp.tic.atendimento', None),
 ('22/01', 'p2', 'P2 — LGPD + anticorrupção', 'Revisão rápida da lei + 25 C/E reais', 'comp.leg.lgpd comp.leg.anticorrupcao', None),
 ('23/01', 'p1', 'RLM + Inglês técnico', '1 h: RLM · 1 h: Inglês técnico (itens reais)', 'basicos.rlm basicos.ingles', None),
 ('24/01', 'rev', 'Revisão da semana', 'Revisão espaçada, flashcards e lacunas em reforço', 'comp esp.tic', None),
 ('25/01', 'ref', 'Reforço das lacunas do ledger', 'Os 2–3 temas com mais erros abertos · teoria curta + 20 C/E reais · fechar ou manter lacuna', 'esp.tic', None),
 ('26/01', 'p1', 'Língua Portuguesa', '20–25 itens reais de LP + revisão da lista de erros de língua', 'basicos.lp', None),
 ('27/01', 'disc', 'Discursiva: inédita: fiscalização de contrato de TIC com SLA', '20–30 linhas em até 1 h · corrigir pelo padrão (CAC, OT, DLP) e lançar no ledger', 'disc.tic esp.tic.contratos', None),
 ('28/01', 'bloco', 'Bloco P3 — técnico: segurança + BD', '30 itens C/E em 1h15 (reais primeiro) + correção', 'esp.tic.seguranca esp.tic.bd', None),
 ('29/01', 'p2', 'P2 — Lei 14.133 + Constitucional/Administrativo', 'Revisão rápida da lei + 25 C/E reais', 'comp.leg.licitacoes comp.const comp.adm', None),
 ('30/01', 'p1', 'RLM + Inglês técnico', '1 h: RLM · 1 h: Inglês técnico (itens reais)', 'basicos.rlm basicos.ingles', None),
 ('31/01', 'sim', 'Simulado 4 · parte A: P1 + P2', '70 itens (P1 40 + P2 30) em 2 h, modo prova · sem gabarito até a parte B', 'basicos comp', None),
 ('01/02', 'sim', 'Simulado 4 · parte B: P3 + discursiva', '50 itens de P3 (1h15) + discursiva (45 min) · correção no dia seguinte', 'esp.tic disc.tic', None),
 ('02/02', 'p1', 'Língua Portuguesa', '20–25 itens reais de LP + revisão da lista de erros de língua', 'basicos.lp', None),
 ('03/02', 'disc', 'Discursiva: COREN-PR 2024: análise de dados', '20–30 linhas em até 1 h · corrigir pelo padrão (CAC, OT, DLP) e lançar no ledger', 'disc.tic esp.tic.bd', None),
 ('04/02', 'bloco', 'Bloco P3 — exclusivos: misto', '30 itens C/E em 1h15 (reais primeiro) + correção', 'esp.tic.contratos esp.tic.gestao esp.tic.auditoria', None),
 ('05/02', 'p2', 'P2 — Sistema Cofen/Corens (rodada 3)', 'Revisão rápida da lei + 25 C/E reais', 'comp.leg.enfermagem', None),
 ('06/02', 'p1', 'RLM + Inglês técnico', '1 h: RLM · 1 h: Inglês técnico (itens reais)', 'basicos.rlm basicos.ingles', None),
 ('07/02', 'rev', 'Revisão da semana', 'Revisão espaçada, flashcards e lacunas em reforço', 'comp esp.tic', None),
 ('08/02', 'ref', 'Reforço das lacunas do ledger', 'Os 2–3 temas com mais erros abertos · teoria curta + 20 C/E reais · fechar ou manter lacuna', 'esp.tic', None),
 ('09/02', 'p1', 'Língua Portuguesa', '20–25 itens reais de LP + revisão da lista de erros de língua', 'basicos.lp', None),
 ('10/02', 'disc', 'Discursiva: CFP 2024: VLANs', '20–30 linhas em até 1 h · corrigir pelo padrão (CAC, OT, DLP) e lançar no ledger', 'disc.tic esp.tic.redes', None),
 ('11/02', 'bloco', 'Bloco P3 — técnico: fundamentos + eng. de software', '30 itens C/E em 1h15 (reais primeiro) + correção', 'esp.tic.fundamentos esp.tic.engsw', None),
 ('12/02', 'p2', 'P2 — Improbidade + LGPD (rodada final)', 'Revisão rápida da lei + 25 C/E reais', 'comp.leg.improbidade comp.leg.lgpd', None),
 ('13/02', 'p1', 'RLM + Inglês técnico', '1 h: RLM · 1 h: Inglês técnico (itens reais)', 'basicos.rlm basicos.ingles', None),
 ('14/02', 'sim', 'Simulado 5 · parte A: P1 + P2', '70 itens (P1 40 + P2 30) em 2 h, modo prova · sem gabarito até a parte B', 'basicos comp', None),
 ('15/02', 'sim', 'Simulado 5 · parte B: P3 + discursiva', '50 itens de P3 (1h15) + discursiva (45 min) · correção no dia seguinte', 'esp.tic disc.tic', None),
 ('16/02', 'p1', 'Língua Portuguesa', '20–25 itens reais de LP + revisão da lista de erros de língua', 'basicos.lp', None),
 ('17/02', 'disc', 'Discursiva: inédita: migração de sistema e atendimento aos Corens', '20–30 linhas em até 1 h · corrigir pelo padrão (CAC, OT, DLP) e lançar no ledger', 'disc.tic esp.tic.infra esp.tic.atendimento', None),
 ('18/02', 'bloco', 'Bloco P3 — P3 misto em modo prova', '30 itens C/E em 1h15 (reais primeiro) + correção', 'esp.tic', None),
 ('19/02', 'p2', 'P2 — P2 misto em modo prova', 'Revisão rápida da lei + 25 C/E reais', 'comp', None),
 ('20/02', 'p1', 'RLM + Inglês técnico', '1 h: RLM · 1 h: Inglês técnico (itens reais)', 'basicos.rlm basicos.ingles', None),
 ('21/02', 'sim', 'Simulado 6 (último) · parte A: P1 + P2', '70 itens (P1 40 + P2 30) em 2 h, modo prova · sem gabarito até a parte B', 'basicos comp', None),
 ('22/02', 'sim', 'Simulado 6 (último) · parte B: P3 + discursiva', '50 itens de P3 (1h15) + discursiva (45 min) · correção no dia seguinte', 'esp.tic disc.tic', None),
 ('23/02', 'rev', 'Revisão final', 'Só flashcards, lacunas em reforço e a lista de erros de língua · sem tema novo', 'basicos comp esp.tic', None),
 ('24/02', 'rev', 'Revisão final', 'Só flashcards, lacunas em reforço e a lista de erros de língua · sem tema novo', 'basicos comp esp.tic', None),
 ('25/02', 'rev', 'Revisão final', 'Só flashcards, lacunas em reforço e a lista de erros de língua · sem tema novo', 'basicos comp esp.tic', None),
 ('26/02', 'rev', 'Revisão final', 'Só flashcards, lacunas em reforço e a lista de erros de língua · sem tema novo', 'basicos comp esp.tic', None),
 ('27/02', 'leve', 'Véspera', '30–40 min: lista de erros recorrentes · separar o que o edital exige · dormir cedo', '', None),
 ('28/02', 'prova', 'PROVA COFEN (tarde)', 'Objetiva 120 itens + discursiva · chegar cedo · levar o que o edital exige (documento e caneta)', '', None),
]

MATERIAIS = {}

FERIADOS = {
 "25/12": "Natal",
 "01/01": "Confraternização Universal",
 "09/02": "Carnaval",
 "10/02": "Quarta-feira de Cinzas",
}


def horas(d, tipo):
    """Pedido de 27/11: 2 h por dia até 14/12; 5 h por dia de 15/12 a 03/01; 2 h por dia depois. Todos os dias."""
    if tipo == "prova":
        return 0
    if d == "27/02":
        return 0.5
    x = D(d)
    if D("15/12") <= x <= D("03/01"):
        return 5
    return 2


MD_CABECALHO = [
 "# Cronograma — COFEN 2026 · Cargo 407 Analista de TIC — Gaby", "",
 "**Prova:** 28/02/2027 (domingo, tarde) · **Estudo:** 27/11/2026 → 27/02/2027, todos os dias  ",
 "**Formato:** Quadrix C/E (+1/−1), 120 itens (P1 40 · P2 30 · P3 50) + discursiva de 20–30 linhas  ",
 "**Mínimos:** P1 ≥ 10 · P2 ≥ 8 · P3 ≥ 12 · objetiva ≥ 34 · discursiva ≥ 5  ",
 "**Painel:** `cronograma.html` (marca feito/parcial, horas e notas). Fonte: `plano.py` (rodar `python3 pessoal/gaby/cronograma/plano.py` depois de editar).", "",
 "## Capacidade", "",
 "| Período | Horas/dia | Total |",
 "|---------|-----------|-------|",
 "| 27/11 → 14/12 | 2 h | 36 h |",
 "| 15/12 → 03/01 | 5 h | 100 h |",
 "| 04/01 → 27/02 | 2 h | ~110 h |", "",
 "**Dia de 2 h:** 10 min de revisão espaçada · 40–50 min de teoria · 40 min de C/E · 20–30 min de correção e ledger.  ",
 "**Perdeu um dia:** não dobre o seguinte; o tema vai para a próxima segunda (reforço) ou para um dia de revisão.  ",
 "**Aproveitamento do CGU:** redes, Linux, Windows/AD, nuvem e virtualização já têm material; na fase 2 eles entram como revisão com itens Quadrix, não como teoria do zero.  ",
 "**Pedidos:** `material do dia` · `N itens <tag>` · `corrigir meu gabarito` · `corrigir minha discursiva` · `ajustar cronograma`", "",
 "## Fases", "",
 "| Fase | Período | Objetivo |",
 "|------|---------|----------|",
]

MD_POS_FASES = ["", "**Prazos:** inscrição até **11/01/2027** (taxa R$ 100) · simulados completos em **15/12** e **03/01**; simulados em dois dias em 17–18/01, 31/01–01/02, 14–15/02 e 21–22/02.", ""]

MD_RODAPE = [
 "## Checklist", "",
 "### P2 e Sistema Cofen/Corens",
 "- [ ] Lei 5.905, Decreto 94.406, Res. COFEN 507/2016, 726/2023, 751/2024",
 "- [ ] Improbidade · Lei 9.784 · LGPD · Lei 14.133 · Anticorrupção",
 "- [ ] Constitucional (art. 5º, 196–200) · Administrativo", "",
 "### P3 — exclusivos do 407",
 "- [ ] Contratos de TIC (IN SGD 94/2022) · governança (ITIL, COBIT) · gestão de TIC",
 "- [ ] Políticas, normas e auditoria · atendimento técnico estratégico", "",
 "### P3 — técnico",
 "- [ ] Infra (servidores, ativos, migração, backup) · redes · segurança",
 "- [ ] Banco de dados · eng. de software · fundamentos · ética/LAI", "",
 "### P1 e discursiva",
 "- [ ] LP, RLM e Inglês técnico com itens reais",
 "- [ ] 11 discursivas avulsas + 6 nos simulados", "",
 "## Ajustes", "",
 "Ledger: `pessoal/gaby/cronograma/lacunas.yaml`. Depois de cada simulado: `diagnóstico de gaps` e `ajustar cronograma`.", "",
 "- **27/11:** plano criado com o foco só no COFEN (inscrição da CGU perdida). Horas informadas pela Gaby: 2 h/dia até 14/12, 5 h/dia de 15/12 a 03/01, 2 h/dia depois; todos os dias. Começo direto pelo cronograma, sem diagnóstico prévio: o simulado de 15/12 faz esse papel.",
]

if __name__ == "__main__":
    cg.gerar(
        pathlib.Path(__file__).resolve().parent, trilha="tic",
        fases=FASES, dias=DIAS, materiais=MATERIAIS, feriados=FERIADOS, horas=horas,
        md_cabecalho=MD_CABECALHO, md_pos_fases=MD_POS_FASES, md_rodape=MD_RODAPE,
    )
