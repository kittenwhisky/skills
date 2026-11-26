# RESOURCES.md Format

`RESOURCES.md` is the controlled set of sources for this Mission. Knowledge comes from here, never from parametric guesses; wisdom comes from the communities listed here. The grounding rules that govern it are in [SKILL.md](SKILL.md#grounding).

## Structure

```md
# {Topic} Resources

## Primary resources

### Knowledge

- Anne Fletcher, *Thin for Life*: `C:\...\Books & Articles\Weightloss\Anne Fletcher - Thin for life.md`
  What long-term weight-loss maintainers actually do. Use for: maintenance habits, environment changes.

### Wisdom (Communities)

- Local: Thursday walking group at {park}
  Use for: accountability, real-world feedback on new routines.

## Secondary resources

### Knowledge

- [NHS: "Eating slowly"](https://example.com) (added with permission 2026-12-10)
  Use for: the physiology of satiety, which the Library does not cover.

### Wisdom (Communities)

## Gaps

- Satiety physiology: no Primary resource covers it (2026-12-10, Secondary search approved).
```

## Rules

- **Primary means chosen by the user.** Library books and communities the user picked. Only the user moves a resource into Primary.
- **Secondary means found by the agent,** and only with the user's permission. Note the date permission was given.
- **Library books by path.** List each book by the full path of its converted Markdown file. Make it a wikilink only when the Library and this workspace share an Obsidian vault.
- **Annotate every entry.** One line: what it covers and when to reach for it.
- **Surface gaps explicitly.** When the Primary resources fall short of what the Mission needs, record it under `## Gaps`, with the date and whether a Secondary search was approved.
- **Prune ruthlessly.** A resource that turned out wrong, shallow or off-Mission is removed, not buried.
- **Record community preferences.** If the user opted out of joining communities, note it here so future sessions stop proposing them.
