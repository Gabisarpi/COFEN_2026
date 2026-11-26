# tools/

Scripts do repositório. Rodar sempre da raiz. Dependências: Python 3; PyYAML onde indicado; `pdftotext` (poppler) no extrator de PDF.

| Script | Para que serve | Quando roda | Comando típico |
|--------|----------------|-------------|----------------|
| `acervo_sugestao_hoje.py` | Sugestão do dia: tags do dia no `plano.py` × lacunas abertas × proxy; não fura a fase (PyYAML) | “o que estudo hoje” | `python3 tools/acervo_sugestao_hoje.py [--data AAAA-MM-DD] [--write]` |
| `cronograma_gerar.py` | Módulo do cronograma: valida as tags de `DIAS` no mapa e gera `plano.md` + `cronograma.html` a partir do `template.html` (datas jul–dez = 2026, jan–jun = 2027) | Chamado por um `pessoal/gaby/cronograma/plano.py` (quando existir) | `python3 pessoal/gaby/cronograma/plano.py` |
| `correcao_html.py` | Gera `correcao.html` de uma discursiva corrigida | Toda correção de discursiva | `python3 tools/correcao_html.py pessoal/gaby/respostas/<pasta>` |
| `md_html.py` | Versão HTML de leitura de qualquer `.md` | Quando quiser ler no navegador | `python3 tools/md_html.py <arquivo.md>` |
| `validar_estudo.py` | Valida `lacunas.yaml` e as tags de `DIAS` do `plano.py` (PyYAML) | Após mexer em ledger/plano/mapa; CI | `python3 tools/validar_estudo.py --check` |
| `sync_skills.py` | Confere skills em `.agents/skills/`, recria os symlinks `.cursor`/`.claude` e as seções de `cargos/tic/perfil.md` | Após mexer em skills ou perfil; CI | `python3 tools/sync_skills.py [--check]` |
| `acervo_cobertura.py` | Heatmap acervo × mapa do 407 (Quadrix ×2, demais ×1); atualiza `catalogo.yaml` | Após ingerir prova | `python3 tools/acervo_cobertura.py --write [--write-catalogo]` |
| `acervo_previsao.py` | Ranking de estudo por tag (perfil + acervo); grava `acervo/previsao-cofen.md` | Após ingerir prova | `python3 tools/acervo_previsao.py --write` |
| `acervo_extract_quadrix.py` | Extrai itens C/E de prova + gabarito (PDF) para o Markdown do acervo. Herdado do CGU: conferir na primeira prova Quadrix | A cada prova nova | `python3 tools/acervo_extract_quadrix.py --prova … --gabarito … --out acervo/itens/<id>.md --id <id> --orgao … --ano … --cargo … --tags …` |
