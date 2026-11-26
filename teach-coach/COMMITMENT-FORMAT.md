# Commitment Format

Commitments live in `./commitments/`, one file per Commitment, named `c-NNNN-<dash-case-name>.md`. The file is the single source of truth for the Commitment's current state; learning records hold the history of why. The user views them all through an Obsidian Base built over the YAML properties, so keep the properties exact.

## Template

```md
---
kind: habit
state: building
created: 2026-12-10
started: 2026-12-10
review: 2026-12-17
closed:
source: "[🟢📚] Fletcher, *Thin for Life*, Ch. 6 \"Get Moving\", § \"Walking after meals\""
---
Walk for 10 minutes straight after dinner.

Records: [[lr-0003-evenings-are-hard|evenings are hard]]
```

The body is one or two sentences: the specific thing to do, concrete enough that the user knows on any day whether they did it. Then a `Records:` line linking every learning record about this Commitment, with readable display text.

## Properties

- `kind`: `action` (done once) or `habit` (recurring).
- `state`: see [States](#states).
- `created`: when the Commitment was first offered.
- `started`: when it first became Live; empty while never started.
- `review`: the next Review date while Live; empty otherwise.
- `closed`: when it became Closed; empty otherwise.
- `source`: the citation, with tag and location as [CITATIONS.md](CITATIONS.md) describes.

## States

| Group | Action | Habit |
|---|---|---|
| **Live** | `open` | `building`, `established` |
| **Parked** | `not-started`, `paused` | `not-started`, `paused` |
| **Closed** | `completed`, `retired`, `abandoned` | `ingrained`, `retired`, `abandoned` |

- `building` → `established`: the Habit has held up across Reviews.
- `established` → `ingrained`: the Habit is automatic and needs no more tracking.
- `retired`: dropped after it was started.
- `abandoned`: dropped without ever being started.
- `paused`: was Live, put on hold; it can return to Live.

**The limit:** open Actions plus building Habits never exceed two. Established and ingrained Habits are the stack the next Habit is built on, and never count.

## Review

At each Review, ask how the Commitment went, then:

- Update `state` and set the next `review` date, or clear it when the Commitment leaves Live.
- Set `closed` when it becomes Closed.
- When the Review reveals why it held or failed, write a learning record, and add links in both directions.

A Review that teaches nothing new only updates the Commitment file.

## Links

Links run both ways, always with display text:

- The Commitment's `Records:` line links each related learning record.
- Each learning record links the Commitments it concerns.

When a new link points at an older file, add the link to that file too.
