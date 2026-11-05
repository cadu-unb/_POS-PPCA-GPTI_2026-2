"""Gera as versões "style2" dos relatórios (PT e EN) a partir dos .tex ABNT já existentes.

Uso (a partir de qualquer pasta):
    python ferramentas/gerar_style2.py

Para cada *_Relatorio_PT.tex e *_Report_EN.tex da pasta TEX, escreve *_style2.tex no
mesmo lugar, com o visual do relatório da P2A (P2B-RELATÓRIO.pdf): A4, Times, texto
justificado sem recuo, títulos azuis em sans, cabeçalho com filete, capa com a marca
da UnB e título em versalete verde, resumo e siglas em páginas romanas.
O conteúdo (texto, tabelas, figuras, referências) é o do .tex original; só muda a forma.
O script NÃO compila nada (ver compilar.sh). Rode gerar_tex.py antes, se mudar o Markdown.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

TEX = Path(__file__).resolve().parent.parent
ENTREGA = TEX.parents[1].name  # P3A, P3D, ...

AUTORES = [
    ("Filipe Alves de Sousa", "261108383"),
    ("Emanuel Brandão de Galvão Correia", "262114213"),
    ("Ruben Isaac Dias da Silva", "262115391"),
    ("Carlos Eduardo da Silva Papa", "261107680"),
]

ACRONIMOS = {"pmbok": "PMBOK", "sipa": "SIPA", "gpti": "GPTI", "lgpd": "LGPD", "dtc": "DTC",
             "ia": "IA", "ai": "AI", "gdpr": "GDPR", "ripd": "RIPD", "unb": "UnB", "ppca": "PPCA",
             "guide": "Guide", "standard": "Standard", "quem": "Quem", "who": "Who"}
LIGACOES = {"a", "o", "as", "os", "de", "do", "da", "dos", "das", "e", "em", "no", "na", "nos", "nas",
            "para", "por", "com", "como", "ao", "à", "the", "of", "for", "to", "in", "on", "and", "as",
            "an", "by", "with", "from", "a", "at", "or"}
# Títulos que precisam de maiúsculas que a regra automática não adivinha.
SECAO_FIXA = {
    "O DOMÍNIO PRIVACIDADE NA CONCENTRAÇÃO QUEM": "O domínio Privacidade na concentração Quem",
    "THE PRIVACY DOMAIN IN THE WHO CONCENTRATION": "The Privacy domain in the Who concentration",
}

L = {
    "pt": {
        "babel": "english,brazil", "autores": "Autores", "grupo": "Grupo Reciclagem 1 e Privacidade 2",
        "disc": "Disciplina", "disc_v": "Gestão de Projetos de TI (GPTI) -- PPCA/CIC/UnB",
        "prof": "Professor", "prof_v": "Dr. João Mello da Silva", "entrega": "Entrega",
        "cidade": r"Brasília -- DF, 2026", "sumario": "Sumário", "figs": "Lista de ilustrações",
        "tabs": "Lista de tabelas", "siglas": "Lista de abreviaturas e siglas", "refs": "Referências",
        "hl": f"GPTI/PPCA/UnB • Entrega {{E}} • Grupo SIPA Privacidade 2",
        "hr": "PMBOK 8 : relatório final da fase", "caps": "brazil",
    },
    "en": {
        "babel": "brazil,english", "autores": "Authors", "grupo": "Recycling 1 and Privacy 2 Groups",
        "disc": "Course", "disc_v": "IT Project Management (GPTI) -- PPCA/CIC/UnB",
        "prof": "Professor", "prof_v": "Dr. João Mello da Silva", "entrega": "Deliverable",
        "cidade": r"Brasília -- DF, 2026", "sumario": "Contents", "figs": "List of figures",
        "tabs": "List of tables", "siglas": "List of abbreviations and acronyms", "refs": "References",
        "hl": "GPTI/PPCA/UnB • Deliverable {E} • SIPA Privacy 2 Group",
        "hr": "PMBOK 8 : final phase report", "caps": "english",
    },
}


def sentence_case(s: str) -> str:
    """Caixa alta -> primeira letra maiúscula, resto minúsculo; siglas e nomes próprios preservados."""
    if s in SECAO_FIXA:
        return SECAO_FIXA[s]
    parts = re.split(r"(\\[A-Za-z]+|[{}])", s)
    out, first = [], True
    for p in parts:
        if re.fullmatch(r"\\[A-Za-z]+|[{}]", p) or not p:
            out.append(p)
            continue
        words = re.split(r"(\W+)", p.lower())
        for i, w in enumerate(words):
            if w.lower() in ACRONIMOS:
                words[i] = ACRONIMOS[w.lower()]
            elif w and first and w[0].isalpha():
                words[i] = w[0].upper() + w[1:]
            if w and w[0].isalpha():
                first = False
        out.append("".join(words))
    return "".join(out)


def title_case(s: str) -> str:
    words = re.split(r"(\s+)", s.lower())
    n = 0
    for i, w in enumerate(words):
        if not w.strip():
            continue
        n += 1
        core = re.sub(r"\W", "", w)
        if core in ACRONIMOS:
            words[i] = w.replace(core, ACRONIMOS[core])
        elif any(ch.isdigit() for ch in w):
            words[i] = w.upper()
        elif n > 1 and core in LIGACOES:
            continue
        else:
            words[i] = w[0].upper() + w[1:]
    return "".join(words)


def grab_braced(text: str, start: int) -> tuple[str, int]:
    """Texto do grupo {...} que abre em text[start] == '{'; devolve (conteúdo, índice após '}')."""
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
    raise ValueError("chaves desbalanceadas")


def move_captions(body: str) -> str:
    """Nas figuras, a legenda vai para baixo da imagem (padrão da P2A); nas tabelas fica em cima."""
    def fix(m: re.Match) -> str:
        env = m.group(0)
        cap = re.search(r"\\caption\{", env)
        if not cap:
            return env
        content, end = grab_braced(env, cap.end() - 1)
        label = re.match(r"\\label\{[^}]*\}", env[end:])
        cap_all = "\\caption{" + content + "}" + (label.group(0) if label else "")
        env = env[:cap.start()] + env[end + (len(label.group(0)) if label else 0):]
        # insere depois da linha \includegraphics (ou antes de \fontetab, ou antes do \end)
        img = re.search(r"\\includegraphics[^\n]*\n", env)
        if img:
            return env[:img.end()] + cap_all + "\n" + env[img.end():]
        return env.replace("\\end{figure}", cap_all + "\n\\end{figure}")
    return re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", fix, body, flags=re.S)


def convert(src: Path, lang: str) -> str:
    t = L[lang]
    text = src.read_text(encoding="utf-8")
    pre, rest = text.split(r"\begin{document}", 1)

    # macros do preâmbulo original que o corpo usa (cores, citações numéricas, etc.)
    keep = []
    for ln in pre.splitlines():
        if re.match(r"\\(definecolor|newcommand|defref|newcolumntype|providecommand|Urlmuskip)", ln) \
                and "fontetab" not in ln and "integrantes" not in ln:
            keep.append(ln)

    cover_title = re.search(r"\\vspace\{3cm\}\s*\\textbf\{(.*?)\}\s*\\vfill", rest, re.S).group(1).strip()
    resumos = re.findall(r"\\begin\{resumo\}.*?\\end\{resumo\}", rest, re.S)
    siglas_m = re.search(r"\\begingroup\s*\\SingleSpacing\s*\\begin\{center\}\\textbf\{LIST[^}]*\}\\end\{center\}.*?\\endgroup",
                         rest, re.S)
    siglas = re.sub(r"\\begin\{center\}\\textbf\{LIST[^}]*\}\\end\{center\}",
                    "\\\\section*{" + t["siglas"] + "}", siglas_m.group(0))
    body_start = siglas_m.end()
    refs_at = re.search(r"\\clearpage\s*\\begin\{center\}\s*\\textbf\{REFER[^}]*\}\s*\\end\{center\}", rest)
    body = rest[body_start:refs_at.start()]
    refs = rest[refs_at.end():].replace(r"\end{document}", "").strip()

    body = re.sub(r"^\s*\\clearpage\s*", "", body)
    body = re.sub(r"\\setcounter\{table\}\{0\}\s*", "", body)
    body = re.sub(r"\\section\{(.*)\}", lambda m: "\\section{" + sentence_case(m.group(1)) + "}", body)
    body = move_captions(body)

    resumos = [re.sub(r"\\begin\{resumo\}(\[[^\]]*\])?", lambda m: "\\begin{resumo}" + (m.group(1) or ""), r) for r in resumos]

    ctitle = title_case(cover_title)
    hl = t["hl"].replace("{E}", ENTREGA)
    rows = []
    for i in range(0, len(AUTORES), 2):
        a, b = AUTORES[i], AUTORES[i + 1]
        rows.append(f"{a[0]} & {a[1]} & {b[1]} & {b[0]}")
    autores_tab = "\\\\\n    ".join(rows)

    return f"""% =============================================================================
