# Formato do `deck.json` (cofen-flashcards)

Exemplo de estrutura abaixo (o deck real do repo CGU era da trilha de outra pessoa).

```json
{
 "titulo": "Flashcards Object Lock e Prefixo",
 "eyebrow": "COFEN 2026 · Cargo 407 · Flashcards de 15/12",
 "h1": "Object Lock e prefixo mais longo",
 "lede": "Por que estes cartões, quanto tempo e como usar (1–3 frases).",
 "pessoa": "gaby",
 "cargo": "tic",
 "data": "2026-11-11",
 "material": "pessoal/gaby/simulados/gerados/2026-12-15_flashcards-contratos/flashcards.html",
 "export": "pessoal/gaby/respostas/2026-12-15_flashcards-contratos.yaml",
 "key": "cofen-gaby-fc-contratos",
 "baralhos": [
  {"id": "ol", "nome": "Object Lock", "lacunas": ["retencao-object-lock-ilm"]},
  {"id": "rt", "nome": "Prefixo × AD", "lacunas": ["roteamento-lpm-vs-ad"]}
 ],
 "fontes": {
  "S3": "<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html\">AWS, Locking objects with Object Lock</a>"
 },
 "cartoes": [
  {"id": "ol3", "d": "ol", "k": "ce", "g": "E", "lacuna": "retencao-object-lock-ilm",
   "f": "Assertiva para julgar (HTML simples).",
   "a": "Explicação do gabarito.",
   "h": "Frase-gancho curta.",
   "s": "S3"}
 ]
}
```

| Campo | Regra |
|---|---|
| `titulo` | nome do artifact (2–4 palavras, sem explicação depois de dois-pontos) |
| `data` | dia em que o deck foi gerado, `AAAA-MM-DD` |
| `material` / `export` | caminhos a partir da raiz do repo; `export` em `pessoal/<pessoa>/respostas/`, termina em `.yaml` |
| `key` | prefixo único do `localStorage` (`cofen-<pessoa>-fc-<tema>`); trocar a chave zera as marcações dos aparelhos |
| `baralhos` | 1 a 4; `id` curto; com um baralho só, os botões de filtro somem |
| `cartoes[].k` | `conceito` ou `ce`; `ce` exige `g` = `C` ou `E` |
| `cartoes[].lacuna` | id existente em `lacunas.yaml` (o build confere quando acha o ledger) |
| `resolucao` (raiz) | `"detalhada"` só com a opção `resolucao-detalhada` ativa para a pessoa; exige `termos` e `viz` em todo cartão |
| `cartoes[].termos` / `viz` | mesmo formato do `cofen-material-nucleos` (`Termo :: definição` separados por ` \|\| `; `viz` em prosa) |
| `cartoes[].s` | chave de `fontes` ou o texto/HTML da fonte |

O build (`scripts/build.py`) avisa quando um baralho tem menos de 2 C/E ou um só gabarito, e
recusa ids repetidos, baralho inexistente, gabarito ausente, fonte não declarada e lacuna fora do ledger.
