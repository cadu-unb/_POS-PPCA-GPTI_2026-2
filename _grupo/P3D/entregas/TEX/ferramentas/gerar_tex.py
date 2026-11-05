"""Gera os .tex da P3D a partir dos Markdown congelados em ../MD.

Uso (a partir de _grupo/P3D/entregas/TEX):
    python ferramentas/gerar_tex.py

Gera: relatório PT/EN, lições PT/EN e as figuras TikZ (Fig1, Fig4, Fig5 e FigP1) em figuras/.
As figuras 2 (mapa 7 x 5) e 3 (matriz 6 x 7) são tabelas coloridas dentro do próprio relatório.
Os pôsteres (PT/EN) são escritos à mão; este script não os toca.
O script NÃO compila nada. A compilação é feita pelo grupo (ver README.md).
Baseado em ../../../P3A/entregas/TEX/ferramentas/gerar_tex.py.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

TEX = Path(__file__).resolve().parent.parent
MD = TEX.parent / "MD"

L = {
    "pt": {
        "md_report": "P3D_Privacidade2_Relatorio_PT.md", "md_lessons": "P3D_Privacidade2_Licoes_PT.md",
        "out_report": "P3D_Privacidade2_Relatorio_PT.tex", "out_lessons": "P3D_Privacidade2_Licoes_PT.tex",
        "docopts": "english,brazil", "kw": "Palavras-chave", "source": "Fonte", "fig_dir": "_PT",
        "contents": "SUMÁRIO", "listfig": "LISTA DE ILUSTRAÇÕES", "listtab": "LISTA DE TABELAS",
        "siglas": "LISTA DE ABREVIATURAS E SIGLAS", "refs_title": "REFERÊNCIAS", "nota": "Nota de natureza",
        "cover": r"UNIVERSIDADE DE BRASÍLIA -- UNB\\PROGRAMA DE PÓS-GRADUAÇÃO EM COMPUTAÇÃO APLICADA -- PPCA\\DISCIPLINA: GESTÃO DE PROJETOS DE TI (GPTI)\\PROFESSOR: Dr. JOÃO MELLO DA SILVA",
        "group_label": "Grupo SIPA Privacidade 2", "cover_city": r"BRASÍLIA -- DF\\2026",
        "title_caps": "PMBOK 8: PRINCÍPIOS, ÁREAS DE FOCO, DOMÍNIOS E ADAPTAÇÃO SOB MEDIDA",
        "legend_bands": "Faixas: azul = dimensão proativa; turquesa = dimensão de responsabilidade; cinza = dimensão orientada a valor.",
        "src_prefix": r"^Fonte:\s*", "src_prefix2": r"^Fonte dos ",
    },
    "en": {
        "md_report": "P3D_Privacidade2_Report_EN.md", "md_lessons": "P3D_Privacidade2_Lessons_EN.md",
        "out_report": "P3D_Privacidade2_Report_EN.tex", "out_lessons": "P3D_Privacidade2_Lessons_EN.tex",
        "docopts": "brazil,english", "kw": "Keywords", "source": "Source", "fig_dir": "_EN",
        "contents": "CONTENTS", "listfig": "LIST OF FIGURES", "listtab": "LIST OF TABLES",
        "siglas": "LIST OF ABBREVIATIONS AND ACRONYMS", "refs_title": "REFERENCES", "nota": "Nature of the work",
        "cover": r"UNIVERSITY OF BRASÍLIA -- UnB\\GRADUATE PROGRAM IN APPLIED COMPUTING -- PPCA\\COURSE: IT PROJECT MANAGEMENT (GPTI)\\PROFESSOR: Dr. JOÃO MELLO DA SILVA",
        "group_label": "SIPA Privacy 2 Group", "cover_city": r"BRASÍLIA -- DF\\2026",
        "title_caps": "PMBOK 8: PRINCIPLES, FOCUS AREAS, PERFORMANCE DOMAINS AND TAILORING",
        "legend_bands": "Bands: blue = proactive dimension; turquoise = ownership dimension; gray = value-driven dimension.",
        "src_prefix": r"^Source:\s*", "src_prefix2": r"^Source of the ",
    },
}

# Legendas das 14 tabelas comuns (as tabelas do mapa 7x5 e da matriz 6x7 são figuras)
TABLE_CAPTIONS = {
    "pt": [
        ("Estrutura do PMBOK 8: Standard e Guide", r"Elaborado pelos autores (2026), com base em \cit{pmi}."),
        ("Dimensões da mentalidade e princípios", r"Elaborado pelos autores (2026), com base em \cit{pmi}."),
        ("Perguntas práticas e consequências de cada princípio", r"Elaborado pelos autores (2026), com base em \cit{pmi}."),
        ("Abordagens de desenvolvimento: preditiva, adaptativa e híbrida", r"Elaborado pelos autores (2026), com base em \cit{pmi}."),
        ("Fatores de escolha da abordagem de desenvolvimento", r"Elaborado pelos autores (2026), com base em \cit{pmi}."),
        ("As cinco áreas de foco", r"Elaborado pelos autores (2026), com base em \cit{pmi}."),
        ("Contagem de processos por área de foco", r"Elaborado pelos autores (2026), a partir de \cit{pmi}."),
        ("Inventário dos 40 processos do PMBOK 8", r"Elaborado pelos autores (2026), com base em \cit{pmi}; a concentração é o agrupamento analítico deste trabalho."),
        ("Consideração de adaptação característica de cada domínio", r"Elaborado pelos autores (2026), com base em \cit{pmi}."),
        ("Exemplos hipotéticos das cinco operações sobre processos", "Elaborado pelos autores (2026); exemplos ilustrativos, não prescrições do PMBOK 8."),
        ("Situações comuns e sugestões de adaptação", r"Elaborado pelos autores (2026), com base em \cit{pmi}."),
        ("Concentrações analíticas e contagem de processos", "Elaborado pelos autores (2026)."),
        ("Pontos do PMBOK 8 que tocam dados pessoais", r"Elaborado pelos autores (2026), com base em \cit{pmi}."),
        ("Relatório final do trabalho", r"Elaborado pelos autores (2026), no formato do \textit{Final report} de \cit{pmi}."),
    ],
    "en": [
        ("Structure of PMBOK 8: Standard and Guide", r"Prepared by the authors (2026), based on \cit{pmi}."),
        ("Mindset dimensions and principles", r"Prepared by the authors (2026), based on \cit{pmi}."),
        ("Practical questions and consequences of each principle", r"Prepared by the authors (2026), based on \cit{pmi}."),
        ("Development approaches: predictive, adaptive and hybrid", r"Prepared by the authors (2026), based on \cit{pmi}."),
        ("Factors for choosing the development approach", r"Prepared by the authors (2026), based on \cit{pmi}."),
        ("The five Focus Areas", r"Prepared by the authors (2026), based on \cit{pmi}."),
        ("Process count by Focus Area", r"Prepared by the authors (2026), from \cit{pmi}."),
        ("Inventory of the 40 PMBOK 8 processes", r"Prepared by the authors (2026), based on \cit{pmi}; the concentration is the analytical grouping of this work."),
        ("Characteristic tailoring consideration of each domain", r"Prepared by the authors (2026), based on \cit{pmi}."),
        ("Hypothetical examples of the five operations on processes", "Prepared by the authors (2026); illustrative examples, not PMBOK 8 prescriptions."),
        ("Common situations and tailoring suggestions", r"Prepared by the authors (2026), based on \cit{pmi}."),
        ("Analytical concentrations and process count", "Prepared by the authors (2026)."),
        ("PMBOK 8 points that touch personal data", r"Prepared by the authors (2026), based on \cit{pmi}."),
        ("Final report of the work", r"Prepared by the authors (2026), following the \textit{Final report} format of \cit{pmi}."),
    ],
}

# (sigla, PT, EN)
SIGLAS = [
    ("1AHV", "\\textit{Adopt a Holistic View}: adotar uma visão holística", "Adopt a Holistic View"),
    ("2FOV", "\\textit{Focus on Value}: focar em valor", "Focus on Value"),
    ("3QPD", "\\textit{Embed Quality Into Processes and Deliverables}: embutir qualidade em processos e entregas", "Embed Quality Into Processes and Deliverables"),
    ("4BAL", "\\textit{Be an Accountable Leader}: ser um líder responsável", "Be an Accountable Leader"),
    ("5SPA", "\\textit{Integrate Sustainability Within All Project Areas}: integrar sustentabilidade em todas as áreas do projeto", "Integrate Sustainability Within All Project Areas"),
    ("6BEC", "\\textit{Build an Empowered Culture}: construir uma cultura empoderada", "Build an Empowered Culture"),
    ("A, S, I, P", "Temas em análise fora do PMI: análise de negócios, sustentabilidade, inovação e privacidade", "Themes under analysis outside PMI: business analysis, sustainability, innovation and privacy"),
    ("CL", "Encerramento (\\textit{Closing}), área de foco", "Closing Focus Area"),
    ("EX", "Execução (\\textit{Executing}), área de foco", "Executing Focus Area"),
    ("FI", "Domínio Finanças (\\textit{Finance})", "Finance domain"),
    ("GDPR", "\\textit{General Data Protection Regulation} (Regulamento Geral sobre a Proteção de Dados)", "General Data Protection Regulation"),
    ("GO", "Domínio Governança (\\textit{Governance})", "Governance domain"),
    ("IA", "Inteligência artificial", "Artificial intelligence (AI)"),
    ("IN", "Iniciação (\\textit{Initiating}), área de foco", "Initiating Focus Area"),
    ("ISO", "\\textit{International Organization for Standardization}", "International Organization for Standardization"),
    ("MC", "Monitoramento e controle (\\textit{Monitoring and Controlling}), área de foco", "Monitoring and Controlling Focus Area"),
    ("PL", "Planejamento (\\textit{Planning}), área de foco", "Planning Focus Area"),
    ("PMBOK", "\\textit{Project Management Body of Knowledge}", "Project Management Body of Knowledge"),
    ("PMI", "\\textit{Project Management Institute}", "Project Management Institute"),
    ("PMO", "Escritório de projetos (\\textit{Project Management Office})", "Project Management Office"),
    ("RE", "Domínio Recursos (\\textit{Resources})", "Resources domain"),
    ("RI", "Domínio Riscos (\\textit{Risk})", "Risk domain"),
    ("SH", "Domínio Cronograma (\\textit{Schedule})", "Schedule domain"),
    ("SIPA", "Sustentabilidade, Inovação, Privacidade e Análise de negócios com decisões ajustadas a riscos", "Sustainability, Innovation, Privacy and Business analysis with risk-adjusted decisions"),
    ("SO", "Domínio Escopo (\\textit{Scope})", "Scope domain"),
    ("SOX", "\\textit{Sarbanes-Oxley Act}", "Sarbanes-Oxley Act"),
    ("ST", "Domínio Partes Interessadas (\\textit{Stakeholders})", "Stakeholders domain"),
    ("TIC", "Tecnologia da informação e comunicação", "Information and communication technology (ICT)"),
]

REF_KEYS = [
    (r"^ISO", "iso"), (r"^MANZOOR", "manzoor"), (r"^NOLL", "noll"), (r"^PMI", "pmi"), (r"^REED", "reed"),
    (r"^SILVIUS-ZUCHI", "silvius"), (r"^(UNIÃO EUROPEIA|EUROPEAN UNION)", "gdpr"),
]

UNI = {"→": r"\ensuremath{\rightarrow}", "…": r"\ldots{}", "≥": r"\ensuremath{\geq}", "≤": r"\ensuremath{\leq}",
       "≠": r"\ensuremath{\neq}", "×": r"\ensuremath{\times}"}
ESC = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}


def esc_plain(s: str) -> str:
    out = []
    for ch in s:
        out.append(ESC.get(ch) or UNI.get(ch) or ch)
    s = "".join(out)
    parts = s.split('"')
    if len(parts) > 1 and len(parts) % 2 == 1:
        s = parts[0]
        for i, p in enumerate(parts[1:], start=1):
            s += (r"\textquotedblleft{}" if i % 2 == 1 else r"\textquotedblright{}") + p
    return s


class Ctx:
    def __init__(self, keymap, ref_mode=False):
        self.keymap, self.ref_mode = keymap, ref_mode


INLINE = re.compile(r"\*\*(.+?)\*\*|\*(.+?)\*|\[(\d+(?:,\s*\d+)*)(?:,\s*([^\]]+))?\]")


def inline(s: str, ctx: Ctx) -> str:
    pos, out = 0, []
    for m in INLINE.finditer(s):
        out.append(esc_plain(s[pos:m.start()]))
        if m.group(1) is not None:
            out.append(r"\textbf{" + inline(m.group(1), ctx) + "}")
        elif m.group(2) is not None:
            out.append((r"\textbf{" if ctx.ref_mode else r"\textit{") + inline(m.group(2), ctx) + "}")
        else:
            nums = [int(x) for x in re.split(r",\s*", m.group(3))]
            refs = ", ".join(r"\refnum{%s}" % ctx.keymap[n] for n in nums)
            loc = (", " + inline(m.group(4), ctx)) if m.group(4) else ""
            out.append("[" + refs + loc + "]")
        pos = m.end()
    out.append(esc_plain(s[pos:]))
    return "".join(out)


def parse_blocks(text: str):
    lines = text.split("\n")
    blocks, i, n = [], 0, len(lines)
    while i < n:
        ln = lines[i]
        if ln.startswith("```"):
            j = i + 1
            while j < n and not lines[j].startswith("```"):
                j += 1
            blocks.append(("fence", ln[3:].strip(), "\n".join(lines[i + 1:j])))
            i = j + 1
        elif ln.startswith("<!--"):
            j = i
            while j < n and "-->" not in lines[j]:
                j += 1
            blocks.append(("comment", "\n".join(lines[i:j + 1])))
            i = j + 1
        elif ln.startswith("#"):
            lvl = len(ln) - len(ln.lstrip("#"))
            blocks.append(("h", lvl, ln[lvl:].strip()))
            i += 1
        elif ln.startswith("|"):
            j = i
            while j < n and lines[j].startswith("|"):
                j += 1
            blocks.append(("table", [[c.strip() for c in r.strip().strip("|").split("|")] for r in lines[i:j]]))
            i = j
        elif ln.strip() == "---" or not ln.strip():
            i += 1
        else:
            j, buf = i, []
            while j < n and lines[j].strip() and not lines[j].startswith(("#", "|", "```", "<!--")) and lines[j].strip() != "---":
                buf.append(lines[j])
                j += 1
            blocks.append(("p", buf))
            i = j
    return blocks


def para_text(buf, ctx):
    parts = []
    for k, ln in enumerate(buf):
        hard = ln.endswith("  ") and k < len(buf) - 1
        parts.append(inline(ln.strip(), ctx) + (r"\\" if hard else ""))
    return " ".join(parts)


def strip_num(title):
    return re.sub(r"^\d+(\.\d+)*\.?\s+", "", title)


def parse_refs(blocks):
    idx = next(i for i, b in enumerate(blocks) if b[0] == "h" and b[1] == 2 and b[2] in ("Referências", "References"))
    items = []
    for b in blocks[idx + 1:]:
        if b[0] == "p":
            txt = " ".join(x.strip() for x in b[1])
            m = re.match(r"^\[(\d+)\]\s+(.*)$", txt)
            if m:
                items.append((int(m.group(1)), m.group(2)))
    keymap = {}
    for n, txt in items:
        for pat, key in REF_KEYS:
            if re.search(pat, txt):
                keymap[n] = key
                break
        else:
            raise SystemExit(f"Referência sem chave: {txt[:60]}")
    return idx, items, keymap


# ---------------------------------------------------------------------------
# Tabelas
# ---------------------------------------------------------------------------
def table_tex(rows, cap, ctx, label):
    header, body = rows[0], rows[2:]
    nc = len(header)
    lens = []
    for c in range(nc):
        vals = [len(re.sub(r"[*\[\]]", "", r[c])) for r in body if c < len(r)] + [len(header[c])]
        lens.append(max(6, sum(vals) / len(vals)) ** 0.75)
    tot = sum(lens)
    w = [int(round(1000 * x / tot)) for x in lens]
    w[-1] += 1000 - sum(w)
    right = [bool(re.match(r"^[-:]+:$", rows[1][c].strip())) for c in range(nc)]
    align = [r"\raggedleft\arraybackslash" if right[c] else r"\raggedright\arraybackslash" for c in range(nc)]
    colspec = "@{}" + "".join(
        r">{%s}p{\dimexpr(\linewidth-%d\tabcolsep)*%d/1000\relax}" % (align[c], 2 * (nc - 1), x) for c, x in enumerate(w)
    ) + "@{}"
    hdr = " & ".join(r"\textbf{" + inline(h, ctx) + "}" for h in header) + r"\\"
    size = r"\footnotesize" if nc >= 4 else r"\small"
    out = [r"\begingroup\SingleSpacing" + size, r"\begin{longtable}{" + colspec + "}",
           r"\caption{" + cap[0] + r"}\label{tab:" + label + r"}\\", r"\hline", hdr, r"\hline", r"\endfirsthead",
           r"\hline", hdr, r"\hline", r"\endhead", r"\hline", r"\endfoot", r"\hline", r"\endlastfoot"]
    for r in body:
        out.append(" & ".join(inline(c, ctx) for c in r) + r"\\[3pt]")
    out += [r"\end{longtable}", r"\endgroup", r"\fontetab{" + cap[1] + "}"]
    return "\n".join(out)


def heat_tabular(rows, ctx):
    """Mapa 7 x 5: células sombreadas pela contagem; linha e coluna de total sem sombra."""
    header, body = rows[0], rows[2:]
    nc = len(header)
    spec = "@{}l" + "r" * (nc - 1) + "@{}"
    out = [r"\begin{tabular}{" + spec + "}", r"\hline",
           " & ".join(r"\textbf{" + inline(h, ctx) + "}" for h in header) + r"\\", r"\hline"]
    for k, r in enumerate(body):
        is_total = k == len(body) - 1
        cells = []
        for c, cell in enumerate(r):
            txt = inline(cell, ctx)
            num = re.sub(r"[*\s]", "", cell)
            if not is_total and 0 < c < nc - 1 and num.isdigit():
                pct = 11 * int(num)
                if pct > 0:
                    txt = r"\cellcolor{exLine!%d}%s" % (pct, txt)
            cells.append(txt)
        if is_total:
            out.append(r"\hline")
        out.append(" & ".join(cells) + r"\\")
    out += [r"\hline", r"\end{tabular}"]
    return "\n".join(out)


BAND = ["bandaProativa", "bandaValor", "bandaProativa", "bandaResp", "bandaValor", "bandaResp"]  # 1AHV 2FOV 3QPD 4BAL 5SPA 6BEC


def matrix_tabular(rows, ctx):
    """Matriz 6 x 7: três faixas de cor por dimensão da mentalidade."""
    header, body = rows[0], rows[2:]
    nc = len(header)
    first = 130
    rest = (1000 - first) // (nc - 1)
    ws = [first] + [rest] * (nc - 1)
    ws[-1] += 1000 - sum(ws)
    spec = "@{}" + "".join(
        r">{\raggedright\arraybackslash}p{\dimexpr(\linewidth-%d\tabcolsep)*%d/1000\relax}" % (2 * (nc - 1), x) for x in ws
    ) + "@{}"
    out = [r"\begin{tabular}{" + spec + "}", r"\hline",
           " & ".join(r"\textbf{" + inline(h, ctx) + "}" for h in header) + r"\\", r"\hline"]
    for k, r in enumerate(body):
        out.append(r"\rowcolor{%s}" % BAND[k] + " & ".join(inline(c, ctx) for c in r) + r"\\")
    out += [r"\hline", r"\end{tabular}"]
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Preâmbulo, capa, siglas
# ---------------------------------------------------------------------------
def preamble(lang, keymap, title_comment):
    c = L[lang]
    defs = "\n".join(r"\defref{%s}{%d}" % (k, n) for n, k in sorted(keymap.items()))
    return rf"""% =============================================================================
