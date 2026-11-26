# Instruções para agentes (Claude Code / Cursor)

Repo de estudo da Gaby para o COFEN 2026, Cargo 407 (Analista de TIC), banca Quadrix.

## Sempre

1. Ler `REPO.md` → `pessoal/gaby/CONTINUIDADE.md` → `cargos/tic/perfil.md`.
2. Destinos em `$P = pessoal/gaby/`: cadernos C/E → `simulados/gerados/YYYY-MM-DD_tema/` · flashcards → `flashcards/` (`.tsv` **e** `_notebooklm.md`) · respostas/correções → `respostas/` · teoria/revisão → `revisao/` · fontes de áudio → `audio/notebooklm/` · leituras → `leituras/` · lacunas → `cronograma/lacunas.yaml`.
3. **Feito** só com aviso explícito da Gaby; gerar material não conta como conclusão.
4. **Push só com autorização da Gaby** em cada envio.

## Simulados Quadrix (C/E)

- Itens **novos**; acervo = estilo, não cópia literal.
- Gabarito sempre em arquivo separado.
- Calibrar pelo estilo Quadrix (ver `cargos/tic/perfil.md`): enunciado curto, cobrança literal de lei/norma.
- Anti-dedução: meia-verdade, C contra-intuitivo, E plausível; evitar C de cartilha e E gritante.

## Gaps / cronograma

- Ledger: `$P/cronograma/lacunas.yaml`.
- `CONTINUIDADE.md` guarda só ~7 dias de estado; o resto vai para `$P/historico/AAAA-MM.md`.

## Skills (fonte única para Claude Code e Cursor)

- Canônico: `.agents/skills/<nome>/SKILL.md`. `.claude/skills` e `.cursor/skills` são symlinks para `.agents/skills`.
- **Windows:** `git config core.symlinks true` (e Modo de Desenvolvedor, se o Git pedir). Se o clone criar um arquivo de texto no lugar do symlink, rode `python3 tools/sync_skills.py`.
- Conferência: `python3 tools/sync_skills.py --check` · `python3 tools/validar_estudo.py --check` (também no GitHub Actions).

| Skill | Para quê |
|-------|----------|
| `cofen-simulado-quadrix` | Simulado completo (120 + discursiva), blocos, reforço de lacunas, correção |
| `cofen-calibrar-itens` | Régua obrigatória antes de gravar qualquer item C/E (invariante) |
| `cofen-material-nucleos` | Caderno HTML por núcleos recorrentes (reais + inéditos, resolução oculta, export YAML) |
| `cofen-flashcards` | Flashcards `.tsv` + `_notebooklm.md` (sempre) e baralho HTML (opcional) |
| `cofen-folha-revisao` | Folha de revisão ativa de um tópico |
| `cofen-redacao-discursiva` | Editor HTML da discursiva (20–30 linhas) |
| `cofen-leituras-dirigidas` | Leitura técnica curta antes da discursiva |
| `cofen-diagnostico-gaps` | Ledger de lacunas, “o que estudo hoje”, ajuste de cronograma |
| `cofen-acervo` | Ingestão de provas Quadrix e heatmap |
| `cofen-preferencias-opcionais` | Opções individuais (interface, resolução detalhada, revisão) |

- Áudio: feito pela Gaby no NotebookLM a partir das fontes em `audio/notebooklm/` (modelo em `pessoal/gaby/audio/notebooklm/_MODELO.md`). Não pedir acesso ao navegador para isso.
