"""Aviso de uso de inteligência artificial (declaração, considerações finais e nota dos pôsteres).

Norma de referência: COPE, "Authorship and AI tools" (position statement, 13/02/2023). Ela diz que
ferramentas de IA não podem ser autoras, que quem as usa em redação, imagens/figuras ou dados deve
declarar o uso, e que os autores respondem pelo conteúdo, inclusive o produzido com IA.
https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools

Onde o aviso aparece:
- relatórios: subseção "Uso de inteligência artificial" no fim da conclusão (considerações finais);
  caixa opcional na capa (desligada por padrão). No LaTeX, duas chaves no preâmbulo:
      \\avisofinaltrue / \\avisofinalfalse   (subseção final)
      \\avisocapatrue  / \\avisocapafalse    (caixa na capa)
- pôsteres: nota de rodapé curta;
- lições aprendidas: uma linha pequena no fim do arquivo (sem destaque).

Uso (a partir de qualquer pasta; idempotente: remove e reinsere):
    python ferramentas/aviso_ia.py            # aplica em MD, pôsteres (TEX e style2), relatórios e lições
    python ferramentas/aviso_ia.py --remover  # remove tudo que está entre os marcadores AVISO-IA

O texto vive só aqui. gerar_tex.py e gerar_style2.py importam este módulo, então o aviso
sobrevive à regeneração dos .tex. Para localizar: grep -rn "AVISO-IA" _grupo/*/entregas
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

URL = "https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools"
URL_SHORT = "publicationethics.org/guidance/cope-position/authorship-and-ai-tools"
INI, FIM = "AVISO-IA:INICIO", "AVISO-IA:FIM"
KIND = Path(__file__).resolve().parents[3].name          # "P3A" ou "P3D"
PMI_NUM = {("P3A", "pt"): 13, ("P3A", "en"): 14, ("P3D", "pt"): 4, ("P3D", "en"): 5}  # nº do PMBOK 8 nas listas

TXT = {
    "pt": {
        "title": "Declaração de uso de inteligência artificial",
        "sub": "Uso de inteligência artificial",
        "body": ("Foi utilizada IA generativa (ChatGPT Astral 6 Sol e Sonnet 5.5, ambos no modo alto) como apoio "
                 "à revisão de texto, à formatação, à criação de figuras e à formulação de tabelas. A IA não é "
                 "autora: o grupo é responsável pelo conteúdo, conforme a posição do COPE sobre autoria e "
                 "ferramentas de IA (COPE, 2023)."),
        "ref": ("COMMITTEE ON PUBLICATION ETHICS (COPE). {i}Authorship and AI tools: COPE position statement{e}. "
                "13 fev. 2023. Disponível em: {u}."),
        "short": ("Uso de IA: IA generativa (ChatGPT Astral 6 Sol e Sonnet 5.5, modo alto) apoiou a revisão de "
                  "texto, a formatação, a criação de figuras e a formulação de tabelas. O grupo é responsável "
                  "pelo conteúdo (COPE, 2023: {u})."),
        "short_label": "Uso de IA:",
        "mini": ("Uso de IA: IA generativa (ChatGPT Astral 6 Sol e Sonnet 5.5, modo alto) apoiou a revisão de "
                 "texto, a formatação, a criação de figuras e a formulação de tabelas; o grupo é responsável "
                 "pelo conteúdo (COPE, 2023)."),
        # subseção das considerações finais
        "f_intro": ("Este trabalho usou IA generativa (ChatGPT Astral 6 Sol e Sonnet 5.5, ambos no modo alto) como "
                    "apoio à revisão de texto, à formatação, à criação de figuras e à formulação de tabelas. "
                    "Seguimos a posição do COPE sobre autoria e ferramentas de IA (COPE, 2023), que pede declarar o "
                    "uso e manter a responsabilidade com os autores. Três pontos orientam a leitura desta declaração."),
        "f_fonte_h": "A IA não é autora nem fonte.",
        "f_fonte": ("Nenhuma afirmação sobre o PMBOK 8, a LGPD ou a literatura deve ser aceita porque um modelo de "
                    "linguagem a produziu. Cada uma indica a sua fonte (seção, tabela, norma ou referência) para que "
                    "quem lê possa conferi-la."),
        "f_risco_h": "Riscos conhecidos desse uso.",
        "f_risco": ("Modelos de linguagem podem inventar referências, trocar números e suavizar ressalvas, e a "
                    "tradução entre português e inglês pode deslocar sentidos técnicos. Por isso, referências, "
                    "contagens e nomes de processos são os pontos que mais merecem conferência contra as fontes, e "
                    "este relatório não substitui a leitura da edição do PMBOK 8."),
        "f_resp_h": "Responsabilidade.",
        "f_resp": ("O grupo responde pelo conteúdo, inclusive pelas partes produzidas com apoio de IA. A declaração "
                   "descreve categorias de uso, não registra cada interação, e o esforço da equipe não foi medido."),
        "f_tema_h": "Relação com o tema.",
        "f_tema": {
            "P3A": ("O trabalho é documental e o cenário de reciclagem é hipotético; não houve coleta nem "
                    "tratamento de dados pessoais de terceiros. Em um projeto real que usasse IA sobre dados de "
                    "pessoas, esse uso entraria no inventário de dados e na avaliação de impacto (P1 e P3)."),
            "P3D": ("O PMBOK 8 não organiza o uso de IA como domínio, mas dedica a ela um apêndice (X3) {pmi}. Um "
                    "projeto que a adote deve tratá-la como qualquer outro elemento a adaptar (*tailoring*), e não "
                    "como exceção ao método."),
        },
    },
    "en": {
        "title": "Statement on the use of artificial intelligence",
        "sub": "Use of artificial intelligence",
        "body": ("Generative AI (ChatGPT Astral 6 Sol and Sonnet 5.5, both in high mode) was used to support text "
                 "editing, formatting, figure creation, and table drafting. AI is not an author: the group is "
                 "responsible for the content, in line with the COPE position on authorship and AI tools "
                 "(COPE, 2023)."),
        "ref": ("COMMITTEE ON PUBLICATION ETHICS (COPE). {i}Authorship and AI tools: COPE position statement{e}. "
                "13 Feb. 2023. Available at: {u}."),
        "short": ("AI use: generative AI (ChatGPT Astral 6 Sol and Sonnet 5.5, high mode) supported text editing, "
                  "formatting, figure creation, and table drafting. The group is responsible for the content "
                  "(COPE, 2023: {u})."),
        "short_label": "AI use:",
        "mini": ("AI use: generative AI (ChatGPT Astral 6 Sol and Sonnet 5.5, high mode) supported text editing, "
                 "formatting, figure creation, and table drafting; the group is responsible for the content "
                 "(COPE, 2023)."),
        "f_intro": ("This work used generative AI (ChatGPT Astral 6 Sol and Sonnet 5.5, both in high mode) to support "
                    "text editing, formatting, figure creation, and table drafting. We follow the COPE position on "
                    "authorship and AI tools (COPE, 2023), which asks authors to disclose the use and to remain "
                    "responsible for the work. Three points guide how to read this statement."),
        "f_fonte_h": "AI is neither an author nor a source.",
        "f_fonte": ("No claim about PMBOK 8, the LGPD, or the literature should be accepted because a language model "
                    "produced it. Each claim points to its source (section, table, regulation, or reference) so that "
                    "readers can check it."),
        "f_risco_h": "Known risks of this use.",
        "f_risco": ("Language models can invent references, swap numbers, and soften caveats, and translation "
                    "between Portuguese and English can shift technical meanings. References, counts, and process "
                    "names are therefore the points that most deserve checking against the sources, and this report "
                    "does not replace reading the PMBOK 8 edition."),
        "f_resp_h": "Responsibility.",
        "f_resp": ("The group is responsible for the content, including the parts produced with AI support. The "
                   "statement describes categories of use, does not log each interaction, and the team's effort "
                   "was not measured."),
        "f_tema_h": "Relation to the topic.",
        "f_tema": {
            "P3A": ("The work is documentary and the recycling scenario is hypothetical; no personal data of third "
                    "parties was collected or processed. In a real project that used AI on data about people, that "
                    "use would enter the data inventory and the impact assessment (P1 and P3)."),
            "P3D": ("PMBOK 8 does not organize the use of AI as a domain, but it devotes an appendix (X3) to it {pmi}. "
                    "A project that adopts AI should treat it like any other element to tailor, not as an exception "
                    "to the method."),
        },
    },
}


def _ref(lang: str, fmt: str) -> str:
    """Referência completa; fmt = 'md' ou 'tex'."""
    t = TXT[lang]["ref"]
    if fmt == "md":
        return t.format(i="*", e="*", u=f"<{URL}>")
    return t.format(i=r"\textit{", e="}", u=r"\url{" + URL + "}")


# ---------------------------------------------------------------- Markdown
def md_final(lang: str, num: int) -> str:
    """Subseção '### N.1 Uso de inteligência artificial' (considerações finais, seção N)."""
    t = TXT[lang]
    tema = t["f_tema"][KIND].format(pmi=f"[{PMI_NUM[(KIND, lang)]}]")
    return (f"<!-- {INI} (subseção final; apagar tudo entre os marcadores a remove) -->\n"
            f"### {num}.1 {t['sub']}\n\n{t['f_intro']}\n\n"
            f"**{t['f_fonte_h']}** {t['f_fonte']}\n\n**{t['f_risco_h']}** {t['f_risco']}\n\n"
            f"**{t['f_resp_h']}** {t['f_resp']}\n\n**{t['f_tema_h']}** {tema}\n\n"
            f"{_ref(lang, 'md')}\n<!-- {FIM} -->\n\n")


def md_poster(lang: str) -> str:
    t = TXT[lang]
    short = t["short"].format(u=f"<{URL}>").replace(t["short_label"], f"**{t['short_label']}**", 1)
    return f"\n<!-- {INI} -->\n---\n*{short}*\n<!-- {FIM} -->\n"


def md_mini(lang: str) -> str:
    return f"\n<!-- {INI} -->\n*{TXT[lang]['mini']}*\n<!-- {FIM} -->\n"


# ------------------------------------------------------------------- LaTeX
def flags_tex() -> str:
    """Chaves do preâmbulo: true/false."""
    return (f"% {INI} (chaves: trocar true/false)\n"
            "\\newif\\ifavisocapa   \\avisocapafalse    % caixa de declaração na capa\n"
            "\\newif\\ifavisofinal  \\avisofinaltrue    % subseção \"Uso de inteligência artificial\" no fim da conclusão\n"
            f"% {FIM}\n")


def tex_box(lang: str, flag: str | None = None) -> str:
    """Caixa para a capa do relatório; com flag, só aparece se \\if<flag> for verdadeiro."""
    t = TXT[lang]
    opn = f"\\if{flag}\n" if flag else ""
    cls = "\\fi\n" if flag else ""
    return (f"% {INI} (caixa na capa; liga com \\avisocapatrue no preâmbulo)\n{opn}"
            r"\begin{center}\fbox{\parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}{\SingleSpacing\small\noindent"
            f"\\textbf{{{t['title']}.}} {t['body']}\\par\\smallskip\\noindent {_ref(lang, 'tex')}}}}}\\end{{center}}\n"
            f"{cls}% {FIM}\n")


def tex_final(lang: str) -> str:
    t = TXT[lang]
    tema = t["f_tema"][KIND].format(pmi=r"\cit{pmi}").replace("*tailoring*", r"\textit{tailoring}")
    return (f"% {INI} (subseção final; liga/desliga com \\avisofinaltrue/\\avisofinalfalse no preâmbulo)\n"
            f"\\ifavisofinal\n\\subsection{{{t['sub']}}}\n\n{t['f_intro']}\n\n"
            f"\\textbf{{{t['f_fonte_h']}}} {t['f_fonte']}\n\n\\textbf{{{t['f_risco_h']}}} {t['f_risco']}\n\n"
            f"\\textbf{{{t['f_resp_h']}}} {t['f_resp']}\n\n\\textbf{{{t['f_tema_h']}}} {tema}\n\n"
            f"\\begingroup\\small\\noindent {_ref(lang, 'tex')}\\par\\endgroup\n\\fi\n% {FIM}\n\n")


def tex_mini(lang: str) -> str:
    return (f"% {INI}\n\\vspace{{\\onelineskip}}\n"
            f"{{\\footnotesize\\SingleSpacing\\noindent\\textit{{{TXT[lang]['mini']}}}\\par}}\n% {FIM}\n")


def _short_tex(lang: str) -> str:
    t = TXT[lang]
    s = t["short"].format(u=r"\texttt{" + URL_SHORT + "}")
    return s.replace(t["short_label"], "\\textbf{" + t["short_label"] + "}", 1)


def poster_orig(lang: str) -> str:
    return (f"% {INI}\n\\vspace{{2mm}}\n"
            "{\\fontsize{10.5}{13}\\selectfont\\color{ctxText}" + _short_tex(lang) + "\\par}\n"
            f"% {FIM}\n")


def poster_style2(lang: str) -> str:
    return (f"% {INI}\n\\begin{{textblock}}{{23}}(0,11.4)\n"
            "{\\small\\noindent " + _short_tex(lang) + "\\par}\n\\end{textblock}\n"
            f"% {FIM}\n")


# -------------------------------------------------------------- injeções
def remove(text: str) -> str:
    """Tira tudo entre os marcadores (MD e TEX). Também leva o '---' que o pôster em MD põe antes."""
    text = re.sub(r"(?:---\n)?<!-- %s.*?<!-- %s -->\n?(?:\n)?" % (INI, FIM), "", text, flags=re.S)
    return re.sub(r"%% %s.*?%% %s\n?(?:\n)?" % (INI, FIM), "", text, flags=re.S)


_FINAL_MD = re.compile(r"^## \d+\. (Relatório final do trabalho|Final report of the work)", re.M)
_FINAL_TEX = re.compile(r"^\\section\{(relatório final do trabalho|final report of the work)\}", re.M | re.I)


def inject_md_report(text: str, lang: str) -> str:
    m = _FINAL_MD.search(text)
    if not m:
        return text
    prev = re.findall(r"^## (\d+)\.", text[:m.start()], re.M)  # seção de conclusão = a anterior
    return text[:m.start()] + md_final(lang, int(prev[-1])) + text[m.start():]


def inject_md_lessons(text: str, lang: str) -> str:
    return text.rstrip("\n") + "\n" + md_mini(lang)


def inject_md_poster(text: str, lang: str) -> str:
    return text.rstrip("\n") + "\n" + md_poster(lang)


def inject_final_tex(text: str, lang: str) -> str:
    """Subseção final (com chave \\ifavisofinal) antes da seção 'Relatório final do trabalho'."""
    m = _FINAL_TEX.search(text)
    return text[:m.start()] + tex_final(lang) + text[m.start():] if m else text


def inject_report_tex(text: str, lang: str) -> str:
    """Relatório abntex2: chaves no preâmbulo, caixa (opcional) na capa e subseção final."""
    text = remove(text)
    m = re.search(r"^\\newcommand\{\\integrantes\}\{.*\}\s*$", text, re.M)
    if m:
        text = text[:m.end()] + "\n" + flags_tex() + text[m.end():]
    block = tex_box(lang, "avisocapa").replace("\n", "\n\\vspace{1.2cm}\n", 1)  # espaço dentro dos marcadores
    text = text.replace("\n\\vfill\n", "\n" + block + "\\vfill\n", 1)
    return inject_final_tex(text, lang)


def inject_lessons_tex(text: str, lang: str) -> str:
    """Lições: uma linha pequena no fim, sem destaque."""
    text = remove(text)
    k = text.rfind("\\end{document}")
    return text[:k] + tex_mini(lang) + "\n" + text[k:]


def inject_poster_orig(text: str, lang: str) -> str:
    text = remove(text)
    m = re.search(r"^\}% (fim do|end of) \\parbox", text, re.M)
    return text[:m.start()] + poster_orig(lang) + "\n" + text[m.start():]


def inject_poster_style2(text: str, lang: str) -> str:
    text = remove(text)
    k = text.rfind("\\end{document}")
    return text[:k] + poster_style2(lang) + "\n" + text[k:]


# ------------------------------------------------------------------- CLI
def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    tex = Path(__file__).resolve().parent.parent
    md = tex.parent / "MD"
    n = f"{KIND}_Privacidade2_"
    pairs = [("pt", "Relatorio_PT", "Licoes_PT", "Poster_PT"), ("en", "Report_EN", "Lessons_EN", "Poster_EN")]
    undo = "--remover" in sys.argv

    def edit(path: Path, fn) -> None:
        if not path.exists():
            print("  (não existe)", path.name)
            return
        s = path.read_text(encoding="utf-8")
        new = remove(s) if undo else fn(remove(s))
        if new != s:
            path.write_text(new, encoding="utf-8")
            print("  ok", path.name)

    for lang, rel, les, pos in pairs:
        edit(md / f"{n}{rel}.md", lambda s, l=lang: inject_md_report(s, l))
        edit(md / f"{n}{les}.md", lambda s, l=lang: inject_md_lessons(s, l))
        edit(md / f"{n}{pos}.md", lambda s, l=lang: inject_md_poster(s, l))
        edit(tex / f"{n}{rel}.tex", lambda s, l=lang: inject_report_tex(s, l))
        edit(tex / f"{n}{les}.tex", lambda s, l=lang: inject_lessons_tex(s, l))
        edit(tex / f"{n}{pos}.tex", lambda s, l=lang: inject_poster_orig(s, l))
        edit(tex / f"{n}{pos}_style2.tex", lambda s, l=lang: inject_poster_style2(s, l))
    print("feito" if not undo else "removido")


if __name__ == "__main__":
    main()
