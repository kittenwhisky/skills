---
name: book-manager
description: Find books in the user's library and convert them to Markdown. `/book-manager find <query>` or `/book-manager convert <book>`.
disable-model-invocation: true
---

# Book manager

Two commands over the user's book library. Scripts live beside this file in `C:\Users\User\.claude\skills\book-manager\`; run them with `python` from there.

## `find <query>`

Read [LIBRARY-SEARCH.md](LIBRARY-SEARCH.md), run the search, and show the matches. Done when the user has seen every match, or has been told nothing matched along with the words searched.

## `convert <book>`

1. **Pick the book.** Search as in `find`. Exactly one match: use it. Several: list them as LIBRARY-SEARCH.md describes and wait for the user's choice.
2. **Pick the save location.** Read [CONVERSION.md](CONVERSION.md), then ask the user where to save, offering the match's `default_output` as the default. When `md_exists` is true, say so and offer reuse (the default) or re-convert.
3. **Convert** with `convert.py`, as CONVERSION.md describes. Reuse means skip this step.

Done when the user has the path of a Markdown file that exists on disk, or has been told which file failed and why.

Converted books get no memory beyond the files on disk: every run asks again.