% {title_comment}
% Formatação: ABNT (classe abnTeX2, modo article), A4, Latin Modern, 12 pt,
% margens 3/2/3/2 cm, espaçamento 1,5, recuo de parágrafo 1,25 cm.
% Figuras esperadas em out/ (compiladas a partir de figuras/):
%   Fig1{c['fig_dir']}.pdf, Fig4{c['fig_dir']}.pdf, Fig5{c['fig_dir']}.pdf
% (as figuras 2 e 3 são tabelas coloridas escritas neste arquivo).
% ARQUIVO GERADO por ferramentas/gerar_tex.py a partir de ../MD. Para mudar o
% conteúdo, edite o Markdown e gere de novo, ou edite este .tex diretamente.
% =============================================================================
\documentclass[12pt,a4paper,article,oneside,{c['docopts']}]{{abntex2}}

\usepackage[T1]{{fontenc}}
\usepackage[utf8]{{inputenc}}
\usepackage{{lmodern}}           % Latin Modern (fonte padrão do LaTeX, com T1)
\usepackage{{amsmath}}
\usepackage{{graphicx}}
\usepackage{{xcolor}}
\usepackage{{array}}
\usepackage{{colortbl}}
\usepackage{{tabularx}}
\usepackage{{longtable}}
\usepackage[expansion=false]{{microtype}}
\usepackage{{url}}
\Urlmuskip=0mu plus 1mu\relax

