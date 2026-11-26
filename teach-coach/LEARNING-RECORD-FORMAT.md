# Learning Record Format

Learning records live in `./learning-records/` and are named `lr-NNNN-<dash-case-name>.md`.

They are the teaching equivalent of ADRs: they capture non-obvious lessons, key insights, Decisions and stated prior knowledge that will steer future sessions. They are used to calculate the zone of proximal development. Current state belongs in the Commitment files; records hold the history of _why_.

## Template

```md
# {Short title of what was learned, decided or established}

{1-3 sentences: what was learned (or decided, or established), and why it matters for future sessions.}

Commitments: [[c-0004-walk-after-dinner|walk after dinner]]
Sources: [🟢📚] Clower, *The French Don't Diet Plan*, Step 3 "…", § "…"
```

That is the whole format. A learning record can be a single paragraph. The value is recording _that_ this is now known and _why_ it changes what comes next, not in filling out sections.

## Optional lines and sections

Only include these when they add genuine value.

- **Commitments**: wikilinks, with display text, to every Commitment this record concerns. Never restate a Commitment's content or state; link to it.
- **Sources**: the Primary or Secondary resources behind a Decision or insight, cited as [CITATIONS.md](CITATIONS.md) describes.
- **Status** frontmatter (`active | superseded by [[lr-NNNN-…|…]]`): when an earlier understanding turns out to be wrong and is replaced.
- **Evidence**: how the user demonstrated the understanding (a question answered, an exercise completed, a Commitment kept).
- **Implications**: what this unlocks or rules out for future sessions, when non-obvious.

## When to write a learning record

Write one when any of these is true:

1. **The user demonstrated genuine understanding of something non-trivial**: not just exposure, but evidence they can use the concept correctly. This sets a new floor for what to teach next.
2. **The user disclosed prior knowledge**: "I already know X." Record it, with the _depth_ claimed, so future sessions don't re-teach it.
3. **A misconception was corrected**: the user believed something wrong and now sees why. These predict future stumbling blocks.
4. **The Mission shifted**: the user discovered they care about something different. Link [[MISSION|the mission]] and update it.
5. **A Decision was made**: the user chose an approach that is not itself an action ("follow Clower's eat-slowly principle rather than counting calories").
6. **A Review produced an insight**: why a Commitment held or failed ("evening Commitments keep failing; mornings work").

### What does _not_ qualify

- Material that was merely covered. Coverage is not learning; wait for evidence.
- A term already captured in `GLOSSARY.md`.
- A Review that went as expected. Update the Commitment file and move on.
- Session-by-session activity logs. Learning records are decision-grade insights, not a journal.

## Editing an existing record

A record's content is fixed once written. You may add a link to it later (when a new Commitment or record relates to it); you never change what it says.

When a later record contradicts an earlier one, mark the old record `Status: superseded by [[lr-NNNN-…|…]]` rather than deleting it. The history of how understanding evolved is itself useful signal.
