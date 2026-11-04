"""Converte planilhas .xls em CSV válido (RFC 4180), com limpeza das células."""

from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from datetime import time
from pathlib import Path

import xlrd

# Tipos de célula do xlrd.
EMPTY, TEXT, NUMBER, DATE, BOOLEAN, ERROR, BLANK = range(7)

# Caracteres que não carregam informação e atrapalham leitores de CSV.
INVISIBLE = dict.fromkeys(map(ord, "​‌‍⁠﻿"))
NEWLINES = re.compile(r"\s*[\r\n  \x0b\x0c\x85]+\s*")
CONTROL = re.compile(r"[\x00-\x08\x0e-\x1f\x7f]")


@dataclass
class Stats:
    """Contadores do que foi corrigido, para o relatório final."""

    text_cells: int = 0
    quoted: int = 0  # células que o csv vai envolver em aspas
    newlines_fixed: int = 0
    cleaned: int = 0  # espaços nas pontas, NBSP, invisíveis, controle
    dates: int = 0
    errors: int = 0
    dropped_rows: int = 0
    dropped_cols: int = 0
    renamed_headers: list[str] = field(default_factory=list)


def clean_text(value: str, newline: str, stats: Stats) -> str:
    """Normaliza um texto sem alterar o conteúdo que importa."""
    original = value
    value = unicodedata.normalize("NFC", value)
    value = value.replace(" ", " ").translate(INVISIBLE)
    value = CONTROL.sub("", value)
    if NEWLINES.search(value):
        stats.newlines_fixed += 1
        value = NEWLINES.sub(newline, value)
    value = value.strip()
    if value != original:
        stats.cleaned += 1
    return value


def format_number(value: float) -> str:
    """11.0 vira 11; os demais usam a representação mais curta que preserva o valor."""
    if value.is_integer() and abs(value) < 1e15:
        return str(int(value))
    return repr(value)


def format_cell(cell: xlrd.sheet.Cell, datemode: int, newline: str, stats: Stats) -> str:
    """Converte uma célula do xlrd em texto de CSV."""
    kind, value = cell.ctype, cell.value
    if kind in (EMPTY, BLANK):
        return ""
    if kind == TEXT:
        stats.text_cells += 1
        return clean_text(value, newline, stats)
    if kind == NUMBER:
        return format_number(value)
    if kind == BOOLEAN:
        return "TRUE" if value else "FALSE"
    if kind == DATE:
        stats.dates += 1
        moment = xlrd.xldate.xldate_as_datetime(value, datemode)
        if value < 1:
            return moment.time().isoformat()
        if moment.time() == time(0):
            return moment.date().isoformat()
        return moment.isoformat(sep=" ")
    stats.errors += 1  # células com #N/A, #DIV/0! etc. viram vazio
    return ""


def unique_headers(headers: list[str], stats: Stats) -> list[str]:
    """Garante cabeçalhos não vazios e sem repetição (nome, nome_2, coluna_N)."""
    seen: dict[str, int] = {}
    result = []
    for index, name in enumerate(headers, start=1):
        base = name or f"coluna_{index}"
        count = seen.get(base, 0) + 1
        seen[base] = count
        final = base if count == 1 else f"{base}_{count}"
        if final != name:
            stats.renamed_headers.append(f"{index}: {name!r} -> {final!r}")
        result.append(final)
    return result


def sheet_rows(sheet: xlrd.sheet.Sheet, datemode: int, newline: str, stats: Stats) -> list[list[str]]:
    """Lê a aba, remove linhas e colunas totalmente vazias e ajusta o cabeçalho."""
    rows = [
        [format_cell(sheet.cell(r, c), datemode, newline, stats) for c in range(sheet.ncols)]
        for r in range(sheet.nrows)
    ]
    kept = [row for row in rows if any(row)]
    stats.dropped_rows += len(rows) - len(kept)
    if not kept:
        return []
    used = [c for c in range(sheet.ncols) if any(row[c] for row in kept)]
    stats.dropped_cols += sheet.ncols - len(used)
    kept = [[row[c] for c in used] for row in kept]
    kept[0] = unique_headers(kept[0], stats)
    return kept


