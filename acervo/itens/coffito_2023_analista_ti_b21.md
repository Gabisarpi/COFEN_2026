---
id: coffito_2023_analista_ti_b21
orgao: "COFFITO"
ano: 2023
banca: quadrix
cargo: "ANALISTA DE TECNOLOGIA DA INFORMAÇÃO"
prova: P3
formato: certo_errado
tags_edital:
  - esp.tic.engsw
itens: 96-100
aderencia: alta
fonte:
  path: acervo/fontes/coffito_2023_analista_ti/prova.pdf
  gabarito: acervo/fontes/coffito_2023_analista_ti/gabarito.pdf
  nota: "extração automática (acervo_extract_quadrix.py); gabarito definitivo. Itens 57, 67 e 114: alterados para “E” (errado). / Item 56: anulado."
---

## Comando

using System; using System.Collections.Generic; class Paciente { public string Nome { get; set; } public int Idade { get; set; } public string Telefone { get; set; } public Paciente(string nome, int idade, string telefone) { Nome = nome; Idade = idade; Telefone = telefone; } } class Agendamento { public DateTime DataHora { get; set; } public Paciente Paciente { get; set; } public Agendamento(DateTime dataHora, Paciente paciente) { DataHora = dataHora; Paciente = paciente; } } class Program { static void Main() { List<Agendamento> agendamentos = new List<Agendamento>(); // Exemplo de agendamento Paciente paciente1 = new Paciente(“João”, 30, “(11)99999-9999”); DateTime dataHora1 = new DateTime(2023, 07, 20, 14, 30, 0); Agendamento agendamento1 = new Agendamento(dataHora1, paciente1); agendamentos.Add(agendamento1); Console.WriteLine(“Agendamento realizado com sucesso!”); } } Com referência ao programa em C# acima, que permite realizar o agendamento de pacientes a sessões de fisioterapia, julgue os itens de 96 a 100.

## Assertivas

| id | texto | gabarito |
|----|-------|----------|
| 96 | A validação dos dados do paciente, antes de realizar o agendamento, é realizada pelo método Paciente. | E |
| 97 | O objetivo da classe Agendamento é manter um registro de todas as sessões de fisioterapia realizadas, incluindo data e hora. | C |
| 98 | No programa, os termos usados get e set referem-se a métodos de acesso. | C |
| 99 | A classe Program tem como finalidade realizar a comunicação com um serviço de envio de SMS para lembrar os pacientes sobre o agendamento. | E |
| 100 | Ao executar o método List<Agendamento>, serão mostrados os detalhes das sessões de fisioterapia, como a duração e o fisioterapeuta responsável. | E |
