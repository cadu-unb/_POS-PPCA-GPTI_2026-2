# Consolidação 1 — histórico da busca bibliográfica

**Registro consolidado em:** 22/10/2026, 16h56 (horário de Brasília).  
**Base consultada:** Web of Science (WoS).  
**Estado do trabalho:** triagem por títulos e resumos; leitura integral ainda não realizada.

Este documento registra como a primeira busca sobre **reciclagem** foi construída, quais contagens foram anotadas e o que motivou cada ajuste. Os horários individuais das consultas na WoS não foram guardados; os horários dos CSVs abaixo indicam apenas quando os arquivos foram gravados localmente.

## 1. Recorte e método

A consulta inicial tentava reunir, de uma vez, resíduos sólidos/reciclagem, gêmeos digitais ou IoT e privacidade ou LGPD:

```text
TS=(("solid* wast* rec*") AND ("digital twin"OR "IoT") AND ("privacy"OR "LGPD"))
```

Essa foi a formulação de partida, antes da correção sintática e da ampliação dos termos; não há contagem registrada para ela. Como a área ainda tem terminologia pouco estável, combinar todos os temas desde o início poderia ocultar estudos úteis. Passamos então a medi-los separadamente e a cruzá-los de forma controlada.

Adotamos a abordagem sistêmica associada a **Gharajedaghi (2011)** como guia de leitura: as faces do tetraedro são **Função, Estrutura, Processo e Contexto**; o volume deste primeiro ciclo é **Reciclagem**. As faces servem para organizar e avaliar os estudos, sem exigir que cada artigo contenha quatro blocos de termos unidos por `AND`. O tetraedro de **Privacidade** e o cruzamento entre os dois volumes ficam para uma etapa futura. A proposta inicial está em [pesquisa.md](../tentativa1/pesquisa.md).

| Face | Pergunta usada na triagem |
| --- | --- |
| Função | O que se busca recuperar, reciclar ou valorizar? |
| Estrutura | Quais produtos, instalações, agentes, dados e relações compõem o sistema? |
| Processo | Como ocorrem triagem, desmontagem, logística reversa e demais operações? |
| Contexto | Em quais fluxos de resíduos, setores e condições o sistema opera? |

## 2. Blocos da consulta

As definições completas e reproduzíveis de `TS=` ficam no dicionário `QUERIES` do [montador de buscas](../../python/wos_query.py). As chaves foram mantidas para que as contagens antigas possam ser reproduzidas.

| Chave | Papel | Termos centrais |
| --- | --- | --- |
| `1` | Contexto original | *solid waste*, *municipal waste*, *urban waste*, *post-consumer waste*, *electronic waste*, *e-waste* |
| `2` | Função | `recycl*`, recuperação de materiais/recursos, valorização |
| `3` | Tecnologia | *digital twin* |
| `4` | Tecnologia | *Internet of Things*, IoT |
| `5` | Contexto adicional | WEEE, resíduos de construção/demolição, produtos em fim de vida, baterias usadas, resíduos plásticos, sucata metálica |
| `6` | Processo | desmontagem, desmanufatura, triagem de resíduos, logística reversa |
| `7` | Teste posterior de contexto | variante da chave `1` com expressões mais específicas para resíduos sólidos municipais/urbanos; ainda sem contagens registradas aqui |

**Observação:** não criamos um bloco `TS=` específico para **Estrutura** nesta rodada. Essa face entrou principalmente na avaliação dos registros encontrados. A chave `7` não substitui a `1` nas contagens históricas.

## 3. Contagens informadas na WoS

Esses números vieram das consultas anotadas durante a exploração. Como não foram preservados todos os filtros da interface, eles são um **histórico da rodada**, não uma garantia de reprodução exata em outra data.

### Blocos isolados

| Expressão | Resultados |
| --- | ---: |
| `1` — Contexto original | 112.123 |
| `2` — Função | 426.477 |
| `3` — Gêmeos digitais | 37.376 |
| `4` — IoT | 199.760 |
| `5` — Contexto adicional | 29.967 |

### Cruzamentos iniciais

| Expressão | Resultados |
| --- | ---: |
| `1 AND 2` | 26.188 |
| `1 AND 3` | 76 |
| `1 AND 4` | 590 |
| `2 AND 3` | 396 |
| `2 AND 4` | 1.064 |
| `3 AND 4` | 4.632 |
| `1 AND 2 AND 3` | 35 |
| `1 AND 2 AND 4` | 181 |
| `2 AND 3 AND 4` | 56 |
| `1 AND 2 AND 3 AND 4` | 7 |