% {src.stem}_style2 -- versão alternativa no estilo do relatório da P2A (P2B-RELATÓRIO.pdf)
% ARQUIVO GERADO por ferramentas/gerar_style2.py a partir de {src.name}.
% Para mudar o conteúdo, edite o original e gere de novo, ou edite este .tex à mão.
% Figuras esperadas em out/ (compiladas a partir de figuras/); marca em figuras/marca_unb.png.
% =============================================================================
\\documentclass[11pt,a4paper]{{article}}

\\usepackage[T1]{{fontenc}}
\\usepackage[utf8]{{inputenc}}
\\usepackage{{mathptmx}}
\\usepackage[scaled=.92]{{helvet}}
\\usepackage[{t['babel']}]{{babel}}
\\usepackage[a4paper,margin=2.5cm,top=2.6cm,bottom=2.4cm,headheight=14pt]{{geometry}}
\\usepackage{{amsmath}}
\\usepackage{{graphicx}}
\\usepackage[table]{{xcolor}}
\\usepackage{{array,tabularx,longtable,booktabs}}
\\usepackage{{url}}
\\usepackage[expansion=false]{{microtype}}
\\usepackage{{titlesec,fancyhdr,caption,tocloft}}
\\usepackage[colorlinks=true,linkcolor=Link,citecolor=Link,urlcolor=Link]{{hyperref}}
\\Urlmuskip=0mu plus 1mu\\relax

