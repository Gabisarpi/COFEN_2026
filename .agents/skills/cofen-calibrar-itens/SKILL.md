---
name: cofen-calibrar-itens
description: >-
  Calibra qualquer questão C/E gerada para o COFEN 2026 (simulado, bloco,
  reforço, material de núcleos, HTML ou MD): densidade do perfil do Cargo 407,
  estilo Quadrix, anti-dedução, cotas e autochecagem. Use sempre ao gerar ou
  reescrever itens Quadrix, dados.js ou caderno, ou quando a pessoa falar em
  calibração, densidade, item fácil demais ou régua.
---

# COFEN — Calibrar itens gerados

Projeto: `COFEN_2026`. O que é do cargo está em **`cargos/tic/perfil.md`**. As skills de geração (`cofen-simulado-quadrix`, `cofen-material-nucleos`, `cofen-flashcards`) **obrigam** esta skill **antes de gravar**.

## Quando acionar (obrigatório)

1. Gerar ou reescrever itens C/E (simulado, bloco, reforço, núcleos, cartões C/E)
2. Montar/atualizar `dados.js` / `caderno.html` / `caderno.md`
3. Pedido de calibração ou queixa de item curto, óbvio ou fora do estilo

Item fora da régua → **reescrever** antes de gravar.

## INVARIANTE — não remover esta skill nem a régua

Proibido apagar, esvaziar ou “simplificar” esta skill, ou tirar o ponteiro das skills de geração, **salvo pedido expresso da Gaby** nesta conversa. Pedido genérico (“melhora a skill”) não autoriza.

## 1) Densidade e estilo — Cargo 407 / Quadrix

- **Tamanho:** a Quadrix usa assertivas mais curtas que a Cebraspe (tipicamente 1–3 linhas). Comando de contexto é opcional; quando houver, curto (cenário de conselho, trecho de norma, tabela de SLA, trecho de log/config).
- **Literalidade:** boa parte da cobrança é texto de lei, norma ou definição de manual com **uma palavra trocada** (prazo, quem aprova, “deverá” × “poderá”, “sempre” × “em regra”). Gerar itens desse tipo nos blocos de legislação, contratos (Lei 14.133, IN SGD/ME 94/2022) e normas (ISO 27001/27002, ITIL, COBIT).
- **TI técnica:** protocolo, porta, camada, comando Linux/Windows, SQL simples — detalhe concreto, sem inventar produto.
- **Gestão (blocos 8–11):** papéis (gestor × fiscal técnico × fiscal administrativo × fiscal requisitante), artefatos (ETP, TR, DFD, plano de fiscalização), indicadores e SLA, princípios de auditoria e controle interno.
- **Código/config:** só quando a assertiva julga o trecho; no máximo ~10% do bloco.

Calibração viva: `cargos/tic/amostra/` (quando existir) e 2–3 itens reais Quadrix da mesma tag no acervo.

## 2) Anti-dedução (obrigatório)

Itens não podem ser resolvidos só por “tom de manual”.

**Dupla calibração (bloco ≥ 10):** (1) amostra da trilha; (2) acervo real — abrir 2–3 itens da mesma tag e registrar `ancoragem_acervo` no meta. Sem acervo Quadrix da tag ainda: registrar `ancoragem_acervo: sem_itens_quadrix` e usar a fonte primária.

**Mecanismos:**

1. Meia-verdade (núcleo certo + detalhe falso: prazo, número, papel, ordem)
2. C contra-intuitivo (soa E, mas é C)
3. E plausível (frase de manual + erro cirúrgico)
4. Literalidade alterada (uma palavra muda o gabarito)
5. Proibir E gritante e C de cartilha
6. Sem pista de redação (não alongar só os E; absolutos não só nos E)
7. Fontes vigentes (texto atual da lei/norma, não o do ano da prova antiga)

**Cotas (bloco ≥ 15):**

| Tipo | Mínimo / teto |
|------|---------------|
| Meia-verdade | ≥ 30% do bloco |
| E plausível (entre os E) | ≥ 25% dos E |
| C contra-intuitivo | ≥ 2 ou ≥ 15% dos C |
| C cartilha sem armadilha | ≤ 20% |
| Itens com absoluto (“sempre”, “somente”, “vedado”) que são C | ≥ 1 em cada 3 com absoluto |

## 3) Checklist na entrega

- [ ] Skill de geração leu esta skill
- [ ] Estilo Quadrix (assertiva curta, literalidade onde couber)
- [ ] Sequência C/E conferida (no HTML, pelo `verificar.py`; no MD, à mão)
- [ ] Anti-dedução + cotas (bloco ≥ 15)
- [ ] `ancoragem_acervo` no meta (bloco ≥ 10)
- [ ] Sem gabarito no enunciado; uma ideia por assertiva
- [ ] `exp` didática: ideia simples + mecanismo + por que C/E

## Integração

| Skill | Papel |
|-------|-------|
| `cofen-simulado-quadrix` | Monta/corrige → calibra com esta antes de gravar |
| `cofen-material-nucleos` | Monta núcleos HTML → calibra com esta |
| `cofen-flashcards` | Cartões C/E → calibra com esta |
| `cofen-diagnostico-gaps` | Depois da correção; não calibra enunciado |

## Anti-padrões

- Copiar o tamanho e o tom Cebraspe do material CGU sem ajustar ao estilo Quadrix
- Item de legislação com número de artigo inventado
- E que só fica errado por imprecisão de redação
- Marcar calibração “ok” sem abrir acervo/amostra no bloco ≥ 10