### Busca fora do Contexto original

| Expressão | Resultados |
| --- | ---: |
| `(2 AND 3) NOT 1` | 361 |
| `(2 AND 4) NOT 1` | 883 |

**Cuidado com a leitura:** `1 AND 2 AND 3 = 35` é a **interseção com** o Contexto original; `(2 AND 3) NOT 1 = 361` é o conjunto **fora** dele. O mesmo vale para `181` e `883` no ramo da IoT.

## 4. Refinamento por contexto e processo

1. A chave `5` ampliou o vocabulário de **Contexto** para fluxos e materiais que a chave `1` poderia não capturar. A consulta isolada retornou **29.967** resultados.
2. O cruzamento `((2 AND 3) AND 5) NOT 1` foi exportado com **34 registros**. Esse número é o tamanho do CSV disponível; não há uma contagem da interface WoS registrada separadamente para essa expressão.
3. A chave `6` reuniu termos de **Processo**. A expressão `((2 AND 3) AND 6) NOT (1 OR 5)` produziu um CSV com **30 registros únicos**. A triagem preliminar por título e resumo classificou **15** como centrais, **12** como apoio/contexto e **3** como fracos. Essas classes ainda não foram validadas por leitura integral.
4. Retiramos apenas a exclusão de `5`: `((2 AND 3) AND 6) NOT 1`. O novo CSV tem **40 registros únicos**: preserva os **30** anteriores e acrescenta **10**, todos presentes no arquivo com `AND 5 NOT 1`. Entre esses dez, a triagem preliminar considerou **7** diretamente alinhados e **3** úteis como apoio/contexto. Portanto, manter `NOT 5` descartava estudos pertinentes.

O `NOT 1` foi usado para **explorar o que escapava do Contexto original**. Ele não deve ser tomado, por si só, como critério definitivo de inclusão ou exclusão do futuro corpus: também pode remover trabalhos relevantes que empregam os termos da chave `1`.

## 5. Arquivos preservados

As contagens abaixo são de **linhas bibliográficas exportadas**, verificadas pelos identificadores únicos da WoS; podem diferir de uma contagem mostrada pela interface em outro momento.

| Consulta / conjunto | CSV | Registros únicos | Gravação local em 22/10/2026 |
| --- | --- | ---: | --- |
| `1 AND 2 AND 3` | [1_and_2_and_3.csv](../tentativa1/1_and_2_and_3.csv) | 35 | 15h18 |
| `(2 AND 3) NOT 1` | [2AND3__NOT_1.csv](../tentativa1/2AND3__NOT_1.csv) | 361 | 15h22 |
| `((2 AND 3) AND 5) NOT 1` | [2AND3-AND5__NOT_1.csv](../tentativa1/2AND3-AND5__NOT_1.csv) | 34 | 15h45 |
| `((2 AND 3) AND 6) NOT (1 OR 5)` | [2AND3-AND6__NOT_1OR5.csv](../tentativa1/2AND3-AND6__NOT_1OR5.csv) | 30 | 16h06 |
| `((2 AND 3) AND 6) NOT 1` | [2AND3-AND6__NOT_1.csv](../tentativa1/2AND3-AND6__NOT_1.csv) | 40 | 16h37 |
| `(((2 AND 3) AND 6) NOT 1) AND 0` | | 40 | 19h42 |

Os CSVs não foram copiados para esta pasta. Os **dez candidatos** escolhidos a partir do conjunto de 40 registros têm fichas curtas em [Manual 1](<../Manual 1/>), com título original e traduzido, resumo traduzido de forma condensada, palavras-chave, ano e DOI. Esta consolidação não repete essas fichas.

## 6. Como continuar e registrar a próxima rodada

Na raiz do repositório, o [montador de buscas](../../python/README.md) mostra as chaves e gera a expressão completa para colar na busca avançada da WoS:

```powershell
python -B python/wos_query.py --list
python -B python/wos_query.py '((2 AND 3) AND 6) NOT 1'
```

Em cada nova consulta, anotar: **data e hora da execução; coleção/índices e demais filtros da WoS; expressão exata; total mostrado na interface; quantidade exportada; nome do CSV; e motivo do ajuste**. Isso permitirá distinguir mudanças na estratégia de mudanças na indexação da base.

O próximo passo de avaliação é escolher **três** entre as dez fichas de [Manual 1](<../Manual 1/>) para leitura integral e registrar, para cada estudo, evidências relativas a Função, Estrutura, Processo e Contexto. Só depois vale consolidar critérios de inclusão e exclusão e iniciar o tetraedro de Privacidade.
