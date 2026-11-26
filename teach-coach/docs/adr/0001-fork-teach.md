# Fork Matt Pocock's teach skill rather than amend it or write a separate coach skill

Coaching turned out to be teaching pushed towards the action end of the knowledge–skills spectrum: the same workspace, Mission, learning records and zone of proximal development, plus Commitments and strict grounding in the user's own Library. We forked `teach` from mattpocock/skills v1.3.2 (commit 6f7f783, 2026-11-25) into one skill, `teach-coach`, and denied the vendored `mattpocock-skills:teach`. Editing the vendored copy would be overwritten by the daily pull, and a separate `coach` skill would duplicate the shared concepts and let them drift.

## Consequences

- Upstream improvements to `teach` no longer arrive automatically. The local marketplace clone keeps pulling them, so compare `skills/productivity/teach/` in that clone against this folder from commit 6f7f783 onwards and merge by hand what fits.
- Naming deliberately departs from upstream for consistency across outputs: `lr-NNNN-`, `c-NNNN-`, `l-NNNN-`. Lessons also do not follow the `YYMMDD <topic>.html` naming parked in `book-manager/parked-decisions.md`.
