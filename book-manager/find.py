"""Search the book library by file name.

Usage: python find.py <query words...> [--root PATH]

Prints JSON: a list of books. Files sharing a stem in one folder are one book
with several formats. Every query word must appear (case-insensitive) in the
file name or its parent folder name (Calibre puts the author in a parent folder).
"""
import argparse
import json
import sys
from pathlib import Path

LIBRARY_ROOT = Path(r"C:\Users\User\Dropbox\3 - Resources\Books & Articles")
# Preference order when a book exists in several formats.
FORMATS = [".epub", ".azw3", ".mobi", ".pdf", ".docx", ".html", ".htm", ".txt"]
CALIBRE_DIR = "Calibre Library"


def default_output(source: Path) -> Path:
    """Next to the source; inside Calibre's data/ subfolder for Calibre-managed books,
    so Calibre moves the .md with the book and never flags it as a stray file."""
    if CALIBRE_DIR in source.parts:
        return source.parent / "data" / (source.stem + ".md")
    return source.with_suffix(".md")


def find(words, root: Path):
    books = {}
    for path in root.rglob("*"):
        ext = path.suffix.lower()
        if ext not in FORMATS or not path.is_file():
            continue
        haystack = f"{path.parent.name} {path.stem}".lower()
        if all(w in haystack for w in words):
            books.setdefault((path.parent, path.stem), []).append(path)

    results = []
    for (folder, stem), files in sorted(books.items(), key=lambda kv: kv[0][1].lower()):
        files.sort(key=lambda p: FORMATS.index(p.suffix.lower()))
        preferred = files[0]
        out = default_output(preferred)
        results.append({
            "title": stem,
            "folder": str(folder),
            "formats": [p.suffix.lower().lstrip(".") for p in files],
            "preferred_source": str(preferred),
            "default_output": str(out),
            "md_exists": out.exists(),
            "in_calibre_library": CALIBRE_DIR in preferred.parts,
        })
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="+")
    ap.add_argument("--root", type=Path, default=LIBRARY_ROOT)
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    words = [w.lower() for w in args.query]
    print(json.dumps(find(words, args.root), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
