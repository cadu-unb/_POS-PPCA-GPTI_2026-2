# P3D — versão LaTeX das entregas

Os seis documentos (relatório, pôster e lições, em português e inglês) em LaTeX, seguindo o que foi feito na P3A: classe `abntex2` em modo `article`, Latin Modern, A4 com margens 3/2/3/2 cm, lista de abreviaturas e siglas, referências numéricas. O conteúdo vem dos Markdown congelados em [`../MD/`](../MD/).

**Estado:** os arquivos foram escritos **sem compilar**. A primeira compilação pode mostrar erros de LaTeX ou de layout; o ajuste é feito nos `.tex`.

## Arquivos

| Arquivo | Conteúdo |
| --- | --- |
| `P3D_Privacidade2_Relatorio_PT.tex`, `P3D_Privacidade2_Report_EN.tex` | Relatório: capa, resumo e abstract, sumário, listas de ilustrações e de tabelas, lista de abreviaturas e siglas, seções 1 a 13, referências numeradas |
| `P3D_Privacidade2_Poster_PT.tex`, `P3D_Privacidade2_Poster_EN.tex` | Pôster A3 retrato, uma página: P1 e P2 lado a lado, P3 em largura total, caixas de limites e referências; bloco de autores e três referências |
| `P3D_Privacidade2_Licoes_PT.tex`, `P3D_Privacidade2_Lessons_EN.tex` | Lições aprendidas (uma a duas páginas) |
| `figuras/Fig1`, `Fig4`, `Fig5` (relatório) e `FigP1`, `FigP3` (pôster), `_PT` e `_EN` | Figuras em TikZ, uma por arquivo, no padrão da figura da P2B; as do pôster têm fontes maiores |
| `ferramentas/gerar_tex.py` | Gera o relatório, as lições e as figuras a partir dos Markdown |
| `compilar.sh` | Compila figuras e documentos |
| `out/` | PDFs e arquivos auxiliares (criada na compilação) |

**Figuras do relatório.** As Figuras 1, 4 e 5 são TikZ. A Figura 2 (mapa de calor 7 × 5) e a Figura 3 (matriz de princípios por domínios) são **tabelas coloridas** escritas dentro do relatório (pacote `colortbl`), então não têm PDF próprio. O pôster usa `FigP1` (relações entre as peças) e `FigP3` (concentrações, em largura total); o mapa de calor do pôster é uma tabela escrita no próprio arquivo.

## Como compilar (WSL)

Dentro de `_grupo/P3D/entregas/TEX/`:

```bash
bash compilar.sh            # figuras e documentos
bash compilar.sh figuras    # só as figuras
bash compilar.sh docs       # só os documentos
```

Cada documento é compilado duas vezes, para resolver sumário e listas. **As figuras precisam ser compiladas antes** dos documentos, porque eles incluem `out/FigN_PT.pdf`. Pacotes: `abntex2`, `tcolorbox`, `adjustbox`, `colortbl`, `longtable`, `lmodern`, `microtype` e `tikz` (os mesmos da P3A, mais `colortbl`).

## Regenerar a partir do Markdown

```bash
python ferramentas/gerar_tex.py
```

Isso **sobrescreve** o relatório, as lições e as figuras. Se você editar esses `.tex` à mão, guarde as edições antes. Os pôsteres não são gerados. O gerador é uma adaptação do da P3A (`../../../P3A/entregas/TEX/ferramentas/gerar_tex.py`).

## Pontos a preencher ou conferir

- **Integrantes do grupo:** a macro `\integrantes` na capa traz o texto provisório "[nomes dos integrantes do grupo]". Edite a linha `\newcommand{\integrantes}{...}` no preâmbulo de cada relatório.
- **Autores no pôster:** o bloco `\blocoautores`, no preâmbulo de cada pôster, usa o mesmo texto do pôster da P3A (Filipe Alves de Sousa e membros do Grupo Colégio Reciclagem 1; disciplina; código 3p2 / 3R31). Confirme se vale para a P3D.
- **Pôster em uma página:** o conteúdo fica em uma caixa única envolvida por `adjustbox`, que reduz tudo proporcionalmente se passar de uma página. O tamanho do texto está em `\corpo`.
- **Capa:** segue a da P2B (universidade, programa, disciplina e professor).
- **Citações numéricas:** cada referência tem um número definido por `\defref{chave}{n}` no preâmbulo (ordem alfabética da lista). Em inglês, a numeração difere da do português porque "European Union" ordena antes de ISO.
- **Declaração de uso de IA:** **não** foi incluída. O plano em `../../plano-abordagem.md` (seção 12) descreve como inserir o aviso e o ambiente LaTeX que o liga e desliga.
- **Figuras:** os esboços Mermaid do Markdown foram redesenhados em TikZ. Confira o resultado visual na primeira compilação.
