"""Gera os .tex da P3A a partir dos Markdown congelados em ../MD.

Uso (a partir de _grupo/P3A/entregas/TEX):
    python ferramentas/gerar_tex.py

Gera: relatório PT/EN, lições PT/EN e as figuras (TikZ independentes) em figuras/.
Os pôsteres (PT/EN) são escritos à mão; este script não os toca.
O script NÃO compila nada. A compilação é feita pelo grupo (ver README.md).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

TEX = Path(__file__).resolve().parent.parent
MD = TEX.parent / "MD"

# ---------------------------------------------------------------------------
# Textos por idioma
# ---------------------------------------------------------------------------
L = {
    "pt": {
        "md_report": "P3A_Privacidade2_Relatorio_PT.md",
        "md_lessons": "P3A_Privacidade2_Licoes_PT.md",
        "out_report": "P3A_Privacidade2_Relatorio_PT.tex",
        "out_lessons": "P3A_Privacidade2_Licoes_PT.tex",
        "docopts": "english,brazil",
        "main_lang": "brazil",
        "resumo_name": "Resumo",
        "refs_name": "Referências",
        "kw": "Palavras-chave",
        "source": "Fonte",
        "fig_dir": "_PT",
        "contents": "SUMÁRIO",
        "listfig": "LISTA DE ILUSTRAÇÕES",
        "listtab": "LISTA DE TABELAS",
        "siglas": "LISTA DE ABREVIATURAS E SIGLAS",
        "refs_title": "REFERÊNCIAS",
        "nota": "Nota de natureza",
        "cover": [
            r"UNIVERSIDADE DE BRASÍLIA -- UNB\\PROGRAMA DE PÓS-GRADUAÇÃO EM COMPUTAÇÃO APLICADA -- PPCA\\DISCIPLINA: GESTÃO DE PROJETOS DE TI (GPTI)\\PROFESSOR: Dr. JOÃO MELLO DA SILVA",
        ],
        "group_label": "Grupo SIPA Privacidade 2",
        "cover_city": r"BRASÍLIA -- DF\\2026",
        "authors_sub": "Integrantes",
        "title_caps": "PRIVACIDADE COMO DOMÍNIO DE DESEMPENHO PROPOSTO PARA O PMBOK 8",
    },
    "en": {
        "md_report": "P3A_Privacidade2_Report_EN.md",
        "md_lessons": "P3A_Privacidade2_Lessons_EN.md",
        "out_report": "P3A_Privacidade2_Report_EN.tex",
        "out_lessons": "P3A_Privacidade2_Lessons_EN.tex",
        "docopts": "brazil,english",
        "main_lang": "english",
        "resumo_name": "Abstract",
        "refs_name": "References",
        "kw": "Keywords",
        "source": "Source",
        "fig_dir": "_EN",
        "contents": "CONTENTS",
        "listfig": "LIST OF FIGURES",
        "listtab": "LIST OF TABLES",
        "siglas": "LIST OF ABBREVIATIONS AND ACRONYMS",
        "refs_title": "REFERENCES",
        "nota": "Nature of the work",
        "cover": [
            r"UNIVERSITY OF BRASÍLIA -- UnB\\GRADUATE PROGRAM IN APPLIED COMPUTING -- PPCA\\COURSE: IT PROJECT MANAGEMENT (GPTI)\\PROFESSOR: Dr. JOÃO MELLO DA SILVA",
        ],
        "group_label": "SIPA Privacy 2 Group",
        "cover_city": r"BRASÍLIA -- DF\\2026",
        "authors_sub": "Members",
        "title_caps": "PRIVACY AS A PROPOSED PMBOK 8 PERFORMANCE DOMAIN",
    },
}

# Legendas das tabelas (12), na ordem em que aparecem; fontes com \cit{chave}
TABLE_CAPTIONS = {
    "pt": [
        ("O que a nova organização precisa tornar observável", "Elaborado pelos autores (2026)."),
        ("Conceitos-chave e sentido adotado", r"Elaborado pelos autores (2026), a partir de \cit{lgpd} e \cit{nistpf}."),
        ("Processos propostos para o domínio Privacidade", "Elaborado pelos autores (2026)."),
        ("Ferramentas e técnicas e fundamentos dos processos propostos", "Elaborado pelos autores (2026), a partir das fontes indicadas na coluna Fundamento."),
        ("Adaptação do esforço por perfil de projeto", r"Elaborado pelos autores (2026), com base em \cit{anpd}."),
        ("Tipos de réplica digital e implicações para a privacidade", r"Elaborado pelos autores (2026), com base em \cit{kritzinger}."),
        ("Resultados esperados e verificação", r"Elaborado pelos autores (2026), com base em \cit{pmi}."),
        ("Aderência do domínio às cinco áreas de foco", "Elaborado pelos autores (2026)."),
        ("Aderência do domínio aos seis princípios", r"Elaborado pelos autores (2026), com base em \cit{pmi}."),
        ("Inclusões e alterações propostas nos processos de Partes Interessadas e Riscos", r"Elaborado pelos autores (2026), com base em \cit{pmi}."),
        ("Interfaces potenciais com as demais concentrações", "Elaborado pelos autores (2026)."),
        ("Relatório final do trabalho", r"Elaborado pelos autores (2026), no formato do \textit{Final report} de \cit{pmi}."),
    ],
    "en": [
        ("What the new organization must make observable", "Prepared by the authors (2026)."),
        ("Key concepts and adopted meaning", r"Prepared by the authors (2026), based on \cit{lgpd} and \cit{nistpf}."),
        ("Processes proposed for the Privacy domain", "Prepared by the authors (2026)."),
        ("Tools, techniques and foundations of the proposed processes", "Prepared by the authors (2026), based on the sources given in the Foundation column."),
        ("Effort tailoring by project profile", r"Prepared by the authors (2026), based on \cit{anpd}."),
        ("Types of digital replica and implications for privacy", r"Prepared by the authors (2026), based on \cit{kritzinger}."),
        ("Expected results and verification", r"Prepared by the authors (2026), based on \cit{pmi}."),
        ("Alignment of the domain with the five Focus Areas", "Prepared by the authors (2026)."),
        ("Alignment of the domain with the six principles", r"Prepared by the authors (2026), based on \cit{pmi}."),
        ("Proposed inclusions and changes to the Stakeholders and Risk processes", r"Prepared by the authors (2026), based on \cit{pmi}."),
        ("Potential interfaces with the other concentrations", "Prepared by the authors (2026)."),
        ("Final report of the work", r"Prepared by the authors (2026), following the \textit{Final report} format of \cit{pmi}."),
    ],
}

# Lista de siglas (sigla, PT, EN)
SIGLAS = [
    ("1AHV", "\\textit{Adopt a Holistic View}: adotar uma visão holística", "Adopt a Holistic View"),
    ("2FOV", "\\textit{Focus on Value}: focar em valor", "Focus on Value"),
    ("3QPD", "\\textit{Embed Quality Into Processes and Deliverables}: embutir qualidade em processos e entregas", "Embed Quality Into Processes and Deliverables"),
    ("4BAL", "\\textit{Be an Accountable Leader}: ser um líder responsável", "Be an Accountable Leader"),
    ("5SPA", "\\textit{Integrate Sustainability Within All Project Areas}: integrar sustentabilidade em todas as áreas do projeto", "Integrate Sustainability Within All Project Areas"),
    ("6BEC", "\\textit{Build an Empowered Culture}: construir uma cultura empoderada", "Build an Empowered Culture"),
    ("ANPD", "Autoridade Nacional de Proteção de Dados", "Brazilian National Data Protection Authority"),
    ("BI", "Concentração Nascimento (\\textit{Birth})", "Birth concentration"),
    ("CD", "Critérios de desenvolvimento", "Development criteria"),
    ("CL", "Encerramento (\\textit{Closing}), área de foco", "Closing Focus Area"),
    ("CN", "Caracterização da necessidade", "Characterization of the need"),
    ("CO", "Concentração Consolidação (\\textit{Consolidation})", "Consolidation concentration"),
    ("DM", "Desenvolvimento e manutenção", "Development and maintenance"),
    ("DTC", "\\textit{Digital Twin Consortium}", "Digital Twin Consortium"),
    ("EX", "Execução (\\textit{Executing}), área de foco", "Executing Focus Area"),
    ("F/S/P/C", "Função, Estrutura, Processo e Contexto", "Function, Structure, Process and Context"),
    ("GDPR", "\\textit{General Data Protection Regulation} (Regulamento Geral sobre a Proteção de Dados)", "General Data Protection Regulation"),
    ("HIPAA", "\\textit{Health Insurance Portability and Accountability Act}", "Health Insurance Portability and Accountability Act"),
    ("IA", "Inteligência artificial", "Artificial intelligence (AI)"),
    ("IN", "Iniciação (\\textit{Initiating}), área de foco", "Initiating Focus Area"),
    ("LGPD", "Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018)", "Brazilian General Data Protection Law (Law No. 13,709/2018)"),
    ("LINDDUN", "\\textit{Linkability, Identifiability, Non-repudiation, Detectability, Disclosure of information, Unawareness, Non-compliance}", "Linkability, Identifiability, Non-repudiation, Detectability, Disclosure of information, Unawareness, Non-compliance"),
    ("MC", "Monitoramento e controle (\\textit{Monitoring and Controlling}), área de foco", "Monitoring and Controlling Focus Area"),
    ("ME", "Concentração Meios (\\textit{Means})", "Means concentration"),
    ("NIS2", "\\textit{Network and Information Security Directive}", "Network and Information Security Directive"),
    ("NIST", "\\textit{National Institute of Standards and Technology}", "National Institute of Standards and Technology"),
    ("NISTIR", "\\textit{NIST Interagency or Internal Report}", "NIST Interagency or Internal Report"),
    ("P1--P8", "Processos de Privacidade propostos neste trabalho", "Privacy processes proposed in this work"),
    ("PF", "Publicação e formato", "Publication and format"),
    ("PISO", "Procura, Industrialização, Solução e Oferta", "Demand, Industrialization, Solution and Offer (Procura, Industrialização, Solução, Oferta)"),
    ("PL", "Planejamento (\\textit{Planning}), área de foco", "Planning Focus Area"),
    ("PMBOK", "\\textit{Project Management Body of Knowledge}", "Project Management Body of Knowledge"),
    ("PMI", "\\textit{Project Management Institute}", "Project Management Institute"),
    ("RIPD", "Relatório de impacto à proteção de dados pessoais", "Data protection impact assessment (DPIA/RIPD)"),
    ("SIPA", "Sustentabilidade, Inovação, Privacidade e Análise de negócios com decisões ajustadas a riscos", "Sustainability, Innovation, Privacy and Business analysis with risk-adjusted decisions"),
    ("UE", "União Europeia", "European Union"),
    ("WH", "Concentração Quem (\\textit{Who})", "Who concentration"),
]

REF_KEYS = [
    (r"^ANPD", "anpd"), (r"^(BRASIL|BRAZIL)", "lgpd"), (r"^BROOKS", "brooks"), (r"^DENG", "deng"),
    (r"^DHINAKARAN", "dhinakaran"), (r"^DIGITAL TWIN CONSORTIUM.*\*Digital Twin Consortium defines", "dtc2020"),
    (r"^DIGITAL TWIN CONSORTIUM.*capabilities periodic table\*\.\s*(Versão|Version) 1\.2", "dtccpt"),
    (r"^DIGITAL TWIN CONSORTIUM.*AI agent", "dtcai"), (r"^JØRGENSEN", "jorgensen"), (r"^KORCHENKO", "korchenko"),
    (r"^KRITZINGER", "kritzinger"), (r"^NIST", "nistpf"), (r"^PMI", "pmi"), (r"^SHAIKH", "shaikh"),
    (r"^SON,", "son"), (r"^(UNIÃO EUROPEIA|EUROPEAN UNION)", "gdpr"), (r"^WANG", "wang"),
]

# ---------------------------------------------------------------------------
# Conversão de inline
# ---------------------------------------------------------------------------
UNI = {"→": r"\ensuremath{\rightarrow}", "…": r"\ldots{}", "≥": r"\ensuremath{\geq}", "≤": r"\ensuremath{\leq}"}
ESC = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}

CITE = re.compile(r"\[(\d+(?:,\s*\d+)*)(?:,\s*([^\]]+))?\]")
BOLD = re.compile(r"\*\*(.+?)\*\*")
ITAL = re.compile(r"\*(.+?)\*")
URL = re.compile(r"https?://[^\s)]+")


def esc_plain(s: str) -> str:
    out = []
    for ch in s:
        if ch in ESC:
            out.append(ESC[ch])
        elif ch in UNI:
            out.append(UNI[ch])
        else:
            out.append(ch)
    s = "".join(out)
    # aspas retas -> aspas tipográficas
    parts = s.split('"')
    if len(parts) > 1 and len(parts) % 2 == 1:
        s = parts[0]
        for i, p in enumerate(parts[1:], start=1):
            s += (r"\textquotedblleft{}" if i % 2 == 1 else r"\textquotedblright{}") + p
    return s


class Ctx:
    """Contexto de conversão: mapa número->chave de referência e destaque das referências."""

    def __init__(self, keymap: dict[int, str], ref_mode: bool = False):
        self.keymap = keymap
        self.ref_mode = ref_mode


def inline(s: str, ctx: Ctx) -> str:
    pos, out = 0, []
    pat = re.compile(r"\*\*(.+?)\*\*|\*(.+?)\*|\[(\d+(?:,\s*\d+)*)(?:,\s*([^\]]+))?\]|(https?://[^\s)]+?)(?=[.,;]?(?:\s|$|\)))")
    for m in pat.finditer(s):
        out.append(esc_plain(s[pos:m.start()]))
        if m.group(1) is not None:
            out.append(r"\textbf{" + inline(m.group(1), ctx) + "}")
        elif m.group(2) is not None:
            tag = r"\textbf{" if ctx.ref_mode else r"\textit{"
            out.append(tag + inline(m.group(2), ctx) + "}")
        elif m.group(3) is not None:
            nums = [int(x) for x in re.split(r",\s*", m.group(3))]
            refs = ", ".join(r"\refnum{%s}" % ctx.keymap[n] for n in nums)
            loc = (", " + inline(m.group(4), ctx)) if m.group(4) else ""
            out.append("[" + refs + loc + "]")
        else:
            out.append(r"\url{" + m.group(5) + "}")
        pos = m.end()
    out.append(esc_plain(s[pos:]))
    return "".join(out)


# ---------------------------------------------------------------------------
# Leitura do Markdown
# ---------------------------------------------------------------------------
def parse_blocks(text: str):
    lines = text.split("\n")
    blocks, i, n = [], 0, len(lines)
    while i < n:
        ln = lines[i]
        if ln.startswith("```"):
            lang, j = ln[3:].strip(), i + 1
            while j < n and not lines[j].startswith("```"):
                j += 1
            blocks.append(("fence", lang, "\n".join(lines[i + 1:j])))
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
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in lines[i:j]]
            blocks.append(("table", rows))
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


def para_text(buf: list[str], ctx: Ctx) -> str:
    parts = []
    for k, ln in enumerate(buf):
        hard = ln.endswith("  ") and k < len(buf) - 1
        parts.append(inline(ln.strip(), ctx) + (r"\\" if hard else ""))
    return " ".join(parts)


def strip_num(title: str) -> str:
    return re.sub(r"^\d+(\.\d+)*\.?\s+", "", title)


# ---------------------------------------------------------------------------
# Referências
# ---------------------------------------------------------------------------
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
    colspec = "@{}" + "".join(
        r">{\raggedright\arraybackslash}p{\dimexpr(\linewidth-%d\tabcolsep)*%d/1000\relax}" % (2 * (nc - 1), x) for x in w
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


# ---------------------------------------------------------------------------
# Preâmbulo
# ---------------------------------------------------------------------------
def preamble(lang: str, keymap: dict[int, str], title_comment: str, with_lists: bool) -> str:
    c = L[lang]
    defs = "\n".join(r"\defref{%s}{%d}" % (k, n) for n, k in sorted(keymap.items()))
    return rf"""% =============================================================================
