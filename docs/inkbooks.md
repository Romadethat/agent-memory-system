# Inkbooks — Durable Agent Books

> Memory forgets between sessions. Files persist but scatter. Books are the middle layer: durable, structured, surgically editable knowledge artifacts an agent actually maintains.

## What an Inkbook Is

An `.inkbook` file is a portable notebook container (ZIP package with a manifest + notebook JSON) holding chapters and pages. Think of it as a book your agent owns:

- **Chapters** organize by theme (Operating Rules, Projects, Environment, People)
- **Pages** are individual entries — one lesson, one procedure, one decision record
- **Update Log** chapter tracks what changed and when (append-only)
- Books are portable — copy them between machines, hand them to other agents, archive them

## The Core Book Set

A mature agent keeps a small set of living books:

| Book | Holds | Rule |
|------|-------|------|
| **Self/Memory book** | Identity doctrine, operating rules, self-knowledge | Surgical appends only |
| **Sandbox book** | Candidate patterns awaiting promotion | Promote or reject — nothing lives here forever |
| **Evolution book** | Lineage events, mutations, genes/capsules | Append-only history |
| **Project books** | Per-project context (goal/status/next-step) | One per project slot |

Plus optional topical books: research volumes, reference libraries, skill collections.

## The Sandbox Promotion Gate

The Sandbox is how lessons earn permanence:

```
Learn something → record in Sandbox (with source + date)
     ↓
Reuse it 2–3 times, it holds up?
     ↓
Promote: move to the permanent book (or a skill)
     ↓
Rejected lessons stay recorded with WHY they failed
     ↓
Past Lessons chapter caches references, never duplicates content
```

Anti-pattern: promoting every first impression. The gate exists because some "lessons" are just one weird day.

## Surgical Editing Law

NEVER full-rebuild a living book. Rebuilds risk data loss and break page identity.

Instead use surgical operations:

- `add-page` — append one entry to a chapter
- `edit-page` / `rename-page` / `move-page` — targeted changes
- `delete-page` — moves to a recoverable trash, not oblivion
- `update-log` — append to the Update Log chapter
- Every operation: validate before AND after, timestamped backup first, atomic write

Full rebuild scripts are only acceptable for books you generate from scratch (e.g., compiling a fresh reference volume from sources) — never for a book that accumulated live history.

## Multi-Agent Updating

Books designed for multi-agent extension carry:

- An **Update Log** with dated additive sections (never silently rewrite)
- Clear **ownership** per chapter (who may append)
- **Companion links** to related books (point, don't duplicate)
- A **Book Index** page listing every book's path, update script, and scope

One fast doctrine book + deep audit books beats one bloated mega-book.

## Governance

When copies, forks, and historical editions accumulate:

- Track **canonical source** vs copies (hash comparison catches drift)
- Record **edition + validFrom + owner** on build
- Distinguish **historical** from **current** — historical ≠ dead; why-questions traverse lineage
- **Ancestor ≠ duplicate** — lineage beats duplicate detection; when in doubt, don't delete
- Ask the routing gate before trusting any book: which is canonical, who owns it, is it superseded?

See [knowledge-routing.md](knowledge-routing.md) for where a given fact belongs.
