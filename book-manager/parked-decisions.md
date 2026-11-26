# Parked decisions

Decided or deferred while designing `book-manager` (grilling session, 2026-11-26). Not read by the skill at run time except as a pointer target.

## Session 2: indexing and splitting (open)

Book-manager v1 converts a whole book into one `.md`. A second grilling session decides whether and how that changes, optimising for how Claude retrieves from long text:

- Split converted books per chapter, or keep one file?
- A per-book index ("book card"): keywords for the whole book, plus keywords per chapter, searched before any source text is read.
- Convert chapters on demand, rather than the whole book up front?
- When indexing runs: when a book is added to the library (automatic or user-triggered), or lazily when a teach/coach session's goal needs the book.
- Whether Claude's built-in long-document handling makes an index unnecessary; test before building.

## For Teach-Coach (answering, summarising, comparing)

Teach-Coach now exists at `~/.claude/skills/teach-coach/` and is the source of truth for answering from books. It adopted per-claim chapter/heading citations, short quotes, "the Library does not cover this", pure-CSS hover pop-ups and HTML lessons in `lessons\`. It overrode lesson naming (`l-NNNN-<name>.html`, not `YYMMDD <topic>.html`). It also needs converted books to keep chapter and subsection headings as Markdown headings, because its citations name them. The original notes, for history:

- Jobs: answer questions about one book, summarise a book or chapter, compare across books. Recommending books for a topic and writing reading notes come later.
- Cite the chapter or heading for each claim, with short direct quotes for key points; say when the book does not cover something rather than filling from general knowledge.
- Citations as hover pop-ups: a small superscript marker in the text; hovering shows book, chapter/heading and the quote. Pure CSS tooltip in a self-contained HTML file, no JS, no external assets.
- Summaries, lessons and comparisons saved as HTML in a `lessons\` folder, named `YYMMDD <topic>.html`, chat gets a one-line pointer; quick factual questions answered in chat.
- Teach-Coach reads Markdown produced by `book-manager` and reaches books through it.
