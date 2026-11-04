# Tentativa 3 — Privacidade, construção passo a passo

**Início:** 04/11/2026.  
**Volume do tetraedro:** privacidade.  
**Estado:** contagens e amostras iniciais registradas; próximo recorte: gêmeos digitais.

Esta tentativa recomeça a investigação de privacidade na Web of Science (WoS). Os resultados da [Tentativa 2](../tentativa2/README.md) servem como histórico, mas não serão copiados como resultados desta rodada. As quatro faces propostas — **Função, Contexto, Estrutura e Processo** — são testadas como radicais literais. Depois do recorte por gêmeos digitais, voltaremos a acrescentar cada face **uma por vez** e, quando útil, mediremos seu conjunto complementar.

O tema **gêmeos digitais** é parte central da investigação. A primeira bateria mediu o alcance dos radicais dos quatro pilares dentro do universo amplo de privacidade. A partir do resultado dessa bateria, o próximo conjunto de partida será `8 AND 3`: privacidade **e** `digital twin*`. As faces serão então reavaliadas nesse recorte, uma por vez.

## O que medimos

As chaves abaixo já existem no [montador de consultas](../../python/wos_query.py):

| Papel nesta rodada | Chave | Termos procurados em inglês |
| --- | --- | --- |
| Privacidade, conjunto de partida | `8` | `privac*`, `data protect*`, `personal data`, `personal information`, `personally identifiable information` |
| Gêmeos digitais | `3` | `digital twin*` |
| Função, termo literal | `0F` | `function*` |
| Contexto, termo literal | `0C` | `context*` |
| Estrutura, termo literal | `0E` | `structur*` |
| Processo, termo literal | `0P` | `process*` |

Os códigos `0F`, `0C`, `0E` e `0P` medem **presença das palavras** nos campos `TS=`. Eles não provam que um estudo discute conceitualmente uma face. Na triagem, descreveremos separadamente **o que a proteção busca alcançar** (Função), **em que ambiente ocorre** (Contexto), **quais componentes e relações existem** (Estrutura) e **como os dados são tratados** (Processo). As chaves temáticas `9`–`12` da Tentativa 2 poderão ajudar numa etapa posterior, sem misturar seus resultados com estes testes literais.

Na leitura dos artigos sobre gêmeos digitais, registrar também a **contraparte física ou real**: entidade representada, sensores/fontes de dados, fluxo entre os lados e informações pessoais envolvidas. Termos ingleses a observar incluem *physical twin*, *physical counterpart* e *real-world counterpart*. O [Digital Twin Consortium](https://www.digitaltwinconsortium.org/glossary/glossary/) usa *physical twin* para as entidades e processos do mundo real correspondentes a um gêmeo digital. Esses termos serão observados nos registros antes de decidir se entram em uma nova expressão; sua ausência literal não elimina um artigo.

## Sequência de trabalho

1. **Feito:** medir `8`, `8 AND 0F`, `8 NOT 0F`, os outros pilares isolados e cruzamentos de três e quatro pilares. Registrar totais da WoS e tamanho efetivo de cada CSV no [registro](registro-pesquisa.md).
2. **Próxima consulta, isoladamente:** medir `8 AND 3`. Registrar o total sob os mesmos filtros da WoS.
3. Depois dessa contagem, comparar `8 AND 3 AND 0` e `(8 AND 3) NOT 0`. A chave `0` usa `OR` entre os quatro radicais; `NOT 0` indica ausência literal dos quatro.
4. Com o tamanho desses conjuntos conhecido, decidir uma amostra pequena para títulos e resumos. Registrar evidência de privacidade e a relação entre o gêmeo digital e sua contraparte real.
5. Só após essa inspeção testar as faces individualmente dentro de `8 AND 3` e ampliar o vocabulário de gêmeos digitais, se surgirem termos adicionais úteis.

`8 NOT 0F` significa registros sobre privacidade **sem o radical `function*` nos campos pesquisados**. Não significa ausência conceitual de Função. O mesmo cuidado vale para as demais faces. O resultado `8` deve ser igual à soma dos resultados `8 AND 0F` e `8 NOT 0F` quando as três consultas usam os mesmos filtros e a mesma atualização da base.

Use a **Busca Avançada / Query Builder** da WoS. O campo `TS=` cobre título, resumo, palavras-chave dos autores e *Keywords Plus* ([campos da WoS](https://webofscience.zendesk.com/hc/en-us/articles/26916258216209-Web-of-Science-Core-Collection-Search-Fields)); a WoS aceita `AND`, `OR` e `NOT` para combinar conjuntos ([operadores](https://webofscience.zendesk.com/hc/en-us/articles/20016122409105-Search-Operators)).

Na raiz do projeto, gere cada consulta; o programa também sugere um nome caso haja exportação posterior:

```powershell
python -B python/wos_query.py --folder _wos/tentativa3 "8 AND 3"
```

O programa **não consulta a WoS**: copie a expressão impressa, execute-a na base e preencha o [registro da pesquisa](registro-pesquisa.md). Para esta etapa, **bastam as contagens**, sem CSV. Anote coleção/índices, anos, idioma, tipos de documento, outros filtros, modo *Exact Search*, data e hora; mantenha essas escolhas nas comparações. Se a inspeção indicar artigos promissores, uma exportação de **10 a 20 registros por conjunto** basta para a triagem inicial; o critério e a ordenação da amostra precisam ficar registrados. O [Manual 3](<../Manual 3/README.md>) receberá apenas fichas dos artigos selecionados, com indicação da consulta e, se houver, do CSV de origem.

| Ordem | Expressão no montador | Resultados WoS |
| ---: | --- | --- |
| | |
| | |
| | |
