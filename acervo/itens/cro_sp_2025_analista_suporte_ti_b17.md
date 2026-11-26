---
id: cro_sp_2025_analista_suporte_ti_b17
orgao: "CRO-SP"
ano: 2025
banca: quadrix
cargo: "Analista de Suporte de Tecnologia de Informação"
prova: P3
formato: certo_errado
tags_edital:
  - esp.tic.seguranca
itens: 106-110
aderencia: alta
fonte:
  path: acervo/fontes/cro_sp_2025_analista_suporte_ti/prova.pdf
  gabarito: acervo/fontes/cro_sp_2025_analista_suporte_ti/gabarito.pdf
  nota: "extração automática (acervo_extract_quadrix.py); gabarito definitivo. "
---

## Comando

Durante a modernização da infraestrutura tecnológica de uma clínica odontológica especializada em implantodontia e ortodontia digital, a equipe de TI identificou que o sistema de prontuário eletrônico utilizado pelos dentistas armazena localmente, de forma temporária, imagens DICOM de tomografias e escaneamentos intraorais em dispositivos móveis e estações de trabalho. Observou-se, também, que os profissionais acessam esses dados em regime de plantão, muitas vezes das suas residências ou consultórios externos, via conexões sem autenticação forte e utilizando os seus próprios dispositivos. A equipe de TI, então, iniciou um plano de ação para aumentar a segurança cibernética da clínica, com foco em controle de acesso e autenticação, criptografia de dados e dispositivos e segurança em dispositivos móveis. Com base nessa situação hipotética, julgue os itens a seguir.

## Assertivas

| id | texto | gabarito |
|----|-------|----------|
| 106 | A ausência de autenticação multifator (MFA) no acesso remoto ao sistema clínico, mesmo com senhas fortes e VPN, representa uma falha crítica de segurança, pois isso compromete a estratégia de defesa em profundidade exigida em ambientes que lidam com dados sensíveis de saúde. | C |
| 107 | A autenticação biométrica em dispositivos móveis é considerada, isoladamente, uma substituição segura para a autenticação multifator em sistemas que acessam dados de prontuários eletrônicos. | E |
| 108 | A implementação de criptografia de disco completo com uso de chaves armazenadas no TPM (Trusted Platform Module) do dispositivo é uma abordagem recomendada para proteger os dados em repouso, sem comprometer a usabilidade do sistema durante o boot. | C |
| 109 | A utilização de criptografia apenas na camada de transporte (por exemplo, HTTPS/TLS 1.2) é suficiente para garantir a segurança das imagens odontológicas armazenadas temporariamente no dispositivo local do dentista. | E |
| 110 | A configuração de políticas de conformidade em soluções de MDM pode impedir o acesso aos dados clínicos sensíveis, caso o dispositivo móvel do profissional não esteja com as atualizações de segurança aplicadas, garantindo maior controle sobre o estado do endpoint. | C |