% {title_comment}
% Formatação: ABNT (classe abnTeX2, modo article), A4, Latin Modern, 12 pt,
% margens 3/2/3/2 cm, espaçamento 1,5, recuo de parágrafo 1,25 cm.
% Figuras esperadas em out/ (compiladas a partir de figuras/):
%   Fig1..Fig5{c['fig_dir']}.pdf
% ARQUIVO GERADO por ferramentas/gerar_tex.py a partir de ../MD. Para mudar o
% conteúdo, edite o Markdown e gere de novo, ou edite este .tex diretamente.
% =============================================================================
\documentclass[12pt,a4paper,article,oneside,{c['docopts']}]{{abntex2}}

\usepackage[T1]{{fontenc}}
\usepackage[utf8]{{inputenc}}
\usepackage{{lmodern}}           % Latin Modern (fonte padrão do LaTeX, com T1)
\usepackage{{amsmath}}
\usepackage{{graphicx}}
\usepackage{{array}}
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


def cover(lang: str) -> str:
    c = L[lang]
    return rf"""% ------------------------------- CAPA ----------------------------------------
\thispagestyle{{empty}}
\noindent\begin{{minipage}}[t][0.92\textheight]{{\textwidth}}
\centering
\SingleSpacing
\textbf{{{c['cover'][0]}}}

\vspace{{1cm}}

\textbf{{{c['group_label']}}}: \integrantes

\vspace{{3cm}}

\textbf{{{c['title_caps']}}}

\vfill

{c['cover_city']}
\end{{minipage}}
\clearpage
"""