def write_csv(rows: list[list[str]], path: Path, delimiter: str, encoding: str, stats: Stats) -> None:
    """Grava o CSV. Vírgulas, aspas e quebras são tratadas por aspas, não por remoção."""
    special = (delimiter, '"', "\n", "\r")
    stats.quoted += sum(1 for row in rows for cell in row if any(ch in cell for ch in special))
    with path.open("w", encoding=encoding, newline="") as handle:
        writer = csv.writer(handle, delimiter=delimiter, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        writer.writerows(rows)


def verify(rows: list[list[str]], path: Path, delimiter: str, encoding: str) -> None:
    """Relê o arquivo gravado e confirma que nada quebrou nem mudou de coluna."""
    with path.open("r", encoding=encoding, newline="") as handle:
        again = list(csv.reader(handle, delimiter=delimiter))
    if again != rows:
        raise ValueError("a releitura do CSV difere do conteúdo original")
    widths = {len(row) for row in again}
    if widths != {len(rows[0])}:
        raise ValueError(f"linhas com número diferente de colunas: {sorted(widths)}")


def safe_name(text: str) -> str:
    return re.sub(r'[\\/:*?"<>|\s]+', "_", text).strip("_") or "aba"


def convert(source: Path, args: argparse.Namespace) -> list[Path]:
    """Converte uma planilha; devolve os CSVs criados."""
    book = xlrd.open_workbook(source)
    folder = Path(args.output_dir) if args.output_dir else source.parent
    folder.mkdir(parents=True, exist_ok=True)
    sheets = [s for s in book.sheets() if s.nrows and s.ncols]
    if not sheets:
        raise ValueError("a planilha não tem dados")
    created = []
    for sheet in sheets:
        stats = Stats()
        rows = sheet_rows(sheet, book.datemode, args.newline, stats)
        if not rows:
            print(f"  aba {sheet.name!r}: vazia, ignorada")
            continue
        name = source.stem if len(sheets) == 1 else f"{source.stem}__{safe_name(sheet.name)}"
        target = folder / f"{name}.csv"
        if target.exists() and not args.force:
            raise FileExistsError(f"{target} já existe (use --force para sobrescrever)")
        write_csv(rows, target, args.delimiter, args.encoding, stats)
        verify(rows, target, args.delimiter, args.encoding)
        created.append(target)
        report(sheet.name, target, rows, stats)
    return created


def report(sheet_name: str, target: Path, rows: list[list[str]], stats: Stats) -> None:
    print(f"  aba {sheet_name!r} -> {target}")
    print(f"    {len(rows) - 1} registros, {len(rows[0])} colunas (releitura conferida)")
    print(f"    {stats.quoted} células protegidas com aspas (vírgula, aspas ou quebra)")
    if stats.newlines_fixed:
        print(f"    {stats.newlines_fixed} células com quebra de linha ajustadas")
    if stats.cleaned:
        print(f"    {stats.cleaned} textos limpos (espaços, NBSP, invisíveis, controle)")
    if stats.dropped_rows or stats.dropped_cols:
        print(f"    removidas {stats.dropped_rows} linhas e {stats.dropped_cols} colunas vazias")
    if stats.errors:
        print(f"    {stats.errors} células com erro do Excel viraram vazio")
    for item in stats.renamed_headers:
        print(f"    cabeçalho renomeado: coluna {item}")


def main(argv: list[str] | None = None) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Converte arquivos .xls em CSV bem formado.")
    parser.add_argument("files", nargs="+", type=Path, help="caminho de um ou mais arquivos .xls")
    parser.add_argument("-o", "--output-dir", help="pasta de saída (padrão: a mesma do arquivo)")
    parser.add_argument("--delimiter", default=",", help="separador de campos (padrão: vírgula)")
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="codificação de saída; use utf-8-sig para abrir direto no Excel (padrão: utf-8)",
    )
    parser.add_argument(
        "--newline",
        default=" ",
        help="texto que substitui quebras de linha dentro de células (padrão: espaço)",
    )
    parser.add_argument("--force", action="store_true", help="sobrescreve CSVs existentes")
    args = parser.parse_args(argv)
    if len(args.delimiter) != 1:
        parser.error("--delimiter deve ter exatamente um caractere")

    failures = 0
    for source in args.files:
        print(source)
        try:
            if not source.is_file():
                raise FileNotFoundError(f"{source} não existe")
            convert(source, args)
        except xlrd.XLRDError as exc:
            failures += 1
            print(f"  Erro: não é um .xls válido ({exc})", file=sys.stderr)
        except (OSError, ValueError) as exc:
            failures += 1
            print(f"  Erro: {exc}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
