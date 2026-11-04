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

## Etapa 2 — privacidade e gêmeos digitais

O cruzamento dos quatro radicais reduziu o universo de privacidade a 193 resultados, mas esse número, por si só, não mede a presença do tema gêmeos digitais. Por isso, a consulta `8 AND 3` partiu diretamente de **privacidade + gêmeo digital**, usando a chave `3` já existente. Sua definição histórica foi preservada.

| Ordem | Expressão no montador | Resultados WoS | CSV exportado | Registros no CSV |
| ---: | --- | ---: | --- | ---: |
| 13 | `8 AND 3` | 1.270 | [8AND3.csv](saida_wos/8AND3.csv) | 20 |
| 14 | `8 AND 3 AND 0` | 646 | [8AND3AND0.csv](saida_wos/8AND3AND0.csv) | 20 |
| 15 | `(8 AND 3) NOT 0` | 624 | [8AND3_NOT_0.csv](saida_wos/8AND3_NOT_0.csv) | 20 |

**Verificação:** 646 + 624 = 1.270. Os três CSVs contêm 20 identificadores WoS únicos cada. São amostras dos conjuntos, não seus totais. A planilha de visualização com menos campos pode ser usada na leitura; os CSVs de origem ficam como referência bibliográfica.

`8 AND 3` será o conjunto de referência para testar cada face isoladamente. **Gêmeo físico/real** será tratado como contraparte do gêmeo digital na definição e na futura triagem; expressões como *physical twin*, *physical counterpart* e *real-world counterpart* poderão ser testadas em consulta própria. Nenhuma dessas expressões foi requisito das consultas 13–15.

As condições da sessão WoS ainda precisam ser registradas no início deste documento. Próximo passo: testar a presença dos termos da contraparte física dentro de `8 AND 3`, sem torná-los critério definitivo de inclusão.

| Ordem | Expressão no montador | Objetivo | Resultados WoS | CSV |
| ---: | --- | --- | ---: | --- |
| 16 | `8 AND 3 AND 13` | Testar *physical twin*, *real twin*, *physical counterpart* ou *real-world counterpart* no conjunto de privacidade e gêmeos digitais | 19 | 19 |

Registrar qualquer revisão sem sobrescrever contagens antigas.