def siglas_block(lang: str) -> str:
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


# ---------------------------------------------------------------------------
# Relatório
# ---------------------------------------------------------------------------
def abstract_of(md_name: str, ctx_dummy: Ctx):
    blocks = parse_blocks((MD / md_name).read_text(encoding="utf-8"))
    i = next(k for k, b in enumerate(blocks) if b[0] == "h" and b[1] == 2 and b[2] in ("Resumo", "Abstract"))
    paras = []
    for b in blocks[i + 1:]:
        if b[0] == "h":
            break
        if b[0] == "p":
            paras.append(b[1])
    return paras  # [texto, palavras-chave]


def build_report(lang: str) -> str:
    c = L[lang]
    other = "en" if lang == "pt" else "pt"
    blocks = parse_blocks((MD / c["md_report"]).read_text(encoding="utf-8"))
    ridx, items, keymap = parse_refs(blocks)
    ctx = Ctx(keymap)
    body_blocks = blocks[:ridx]

    # metadados (primeiro parágrafo depois do h1)
    meta = next(b for b in body_blocks if b[0] == "p")
    # resumo/abstract
    own = abstract_of(c["md_report"], ctx)
    oth_blocks = parse_blocks((MD / L[other]["md_report"]).read_text(encoding="utf-8"))
    _, _, other_keymap = parse_refs(oth_blocks)
    oth = abstract_of(L[other]["md_report"], Ctx(other_keymap))

    out = [preamble(lang, keymap, f"P3A -- Privacidade 2 ({'PT-BR' if lang == 'pt' else 'EN'})", True),
           r"\begin{document}", "", cover(lang)]

    def resumo_env(paras, ctx_, name_kw, label=None, olang=None):
        txt = para_text(paras[0], ctx_)
        kw = para_text(paras[1], ctx_)
        head = r"\begin{resumo}" + (f"[{label}]" if label else "")
        lines = [head]
        if olang:
            lines.append(r"\begin{otherlanguage*}{%s}" % olang)
        lines += [txt, "", r"\vspace{\onelineskip}", r"\noindent" + kw]
        if olang:
            lines.append(r"\end{otherlanguage*}")
        lines.append(r"\end{resumo}")
        return "\n".join(lines)

    if lang == "pt":
        out.append(resumo_env(own, ctx, "kw"))
        out.append("")
        out.append(resumo_env(oth, Ctx(other_keymap), "kw", "Abstract", "english"))
    else:
        out.append(resumo_env(own, ctx, "kw", "Abstract"))
        out.append("")
        out.append(resumo_env(oth, Ctx(other_keymap), "kw", "Resumo", "brazilian"))
    out += ["", r"\clearpage", "", r"\tableofcontents", r"\clearpage", r"\listoffigures", r"\clearpage",
            r"\listoftables", r"\clearpage", siglas_block(lang)]

    # nota de natureza
    out.append(r"\begin{flushleft}\small\SingleSpacing")
    out.append(r"\noindent\textbf{%s.} " % c["nota"] + para_text(meta[1], ctx))
    out.append(r"\end{flushleft}")
    out.append(r"\vspace{\onelineskip}")

    pending_fig = None
    tcount = 0
    seen_resumo = False
    skip_resumo = False
    first_h1 = True
    meta_done = False
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
                out.append("")
                out.append(r"\section{" + inline(strip_num(title).upper(), ctx) + "}")
            elif lvl == 3:
                out.append(r"\subsection{" + inline(strip_num(title), ctx) + "}")
            else:
                out.append(r"\subsubsection{" + inline(strip_num(title), ctx) + "}")
            continue
        if skip_resumo:
            continue
        if t == "p":
            if b is meta:
                continue
            first = b[1][0]
            if re.match(r"^\*\*(Figura|Figure) \d+", first):
                pending_fig = " ".join(x.strip() for x in b[1])
                continue
            out.append("")
            out.append(para_text(b[1], ctx))
        elif t == "comment":
            continue
        elif t == "fence":
            m = re.match(r"^\*\*(?:Figura|Figure) (\d+) — (.+?)\*\*\s*(.*)$", pending_fig or "")
            if not m:
                raise SystemExit("Figura sem legenda anterior")
            num, title, rest = m.group(1), m.group(2).rstrip("."), m.group(3)
            src = re.search(r"\*([^*]+)\*\s*$", rest)
            source = src.group(1).strip().rstrip(".") if src else ""
            interp = rest[:src.start()].strip() if src else rest.strip()
            source = source.replace("Elaboração própria", "Elaborado pelos autores (2026)")
            source = source.replace("Authors' own elaboration", "Prepared by the authors (2026)")
            source = inline(source, ctx) + "."
            out += ["", r"\begin{figure}[!htbp]", r"\centering",
                    r"\caption{" + inline(title, ctx) + r"}\label{fig:%s}" % num,
                    r"\includegraphics[width=\linewidth]{out/Fig%s%s.pdf}" % (num, c["fig_dir"]),
                    r"\fontetab{" + source + "}", r"\end{figure}"]
            if interp:
                out += ["", inline(interp, ctx)]
            pending_fig = None
        elif t == "table":
            cap = TABLE_CAPTIONS[lang][tcount]
            out += ["", table_tex(b[1], cap, ctx, f"t{tcount + 1}")]
            tcount += 1
    assert tcount == len(TABLE_CAPTIONS[lang]), (lang, tcount)

    # Referências
    out += ["", r"\clearpage", r"\begin{center}", r"\textbf{%s}" % c["refs_title"], r"\end{center}", "",
            r"\begingroup", r"\SingleSpacing", r"\setlength{\parindent}{0pt}", r"\setlength{\parskip}{10pt}", ""]
    rctx = Ctx(keymap, ref_mode=True)
    for n, txt in items:
        out.append(r"\refitem{%s}{%s}" % (keymap[n], inline(txt, rctx)))
        out.append("")
    out += [r"\endgroup", "", r"\end{document}", ""]
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Lições aprendidas
# ---------------------------------------------------------------------------
def build_lessons(lang: str) -> str:
    c = L[lang]
    blocks = parse_blocks((MD / c["md_lessons"]).read_text(encoding="utf-8"))
    ctx = Ctx({})
    out = [preamble(lang, {}, f"P3A -- Lições aprendidas ({'PT-BR' if lang == 'pt' else 'EN'})", False),
           r"\begin{document}", r"\SingleSpacing", r"\thispagestyle{plain}", ""]
    title = next(b[2] for b in blocks if b[0] == "h" and b[1] == 1)
    out.append(r"\begin{center}\textbf{" + inline(title.upper(), ctx) + r"}\end{center}")
    for b in blocks:
        if b[0] == "h" and b[1] == 2:
            out.append("")
            out.append(r"\subsection*{" + inline(b[2], ctx) + "}")
        elif b[0] == "p":
            out.append("")
            out.append(para_text(b[1], ctx))
    out += ["", r"\end{document}", ""]
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Figuras (TikZ independentes, no estilo da P2B)
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
\definecolor{phFill}{RGB}{234,242,245}