% Margens ABNT: superior 3 cm, inferior 2 cm, esquerda 3 cm, direita 2 cm
\setlrmarginsandblock{{3cm}}{{2cm}}{{*}}
\setulmarginsandblock{{3cm}}{{2cm}}{{*}}
\checkandfixthelayout

\setlength{{\parindent}}{{1.25cm}}
\setlength{{\parskip}}{{0pt}}
\setlength{{\emergencystretch}}{{3em}}
\setcounter{{secnumdepth}}{{3}}
\setcounter{{tocdepth}}{{3}}
\renewcommand{{\contentsname}}{{{c['contents']}}}
\renewcommand{{\listfigurename}}{{{c['listfig']}}}
\renewcommand{{\listtablename}}{{{c['listtab']}}}

% Cores das figuras-tabela (mapa de calor e matriz de princípios)
\definecolor{{exLine}}{{RGB}}{{23,54,93}}
\definecolor{{bandaProativa}}{{RGB}}{{220,233,247}}
\definecolor{{bandaResp}}{{RGB}}{{200,240,236}}
\definecolor{{bandaValor}}{{RGB}}{{238,242,245}}

% Tabelas: sem filetes verticais (padrão IBGE adotado pela ABNT)
\renewcommand{{\arraystretch}}{{1.2}}

