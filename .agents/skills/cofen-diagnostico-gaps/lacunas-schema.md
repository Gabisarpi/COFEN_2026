# Schema — `$P/cronograma/lacunas.yaml`

Ledger canônico de lacunas da Gaby (`pessoal/gaby/cronograma/lacunas.yaml`).  
A skill `cofen-diagnostico-gaps` cria/atualiza o arquivo.

```yaml
atualizado: "YYYY-MM-DD"          # última atualização do ledger
prova: "2027-02-28"
notas: |
  Texto livre opcional (ex.: pós-simulado 120). Só as últimas ~10 linhas de resumo;
  o histórico fica nas correções em $P/respostas/ e no git.

entradas:
  - id: fiscal-tecnico-x-administrativo   # slug estável (kebab); não renomear sem necessidade
    tag: esp.tic.contratos
    tema: "papéis do fiscal técnico × fiscal administrativo"
    severidade: alta                # alta | media | baixa
    ocorrencias: 1
    primeira_data: "2026-12-15"
    ultima_data: "2026-12-15"
    status: em_reforco              # aberto | em_reforco | resolvido
    erros_com_certeza: 1            # opcional
    detalhes:
      - "Fiscal administrativo acompanha obrigações trabalhistas/previdenciárias, não a qualidade técnica"
    fontes:
      - tipo: objetiva              # objetiva | discursiva | revisao | simulado
        path: pessoal/gaby/simulados/gerados/.../gabarito.md
        data: "2026-12-15"
    acertos_pos:                    # opcional: acertos posteriores ao último erro, em variações inéditas
      - data: "2026-12-18"
        confianca: duvida           # certeza | duvida
        fonte: pessoal/gaby/respostas/2026-12-18_bloco.yaml   # opcional

  - id: rto-rpo-confusao
    tag: esp.tic.seguranca
    tema: "RTO × RPO (tempo de retomada × ponto de dados)"
    severidade: alta
    ocorrencias: 1
    primeira_data: "2026-10-20"
    ultima_data: "2026-10-20"
    status: aberto
    detalhes:
      - "RPO é a perda de dados tolerada (ponto no tempo), não o prazo de retomada"
    fontes:
      - tipo: objetiva
        path: pessoal/gaby/simulados/gerados/.../gabarito.md
        data: "2026-10-20"
```

## Regras

- `tag`: somente valores de `$C/mapa-edital.md`
- Mesclar por `id` (preferencial) ou por `tag`+`tema` equivalentes
- `ocorrencias` incrementa a cada nova evidência do mesmo gap
- `erros_com_certeza` (opcional, inteiro ≥ 0): incrementa quando o erro foi marcado com certeza; pesa na priorização (`cofen-diagnostico-gaps` §3)
- `acertos_pos` (opcional, lista de `{data: "YYYY-MM-DD", confianca: certeza|duvida, fonte: <path opcional>}`): acertos depois do último erro, em variação distinta (refação idêntica não entra). Erro novo zera a lista e volta `status: aberto`
- `status: resolvido` exige ≥ 2 itens de `acertos_pos` com `confianca: certeza` em datas diferentes (regras completas em `cofen-diagnostico-gaps` §2)
- `fora_do_padrao` (opcional, booleano): `true` quando a lacuna nasceu só de itens inéditos e o subtópico tem 0 itens da banca no acervo. A entrada fica visível, mas não gera itens, folha ou flashcard e não pesa na priorização. Ativar só se a Gaby registrar essa regra em `pessoal/gaby/preferencias-estudo.md`.
- Os campos opcionais podem faltar: entradas antigas sem eles continuam válidas e não são preenchidas retroativamente
- LP: usar a tag `disc.tic` e `tema` iniciando com `LP —`
