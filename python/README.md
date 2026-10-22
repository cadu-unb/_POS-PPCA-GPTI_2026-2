# Montador de buscas da Web of Science

Requer apenas Python 3.10 ou superior. No terminal, a partir da raiz do projeto:

```powershell
python python/wos_query.py --list
python python/wos_query.py "((2 AND 3) AND 6) NOT (1 OR 5)"
```

O segundo comando imprime a expressão completa para colar na **busca avançada** da
Web of Science, com linhas vazias ao redor, e sugere pasta e nome para exportar
o CSV. Também é possível executar `python python/wos_query.py` sem
argumentos e digitar a combinação quando aparecer `Expressão:`.

A pasta sugerida é `_wos/tentativa1`. Para mudar:

```powershell
python python/wos_query.py --folder _wos/tentativa2 "8 AND 3"
```

O nome do arquivo usa as chaves e operadores, sem parênteses. Um hífen indica
um agrupamento; `__NOT_` indica exclusão. Por exemplo, `(2 AND 3) NOT 1`
vira `2AND3__NOT_1.csv`, e `((2 AND 3) AND 5) NOT 1` vira
`2AND3-AND5__NOT_1.csv`. O programa apenas
**sugere** esse nome; a exportação continua sendo feita na Web of Science.

As chaves e suas buscas `TS=` ficam no dicionário `QUERIES`, no começo de
`wos_query.py`. A chave `1` guarda o Contexto original para reproduzir os
resultados anteriores; a chave `7` contém uma versão corrigida para teste.
Use parênteses para deixar clara a ordem de `AND`, `OR` e `NOT`. Chaves ainda
não cadastradas geram erro em vez de uma busca incompleta.

As chaves `8` a `12` iniciam a rodada de Privacidade descrita em
[_wos/tentativa2/README.md](../_wos/tentativa2/README.md). Para essas buscas,
informe `--folder _wos/tentativa2`, pois a pasta padrão continua sendo
`_wos/tentativa1`.

## Filtros literais dos quatro pilares

As chaves opcionais abaixo procuram as **palavras** dos pilares em inglês.
Elas não são requisitos do tetraedro nem substituem a análise conceitual de
Função, Estrutura, Processo e Contexto.

| Chave | Consulta | Leitura |
| --- | --- | --- |
| `0` | `TS=(context* OR structur* OR process* OR function*)` | Pelo menos um dos quatro radicais |
| `0C` | `TS=(context*)` | Contexto |
| `0E` | `TS=(structur*)` | Estrutura |
| `0P` | `TS=(process*)` | Processo |
| `0F` | `TS=(function*)` | Função |

Exemplos para comparar uma busca já feita com seus subconjuntos:

```powershell
python -B python/wos_query.py --folder _wos/tentativa2 "3 AND 12 AND 0"
python -B python/wos_query.py --folder _wos/tentativa2 "3 AND 12 AND 0C"
python -B python/wos_query.py --folder _wos/tentativa2 "3 AND 12 AND 0P"
```

`0` usa `OR`: exige **ao menos um** radical, não os quatro. Para testar duas
faces simultaneamente, combine as chaves, por exemplo `0C AND 0P`. A ausência
dessas palavras no resultado não prova a ausência do pilar no artigo.
