# Teach-Coach

The design vocabulary of the `teach-coach` skill: Claude teaches and coaches the user towards real-world goals, grounded in resources the user controls rather than its own general knowledge. A workspace's own `GLOSSARY.md` holds the subject vocabulary of one Mission; this file holds the skill's.

## Language

**Library**:
The user's controlled collection of books converted to Markdown.
_Avoid_: corpus, knowledge base

**Mission**:
One real-world goal the user is pursuing (for example, losing weight), with its own folder and history spanning many sessions.
_Avoid_: goal folder, topic, course

**Primary resource**:
A resource the user chose for a **Mission**, such as a **Library** book or a community they picked, and the default source for every answer.
_Avoid_: shelf, core source, main reference

**Secondary resource**:
A resource the agent found itself and may draw on only with the user's permission, when the **Primary resources** fall short.
_Avoid_: external source, web source, fallback

**Provenance**:
How much of an answer is backed by **Primary resources**, as opposed to **Secondary resources** or uncited reasoning.
_Avoid_: confidence, accuracy, trustworthiness

## Progress

**Decision**:
A chosen approach within a **Mission** that is not itself something to do.
_Avoid_: strategy, rule

**Commitment**:
Something to do for a **Mission**, either an **Action** or a **Habit**, that is always **Live**, **Parked** or **Closed**.
_Avoid_: task, goal, resolution, candidate

**Live**:
The state of a **Commitment** the user is currently doing; an open **Action** or a building or established **Habit**.
_Avoid_: active, current

**Parked**:
The state of a **Commitment** that was offered but not started, or that was paused.
_Avoid_: backlog, someday/maybe, candidate

**Closed**:
The final state of a **Commitment**: completed (**Action**), ingrained (**Habit**), retired (dropped after starting) or abandoned (never started).
_Avoid_: done, archived

**Action**:
A **Commitment** done once and then finished.
_Avoid_: task, to-do, step

**Habit**:
A **Commitment** to a recurring behaviour; new Habits are stacked on top of established ones.
_Avoid_: routine, practice

**Review**:
The check-in on **Commitments** that are due, which updates their state.
_Avoid_: check-up, retro
