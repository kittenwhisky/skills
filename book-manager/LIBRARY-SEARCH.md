# Library search

```
python find.py <query words...>
```

Searches file names under `C:\Users\User\Dropbox\3 - Resources\Books & Articles` and every subfolder, Calibre Library included. Book formats only (epub, azw3, mobi, pdf, docx, html, txt), so Calibre's own `metadata.db`, `metadata.opf` and `cover.jpg` never appear.

## Matching

Every query word must appear in the file name or its parent folder name, case-insensitive. Calibre names files `Title - Author.ext` inside `Author\Title (id)\`, so author and title words both match.

Search with the most distinctive one or two words (a surname, an unusual title word). On zero matches, retry with fewer or alternative words before reporting nothing found.

## Output fields

JSON list, one entry per book; files sharing a stem in one folder are one book.

- `formats`: in preference order (epub, azw3, mobi, pdf, ...); `preferred_source` is the first.
- `default_output`: where the `.md` goes by default (see CONVERSION.md).
- `md_exists`: a `.md` already sits at `default_output`.
- `in_calibre_library`: the book still lives in a Calibre-managed folder.

## Showing matches

Show a numbered list: title, folder, formats, and whether a `.md` exists. The user picks by number.
