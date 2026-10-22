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
