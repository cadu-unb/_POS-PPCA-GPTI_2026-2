# Registro da pesquisa — Tentativa 3

Preencher os campos abaixo ao executar a primeira consulta. Contagens da Tentativa 2 não entram nesta tabela.

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

Execute na ordem. Registre o total mostrado pela WoS. Se exportar registros, indique quantos vieram no CSV; o total de resultados e o número exportado podem ser diferentes.

| Ordem | Expressão no montador | Pergunta | Resultados WoS | Registros exportados | CSV de origem | Data/hora | Observações |
| ---: | --- | --- | ---: | ---: | --- | --- | --- |
| 1 | `8` | Qual o tamanho do conjunto inicial de privacidade? | 239'397 | — | — | — | — |
| 2 | `8 AND 0F` | Quantos também contêm `function*`? | 23'679 | — | — | — | — |
| 3 | `8 NOT 0F` | Quantos não contêm `function*`? | 215'718 | — | — | — | — |

**Verificação após as três consultas:** `8` = (`8 AND 0F`) + (`8 NOT 0F`), desde que a configuração e a base permaneçam iguais. Se não fechar, registrar a diferença antes de avançar.

## Inspeção preliminar

Depois das contagens, registrar uma pequena amostra de **cada** lado. Informar a ordenação usada e o critério de escolha para permitir nova inspeção. Manter termos originais dos artigos em inglês; comentários em português.

| Conjunto | Título original / DOI ou UT | Termos em inglês observados | Relação com privacidade e Função | Decisão provisória |
| --- | --- | --- | --- | --- |
| `8 AND 0F` | a preencher | a preencher | a preencher | a preencher |
| `8 NOT 0F` | a preencher | a preencher | a preencher | a preencher |

## Próxima etapa

Após avaliar Função, acrescentar **Contexto** (`8 AND 0C` e `8 NOT 0C`) neste mesmo registro, com outra tabela de contagens e inspeção. Depois fazer Estrutura (`0E`) e Processo (`0P`), sempre partindo de `8`. Por fim, comparar `8 AND 0` com `8 NOT 0` para observar a presença de ao menos um radical versus a ausência dos quatro. Registrar aqui qualquer revisão dos termos antes de repetir uma consulta; não sobrescrever contagens antigas.
