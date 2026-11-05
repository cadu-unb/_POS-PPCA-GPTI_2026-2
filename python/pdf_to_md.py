"""Converte artigos em PDF para Markdown, em duas fases (extrair e aplicar).

Fase 1 (`extract`): lê cada PDF com o PyMuPDF (modo layout), monta o Markdown e troca
equações e parágrafos com matemática embaralhada por marcadores `{{EQ id}}` / `{{PAR id}}`.
Para cada marcador, grava um recorte PNG da página e o texto bruto em `items.json`.

Fase 2 (`apply`): lê `transcricoes.json` (id -> LaTeX da equação ou parágrafo corrigido,
feito a partir do recorte) e grava os `.md` finais. Marcadores sem transcrição ficam
com o texto bruto e um aviso, para nada desaparecer em silêncio.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import pymupdf
import pymupdf.layout  # noqa: F401  (ativa a análise de layout no pymupdf4llm)
import pymupdf4llm

SKIP = {"page-header", "page-footer"}
MATH_CHARS = re.compile(r"[∀∃∈∉∪∩∑∏∫√≤≥≈≠∂∇⊂⊆∞⊗⊕∥‖∼]")
GLUED_WORDS = re.compile(r"[a-z]{22,}")
PICTURE_TEXT = re.compile(r"<!-- Start of picture text -->.*?<!-- End of picture text -->", re.S)
MARKER = re.compile(r"\{\{(EQ|PAR) ([^}]+)\}\}")


def doc_ids(folder: Path) -> list[tuple[str, Path]]:
    """Dá a cada PDF um id estável (d01, d02, ...) pela ordem alfabética."""
    pdfs = sorted(folder.glob("*.pdf"))
    return [(f"d{index:02d}", pdf) for index, pdf in enumerate(pdfs, start=1)]


def looks_garbled(text: str) -> bool:
    """Parágrafo com sobrescritos, símbolos matemáticos ou palavras coladas: precisa de revisão."""
    plain = PICTURE_TEXT.sub("", text)
    scripts = plain.count("<sup>") + plain.count("<sub>")
    return scripts >= 2 or bool(MATH_CHARS.search(plain)) or bool(GLUED_WORDS.search(plain))


def crop(page: pymupdf.Page, bbox: list[float], target: Path, margin: float = 6) -> None:
    rect = pymupdf.Rect(bbox) + (-margin, -margin, margin, margin)
    rect &= page.rect
    page.get_pixmap(clip=rect, dpi=220).save(target)


FLOATS = {"picture", "caption", "table", "footnote"}
SENTENCE_END = re.compile(r"[.!?:;)\]\"”’]\s*$")


def reading_order(boxes: list[dict], width: float) -> list[dict]:
    """Ordena as caixas de uma página: blocos de largura total separam trechos de duas colunas."""
    mid = width / 2
    ordered: list[dict] = []
    run_left: list[dict] = []
    run_right: list[dict] = []

    def flush() -> None:
        ordered.extend(sorted(run_left, key=lambda b: b["bbox"][1]))
        ordered.extend(sorted(run_right, key=lambda b: b["bbox"][1]))
        run_left.clear()
        run_right.clear()

    for box in sorted(boxes, key=lambda b: (b["bbox"][1], b["bbox"][0])):
        x0, _, x1, _ = box["bbox"]
        if x0 < mid - 0.1 * width and x1 > mid + 0.1 * width:
            flush()
            ordered.append(box)
        elif x1 <= mid + 0.05 * width:
            run_left.append(box)
        else:
            run_right.append(box)
    flush()
    return ordered


def merge_continuations(blocks: list[dict]) -> list[dict]:
    """Junta parágrafos partidos por coluna ou página, deixando legendas e notas depois."""
    result: list[dict] = []
    index = 0
    while index < len(blocks):
        block = blocks[index]
        if block["kind"] in ("text", "list-item") and not SENTENCE_END.search(block["text"]):
            skipped = []
            probe = index + 1
            while probe < len(blocks) and blocks[probe]["kind"] in FLOATS:
                skipped.append(blocks[probe])
                probe += 1
            nxt = blocks[probe] if probe < len(blocks) else None
            if nxt and nxt["kind"] == "text" and nxt["text"][:1].islower():
                if block["text"].endswith("-"):  # hifenização de fim de linha
                    block["text"] = block["text"][:-1] + nxt["text"]
                else:
                    block["text"] = block["text"] + " " + nxt["text"]
                block["segments"] += nxt["segments"]
                blocks[index : probe + 1] = [block, *skipped]
                continue
        result.append(block)
        index += 1
    return result


def convert_pdf(doc_id: str, pdf: Path, work: Path) -> tuple[str, list[dict]]:
    chunks = pymupdf4llm.to_markdown(
        str(pdf),
        write_images=False,
        use_ocr=False,
        header=False,
        footer=False,
        page_chunks=True,
    )
    document = pymupdf.open(pdf)
    blocks: list[dict] = []
    for number, chunk in enumerate(chunks, start=1):
        text, page = chunk["text"], document[number - 1]
        boxes = [b for b in chunk["page_boxes"] if b["class"] not in SKIP]
        for box in reading_order(boxes, page.rect.width):
            raw = text[box["pos"][0] : box["pos"][1]].strip()
            if raw:
                blocks.append(
                    {
                        "kind": box["class"],
                        "text": raw,
                        "id": f"{doc_id}-p{number:02d}-b{box['index']:02d}",
                        "segments": [(number, box["bbox"])],
                    }
                )
    items: list[dict] = []
    parts: list[str] = []
    for block in merge_continuations(blocks):
        kind, raw, item_id = block["kind"], block["text"], block["id"]
        garbled = kind == "formula" or (kind not in ("table", "picture") and looks_garbled(raw))
        if kind == "picture":
            parts.append("*[Figura ou diagrama omitido.]*")
        elif garbled:
            marker = "EQ" if kind == "formula" else "PAR"
            parts.append(f"{{{{{marker} {item_id}}}}}")
            crops = []
            for position, (number, bbox) in enumerate(block["segments"]):
                name = f"{item_id}" + (f"_{position}" if position else "") + ".png"
                crop(document[number - 1], bbox, work / "crops" / name)
                crops.append(name)
            clean = PICTURE_TEXT.sub(lambda m: m.group(0)[28:-26], raw)
            items.append({"id": item_id, "kind": marker, "page": block["segments"][0][0], "crops": crops, "raw": clean})
        else:
            parts.append(PICTURE_TEXT.sub("", raw).strip())
    markdown = "\n\n".join(part for part in parts if part)
    return re.sub(r"\n{3,}", "\n\n", markdown) + "\n", items


TERMINAL = re.compile(r"[.!?:][\"”’)\]]*\s*$")
NOT_PROSE = ("#", "|", "$$", ">", "-", "*[Figura", "<")
MARKUP = re.compile(r"[#*_`>\s]+")


def postprocess(text: str) -> str:
    """Limpezas de texto que independem dos marcadores: cabeçalhos correntes, quebras e títulos."""
    paragraphs = [p.strip() for p in text.split("\n\n")]
    # 1. cabeçalhos/rodapés correntes que o classificador tomou por texto: curtos e repetidos
    plain = [MARKUP.sub(" ", p).strip() for p in paragraphs]
    counts: dict[str, int] = {}
    for item in plain:
        counts[item] = counts.get(item, 0) + 1
    paragraphs = [p for p, item in zip(paragraphs, plain) if not (item and len(item) <= 80 and counts[item] >= 3 and not item[0].isdigit())]
    # 1b. negrito/itálico quebrado palavra por palavra ("_a_ _b_" -> "_a b_") e <br> sobrando em células
    paragraphs = [p.replace("_ _", " ").replace("** **", " ").replace("<br>|", "|") for p in paragraphs]
    # 2. linhas de filete de nota de rodapé
    paragraphs = [re.sub(r"^_{5,}\s*", "", p) for p in paragraphs]
    # 3. títulos sem negrito ou itálico em volta
    paragraphs = [re.sub(r"^(#+) (?:\*\*|_)(.+?)(?:\*\*|_)\s*$", r"\1 \2", p) for p in paragraphs]
    # 4. continuação de parágrafo (começa em minúscula, anterior sem ponto final)
    merged: list[str] = []
    for paragraph in paragraphs:
        previous = merged[-1] if merged else ""
        if (
            paragraph[:1].islower()
            and previous
            and not previous.startswith(NOT_PROSE)
            and not previous.endswith("$$")
            and not TERMINAL.search(previous)
            and not paragraph.startswith(("where ", "http"))
        ):
            merged[-1] = (previous[:-1] + paragraph) if previous.endswith("-") else f"{previous} {paragraph}"
        elif paragraph:
            merged.append(paragraph)
    return "\n\n".join(merged) + "\n"


def extract(args: argparse.Namespace) -> int:
    work = Path(args.work)
    (work / "crops").mkdir(parents=True, exist_ok=True)
    all_items: list[dict] = []
    for doc_id, pdf in doc_ids(Path(args.pdf_dir)):
        markdown, items = convert_pdf(doc_id, pdf, work)
        (work / f"{doc_id}.md").write_text(markdown, encoding="utf-8")
        (work / f"{doc_id}.name").write_text(pdf.stem, encoding="utf-8")
        all_items += items
        eqs = sum(1 for item in items if item["kind"] == "EQ")
        print(f"{doc_id} {pdf.name[:60]}: {len(items) - eqs} parágrafos e {eqs} equações para revisar")
    (work / "items.json").write_text(json.dumps(all_items, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n{len(all_items)} itens em {work / 'items.json'}")
    return 0


def apply(args: argparse.Namespace) -> int:
    work, out = Path(args.work), Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    done = json.loads(Path(args.transcriptions).read_text(encoding="utf-8")) if args.transcriptions else {}
    raw = {item["id"]: item for item in json.loads((work / "items.json").read_text(encoding="utf-8"))}
    missing = 0

    def replace(match: re.Match) -> str:
        nonlocal missing
        kind, item_id = match.groups()
        value = done.get(item_id)
        if value is None:
            missing += 1
            return f"> **[REVISAR {item_id}]** {raw[item_id]['raw']}"
        if value.startswith("TEXT:"):  # falso positivo do classificador: texto puro
            return value[5:].strip()
        if kind == "EQ":
            return f"$$\n{value.strip()}\n$$"
        return value.strip()

    patches: dict = {}
    if args.patches:
        namespace: dict = {}
        exec(Path(args.patches).read_text(encoding="utf-8"), namespace)  # arquivo local do próprio usuário
        patches = namespace["PATCHES"]

    for md_file in sorted(work.glob("d??.md")):
        name = (work / f"{md_file.stem}.name").read_text(encoding="utf-8")
        # "$" do texto original é moeda ou símbolo de nota: escapa para não virar matemática
        text = md_file.read_text(encoding="utf-8").replace("$", "\\$")
        for old, new in patches.get(md_file.stem, []):
            if old.startswith("TABLE:"):  # troca a tabela inteira que começa na linha indicada
                lines = text.split("\n")
                if old[6:] not in lines:
                    print(f"AVISO {md_file.stem}: tabela não encontrada: {old[6:][:60]!r}", file=sys.stderr)
                    continue
                start = lines.index(old[6:])
                end = start
                while end < len(lines) and lines[end].startswith("|"):
                    end += 1
                text = "\n".join(lines[:start] + new.strip("\n").split("\n") + lines[end:])
            elif old.startswith("ALL:"):
                text = text.replace(old[4:], new)
            elif text.count(old) != 1:
                print(f"AVISO {md_file.stem}: trecho do patch encontrado {text.count(old)}x: {old[:60]!r}", file=sys.stderr)
            else:
                text = text.replace(old, new)
        text = postprocess(MARKER.sub(replace, text))
        (out / f"{name}.md").write_text(text, encoding="utf-8")
        print(f"{out / (name + '.md')}")
    print(f"\n{missing} marcador(es) sem transcrição")
    return 1 if missing else 0


def main(argv: list[str] | None = None) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="PDF -> Markdown em duas fases.")
    sub = parser.add_subparsers(dest="command", required=True)
    one = sub.add_parser("extract", help="gera Markdown com marcadores e recortes")
    one.add_argument("pdf_dir")
    one.add_argument("--work", required=True, help="pasta de trabalho (recortes, items.json)")
    one.set_defaults(run=extract)
    two = sub.add_parser("apply", help="aplica as transcrições e grava os .md finais")
    two.add_argument("--work", required=True)
    two.add_argument("--out-dir", required=True)
    two.add_argument("--transcriptions", help="JSON id -> texto/LaTeX")
    two.add_argument("--patches", help="arquivo .py com PATCHES = {doc: [(antigo, novo), ...]}")
    two.set_defaults(run=apply)
    args = parser.parse_args(argv)
    return args.run(args)


if __name__ == "__main__":
    raise SystemExit(main())