% Fonte abaixo de tabelas e figuras (ABNT NBR 14724)
\newcommand{{\fontetab}}[1]{{\par\vspace{{3pt}}{{\small\noindent {c['source']}: #1\par}}}}

% Citações numéricas: o número de cada referência é definido uma vez (ordem
% alfabética da lista) e usado por \refnum{{chave}}, \cit{{chave}} e \refitem.
\newcommand{{\defref}}[2]{{\expandafter\gdef\csname refnum@#1\endcsname{{#2}}}}
\newcommand{{\refnum}}[1]{{\csname refnum@#1\endcsname}}
\newcommand{{\cit}}[1]{{[\refnum{{#1}}]}}
\newcommand{{\refitem}}[2]{{\par\noindent\hangindent=1.2cm\hangafter=1\makebox[1.2cm][l]{{[\refnum{{#1}}]}}#2\par}}
{defs}

% Integrantes do grupo (preencher; a capa usa esta macro)
\newcommand{{\integrantes}}{{[nomes dos integrantes do grupo]}}
"""


def cover(lang):
    c = L[lang]
    return rf"""% ------------------------------- CAPA ----------------------------------------
\thispagestyle{{empty}}
\noindent\begin{{minipage}}[t][0.92\textheight]{{\textwidth}}
\centering
\SingleSpacing
\textbf{{{c['cover']}}}

\vspace{{1cm}}

\textbf{{{c['group_label']}}}: \integrantes

\vspace{{3cm}}

\textbf{{{c['title_caps']}}}

\vfill

{c['cover_city']}
\end{{minipage}}
\clearpage
"""


def siglas_block(lang):
    idx = 1 if lang == "pt" else 2
    rows = "\n".join(r"\textbf{%s} & %s\\[2pt]" % (s[0], s[idx]) for s in SIGLAS)
    return rf"""
\begingroup
\SingleSpacing
\begin{{center}}\textbf{{{L[lang]['siglas']}}}\end{{center}}
\small
\begin{{longtable}}{{@{{}}>{{\raggedright\arraybackslash}}p{{2.6cm}}>{{\raggedright\arraybackslash}}p{{\dimexpr\linewidth-2.6cm-2\tabcolsep\relax}}@{{}}}}
{rows}
\end{{longtable}}
\endgroup
\clearpage
"""


def abstract_of(md_name):
    blocks = parse_blocks((MD / md_name).read_text(encoding="utf-8"))
    i = next(k for k, b in enumerate(blocks) if b[0] == "h" and b[1] == 2 and b[2] in ("Resumo", "Abstract"))
    paras = []
    for b in blocks[i + 1:]:
        if b[0] == "h":
            break
        if b[0] == "p":
            paras.append(b[1])
    return paras


FIG_KIND = {"1": "tikz", "2": "heat", "3": "matrix", "4": "tikz", "5": "tikz"}


def reorder_figure_tables(blocks):
    """Se a tabela de uma figura-tabela vem ANTES da legenda, move a tabela para depois do comentário."""
    out = list(blocks)
    for i, b in enumerate(out):
        if b[0] == "p" and re.match(r"^\*\*(Figura|Figure) (\d+)", b[1][0]):
            num = re.match(r"^\*\*(Figura|Figure) (\d+)", b[1][0]).group(2)
            if FIG_KIND.get(num) in ("heat", "matrix"):
                nxt = [x[0] for x in out[i + 1:i + 3]]
                if "table" not in nxt and i > 0 and out[i - 1][0] == "table":
                    tbl = out.pop(i - 1)
                    i -= 1
                    j = i + 1
                    while j < len(out) and out[j][0] == "comment":
                        j += 1
                    out.insert(j, tbl)
                    return reorder_figure_tables(out)
    return out


def clean_source(src, lang):
    c = L[lang]
    src = src.replace("Elaboração própria", "Elaborado pelos autores (2026)").replace("Authors' own elaboration", "Prepared by the authors (2026)")
    src = re.sub(c["src_prefix"], "", src)
    m = re.match(c["src_prefix2"], src)
    if m:
        src = src[m.end():]
        src = src[0].upper() + src[1:]
    return src


def build_report(lang):
    c = L[lang]
    other = "en" if lang == "pt" else "pt"
    blocks = reorder_figure_tables(parse_blocks((MD / c["md_report"]).read_text(encoding="utf-8")))
    ridx, items, keymap = parse_refs(blocks)
    ctx = Ctx(keymap)
    body_blocks = blocks[:ridx]
    meta = next(b for b in body_blocks if b[0] == "p")
    own = abstract_of(c["md_report"])
    oth_blocks = parse_blocks((MD / L[other]["md_report"]).read_text(encoding="utf-8"))
    _, _, other_keymap = parse_refs(oth_blocks)
    oth = abstract_of(L[other]["md_report"])

    out = [preamble(lang, keymap, f"P3D -- Privacidade 2 ({'PT-BR' if lang == 'pt' else 'EN'})"),
           r"\begin{document}", "", cover(lang)]

    def resumo_env(paras, ctx_, label=None, olang=None):
        lines = [r"\begin{resumo}" + (f"[{label}]" if label else "")]
        if olang:
            lines.append(r"\begin{otherlanguage*}{%s}" % olang)
        lines += [para_text(paras[0], ctx_), "", r"\vspace{\onelineskip}", r"\noindent" + para_text(paras[1], ctx_)]
        if olang:
            lines.append(r"\end{otherlanguage*}")
        lines.append(r"\end{resumo}")
        return "\n".join(lines)

    if lang == "pt":
        out += [resumo_env(own, ctx), "", resumo_env(oth, Ctx(other_keymap), "Abstract", "english")]
    else:
        out += [resumo_env(own, ctx, "Abstract"), "", resumo_env(oth, Ctx(other_keymap), "Resumo", "brazilian")]
    out += ["", r"\clearpage", "", r"\tableofcontents", r"\clearpage", r"\listoffigures", r"\clearpage",
            r"\listoftables", r"\clearpage", siglas_block(lang)]
    out += [r"\begin{flushleft}\small\SingleSpacing", r"\noindent\textbf{%s.} " % c["nota"] + para_text(meta[1], ctx),
            r"\end{flushleft}", r"\vspace{\onelineskip}"]

    pending_fig, tcount = None, 0
    skip_resumo = False
    for b in body_blocks:
        t = b[0]
        if t == "h":
            lvl, title = b[1], b[2]
            if lvl == 1:
                continue
            if lvl == 2 and title in ("Resumo", "Abstract"):
                skip_resumo = True
                continue
            skip_resumo = False
            if lvl == 2:
                out += ["", r"\section{" + inline(strip_num(title).upper(), ctx) + "}"]
            elif lvl == 3:
                out.append(r"\subsection{" + inline(strip_num(title), ctx) + "}")
            else:
                out.append(r"\subsubsection{" + inline(strip_num(title), ctx) + "}")
            continue
        if skip_resumo or t == "comment":
            continue
        if t == "p":
            if b is meta:
                continue
            if re.match(r"^\*\*(Figura|Figure) \d+", b[1][0]):
                pending_fig = " ".join(x.strip() for x in b[1])
                continue
            out += ["", para_text(b[1], ctx)]
        elif t in ("fence", "table") and pending_fig is not None:
            m = re.match(r"^\*\*(?:Figura|Figure) (\d+) — (.+?)\*\*\s*(.*)$", pending_fig)
            if not m:
                raise SystemExit("Figura sem legenda anterior")
            num, title, rest = m.group(1), m.group(2).rstrip("."), m.group(3)
            src = re.search(r"\*([^*]+)\*\s*$", rest)
            source = clean_source(src.group(1).strip().rstrip("."), lang) if src else ""
            interp = rest[:src.start()].strip() if src else rest.strip()
            kind = FIG_KIND[num]
            assert (kind == "tikz") == (t == "fence"), (num, kind, t)
            out += ["", r"\begin{figure}[!htbp]", r"\centering", r"\caption{" + inline(title, ctx) + r"}\label{fig:%s}" % num]
            if kind == "tikz":
                out.append(r"\includegraphics[width=\linewidth]{out/Fig%s%s.pdf}" % (num, c["fig_dir"]))
            elif kind == "heat":
                out += [r"\begingroup\SingleSpacing\small", heat_tabular(b[1], ctx), r"\endgroup"]
            else:
                out += [r"\begingroup\SingleSpacing\scriptsize", matrix_tabular(b[1], ctx), r"\endgroup",
                        r"\par\vspace{3pt}{\scriptsize\noindent " + c["legend_bands"] + r"\par}"]
            out += [r"\fontetab{" + inline(source, ctx) + ".}", r"\end{figure}"]
            if interp:
                out += ["", inline(interp, ctx)]
            pending_fig = None
        elif t == "table":
            cap = TABLE_CAPTIONS[lang][tcount]
            out += ["", table_tex(b[1], cap, ctx, f"t{tcount + 1}")]
            tcount += 1
    assert tcount == len(TABLE_CAPTIONS[lang]), (lang, tcount)
    assert pending_fig is None

    out += ["", r"\clearpage", r"\begin{center}", r"\textbf{%s}" % c["refs_title"], r"\end{center}", "",
            r"\begingroup", r"\SingleSpacing", r"\setlength{\parindent}{0pt}", r"\setlength{\parskip}{10pt}", ""]
    rctx = Ctx(keymap, ref_mode=True)
    for n, txt in items:
        out += [r"\refitem{%s}{%s}" % (keymap[n], inline(txt, rctx)), ""]
    out += [r"\endgroup", "", r"\end{document}", ""]
    return "\n".join(out)


def build_lessons(lang):
    c = L[lang]
    blocks = parse_blocks((MD / c["md_lessons"]).read_text(encoding="utf-8"))
    ctx = Ctx({})
    out = [preamble(lang, {}, f"P3D -- Lições aprendidas ({'PT-BR' if lang == 'pt' else 'EN'})"),
           r"\begin{document}", r"\SingleSpacing", r"\thispagestyle{plain}", ""]
    title = next(b[2] for b in blocks if b[0] == "h" and b[1] == 1)
    out.append(r"\begin{center}\textbf{" + inline(title.upper(), ctx) + r"}\end{center}")
    for b in blocks:
        if b[0] == "h" and b[1] == 2:
            out += ["", r"\subsection*{" + inline(b[2], ctx) + "}"]
        elif b[0] == "p":
            out += ["", para_text(b[1], ctx)]
    out += ["", r"\end{document}", ""]
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Figuras TikZ (padrão da P2B)
# ---------------------------------------------------------------------------
FIG_HEAD = r"""\documentclass[11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,shapes.geometric}

\geometry{paperwidth=16cm,paperheight=@@H@@cm,margin=0cm}
\pagestyle{empty}
\setlength{\parindent}{0pt}

\definecolor{ctxFill}{RGB}{238,242,245}
\definecolor{ctxLine}{RGB}{155,168,179}
\definecolor{ctxText}{RGB}{38,52,67}
\definecolor{exFill}{RGB}{220,233,247}
\definecolor{exLine}{RGB}{23,54,93}
\definecolor{prFill}{RGB}{200,240,236}
\definecolor{prLine}{RGB}{8,127,140}
\definecolor{prText}{RGB}{6,79,87}

\begin{document}
\noindent
\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
  \path[use as bounding box] (0,0) rectangle (16,@@H@@);
"""
FIG_TAIL = "\\end{tikzpicture}\n\\end{document}\n"
ARR = "-{Triangle[length=5pt,width=5pt]}"
ARR2 = "{Triangle[length=5pt,width=5pt]}-{Triangle[length=5pt,width=5pt]}"

FIG_LABELS = {
    "pt": dict(
        std="STANDARD", std2="valor · mindset e 6 princípios\\\\ciclos de vida · 5 áreas de foco",
        gui="GUIDE", gui2="7 domínios · 40 processos · adaptação\\\\entradas e saídas · ferramentas e técnicas",
        ana="Agrupamento analítico deste trabalho (não é do PMI)", ana2="4 concentrações: Consolidação · Nascimento · Meios · Quem",
        pmi="PMBOK 8 [4]",
        steps=["1 · Escolher abordagem inicial", "2 · Adaptar à organização", "3 · Adaptar ao projeto", "4 · Melhorar continuamente"],
        learn="aprendizado", wider="revisão mais ampla",
        cond="Condicionantes", cond2="criticidade · escala · equipe · cultura · contrato",
        ops="Operações sobre processos", ops2="adicionar · modificar · remover · combinar · alinhar",
        cards=[("Consolidação", "Governança", "9"), ("Nascimento", "Escopo + Cronograma", "9"),
               ("Meios", "Finanças + Recursos", "9"), ("Quem", "Partes Interessadas + Riscos", "13")],
        procs="processos", ext="em análise", exts=["A", "S", "I", "P"],
        l1="Camada 1 · Princípios (mentalidade)", pa="Proativa", pb="De responsabilidade", pc="Orientada a valor",
        tl="TAILORING", tl2="abordagem · processos · engajamento", cyc="Ciclo de quatro passos",
        l3="Camada 3 · Estrutura de trabalho", af="5 áreas de foco", dd="7 domínios · 40 processos",
        orient="orientam", adjusts="ajusta a aplicação",
    ),
    "en": dict(
        std="STANDARD", std2="value · mindset and 6 principles\\\\life cycles · 5 Focus Areas",
        gui="GUIDE", gui2="7 domains · 40 processes · tailoring\\\\inputs and outputs · tools and techniques",
        ana="Analytical grouping of this work (not from PMI)", ana2="4 concentrations: Consolidation · Birth · Means · Who",
        pmi="PMBOK 8 [5]",
        steps=["1 · Select initial approach", "2 · Tailor for the organization", "3 · Tailor for the project", "4 · Improve continuously"],
        learn="learning", wider="broader review",
        cond="Conditioning factors", cond2="criticality · scale · team · culture · contract",
        ops="Operations on processes", ops2="add · modify · remove · blend · align",
        cards=[("Consolidation", "Governance", "9"), ("Birth", "Scope + Schedule", "9"),
               ("Means", "Finance + Resources", "9"), ("Who", "Stakeholders + Risk", "13")],
        procs="processes", ext="under analysis", exts=["A", "S", "I", "P"],
        l1="Layer 1 · Principles (mindset)", pa="Proactive", pb="Ownership", pc="Value-driven",
        tl="TAILORING", tl2="approach · processes · engagement", cyc="Four-step cycle",
        l3="Layer 3 · Work structure", af="5 Focus Areas", dd="7 domains · 40 processes",
        orient="guide", adjusts="adjusts application",
    ),
}


def fig1(l):
    s = FIG_HEAD.replace("@@H@@", "6.6")
    s += (f"  \\node[anchor=west,text=exLine] at (0.2,6.25) {{\\textbf{{{l['pmi']}}}}};\n"
          "  \\draw[fill=exFill,draw=exLine,line width=1.3pt,rounded corners=0.25cm] (0.2,2.9) rectangle (7.2,5.9);\n"
          "  \\draw[fill=exFill,draw=exLine,line width=1.3pt,rounded corners=0.25cm] (8.8,2.9) rectangle (15.8,5.9);\n"
          f"  \\node[align=center,text=exLine] at (3.7,4.4) {{\\large\\textbf{{{l['std']}}}\\\\ {l['std2']}}};\n"
          f"  \\node[align=center,text=exLine] at (12.3,4.4) {{\\large\\textbf{{{l['gui']}}}\\\\ {l['gui2']}}};\n"
          f"  \\draw[draw=exLine,line width=1.2pt,{ARR2}] (7.2,4.4) -- (8.8,4.4);\n"
          "  \\draw[fill=ctxFill,draw=ctxLine,line width=1.1pt,dash pattern=on 5pt off 4pt,rounded corners=0.25cm] (3.6,0.2) rectangle (12.4,1.9);\n"
          f"  \\node[align=center,text=ctxText] at (8.0,1.05) {{\\textbf{{{l['ana']}}}\\\\ {l['ana2']}}};\n"
          f"  \\draw[draw=ctxLine,line width=1.1pt,dash pattern=on 4pt off 3pt,{ARR}] (12.3,2.9) -- (12.3,2.4) -- (10.5,2.4) -- (10.5,1.9);\n")
    return s + FIG_TAIL


def fig4(l):
    s = FIG_HEAD.replace("@@H@@", "6.4")
    xs = [0.2, 4.2, 8.2, 12.2]
    for i, (x, txt) in enumerate(zip(xs, l["steps"])):
        s += (f"  \\draw[fill=exFill,draw=exLine,line width=1.2pt,rounded corners=0.2cm] ({x},2.6) rectangle ({x + 3.6},4.2);\n"
              f"  \\node[align=center,text width=3.3cm,text=exLine] at ({x + 1.8},3.4) {{\\footnotesize\\textbf{{{txt}}}}};\n")
        if i < 3:
            s += f"  \\draw[draw=exLine,line width=1.1pt,{ARR}] ({x + 3.6},3.4) -- ({x + 4.0},3.4);\n"
    s += (f"  \\draw[draw=prLine,line width=1.1pt,dash pattern=on 4pt off 3pt,{ARR}] (14.0,4.2) -- (14.0,4.8) -- (10.0,4.8) -- (10.0,4.2);\n"
          f"  \\node[text=prText,fill=white,inner sep=2pt] at (12.0,4.8) {{\\footnotesize {l['learn']}}};\n"
          f"  \\draw[draw=prLine,line width=1.1pt,dash pattern=on 4pt off 3pt,{ARR}] (14.0,4.2) -- (14.0,5.7) -- (2.0,5.7) -- (2.0,4.2);\n"
          f"  \\node[text=prText,fill=white,inner sep=2pt] at (8.0,5.7) {{\\footnotesize {l['wider']}}};\n"
          "  \\draw[fill=ctxFill,draw=ctxLine,line width=1pt,dash pattern=on 5pt off 4pt,rounded corners=0.2cm] (0.2,0.2) rectangle (7.6,1.6);\n"
          f"  \\node[align=center,text=ctxText,text width=7.0cm] at (3.9,0.9) {{\\footnotesize\\textbf{{{l['cond']}}}\\\\ {l['cond2']}}};\n"
          f"  \\draw[draw=ctxLine,line width=1pt,dash pattern=on 4pt off 3pt,{ARR}] (6.2,1.6) -- (6.2,2.6);\n"
          "  \\draw[fill=ctxFill,draw=ctxLine,line width=1pt,dash pattern=on 5pt off 4pt,rounded corners=0.2cm] (8.4,0.2) rectangle (15.8,1.6);\n"
          f"  \\node[align=center,text=ctxText,text width=7.0cm] at (12.1,0.9) {{\\footnotesize\\textbf{{{l['ops']}}}\\\\ {l['ops2']}}};\n"
          f"  \\draw[draw=ctxLine,line width=1pt,dash pattern=on 4pt off 3pt,{ARR}] (10.0,1.6) -- (10.0,2.6);\n")
    return s + FIG_TAIL


def fig5(l):
    s = FIG_HEAD.replace("@@H@@", "5.0")
    for k, ((t, d, n), e) in enumerate(zip(l["cards"], l["exts"])):
        x = 0.2 + k * 3.95
        s += (f"  \\draw[fill=exFill,draw=exLine,line width=1.2pt,rounded corners=0.2cm] ({x},2.2) rectangle ({x + 3.65},4.7);\n"
              f"  \\node[align=center,text width=3.4cm,text=exLine] at ({x + 1.825},3.45) {{\\textbf{{{t}}}\\\\ {d}\\\\ \\large\\textbf{{{n}}} {l['procs']}}};\n"
              f"  \\draw[fill=ctxFill,draw=ctxLine,line width=1pt,dash pattern=on 5pt off 4pt,rounded corners=0.15cm] ({x + 0.4},0.3) rectangle ({x + 3.25},1.4);\n"
              f"  \\node[align=center,text=ctxText] at ({x + 1.825},0.85) {{\\footnotesize\\textbf{{+ {e}}} · {l['ext']}}};\n"
              f"  \\draw[draw=ctxLine,line width=1pt,dash pattern=on 4pt off 3pt] ({x + 1.825},2.2) -- ({x + 1.825},1.4);\n")
    return s + FIG_TAIL


def figP1(l):
    s = FIG_HEAD.replace("@@H@@", "8.4")
    s += (f"  \\node[anchor=west,text=exLine] at (0.2,8.05) {{\\footnotesize\\textbf{{{l['l1']}}}}};\n")
    for x, a, b in [(0.2, l["pa"], "1AHV · 3QPD"), (5.5, l["pb"], "4BAL · 6BEC"), (10.8, l["pc"], "2FOV · 5SPA")]:
        s += (f"  \\draw[fill=exFill,draw=exLine,line width=1.1pt,rounded corners=0.2cm] ({x},6.1) rectangle ({x + 5.0},7.7);\n"
              f"  \\node[align=center,text=exLine] at ({x + 2.5},6.9) {{\\textbf{{{a}}}\\\\ {b}}};\n")
    s += (f"  \\draw[draw=exLine,line width=1.2pt,{ARR}] (8.0,6.1) -- (8.0,5.55);\n"
          f"  \\node[text=exLine,fill=white,inner sep=2pt,anchor=west] at (8.15,5.85) {{\\footnotesize {l['orient']}}};\n"
          "  \\draw[fill=prFill,draw=prLine,line width=1.6pt,rounded corners=0.25cm] (3.2,3.5) rectangle (12.8,5.5);\n"
          f"  \\node[align=center,text=prText] at (8.0,4.5) {{\\large\\textbf{{{l['tl']}}}\\\\ {l['tl2']}\\\\ \\footnotesize {l['cyc']}: 1 $\\rightarrow$ 2 $\\rightarrow$ 3 $\\rightarrow$ 4}};\n"
          f"  \\draw[draw=exLine,line width=1.2pt,{ARR}] (8.0,3.5) -- (8.0,2.55);\n"
          f"  \\node[text=exLine,fill=white,inner sep=2pt,anchor=west] at (8.15,3.0) {{\\footnotesize {l['adjusts']}}};\n"
          f"  \\node[anchor=west,text=exLine] at (0.2,2.3) {{\\footnotesize\\textbf{{{l['l3']}}}}};\n"
          "  \\draw[fill=exFill,draw=exLine,line width=1.1pt,rounded corners=0.2cm] (0.2,0.2) rectangle (7.6,1.9);\n"
          "  \\draw[fill=exFill,draw=exLine,line width=1.1pt,rounded corners=0.2cm] (8.4,0.2) rectangle (15.8,1.9);\n"
          f"  \\node[text=exLine] at (3.9,1.05) {{\\textbf{{{l['af']}}}}};\n"
          f"  \\node[text=exLine] at (12.1,1.05) {{\\textbf{{{l['dd']}}}}};\n")
    return s + FIG_TAIL


FIGS = [("Fig1", fig1), ("Fig4", fig4), ("Fig5", fig5), ("FigP1", figP1)]


def main():
    (TEX / "figuras").mkdir(exist_ok=True)
    for lang in ("pt", "en"):
        for name, f in FIGS:
            (TEX / "figuras" / f"{name}{L[lang]['fig_dir']}.tex").write_text(f(FIG_LABELS[lang]), encoding="utf-8")
        (TEX / L[lang]["out_report"]).write_text(build_report(lang), encoding="utf-8")
        (TEX / L[lang]["out_lessons"]).write_text(build_lessons(lang), encoding="utf-8")
    print("gerado em", TEX)


if __name__ == "__main__":
    main()
