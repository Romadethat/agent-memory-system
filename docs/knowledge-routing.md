# Knowledge Routing — One Home Per Fact

> Every piece of knowledge has exactly ONE canonical home. Duplication isn't redundancy — it's future contradiction.

## The Routing Table

| Fact type | Home | Why |
|-----------|------|-----|
| Who the user is, preferences, corrections | **Agent memory** (hot, injected every turn) | Must shape every response without being asked |
| Repeatable procedure | **Skill file** | Loadable, versionable, patchable |
| Deep reference knowledge | **Vault** (wiki/entities/sources) | Searchable shared world; librarians can shelve it |
| Personal lesson / candidate pattern | **Sandbox book** | Awaiting proof; promotion gate decides |
| Self-doctrine / identity rules | **Self/Memory book** (surgical appends) | Durable record of who the agent is |
| Lineage events, mutations, awakenings | **Evolution book** | Append-only history of what the agent became |
| Current project state | **Slot PROJECT.md** | Single source of truth for "what are we doing" |
| Farm specialist lessons | **That agent's own book** | Vault = shared world, books = personal experience |

When in doubt: point, don't duplicate. Cross-reference with links.

## Memory vs Files — The Classic Split

- **Memory** = active context. Small, hot, re-read every session. Facts that must never be re-explained.
- **Files** = permanent knowledge. Large, cold, searchable on demand. Everything else.

The failure modes are symmetrical:
- Everything in memory → context overflow, the agent drowns
- Everything in files → the agent forgets to look, knowledge rots unvisited

## The Staleness Law

A fact that will be stale in a week does not belong in memory. Task progress, PR numbers, "phase 2 done," file counts — that's session history, not identity. Route it to logs/books/slots where it can age gracefully.

Corollary: when memory and files disagree about something stable, trust the newer source and RECONCILE the stale one immediately. Un-reconciled contradictions compound.

## Corrections Are Gold

When the user corrects you ("it's X not Y", "stop doing Z"), that correction is the highest-value memory write available. It prevents repeat steering — the entire point of persistent memory. Record:

- The fact itself
- The correction date
- The exact trigger phrase if they gave one ("when I say drop it, I mean drop it")

## Librarian Pattern (optional at scale)

Small local models can work the vault as librarians so the frontier model doesn't burn context on housekeeping:

- **Organizer/Researcher** — catalogs, classifies, builds source packets from vault content
- **Author** — compiles verbatim reference books (small models paraphrase badly; reference books must build VERBATIM from source)
- Run on cron; every Nth run = reflection pass where each librarian updates its own memory book

Key lesson: small models echo JSON templates — feed them plain text + simple headers, not structured schemas.

## Governance Gate

At library scale, ask before trusting any book:

1. Which copy is **canonical**? (hash comparison catches drift)
2. What **edition** is it, valid from when, owned by whom?
3. Is it **current or historical**? Historical ≠ dead — why-questions traverse lineage.
4. Is it a **fork**? Ancestor ≠ duplicate. When in doubt, don't delete.
