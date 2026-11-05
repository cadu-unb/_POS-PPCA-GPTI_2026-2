"""Mostra, artigo a artigo, o título original e o nome para salvar o PDF."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# Importar wos_query não deve deixar __pycache__ ao lado dos scripts.
sys.dont_write_bytecode = True
from wos_query import wait_and_copy  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parent.parent
WOS = PROJECT_ROOT / "_wos"
DEFAULT_SOURCE = WOS / "Manual 3" / "candidatos-leitura-integral.md"
# Pasta dos PDFs do Manual 3; também serve de destino para artigos sem ficha em Manual 1 ou 2.
DEFAULT_NEW_FOLDER = WOS / "Manual 3" / "artigos" / "pdf"

# Linha de tabela: | n | [Título](https://doi.org/...) (ano ...) | ... | origem |
ROW = re.compile(
    r"^\|\s*\d+\s*\|\s*\[(?P<title>.+?)\]\((?P<doi>https://doi\.org/[^)\s]+)\)"
    r"\s*\((?P<year>\d{4})[^)]*\)\s*\|(?P<rest>.*)$"
)
FICHA = re.compile(r"Manual (?P<manual>\d+), (?P<number>\d+)")
NUMBER_PREFIX = re.compile(r"^\d+\s*-\s*")
ILLEGAL = re.compile(r'[\\/:*?"<>|]')
MAX_NAME = 110


@dataclass
class Article:
    title: str
    doi: str
    year: str
    number: int
    folder: Path

    @property
    def stem(self) -> str:
        return f"{self.number:02d} - {short_title(self.title)}"

    @property
    def filename(self) -> str:
        return f"{self.stem}.pdf"

    def existing(self, search: list[Path]) -> Path | None:
        """PDF já salvo com o mesmo título, em qualquer pasta de busca (número e caixa ignorados)."""
        wanted = short_title(self.title).casefold()
        for folder in dict.fromkeys([self.folder, *search]):
            if not folder.is_dir():
                continue
            for pdf in sorted(folder.glob("*.pdf")):
                if NUMBER_PREFIX.sub("", pdf.stem).casefold() == wanted:
                    return pdf
        return None


def short_title(title: str) -> str:
    """Corta o subtítulo (depois de ':'), tira caracteres proibidos e limita o tamanho."""
    name = title.split(":")[0]
    name = " ".join(ILLEGAL.sub(" ", name).split()).rstrip(". ")
    if len(name) > MAX_NAME:
        name = name[:MAX_NAME].rsplit(" ", 1)[0].rstrip(" ,;-")
    return name


def load_articles(source: Path, new_folder: Path) -> list[Article]:
    """Lê as tabelas do Markdown, sem repetir artigos que aparecem em mais de uma lista."""
    articles: list[Article] = []
    seen: set[str] = set()
    next_new = 1
    for line in source.read_text(encoding="utf-8").splitlines():
        match = ROW.match(line)
        if match is None or match["doi"].lower() in seen:
            continue
        seen.add(match["doi"].lower())
        ficha = FICHA.search(match["rest"])
        if ficha:  # mesma numeração e pasta das fichas dos Manuais 1 e 2
            number, folder = int(ficha["number"]), WOS / f"Manual {ficha['manual']}"
        else:
            number, folder = next_new, new_folder
            next_new += 1
        articles.append(Article(match["title"], match["doi"], match["year"], number, folder))
    return articles


def relative(path: Path) -> str:
    try:
        return path.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return str(path)


def show(article: Article, position: int, total: int) -> None:
    print(f"\n[{position}/{total}] {article.year}  {article.doi}")
    print(f"Título original: {article.title}")


def main(argv: list[str] | None = None) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(
        description="Percorre os artigos candidatos: título original e nome para salvar o PDF."
    )
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="Markdown com as tabelas")
    parser.add_argument(
        "--folder",
        type=Path,
        default=DEFAULT_NEW_FOLDER,
        help="pasta dos PDFs do Manual 3 e dos artigos sem ficha (padrão: _wos/Manual 3/artigos/pdf)",
    )
    parser.add_argument("--list", action="store_true", help="só lista todos, sem esperar Enter")
    parser.add_argument("--all", action="store_true", help="inclui os que já têm PDF salvo")
    parser.add_argument("--start", type=int, default=1, help="começa pelo artigo N da lista")
    parser.add_argument("--no-copy", action="store_true", help="mostra os nomes sem copiar")
    args = parser.parse_args(argv)

    if not args.source.is_file():
        print(f"Erro: {args.source} não existe", file=sys.stderr)
        return 2
    articles = load_articles(args.source, args.folder)
    if not articles:
        print("Erro: nenhum artigo com DOI encontrado nas tabelas", file=sys.stderr)
        return 2

    total = len(articles)
    search = [*sorted(WOS.glob("Manual *")), args.folder]
    saved = {index: article.existing(search) for index, article in enumerate(articles, start=1)}
    pending = [
        (index, article)
        for index, article in enumerate(articles, start=1)
        if index >= args.start and (args.all or saved[index] is None)
    ]
    done = sum(1 for path in saved.values() if path is not None)
    print(f"{total} artigos distintos; {done} já têm PDF salvo; {len(pending)} nesta rodada.")
    if not args.all:
        for index, path in saved.items():
            if path is not None and index >= args.start:
                print(f"  pulado [{index}/{total}]: já existe {relative(path)}")

    if args.list:
        for index, article in pending:
            show(article, index, total)
            print(f"Nome do arquivo: {article.filename}  ({relative(article.folder)})")
        return 0

    for index, article in pending:
        show(article, index, total)
        try:
            if args.no_copy:
                print(f"Nome do arquivo: {article.filename}  ({relative(article.folder)})")
                continue
            wait_and_copy("Enter para copiar o título original...", article.title)
            print(f"Nome do arquivo: {article.filename}  ({relative(article.folder)})")
            wait_and_copy("Enter para copiar o nome (sem .pdf)...", article.stem)
        except (EOFError, KeyboardInterrupt):
            print(f"\nInterrompido no artigo {index}. Para continuar: --start {index}")
            return 1
    print("\nFim da lista.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
