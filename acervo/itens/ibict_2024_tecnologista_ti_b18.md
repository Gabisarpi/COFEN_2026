---
id: ibict_2024_tecnologista_ti_b18
orgao: "IBICT"
ano: 2024
banca: quadrix
cargo: "CARGO TECNOLOGISTA – PERFIL: TECNOLOGIA DA INFORMAÇÃO"
prova: P3
formato: certo_errado
tags_edital:
  - esp.tic.bd
itens: 96-100
aderencia: media
fonte:
  path: acervo/fontes/ibict_2024_tecnologista_ti/prova.pdf
  gabarito: acervo/fontes/ibict_2024_tecnologista_ti/gabarito.pdf
  nota: "extração automática (acervo_extract_quadrix.py); gabarito definitivo. Itens 14 e 56: anulados."
---

## Comando

CREATE TABLE Autores (AutorID INT AUTO_INCREMENT PRIMARY KEY, Nome VARCHAR(100), Email VARCHAR(100), InstituicaoID INT, FOREIGN KEY (InstituicaoID) REFERENCES Instituicoes(InstituicaoID)); CREATE TABLE Revistas (RevistaID INT AUTO_INCREMENT PRIMARY KEY, Nome VARCHAR(100), ISSN VARCHAR(20)); CREATE TABLE Artigos (ArtigoID INT AUTO_INCREMENT PRIMARY KEY, Titulo VARCHAR(255), Resumo TEXT, PalavrasChave VARCHAR(255), RevistaID INT, FOREIGN KEY (RevistaID) REFERENCES Revistas(RevistaID)); CREATE TABLE Instituicoes (InstituicaoID INT AUTO_INCREMENT PRIMARY KEY, Nome VARCHAR(100), Cidade VARCHAR(100), Pais VARCHAR(100)); CREATE TABLE Autor_Artigo (AutorID INT, ArtigoID INT, PRIMARY KEY (AutorID, ArtigoID), FOREIGN KEY (AutorID) REFERENCES Autores(AutorID), FOREIGN KEY (ArtigoID) REFERENCES Artigos(ArtigoID)); Com relação ao código SQL acima, no SGBD MySQL, julgue os itens de 96 a 100.

## Assertivas

| id | texto | gabarito |
|----|-------|----------|
| 96 | Para que se mostrem todos os autores e suas instituições afiliadas, pode-se utilizar o comando a seguir. SELECT Autores.Nome AS NomeAutor, Instituicoes.Nome AS Nomelnstituicao FROM Autores INNER JOIN Instituicoes ON Autores.InstituicaoID = Instituicoes.InstituicaoID; | C |
| 97 | Para mostrar todos os artigos publicados na revista RECEN, juntamente com seus autores, pode-se utilizar o comando seguir. SELECT Artigos.Titulo AS TituloArtigo, Autores.Nome AS NomeAutor FROM Artigos INNER JOIN Autores ON Autor_Artigo.AutorID = Autores.AutorID WHERE Artigos.RevistaID = (SELECT RevistaID FROM Revistas WHERE Nome = ‘NomeDaRevista‘); | E |
| 98 | Para que se mostre o número de artigos publicados por cada autor, pode-se utilizar o comando a seguir. SELECT Autores.Nome AS NomeAutor, COUNT(*) AS NumeroArtigos FROM Autores INNER JOIN Autor_Artigo ON Autores.AutorID = Autor_Artigo.AutorID GROUP BY Autores.Nome; | C |
| 99 | Ao se executar o comando a seguir, ocorrerá erro, pois não foi informado o código do autor (AutorID). INSERT INTO Autores (Nome, Email, InstituicaoID) VALUES (‘João Silva’, ‘joao.silva@email.com’, 1); | E |
| 100 | Para que seja atualizado o e-mail do autor João Silva, deve-se executar o comando a seguir. UPDATE Autores SET Email = = ‘joao.silva@gmail.com’ WHERE Nome = ‘João Silva’; | E |
