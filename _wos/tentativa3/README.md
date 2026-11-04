# Tentativa 3 — Privacidade, construção passo a passo

**Início:** 04/11/2026.  
**Volume do tetraedro:** privacidade.  
**Estado:** roteiro aberto; nenhuma contagem desta tentativa foi informada.

Esta tentativa recomeça a investigação de privacidade na Web of Science (WoS). Os resultados da [Tentativa 2](../tentativa2/README.md) servem como histórico, mas não serão copiados como resultados desta rodada. As quatro faces propostas — **Função, Contexto, Estrutura e Processo** — serão acrescentadas **uma por vez** à busca de privacidade. A cada inclusão, também mediremos o conjunto complementar, sem o termo da face. Só depois das contagens e de uma amostra dos registros decidiremos o próximo cruzamento.

## O que medimos

As chaves abaixo já existem no [montador de consultas](../../python/wos_query.py):

| Papel nesta rodada | Chave | Termos procurados em inglês |
| --- | --- | --- |
| Privacidade, conjunto de partida | `8` | `privac*`, `data protect*`, `personal data`, `personal information`, `personally identifiable information` |
| Função, termo literal | `0F` | `function*` |
| Contexto, termo literal | `0C` | `context*` |
| Estrutura, termo literal | `0E` | `structur*` |
| Processo, termo literal | `0P` | `process*` |

Os códigos `0F`, `0C`, `0E` e `0P` medem **presença das palavras** nos campos `TS=`. Eles não provam que um estudo discute conceitualmente uma face. Na triagem, descreveremos separadamente **o que a proteção busca alcançar** (Função), **em que ambiente ocorre** (Contexto), **quais componentes e relações existem** (Estrutura) e **como os dados são tratados** (Processo). As chaves temáticas `9`–`12` da Tentativa 2 poderão ajudar numa etapa posterior, sem misturar seus resultados com estes testes literais.

## Sequência de trabalho

1. Medir `8` para obter o total inicial de registros sobre privacidade.
2. Medir `8 AND 0F` e `8 NOT 0F`: dentro de `8`, presença e ausência de `function*`.
3. Registrar as contagens, sem exportar os conjuntos completos. Para a primeira inspeção, ler **10 títulos de cada lado** na WoS, com a mesma ordenação anotada. Só exportar uma amostra pequena se os títulos justificarem examinar resumos e palavras-chave; anotar termos recorrentes em inglês e por que parecem pertinentes ou não.
4. Repetir o mesmo procedimento, uma face por vez, na ordem **Contexto (`0C`)**, **Estrutura (`0E`)** e **Processo (`0P`)**. Manter `8` como base em cada comparação; não acumular `AND` automaticamente.
5. Depois das quatro comparações individuais, medir `8 AND 0` e `8 NOT 0`. A chave `0` reúne os quatro radicais com `OR`: o segundo conjunto não contém **nenhum** deles. Comparar uma amostra dos dois conjuntos.
6. Somente depois avaliar combinações entre faces, termos temáticos e recortes tecnológicos como gêmeos digitais (`3`) e IoT (`4`).

`8 NOT 0F` significa registros sobre privacidade **sem o radical `function*` nos campos pesquisados**. Não significa ausência conceitual de Função. O mesmo cuidado vale para as demais faces. O resultado `8` deve ser igual à soma dos resultados `8 AND 0F` e `8 NOT 0F` quando as três consultas usam os mesmos filtros e a mesma atualização da base.

Use a **Busca Avançada / Query Builder** da WoS. O campo `TS=` cobre título, resumo, palavras-chave dos autores e *Keywords Plus* ([campos da WoS](https://webofscience.zendesk.com/hc/en-us/articles/26916258216209-Web-of-Science-Core-Collection-Search-Fields)); a WoS aceita `AND`, `OR` e `NOT` para combinar conjuntos ([operadores](https://webofscience.zendesk.com/hc/en-us/articles/20016122409105-Search-Operators)).

Na raiz do projeto, gere cada consulta; o programa também sugere um nome caso haja exportação posterior:

```powershell
python -B python/wos_query.py --folder _wos/tentativa3 "8"
python -B python/wos_query.py --folder _wos/tentativa3 "8 AND 0F"
python -B python/wos_query.py --folder _wos/tentativa3 "8 NOT 0F"
```

O programa **não consulta a WoS**: copie a expressão impressa, execute-a na base e preencha o [registro da pesquisa](registro-pesquisa.md). Para esta etapa, **bastam as contagens**, sem CSV. Anote coleção/índices, anos, idioma, tipos de documento, outros filtros, modo *Exact Search*, data e hora; mantenha essas escolhas nas comparações. Se a inspeção indicar artigos promissores, uma exportação de **10 a 20 registros por conjunto** basta para a triagem inicial; o critério e a ordenação da amostra precisam ficar registrados. O [Manual 3](<../Manual 3/README.md>) receberá apenas fichas dos artigos selecionados, com indicação da consulta e, se houver, do CSV de origem.
