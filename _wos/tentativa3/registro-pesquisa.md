# Registro da pesquisa — Tentativa 3

As contagens de 04/11/2026 já estão anotadas. Ainda faltam as condições da sessão abaixo; contagens da Tentativa 2 não entram nesta tabela.

| Condição da sessão | Valor |
| --- | --- |
| Data e horário da consulta (Brasília) | a preencher |
| Base, coleção e índices | a preencher |
| Intervalo de publicação | a preencher |
| Tipos de documento e idioma | a preencher |
| Outros filtros da interface | a preencher |
| *Exact Search* ligado ou desligado | a preencher |
| Ordenação usada na inspeção de títulos | a preencher |

## Etapa 1 — privacidade e pilares literais

Contagens informadas para consultas realizadas por volta das 19h de 04/11/2026. Os CSVs são exportações locais: **20 registros** nos conjuntos amostrados e **193 registros** no cruzamento dos quatro pilares. O número de linhas de um CSV não substitui o total mostrado pela WoS.

| Ordem | Expressão no montador | Resultados WoS | CSV exportado | Registros no CSV |
| ---: | --- | ---: | --- | ---: |
| 1 | `8` | 239.397 | [8.csv](saida_wos/8.csv) | 20 |
| 2 | `8 AND 0F` | 23.679 | [8AND0F.csv](saida_wos/8AND0F.csv) | 20 |
| 3 | `8 NOT 0F` | 215.718 | [8_NOT_0F.csv](saida_wos/8_NOT_0F.csv) | 20 |
| 4 | `8 AND 0C` | 27.109 | [8AND0C.csv](saida_wos/8AND0C.csv) | 20 |
| 5 | `8 AND 0E` | 24.575 | [8AND0E.csv](saida_wos/8AND0E.csv) | 20 |
| 6 | `8 AND 0P` | 53.335 | [8AND0P.csv](saida_wos/8AND0P.csv) | 20 |
| 7 | `8 AND 0` | 103.033 | [8AND0.csv](saida_wos/8AND0.csv) | 20 |
| 8 | `8 AND 0C AND 0E AND 0P` | 1.169 | [8AND0CAND0EAND0P.csv](saida_wos/8AND0CAND0EAND0P.csv) | 20 |
| 9 | `8 AND 0C AND 0E AND 0F` | 492 | [8AND0CAND0EAND0F.csv](saida_wos/8AND0CAND0EAND0F.csv) | 20 |
| 10 | `8 AND 0C AND 0F AND 0P` | 810 | [8AND0CAND0FAND0P.csv](saida_wos/8AND0CAND0FAND0P.csv) | 20 |
| 11 | `8 AND 0F AND 0E AND 0P` | 857 | [8AND0FAND0EAND0P.csv](saida_wos/8AND0FAND0EAND0P.csv) | 20 |
| 12 | `8 AND 0F AND 0C AND 0E AND 0P` | 193 | [8AND0FAND0EAND0CAND0P.csv](saida_wos/8AND0FAND0EAND0CAND0P.csv) | 193 |

**Verificação das contagens anotadas:** 23.679 + 215.718 = 239.397. Os dois subconjuntos fecham com o total de `8`. Os 12 CSVs foram lidos como CSV, com 72 colunas e identificadores WoS (`UT`) únicos em cada arquivo. Ainda falta registrar a configuração da sessão para documentar a comparação.

## Etapa 2 — proposta de filtro para gêmeos digitais

O cruzamento dos quatro radicais reduziu o universo de privacidade a 193 resultados, mas esse número, por si só, não mede a presença do tema gêmeos digitais. O próximo teste parte diretamente de **privacidade + gêmeo digital**, usando a chave `3` já existente. Não alterar a definição histórica da chave `3`.

| Ordem | Expressão no montador | Pergunta | Resultados WoS | Data/hora | Observações |
| ---: | --- | --- | ---: | --- | --- |
| 13 | `8 AND 3` | Quantos registros associam privacidade e `digital twin*`? | — | — | Próxima consulta |
| 14 | `8 AND 3 AND 0` | Quantos desses registros contêm ao menos um dos quatro radicais? | — | — | Fazer depois de 13 |
| 15 | `(8 AND 3) NOT 0` | Quantos não contêm nenhum dos quatro radicais? | — | — | Fazer depois de 13 |

| Ordem | Expressão no montador | Resultados WoS |
| :---: | --- | --- |
| | "8 AND 3"         | 1270 |
| | "8 AND 3 AND 0"   | 646  |
| | "(8 AND 3) NOT 0" | 624  |

`8 AND 3` será o conjunto de referência para testar cada face isoladamente. **Gêmeo físico/real** será tratado como contraparte do gêmeo digital na definição e na futura triagem; expressões como *physical twin*, *physical counterpart* e *real-world counterpart* poderão ser testadas em consulta própria após a contagem de `8 AND 3`. Nenhuma dessas expressões é requisito desta primeira consulta.

Quando as novas contagens chegarem, conferir se `8 AND 3` = (`8 AND 3 AND 0`) + (`(8 AND 3) NOT 0`) sob a mesma configuração da WoS. Só depois definir a próxima ampliação de termos. Registrar qualquer revisão sem sobrescrever contagens antigas.
