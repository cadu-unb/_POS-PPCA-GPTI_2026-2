# Registro da pesquisa — Tentativa 3

As três contagens iniciais já estão anotadas. Ainda faltam as condições da sessão abaixo; contagens da Tentativa 2 não entram nesta tabela.

| Condição da sessão | Valor |
| --- | --- |
| Data e horário da consulta (Brasília) | a preencher |
| Base, coleção e índices | a preencher |
| Intervalo de publicação | a preencher |
| Tipos de documento e idioma | a preencher |
| Outros filtros da interface | a preencher |
| *Exact Search* ligado ou desligado | a preencher |
| Ordenação usada na inspeção de títulos | a preencher |

## Etapa 1 — volume e Função literal

Execute na ordem e registre apenas o total mostrado pela WoS. **Não é preciso exportar metadados nesta etapa.**

| Ordem | Expressão no montador | Pergunta | Resultados WoS | Data/hora | Observações |
| ---: | --- | --- | ---: | --- | --- |
| 1 | `8` | Qual o tamanho do conjunto inicial de privacidade? | 239'397 | 19h 04/11/2026 | — |
| 2 | `8 AND 0F` | Quantos também contêm `function*`? | 23'679 | 19h 04/11/2026 | — |
| 3 | `8 NOT 0F` | Quantos não contêm `function*`? | 215'718 | 19h 04/11/2026 | — |
| 3 | `8 AND 0C` | | 27'109 | 19h 04/11/2026 | — |
| 3 | `8 AND 0E` | | 24'575 | 19h 04/11/2026 | — |
| 3 | `8 AND 0P` | | 53'335 | 19h 04/11/2026 | — |
| 3 | `8 AND 0`  | | 103'033 | 19h 04/11/2026 | — |
| 3 | `8 AND 0C AND 0E AND 0P`  | | 1,169 | 19h 04/11/2026 | — |
| 3 | `8 AND 0C AND 0E AND 0F`  | | 492 | 19h 04/11/2026 | — |
| 3 | `8 AND 0C AND 0F AND 0P`  | | 810 | 19h 04/11/2026 | — |
| 3 | `8 AND 0F AND 0E AND 0P`  | | 857 | 19h 04/11/2026 | — |
| 3 | `8 AND 0F AND 0C AND 0E AND 0P` | | 193 | 19h 04/11/2026 | — |

**Verificação das contagens anotadas:** 23.679 + 215.718 = 239.397. Os dois subconjuntos fecham com o total de `8`. Ainda falta registrar a configuração da sessão para documentar a comparação.

## Inspeção preliminar

Depois das contagens, ler primeiro **10 títulos de cada** lado, diretamente na WoS. Informar a ordenação usada e o critério de escolha para permitir nova inspeção. Se títulos promissores justificarem olhar resumos e palavras-chave, exportar apenas **10 a 20 registros por conjunto** e anotar o nome do CSV e o número efetivamente exportado. Esta amostra é exploratória; não serve para estimar a proporção de artigos relevantes entre os milhares de resultados. Manter termos originais dos artigos em inglês; comentários em português.

| Conjunto | Título original / DOI ou UT | Termos em inglês observados | Relação com privacidade e Função | Decisão provisória |
| --- | --- | --- | --- | --- |
| `8 AND 0F` | a preencher | a preencher | a preencher | a preencher |
| `8 NOT 0F` | a preencher | a preencher | a preencher | a preencher |

## Próxima etapa

Após avaliar Função, acrescentar **Contexto** (`8 AND 0C` e `8 NOT 0C`) neste mesmo registro, com outra tabela de contagens e inspeção. Depois fazer Estrutura (`0E`) e Processo (`0P`), sempre partindo de `8`. Por fim, comparar `8 AND 0` com `8 NOT 0` para observar a presença de ao menos um radical versus a ausência dos quatro. Registrar aqui qualquer revisão dos termos antes de repetir uma consulta; não sobrescrever contagens antigas.
