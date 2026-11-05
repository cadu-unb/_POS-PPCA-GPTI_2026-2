# P3A — versão LaTeX das entregas

Os seis documentos (relatório, pôster e lições, em português e inglês) em LaTeX, no estilo da entrega P2B: classe `abntex2` em modo `article`, Latin Modern, A4 com margens 3/2/3/2 cm. O conteúdo vem dos Markdown congelados em [`../MD/`](../MD/).

**Estado:** os arquivos foram escritos **sem compilar**. A primeira compilação pode mostrar erros de LaTeX ou de layout; o ajuste é feito nos `.tex`.

## Arquivos

| Arquivo | Conteúdo |
| --- | --- |
| `P3A_Privacidade2_Relatorio_PT.tex`, `P3A_Privacidade2_Report_EN.tex` | Relatório: capa, resumo e abstract, sumário, listas de ilustrações e de tabelas, lista de abreviaturas e siglas, seções 1 a 10, referências numeradas |
| `P3A_Privacidade2_Poster_PT.tex`, `P3A_Privacidade2_Poster_EN.tex` | Pôster A1 retrato, duas colunas, três figuras |
| `P3A_Privacidade2_Licoes_PT.tex`, `P3A_Privacidade2_Lessons_EN.tex` | Lições aprendidas (uma a duas páginas) |
| `figuras/Fig1..Fig5_PT.tex` e `_EN.tex` | Figuras em TikZ, uma por arquivo, no padrão da figura da P2B |
| `ferramentas/gerar_tex.py` | Gera o relatório, as lições e as figuras a partir dos Markdown |
| `compilar.sh` | Compila figuras e documentos |
| `out/` | PDFs e arquivos auxiliares (criada na compilação) |

Os pôsteres são escritos à mão; o gerador não os altera. Eles usam `Fig1`, `Fig2` e `Fig4` (a figura 3 do pôster é a figura 4 do relatório).

## Como compilar (WSL)

Dentro de `_grupo/P3A/entregas/TEX/`:

```bash
bash compilar.sh            # figuras e documentos
bash compilar.sh figuras    # só as figuras
bash compilar.sh docs       # só os documentos
```

Cada documento é compilado duas vezes, para resolver sumário e listas. A compilação manual, como na P2B:

```bash
pdflatex -output-directory=out -interaction=nonstopmode figuras/Fig1_PT.tex
pdflatex -output-directory=out -interaction=nonstopmode P3A_Privacidade2_Relatorio_PT.tex
```

**As figuras precisam ser compiladas antes** dos documentos, porque os documentos incluem `out/FigN_PT.pdf`. Pacotes necessários: `abntex2`, `tcolorbox`, `longtable`, `lmodern`, `microtype` e `tikz` (os mesmos já usados na P2B, mais `tcolorbox`, de `texlive-latex-extra`).

## Regenerar a partir do Markdown

```bash
python ferramentas/gerar_tex.py
```

Isso **sobrescreve** o relatório, as lições e as figuras. Se você editar esses `.tex` à mão, não rode o gerador sem antes guardar as edições. O conteúdo de cada documento é o do Markdown correspondente; os pôsteres não são gerados.

## Pontos a preencher ou conferir

- **Integrantes do grupo:** a macro `\integrantes` na capa traz o texto provisório "[nomes dos integrantes do grupo]". Edite a linha `\newcommand{\integrantes}{...}` no preâmbulo de cada relatório.
- **Capa:** segue a da P2B (universidade, programa, disciplina e professor). Ajuste se o grupo preferir outro formato.
- **Citações numéricas:** cada referência tem um número definido por `\defref{chave}{n}` no preâmbulo (ordem alfabética da lista). Para reordenar a lista, altere os números e a ordem dos `\refitem` no fim do arquivo.
- **Pôster:** o tamanho do texto está em `\corpo`. A página pode precisar de ajuste fino se algum bloco ficar maior que o previsto.
- **Declaração de uso de IA:** **não** foi incluída. O plano em `../../plano-abordagem.md` (seção 11) descreve como inserir o aviso e o ambiente LaTeX que o liga e desliga.
- **Figuras:** os esboços Mermaid do Markdown foram redesenhados em TikZ. Confira o resultado visual na primeira compilação.
