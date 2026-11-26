"""Convert one book file to a single Markdown file.

Usage: python convert.py <source file> <output .md> [--force]

Converter by format: PDF -> pymupdf4llm; everything else -> Calibre's
ebook-convert (Markdown-formatted TXT output, renamed to .md, because
ebook-convert picks its output format from the extension and has no .md writer).

Exit codes:
  0 converted          2 output exists (pass --force to overwrite)
  3 DRM-locked         4 scanned PDF (no text layer)
  1 any other failure (message on stderr)
"""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

EBOOK_CONVERT = r"C:\Program Files\Calibre2\ebook-convert.exe"
# Below this many text characters per page on average, treat a PDF as scanned.
MIN_CHARS_PER_PAGE = 50


def fail(code: int, msg: str):
    print(msg, file=sys.stderr)
    sys.exit(code)


def convert_pdf(source: Path) -> str:
    import pymupdf
    import pymupdf4llm

    with pymupdf.open(source) as doc:
        if doc.needs_pass or doc.is_encrypted:
            fail(3, f"DRM/password-locked PDF: {source}")
        pages = max(doc.page_count, 1)
        chars = sum(len(page.get_text().strip()) for page in doc)
    if chars / pages < MIN_CHARS_PER_PAGE:
        fail(4, f"Scanned PDF, no usable text layer ({chars} chars over {pages} pages): {source}")
    return pymupdf4llm.to_markdown(str(source))


def convert_ebook(source: Path) -> str:
    with tempfile.TemporaryDirectory() as tmp:
        txt = Path(tmp) / "out.txt"
        proc = subprocess.run(
            [EBOOK_CONVERT, str(source), str(txt),
             "--txt-output-formatting=markdown", "--newline=unix",
             "--txt-output-encoding=utf-8"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        log = proc.stdout + proc.stderr
        if proc.returncode != 0 and "DRM" in log:
            fail(3, f"DRM-locked: {source}")
        if proc.returncode != 0 or not txt.exists():
            fail(1, f"ebook-convert failed on {source}:\n{log[-2000:]}")
        return txt.read_text(encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

    if not args.source.is_file():
        fail(1, f"Source not found: {args.source}")
    if args.output.exists() and not args.force:
        fail(2, f"Output exists: {args.output}")

    if args.source.suffix.lower() == ".pdf":
        markdown = convert_pdf(args.source)
    else:
        markdown = convert_ebook(args.source)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(markdown, encoding="utf-8")
    print(f"Converted: {args.output} ({len(markdown):,} chars)")


if __name__ == "__main__":
    main()
