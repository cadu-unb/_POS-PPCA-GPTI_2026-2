"""Expande números de buscas em expressões para a Web of Science."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


# Edite este dicionário quando uma busca mudar. Preserve as chaves antigas
# para conseguir reproduzir as contagens já registradas.
QUERIES: dict[int, str] = {
    1: 'TS=("solid waste*" OR "municipal waste*" OR "urban waste*" OR '
       '"post-consumer waste*" OR "electronic waste*" OR "e-waste")',
    2: 'TS=(recycl* OR "material recover*" OR "resource recover*" OR '
       'valoriz* OR valoris*)',
    3: 'TS=("digital twin*")',
    4: 'TS=("internet of things" OR IoT)',
    5: 'TS=(WEEE OR "construction and demolition waste*" OR "demolition waste*" '
       'OR "end-of-life product*" OR "spent batter*" OR "plastic waste*" '
       'OR "metal scrap*")',
    6: 'TS=(disassembl* OR dismantl* OR demanufactur* OR "waste sort*" '
       'OR "reverse logistic*")',
    7: 'TS=("solid waste*" OR "municipal solid waste*" OR "urban solid waste*" '
       'OR "post-consumer waste*" OR "electronic waste*" OR "e-waste")',
    8: 'TS=(privac* OR "data protect*" OR "personal data" OR '
       '"personal information" OR "personally identifiable information")',
    9: 'TS=("privacy preserv*" OR "privacy protect*" OR "privacy by design" '
       'OR "data minimiz*" OR "data minimis*" OR anonymiz* OR anonymis* '
       'OR pseudonymiz* OR pseudonymis*)',
    10: 'TS=("data govern*" OR "data steward*" OR "data ecosystem*" '
        'OR "data flow*" OR "data shar*" OR "access control")',
    11: 'TS=("data collect*" OR "data process*" OR "data stor*" '
        'OR "data retention" OR "data delet*" OR "consent manag*" '
        'OR "privacy impact assess*" OR "data protection impact assess*")',
    12: 'TS=(LGPD OR GDPR OR "Lei Geral de Proteção de Dados" '
        'OR "General Data Protection Regulation" '
        'OR "Brazilian General Data Protection Law" '
        'OR "privacy regulat*" OR "data protection law*")',
}

LABELS: dict[int, str] = {
    1: "Contexto original (inclui municipal/urban waste*)",
    2: "Função: reciclagem e recuperação",
    3: "Gêmeos digitais",
    4: "IoT",
    5: "Contexto adicional: fluxos e materiais",
    6: "Processo: desmontagem, triagem e logística reversa",
    7: "Contexto corrigido (teste; não substitui 1)",
    8: "Privacidade: núcleo do segundo volume",
    9: "Função: medidas de proteção da privacidade",
    10: "Estrutura: governança e fluxo de dados",
    11: "Processo: ciclo de vida dos dados",
    12: "Contexto: LGPD, GDPR e regulação",
}

TOKEN = re.compile(r"\s*(\d+|AND\b|OR\b|NOT\b|\(|\))", re.IGNORECASE)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FOLDER = PROJECT_ROOT / "_wos" / "tentativa1"


def parse_expression(expression: str) -> list[str]:
    """Valida a expressão e devolve seus números, operadores e parênteses."""
    tokens: list[str] = []
    position = 0

    while position < len(expression):
        if expression[position:].isspace():
            break
        match = TOKEN.match(expression, position)
        if match is None:
            raise ValueError(f"Símbolo inválido perto de: {expression[position:]!r}")
        tokens.append(match.group(1).upper())
        position = match.end()

    if not tokens:
        raise ValueError("Informe uma expressão, por exemplo: (2 AND 3) NOT 1")

    expecting_term = True
    open_groups = 0

    for token in tokens:
        if token.isdecimal():
            if not expecting_term:
                raise ValueError(f"Falta operador antes da chave {token}.")
            key = int(token)
            if key not in QUERIES:
                raise ValueError(f"Chave {key} não definida. Use --list para ver as buscas.")
            expecting_term = False
        elif token == "(":
            if not expecting_term:
                raise ValueError("Falta operador antes de '('.")
            open_groups += 1
        elif token == ")":
            if expecting_term or open_groups == 0:
                raise ValueError("Parêntese ')' fora de lugar.")
            open_groups -= 1
        else:
            if expecting_term:
                raise ValueError(f"Operador {token} sem termo à esquerda.")
            expecting_term = True

    if expecting_term:
        raise ValueError("Expressão termina em operador ou em '('.")
    if open_groups:
        raise ValueError(f"Faltam {open_groups} parêntese(s) de fechamento.")

    return tokens


def expand(tokens: list[str]) -> str:
    """Substitui cada chave pela busca TS, mantendo o agrupamento informado."""
    output = ""
    for token in tokens:
        if token.isdecimal():
            output += f"({QUERIES[int(token)]})"
        elif token in {"AND", "OR", "NOT"}:
            output += f" {token} "
        else:
            output += token
    return output


def filename_for(tokens: list[str]) -> str:
    """Resume agrupamentos com hífen e exclusões com __NOT_, sem parênteses."""
    parts: list[str] = []
    for index, token in enumerate(tokens):
        if token in {"(", ")"}:
            continue
        if token == "NOT":
            parts.append("__NOT_")
        elif token in {"AND", "OR"}:
            if index > 0 and tokens[index - 1] == ")":
                parts.append("-")
            parts.append(token)
            if index + 1 < len(tokens) and tokens[index + 1] == "(":
                parts.append("-")
        else:
            parts.append(token)
    name = "".join(parts)
    return f"{name}.csv"


def main(argv: list[str] | None = None) -> int:
    # PowerShell pode iniciar Python com codificação cp1252 ao redirecionar saída.
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(
        description="Transforma chaves numeradas em uma busca completa da Web of Science."
    )
    parser.add_argument("expression", nargs="*", help='Ex.: "((2 AND 3) AND 6) NOT (1 OR 5)"')
    parser.add_argument("--list", action="store_true", help="mostra as chaves e buscas cadastradas")
    parser.add_argument(
        "--folder",
        default=str(DEFAULT_FOLDER),
        help="pasta sugerida para o CSV (padrão: _wos/tentativa1)",
    )
    args = parser.parse_args(argv)

    if args.list:
        for key, query in QUERIES.items():
            print(f"{key} — {LABELS[key]}\n  {query}")
        return 0

    expression = " ".join(args.expression) if args.expression else input("Expressão: ")
    try:
        tokens = parse_expression(expression)
    except ValueError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 2
    folder = Path(args.folder)
    if not folder.is_absolute():
        folder = PROJECT_ROOT / folder
    print("\nConsulta WoS:\n")
    print(expand(tokens))
    print(f"\nPasta: {folder}\nArquivo: {filename_for(tokens)}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