\\definecolor{{DarkBlue}}{{rgb}}{{0.12,0.15,0.60}}
\\definecolor{{DarkGreen}}{{rgb}}{{0.10,0.50,0.10}}
\\definecolor{{Link}}{{rgb}}{{0.10,0.25,0.75}}

% Macros do original (cores das figuras-tabela, citações numéricas)
{chr(10).join(keep)}

\\newcommand{{\\SingleSpacing}}{{}}
\\newcommand{{\\onelineskip}}{{\\baselineskip}}
\\newcommand{{\\fontetab}}[1]{{\\par\\vspace{{3pt}}{{\\small\\noindent {'Fonte' if lang == 'pt' else 'Source'}: #1\\par}}}}
\\newenvironment{{resumo}}[1][{'Resumo' if lang == 'pt' else 'Abstract'}]{{\\section*{{#1}}\\noindent\\ignorespaces}}{{\\bigskip}}

\\setlength{{\\parindent}}{{0pt}}
\\setlength{{\\parskip}}{{5pt plus 1pt}}
\\setlength{{\\emergencystretch}}{{3em}}
\\setcounter{{secnumdepth}}{{3}}
\\setcounter{{tocdepth}}{{2}}
\\renewcommand{{\\arraystretch}}{{1.2}}

\\titleformat{{\\section}}{{\\sffamily\\Large\\color{{DarkBlue}}}}{{\\thesection}}{{0.8em}}{{}}
\\titleformat{{\\subsection}}{{\\sffamily\\large\\color{{DarkBlue}}}}{{\\thesubsection}}{{0.8em}}{{}}
\\titleformat{{\\subsubsection}}{{\\sffamily\\normalsize\\color{{DarkBlue}}}}{{\\thesubsubsection}}{{0.8em}}{{}}
\\titlespacing*{{\\section}}{{0pt}}{{16pt plus 2pt}}{{7pt}}
\\titlespacing*{{\\subsection}}{{0pt}}{{12pt plus 2pt}}{{5pt}}
\\titlespacing*{{\\subsubsection}}{{0pt}}{{9pt plus 2pt}}{{4pt}}

\\captionsetup{{font=small,labelfont=bf,labelsep=colon}}
\\addto\\captions{t['caps']}{{\\renewcommand{{\\contentsname}}{{{t['sumario']}}}\\renewcommand{{\\listfigurename}}{{{t['figs']}}}\\renewcommand{{\\listtablename}}{{{t['tabs']}}}}}
\\renewcommand{{\\cftsecfont}}{{\\bfseries}}
\\renewcommand{{\\cftsecpagefont}}{{\\bfseries}}
\\renewcommand{{\\cftsecleader}}{{\\cftdotfill{{\\cftdotsep}}}}

\\pagestyle{{fancy}}
\\fancyhf{{}}
\\fancyhead[L]{{\\sffamily\\small {hl}}}
\\fancyhead[R]{{\\sffamily\\small {t['hr']}}}
\\fancyfoot[C]{{\\small\\thepage}}
\\renewcommand{{\\headrulewidth}}{{0.4pt}}

\\begin{{document}}

% ------------------------------- CAPA ----------------------------------------
\\thispagestyle{{empty}}
\\begin{{center}}
\\vspace*{{0.5cm}}
\\includegraphics[width=0.5\\textwidth]{{figuras/marca_unb.png}}

\\vspace{{2.2cm}}
{{\\LARGE\\color{{DarkGreen}}\\textsc{{{ctitle}}}\\par}}
\\vspace{{1.4cm}}

{{\\small
\\textbf{{{t['autores']} -- {t['grupo']}}}\\\\[3pt]
\\begin{{tabular}}{{@{{}}l@{{\\hspace{{0.5cm}}}}r@{{\\hspace{{1.5cm}}}}r@{{\\hspace{{0.5cm}}}}l@{{}}}}
    {autores_tab}
\\end{{tabular}}\\\\[6pt]
\\textbf{{{t['disc']}:}} {t['disc_v']}\\\\
\\textbf{{{t['prof']}:}} {t['prof_v']}\\\\
\\textbf{{{t['entrega']}:}} {ENTREGA} -- {'Grupo SIPA Privacidade 2' if lang == 'pt' else 'SIPA Privacy 2 Group'}\\\\[6pt]
{t['cidade']}\\par}}
\\end{{center}}
\\clearpage
\\pagenumbering{{roman}}
\\setcounter{{page}}{{2}}

{chr(10).join(resumos)}
\\clearpage

{siglas}
\\clearpage

\\tableofcontents
\\bigskip
\\listoffigures
\\bigskip
\\listoftables
\\clearpage
\\pagenumbering{{arabic}}
\\setcounter{{table}}{{0}}

{body.strip()}

\\clearpage
\\section*{{{t['refs']}}}
\\addcontentsline{{toc}}{{section}}{{{t['refs']}}}
{refs}

\\end{{document}}
"""


def main() -> None:
    n = 0
    for pattern, lang in (("*_Relatorio_PT.tex", "pt"), ("*_Report_EN.tex", "en")):
        for src in sorted(TEX.glob(pattern)):
            out = src.with_name(src.stem + "_style2.tex")
            out.write_text(convert(src, lang), encoding="utf-8")
            print("gerado", out.name)
            n += 1
    print(f"{n} arquivo(s).")


if __name__ == "__main__":
    main()
