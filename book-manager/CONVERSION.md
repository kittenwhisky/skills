# Conversion

Turns one book file into one Markdown file, for later reading by other agents (Teach-Coach). One `.md` per book, no chapter splitting yet (see [parked-decisions.md](parked-decisions.md)).

## Save location

Ask the user every time; offer `default_output` from `find.py` as the default:

- **Loose files**: next to the source, same name with `.md` (`Deep Work.epub` → `Deep Work.md`).
- **Calibre Library books**: the book folder's `data\` subfolder. Calibre renames and moves book folders when title or author metadata changes; files in `data\` move with the book and are not flagged as stray.

When a `.md` already exists there, offer reuse (default) or re-convert. Re-convert passes `--force`.

## Command

```
python convert.py "<source file>" "<output .md>" [--force]
```

Use `preferred_source` from `find.py` unless the user names a format. The script picks the converter:

- **PDF** → `pymupdf4llm`, which keeps headings, lists and tables far better than Calibre's PDF input.
- **Everything else** → Calibre's `ebook-convert` with Markdown-formatted TXT output, renamed to `.md`. It writes to a temporary `.txt` because `ebook-convert` chooses its output format by extension and has no `.md` writer.

Large books take a minute or more; run with a generous timeout.

## Exit codes

| Code | Meaning | Tell the user |
|---|---|---|
| 0 | Converted; prints path and size | The output path |
| 2 | Output exists | Ask: reuse or re-convert with `--force` |
| 3 | DRM- or password-locked | The file and that it is locked; stop |
| 4 | Scanned PDF, no text layer | The file and that it needs OCR; stop |
| 1 | Other failure; details on stderr | The file and the error; stop |

On codes 3 and 4, offer the book's next format from `formats` if it has one; otherwise stop there.
