# GPTI 2026/2 — Gestão de Projetos de TI (PPCA/UnB)

Material, pesquisa bibliográfica e entregas do grupo na disciplina PPCA0006. O tema é o gêmeo digital de componentes do sistema de resíduos sólidos, com foco em privacidade (domínio SIPA do PMBOK 8).

## Mapa das pastas

| Pasta | Conteúdo |
| --- | --- |
| `_grupo/` | Entregas por grupo: `P2A`, `P2B`, `P3A`, `P3D`; o resumo da página do curso (`_aprender3/`); `GptiGrupos2026SR.docx` |
| `_wos/` | Pesquisa na Web of Science: buscas (`tentativa1` a `tentativa3`), fichas dos artigos (`Manual 1` a `Manual 3`), referências (`referencias.bib`, `referencias-abnt.md`) |
| `documentos/` | Material de apoio da disciplina e normas (PMBOK 8, SIPA, SRS, Manual Oslo, Agenda 2030, CMMI, PAEE/ALE) |
| `perguntas/` | Questionários e respostas (`parte1`, `parte2`) |
| `_trabalho/` | Orientação atual e palavras-chave de busca |
| `prompt/` | Prompts reutilizáveis |
| `python/` | Scripts de apoio (veja `python/README.md`) |

Cada pasta de conteúdo tem seu próprio `README.md` quando precisa de explicação.

## Convenções

- **PDF e Markdown.** O PDF original e o `.md` convertido ficam lado a lado, exceto em `_wos/Manual 3/artigos/`, onde ficam em `pdf/` e `md/`. Para leitura e busca, usar sempre o `.md` (veja `documentos/README.md`).
- **Documentos compartilhados** ficam no nível de `documentos/`, não dentro de uma pasta de questionário ou de entrega.
- **Entregas em LaTeX.** Os arquivos auxiliares e o PDF vão para `out/` dentro da pasta da entrega, por exemplo `pdflatex -output-directory=out -interaction=nonstopmode arquivo.tex`, rodando duas vezes para resolver as referências cruzadas. Figuras geradas ficam em `out/` e são incluídas a partir dali.
- **Versões antigas** não se guardam na árvore: o histórico do Git as preserva.
- **Temporários** (`.aux`, `.log`, `__pycache__`, arquivos de bloqueio do Office e similares) são ignorados pelo `.gitignore`.

## Scripts

```powershell
python -m pip install -r python/requirements.txt
python python/wos_query.py --list
python python/nomes_artigos.py --list
python python/xls_to_csv.py _wos/tentativa3/saida_wos
```

O `python/README.md` descreve cada script (`wos_query.py`, `nomes_artigos.py`, `xls_to_csv.py`, `pdf_to_md.py`).