\begin{document}
\noindent
\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
  \path[use as bounding box] (0,0) rectangle (16,@@H@@);
"""
FIG_TAIL = "\\end{tikzpicture}\n\\end{document}\n"

FIG_LABELS = {
    "pt": dict(
        co="Consolidação", co2="Governança (9)\\\\+ Análise de negócios",
        bi="Nascimento", bi2="Escopo (6), Cronograma (3)\\\\+ Sustentabilidade",
        me="Meios", me2="Finanças (4), Recursos (5)\\\\+ Inovação",
        quem="Quem (WH)", st="Partes Interessadas", st2="domínio existente (7)",
        pv="+ Privacidade", pv2="domínio proposto", ri="Riscos", ri2="domínio existente (6)",
        areas=[("IN · Iniciação", "P1", "Identificar titulares e dados", "Inventário"),
               ("PL · Planejamento", "P2–P4", "Planejar, avaliar impactos e definir controles", "Plano e avaliação"),
               ("EX · Execução", "P5–P6", "Gerir direitos e implementar controles", "Registros"),
               ("MC · Monitoramento e controle", "P7", "Monitorar riscos e práticas", "Revisões"),
               ("CL · Encerramento", "P8", "Transferir ou encerrar o tratamento", "Destino dos dados")],
        change="mudança relevante",
        fv="F · Função", fv2="efeitos sobre pessoas", sv="S · Estrutura", sv2="papéis e evidências",
        pvv="P · Processo", pvv2="decisões P1–P8", cv="C · Contexto", cv2="lei, tecnologia, cooperativa",
        center="Privacidade", center2="volume conceitual",
        phys="Mundo físico", rep="Réplica digital",
        t1="Modelo digital", t2="Sombra digital", t3="Gêmeo digital",
        manual="atualização manual", auto="fluxo automático", back="retorno automático: efeito sobre pessoas",
        s1="Mobilização digital", s1b="cadastro e rota", s2="Reciclagem", s2b="operação e indicadores",
        s3="Destinação final", s3b="retenção ou descarte",
        mat="materiais separados", rej="rejeitos e suportes", qual="qualidade por rota",
        q=["De quem são os dados?", "Para qual finalidade?", "Quem os recebe?", "Qual o seu destino?"],
        legend5="Cenário hipotético",
    ),
    "en": dict(
        co="Consolidation", co2="Governance (9)\\\\+ Business analysis",
        bi="Birth", bi2="Scope (6), Schedule (3)\\\\+ Sustainability",
        me="Means", me2="Finance (4), Resources (5)\\\\+ Innovation",
        quem="Who (WH)", st="Stakeholders", st2="existing domain (7)",
        pv="+ Privacy", pv2="proposed domain", ri="Risk", ri2="existing domain (6)",
        areas=[("IN · Initiating", "P1", "Identify data subjects and data", "Inventory"),
               ("PL · Planning", "P2–P4", "Plan, assess impacts and define controls", "Plan and assessment"),
               ("EX · Executing", "P5–P6", "Manage rights and implement controls", "Records"),
               ("MC · Monitoring and Controlling", "P7", "Monitor risks and practices", "Reviews"),
               ("CL · Closing", "P8", "Transfer or close the processing", "Data disposition")],
        change="material change",
        fv="F · Function", fv2="effects on people", sv="S · Structure", sv2="roles and evidence",
        pvv="P · Process", pvv2="decisions P1–P8", cv="C · Context", cv2="law, technology, cooperative",
        center="Privacy", center2="conceptual volume",
        phys="Physical world", rep="Digital replica",
        t1="Digital model", t2="Digital shadow", t3="Digital twin",
        manual="manual update", auto="automatic flow", back="automatic return: effect on people",
        s1="Digital mobilization", s1b="registration and route", s2="Recycling", s2b="operations and indicators",
        s3="Final disposal", s3b="retention or deletion",
        mat="sorted materials", rej="tailings and media", qual="quality by route",
        q=["Whose data is it?", "For what purpose?", "Who receives it?", "What happens to it?"],
        legend5="Hypothetical scenario",
    ),
}


def fig1(l):
    s = FIG_HEAD.replace("@@H@@", "7.4")
    cards = [(0.2, l["co"], l["co2"]), (5.5, l["bi"], l["bi2"]), (10.8, l["me"], l["me2"])]
    for x, t, d in cards:
        s += (f"  \\draw[fill=ctxFill,draw=ctxLine,line width=0.9pt,rounded corners=0.25cm] ({x},5.3) rectangle ({x + 5},7.2);\n"
              f"  \\node[align=center,text=ctxText] at ({x + 2.5},6.25) {{\\textbf{{{t}}}\\\\ {d}}};\n")
    s += ("  \\draw[fill=exFill!40,draw=exLine,line width=1.4pt,rounded corners=0.3cm] (0.2,0.2) rectangle (15.8,4.8);\n"
          f"  \\node[anchor=west,text=exLine] at (0.55,4.35) {{\\textbf{{{l['quem']}}}}};\n"
          "  \\draw[fill=exFill,draw=exLine,line width=1pt,rounded corners=0.2cm] (0.6,0.6) rectangle (4.9,3.8);\n"
          "  \\draw[fill=prFill,draw=prLine,line width=1.8pt,rounded corners=0.2cm] (5.6,0.6) rectangle (10.4,3.8);\n"
          "  \\draw[fill=exFill,draw=exLine,line width=1pt,rounded corners=0.2cm] (11.1,0.6) rectangle (15.4,3.8);\n"
          f"  \\node[align=center,text=exLine] at (2.75,2.2) {{\\textbf{{{l['st']}}}\\\\ {l['st2']}}};\n"
          f"  \\node[align=center,text=prText] at (8.0,2.2) {{\\large\\textbf{{{l['pv']}}}\\\\ {l['pv2']}}};\n"
          f"  \\node[align=center,text=exLine] at (13.25,2.2) {{\\textbf{{{l['ri']}}}\\\\ {l['ri2']}}};\n"
          "  \\draw[draw=prLine,line width=1.2pt] (4.9,2.2) -- (5.6,2.2);\n"
          "  \\draw[draw=prLine,line width=1.2pt] (10.4,2.2) -- (11.1,2.2);\n")
    return s + FIG_TAIL


def fig2(l):
    s = FIG_HEAD.replace("@@H@@", "5.9")
    for i, (area, code, act, ev) in enumerate(l["areas"]):
        x = 0.2 + i * 3.2
        s += (f"  \\draw[fill=phFill,draw=exLine,line width=1.2pt,rounded corners=0.2cm] ({x},0.4) rectangle ({x + 2.7},4.0);\n"
              f"  \\node[align=center,text width=2.5cm,text=exLine] at ({x + 1.35},3.35) {{\\footnotesize\\textbf{{{area}}}}};\n"
              f"  \\node[align=center,text=prText] at ({x + 1.35},2.55) {{\\large\\textbf{{{code}}}}};\n"
              f"  \\node[align=center,text width=2.5cm] at ({x + 1.35},1.75) {{\\footnotesize {act}}};\n"
              f"  \\node[align=center,text width=2.5cm,text=ctxText] at ({x + 1.35},0.85) {{\\scriptsize\\textit{{{ev}}}}};\n")
        if i < 4:
            s += f"  \\draw[draw=exLine,line width=1.1pt,-{{Triangle[length=5pt,width=5pt]}}] ({x + 2.7},2.2) -- ({x + 3.2},2.2);\n"
    x_mc, x_pl = 0.2 + 3 * 3.2 + 1.35, 0.2 + 1 * 3.2 + 1.35
    s += (f"  \\draw[draw=prLine,line width=1.1pt,dash pattern=on 4pt off 3pt,-{{Triangle[length=5pt,width=5pt]}}] ({x_mc},4.0) -- ({x_mc},5.0) -- ({x_pl},5.0) -- ({x_pl},4.0);\n"
          f"  \\node[text=prText,fill=white,inner sep=2pt] at ({(x_mc + x_pl) / 2},5.0) {{\\footnotesize {l['change']}}};\n")
    return s + FIG_TAIL


def fig3(l):
    s = FIG_HEAD.replace("@@H@@", "6.2")
    s += ("  \\node[draw=prLine,fill=prFill,line width=1.6pt,ellipse,minimum width=4.4cm,minimum height=2.0cm,align=center,text=prText] (V) at (8,3.1) "
          f"{{\\large\\textbf{{{l['center']}}}\\\\ {l['center2']}}};\n")
    boxes = [("F", 2.6, 5.0, l["fv"], l["fv2"]), ("S", 13.4, 5.0, l["sv"], l["sv2"]),
             ("P", 2.6, 1.2, l["pvv"], l["pvv2"]), ("C", 13.4, 1.2, l["cv"], l["cv2"])]
    for name, x, y, a, b in boxes:
        s += (f"  \\node[draw=exLine,fill=exFill,line width=1pt,rounded corners=0.15cm,align=center,text width=4.6cm,inner sep=5pt,text=exLine] ({name}) at ({x},{y}) "
              f"{{\\textbf{{{a}}}\\\\ {b}}};\n")
    for name in "FSPC":
        s += f"  \\draw[draw=exLine,line width=1pt,-{{Triangle[length=5pt,width=5pt]}}] ({name}) -- (V);\n"
    return s + FIG_TAIL


def fig4(l):
    s = FIG_HEAD.replace("@@H@@", "7.4")
    strips = [(l["t1"], 6.2), (l["t2"], 3.8), (l["t3"], 1.4)]
    for j, (title, yc) in enumerate(strips):
        s += (f"  \\node[anchor=west,text=exLine] at (0.2,{yc + 0.95}) {{\\textbf{{{title}}}}};\n"
              f"  \\draw[fill=ctxFill,draw=ctxLine,line width=0.9pt,rounded corners=0.15cm] (0.4,{yc - 0.55}) rectangle (4.4,{yc + 0.55});\n"
              f"  \\node[text=ctxText] at (2.4,{yc}) {{{l['phys']}}};\n"
              f"  \\draw[fill=exFill,draw=exLine,line width=1pt,rounded corners=0.15cm] (11.6,{yc - 0.55}) rectangle (15.6,{yc + 0.55});\n"
              f"  \\node[text=exLine] at (13.6,{yc}) {{{l['rep']}}};\n")
        if j == 0:
            s += (f"  \\draw[draw=ctxLine,line width=1.1pt,dash pattern=on 4pt off 3pt,-{{Triangle[length=5pt,width=5pt]}}] (4.4,{yc}) -- (11.6,{yc});\n"
                  f"  \\node[text=ctxText,fill=white,inner sep=2pt] at (8,{yc}) {{\\footnotesize {l['manual']}}};\n")
        elif j == 1:
            s += (f"  \\draw[draw=exLine,line width=1.2pt,-{{Triangle[length=5pt,width=5pt]}}] (4.4,{yc}) -- (11.6,{yc});\n"
                  f"  \\node[text=exLine,fill=white,inner sep=2pt] at (8,{yc}) {{\\footnotesize {l['auto']}}};\n")
        else:
            s += (f"  \\draw[draw=exLine,line width=1.2pt,-{{Triangle[length=5pt,width=5pt]}}] (4.4,{yc + 0.25}) -- (11.6,{yc + 0.25});\n"
                  f"  \\draw[draw=prLine,line width=1.4pt,-{{Triangle[length=5pt,width=5pt]}}] (11.6,{yc - 0.25}) -- (4.4,{yc - 0.25});\n"
                  f"  \\node[text=exLine,fill=white,inner sep=2pt] at (8,{yc + 0.25}) {{\\footnotesize {l['auto']}}};\n"
                  f"  \\node[text=prText,fill=white,inner sep=2pt] at (8,{yc - 0.25}) {{\\footnotesize {l['back']}}};\n")
    return s + FIG_TAIL


def fig5(l):
    s = FIG_HEAD.replace("@@H@@", "6.9")
    boxes = [(0.3, l["s1"], l["s1b"]), (5.85, l["s2"], l["s2b"]), (11.4, l["s3"], l["s3b"])]
    for x, a, b in boxes:
        s += (f"  \\draw[fill=exFill!50,draw=exLine,line width=1.2pt,rounded corners=0.2cm] ({x},2.7) rectangle ({x + 4.3},4.7);\n"
              f"  \\node[align=center,text=exLine] at ({x + 2.15},3.7) {{\\textbf{{{a}}}\\\\ {b}}};\n")
    s += ("  \\draw[draw=ctxLine,line width=1.2pt,-{Triangle[length=5pt,width=5pt]}] (4.6,3.7) -- (5.85,3.7);\n"
          "  \\draw[draw=ctxLine,line width=1.2pt,-{Triangle[length=5pt,width=5pt]}] (10.15,3.7) -- (11.4,3.7);\n"
          f"  \\node[text=ctxText,align=center] at (5.22,5.05) {{\\scriptsize {l['mat']}}};\n"
          f"  \\node[text=ctxText,align=center] at (10.78,5.05) {{\\scriptsize {l['rej']}}};\n"
          "  \\draw[draw=exLine,line width=1.1pt,dash pattern=on 4pt off 3pt,-{Triangle[length=5pt,width=5pt]}] (8.0,4.7) -- (8.0,6.0) -- (2.45,6.0) -- (2.45,4.7);\n"
          f"  \\node[text=exLine,fill=white,inner sep=2pt] at (5.2,6.0) {{\\footnotesize {l['qual']}}};\n"
          "  \\draw[fill=prFill,draw=prLine,line width=1.4pt,rounded corners=0.2cm] (0.3,0.2) rectangle (15.7,2.2);\n")
    for k, q in enumerate(l["q"]):
        s += f"  \\node[text=prText,align=center,text width=3.4cm] at ({2.2 + k * 3.85},1.2) {{\\footnotesize\\textbf{{{q}}}}};\n"
    return s + FIG_TAIL


FIGS = [fig1, fig2, fig3, fig4, fig5]


def main():
    (TEX / "figuras").mkdir(exist_ok=True)
    for lang in ("pt", "en"):
        for k, f in enumerate(FIGS, start=1):
            name = TEX / "figuras" / f"Fig{k}{L[lang]['fig_dir']}.tex"
            name.write_text(f(FIG_LABELS[lang]), encoding="utf-8")
        (TEX / L[lang]["out_report"]).write_text(build_report(lang), encoding="utf-8")
        (TEX / L[lang]["out_lessons"]).write_text(build_lessons(lang), encoding="utf-8")
    print("gerado em", TEX)


if __name__ == "__main__":
    main()
