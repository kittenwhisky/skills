# Citations and Provenance

Every substantive claim carries a citation precise enough for the user to find the source text in seconds. A claim is substantive when it states a fact, method or recommendation; framing, questions and encouragement are not claims.

## Source tags

| Tag | Meaning |
|---|---|
| `[🟢📚]` | Primary resource: a Library book or community the user chose |
| `[🟡🌐]` | Secondary resource: found by the agent with the user's permission |
| `[🔴⚠️ (uncited claim)]` | Uncited claim: the agent's own reasoning, backed by no resource |

## Location

- **Primary (book):** Author, *Title*, Ch. N "Chapter title", § "Subsection heading" · Library path. Example: `Fletcher, *Thin for Life*, Ch. 4 "Taking Charge", § "Changing your surroundings" · Weightloss/Thin for life.md`
- **Secondary:** Author or publisher, *Title*, § "Section heading" · URL.
- **Short quote:** add a short direct quote for key points, so the user can search the book for it.

Take chapter and subsection names from the book's own Markdown headings. When a converted book lacks a level (no subsection headings, say), cite the nearest heading above the passage and always add the short quote.

## By output

- **HTML (lessons, reference documents):** place a `🔗` after the claim; hovering it shows the tag, the full location and the quote. Use the shared citation component in `./assets/citations.css` (create it from the snippet below if missing). Pure CSS, no JavaScript.
- **Chat answers:** put the tag and a compact location inline in brackets after the claim: `[🟢📚 Clower, *The French Don't Diet Plan*, Step 3 "…", § "…"]`.
- **Markdown files (learning records, Commitments):** write the tag and full location as plain text, in the `source:` property or a `Sources:` line. Make a Library path a wikilink only when the Library and the workspace share an Obsidian vault.

## Provenance footer

End every chat answer and every lesson with:

```
Provenance: n/m claims from Primary resources (x%)
```

Count the substantive claims you tagged (m) and those tagged `[🟢📚]` (n). Reference documents carry no footer: each claim's tag already shows its provenance.

## Citation component

```css
/* ./assets/citations.css */
.cite { position: relative; cursor: help; text-decoration: none; font-size: 0.8em; vertical-align: super; }
.cite .pop {
  visibility: hidden; opacity: 0; transition: opacity 0.15s;
  position: absolute; z-index: 10; bottom: 1.6em; left: 50%; transform: translateX(-50%);
  width: max-content; max-width: 28em; padding: 0.6em 0.8em;
  background: #fffdf7; color: #222; border: 1px solid #ccc; border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15); font-size: 0.9rem; line-height: 1.4; white-space: normal;
}
.cite:hover .pop, .cite:focus .pop { visibility: visible; opacity: 1; }
.cite .pop q { display: block; margin-top: 0.4em; font-style: italic; }
@media print { .cite .pop { display: none; } }
```

```html
<span class="cite" tabindex="0">🔗<span class="pop">[🟢📚] Fletcher, <cite>Thin for Life</cite>, Ch. 4 "Taking Charge", § "Changing your surroundings" · Weightloss/Thin for life.md<q>…short quote…</q></span></span>
```
