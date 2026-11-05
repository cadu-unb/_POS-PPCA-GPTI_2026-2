"""Ajustes de layout das tabelas do relatório, aplicados sobre o .tex que o gerar_tex.py produz.

Antes, estes ajustes eram feitos à mão nos .tex gerados e se perdiam a cada regeneração. Agora o
gerar_tex.py chama apply() logo depois de montar o relatório, então a regeneração reproduz o resultado.
A função é idempotente (aplicar duas vezes dá o mesmo resultado).

P3A  Tabela 3 (processos propostos): coluna "Área" com siglas IN/PL/EX/MC/CL, legenda na linha "Fonte" e
     larguras reequilibradas.
     Tabela 7 (resultados e verificação): larguras para a coluna "Processos" caber na margem.
     Tabela 8 (aderência às áreas de foco): coluna "Processos" mais larga; evidências em itens, um por linha.
P3D  Tabela 7 (contagem por área de foco): três colunas (sigla, área, processos) com linha de total.
     Tabela 12 (concentrações): colunas numéricas centralizadas e linha de total.
"""

from __future__ import annotations

import re
from pathlib import Path

KIND = Path(__file__).resolve().parents[3].name  # "P3A" ou "P3D"

AREAS = {
    "pt": [("Iniciação", "IN"), ("Planejamento", "PL"), ("Execução", "EX"),
           ("Monitoramento e controle", "MC"), ("Encerramento", "CL")],
    "en": [("Initiating", "IN"), ("Planning", "PL"), ("Executing", "EX"),
           ("Monitoring and controlling", "MC"), ("Monitoring and Controlling", "MC"), ("Closing", "CL")],
}
LEGEND = {
    "pt": "Áreas de foco: IN Iniciação; PL Planejamento; EX Execução; MC Monitoramento e controle; CL Encerramento.",
    "en": "Focus Areas: IN Initiating; PL Planning; EX Executing; MC Monitoring and Controlling; CL Closing.",
}
BUL = r"\newline$\bullet$~"


def _widths(line: str, new: list[int]) -> str:
    it = iter(new)
    return re.sub(r"\*(\d+)/1000", lambda m: "*%d/1000" % next(it), line)


def _span(lines: list[str], label: str) -> tuple[int, int]:
    """(índice do \\begin{longtable}, índice do \\end{longtable}) da tabela com o \\label dado."""
    k = next(i for i, ln in enumerate(lines) if f"\\label{{{label}}}" in ln)
    return k - 1, next(i for i in range(k, len(lines)) if lines[i].startswith(r"\end{longtable}"))


def _p3a(lines: list[str], lang: str) -> None:
    # Tabela 3
    a, b = _span(lines, "tab:t3")
    lines[a] = _widths(lines[a], [210, 80, 490, 220])
    for i in range(a, b):
        ln = lines[i].replace(r"\textbf{Área de foco principal}", r"\textbf{Área}") \
                     .replace(r"\textbf{Primary Focus Area}", r"\textbf{Area}")
        if re.match(r"\\textbf\{P[1-8] ", ln):
            for full, code in AREAS[lang]:
                ln = ln.replace(" & %s & " % full, " & %s & " % code, 1)
        lines[i] = ln
    j = next(i for i in range(b, b + 4) if lines[i].startswith(r"\fontetab"))
    if "IN " not in lines[j]:
        lines[j] = lines[j][:-1] + " " + LEGEND[lang] + "}"

    # Tabela 7
    a, b = _span(lines, "tab:t7")
    lines[a] = _widths(lines[a], [230, 420, 230, 120])

    # Tabela 8
    a, b = _span(lines, "tab:t8")
    lines[a] = _widths(lines[a], [150, 320, 100, 430])
    for i in range(a, b):
        ln = lines[i]
        for old, new in ((r"\textbf{Processos da proposta}", r"\textbf{Processos}"),
                         (r"\textbf{Processes in the proposal}", r"\textbf{Processes}")):
            ln = ln.replace(old, new)
        if re.match(r"\\textbf\{(IN|PL|EX|MC|CL) ", ln):
            cells = ln.split(" & ")
            last, tail = cells[-1], ""
            m = re.search(r"\\\\\[3pt\]\s*$", last)
            if m:
                tail, last = last[m.start():], last[:m.start()]
            items = [s.strip() for s in last.split(";")]
            if len(items) > 1 and BUL not in last and r"$\bullet$" not in last:
                items = [s[:1].upper() + s[1:] for s in items]
                last = r"$\bullet$~" + BUL.join(items)
            cells[-1] = last + tail
            ln = " & ".join(cells)
        lines[i] = ln


def _p3d(lines: list[str], lang: str) -> None:
    pt = lang == "pt"
    # Tabela 7: sigla | área de foco | processos, com total
    a, b = _span(lines, "tab:t7")
    if "p{1.6cm}" not in lines[a]:
        lines[a] = (r"\begin{longtable}{@{}>{\raggedright\arraybackslash}p{1.6cm}>{\raggedright\arraybackslash}p{6.4cm}"
                    r">{\centering\arraybackslash}p{3.2cm}@{}}")
        head = (r"\textbf{Sigla} & \textbf{Área de foco} & \textbf{Processos no PMBOK 8}\\" if pt
                else r"\textbf{Code} & \textbf{Focus Area} & \textbf{Processes in PMBOK 8}\\")
        names = ({"IN": "Iniciação", "PL": "Planejamento", "EX": "Execução", "MC": "Monitoramento e controle",
                  "CL": "Encerramento"} if pt else
                 {"IN": "Initiating", "PL": "Planning", "EX": "Executing", "MC": "Monitoring and Controlling",
                  "CL": "Closing"})
        out = []
        for i in range(a, b + 1):
            ln = lines[i]
            if ln.startswith(r"\textbf{Área}") or ln.startswith(r"\textbf{Area}"):
                ln = head
            m = re.match(r"(IN|PL|EX|MC|CL) & \\textbf\{(\d+)\}(\\\\\[3pt\])$", ln)
            if m:
                ln = "%s & %s & %s%s" % (m.group(1), names[m.group(1)], m.group(2), m.group(3))
            if ln.startswith(r"\end{longtable}"):
                out.append(r"\hline")
                out.append(r" & \textbf{Total} & \textbf{40}\\[3pt]")
            out.append(ln)
        lines[a:b + 1] = out

    # Tabela 12: colunas 3 e 4 centralizadas e linha de total
    a, b = _span(lines, "tab:t12")
    if r"\textbf{Total}" not in "\n".join(lines[a:b + 1]):
        n = {"i": 0}

        def center(m: re.Match) -> str:
            n["i"] += 1
            return r">{\centering\arraybackslash}" if n["i"] >= 3 else m.group(0)

        lines[a] = re.sub(r">\{\\(?:raggedright|raggedleft|centering)\\arraybackslash\}", center, lines[a])
        total = (r"\textbf{Total} & Sete domínios & \textbf{40} & \\[3pt]" if pt
                 else r"\textbf{Total} & Seven domains & \textbf{40} & \\[3pt]")
        k = next(i for i in range(a, b + 1) if lines[i].startswith(r"\end{longtable}"))
        lines[k:k] = [r"\hline", total]


def apply(text: str, lang: str) -> str:
    lines = text.split("\n")
    (_p3a if KIND == "P3A" else _p3d)(lines, lang)
    return "\n".join(lines)
