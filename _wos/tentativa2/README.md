# Tentativa 2 — tetraedro de Privacidade

**Início:** 22/10/2026, 18h45 (horário de Brasília).  
**Situação:** roteiro pronto; contagens da WoS ainda não coletadas.

Nesta rodada, o **volume** do tetraedro é **Privacidade**. Usaremos Função, Estrutura, Processo e Contexto como lentes para descrever os artigos, seguindo o método registrado em [Consolidação 1](<../Consolidação 1/README.md>). Não exigiremos que um artigo contenha as quatro faces como termos de busca. O cruzamento com o volume **Reciclagem** virá depois de entendermos os resultados deste volume.

| Face | Pergunta para a futura triagem |
| --- | --- |
| Função | Que proteção, controle ou autonomia sobre dados pessoais se pretende obter? |
| Estrutura | Quais atores, sistemas, fluxos de dados e regras de acesso estão envolvidos? |
| Processo | Como os dados são coletados, usados, compartilhados, retidos, anonimizados ou excluídos? |
| Contexto | Quais normas, organizações e tecnologias moldam o problema? |

## Blocos numerados

As chaves `1` a `7` continuam reservadas à rodada de Reciclagem. Acrescentamos as chaves `8` a `12` ao [montador de consultas](../../python/wos_query.py), sem alterar as antigas.

**8 — Núcleo do volume: privacidade e dados pessoais**

```text
TS=(privac* OR "data protect*" OR "personal data" OR "personal information" OR "personally identifiable information")
```

**9 — Função: proteção e minimização**

```text
TS=("privacy preserv*" OR "privacy protect*" OR "privacy by design" OR "data minimiz*" OR "data minimis*" OR anonymiz* OR anonymis* OR pseudonymiz* OR pseudonymis*)
```

**10 — Estrutura: governança e circulação dos dados**

```text
TS=("data govern*" OR "data steward*" OR "data ecosystem*" OR "data flow*" OR "data shar*" OR "access control")
```

**11 — Processo: ciclo de vida dos dados**

```text
TS=("data collect*" OR "data process*" OR "data stor*" OR "data retention" OR "data delet*" OR "consent manag*" OR "privacy impact assess*" OR "data protection impact assess*")
```

**12 — Contexto: proteção de dados na regulação**

```text
TS=(LGPD OR GDPR OR "Lei Geral de Proteção de Dados" OR "General Data Protection Regulation" OR "Brazilian General Data Protection Law" OR "privacy regulat*" OR "data protection law*")
```

Estes blocos são **exploratórios**. Termos como *data protection* e *access control* podem trazer estudos mais ligados a segurança do que a privacidade de pessoas; a amostra de títulos e resumos indicará se precisam ser refinados. A busca `TS=` cobre título, resumo, palavras-chave dos autores e *Keywords Plus* na WoS Core Collection, o que também pode trazer resultados apenas tangenciais ([documentação da WoS](https://webofscience.zendesk.com/hc/en-us/articles/26916347018257-Web-of-Science-Core-Collection-Advanced-Search-Field-Tags)).

## Primeira rodada: medir quantidade

Execute as consultas abaixo **na mesma coleção, intervalo de anos e filtros**. Anote o total exibido pela WoS. Primeiro medimos o volume e cada face separadamente; depois testamos sua relação com gêmeos digitais (`3`), IoT (`4`) e regulação (`12`). Nesta rodada não incluímos os blocos de Reciclagem.

| Ordem | Expressão para o montador | Resultados WoS |
| ---: | --- | ---: |
| 1 | `8` | a preencher |
| 2 | `9` | a preencher |
| 3 | `10` | a preencher |
| 4 | `11` | a preencher |
| 5 | `12` | a preencher |
| 6 | `8 AND 3` | a preencher |
| 7 | `8 AND 4` | a preencher |
| 8 | `8 AND 12` | a preencher |
| 9 | `3 AND 12` | a preencher |

Na raiz do projeto, use o montador para obter a expressão completa e o nome sugerido do CSV. **Informe `--folder`**, pois o padrão do programa ainda é `tentativa1`:

```powershell
python -B python/wos_query.py --list
python -B python/wos_query.py --folder _wos/tentativa2 '8 AND 3'
```

O nome sugerido para esse exemplo é `8AND3.csv`. O programa não consulta nem exporta da WoS; cole a expressão impressa na busca avançada e registre a contagem. A WoS usa `AND`, `OR`, `NOT` e parênteses para combinar termos e conjuntos ([orientação oficial](https://webofscience.zendesk.com/hc/en-us/articles/20130361503249-Advanced-Search-Query-Builder)).

**Retorno esperado nesta etapa:** as nove contagens, a coleção consultada, o intervalo de anos e quaisquer filtros ativos. A partir disso, escolheremos cruzamentos adicionais e uma amostra pequena de títulos e resumos para avaliar pertinência antes de exportar um corpus maior.
