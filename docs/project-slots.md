# Project Slots — ADHD-Safe Project Switching

> Context switching is where agent work dies. Slots make switching a first-class operation instead of an archaeology dig.

## The Problem

One shared "current project" state file means: switch projects → old state bleeds into new work → stale receipts fire → agents resume last month's task mid-stream. Humans feel this as "why is it talking about the old thing?"

## The Slot Model

A **project slot** is a complete capsule:

```
projects/
├── active-project.json      # THE single source of truth: which slot is live
├── <slot-id>/
│   ├── PROJECT.md           # goal / status / NEXT STEP / context
│   ├── profile.json         # metadata (created, archived-from, etc.)
│   ├── books/               # project-specific reference books
│   ├── inbox/               # tasks for this project
│   └── outbox/              # deliverables from this project
└── _archive/                # retired slots, kept forever
```

`active-project.json` is tiny on purpose — one id, one name, one path. Everything reads it; only the slot manager writes it.

## The Rules

1. **New project archives the old one.** Move its slot to `_archive/` intact. No deletion.
2. **Switching clears lane state by default** — outboxes + processed receipts wipe so last project's deliverables can't bleed into this one's dispatches.
3. **Every dispatch brief injects the active PROJECT.md** (capped — reload-proof context). Agents never wonder what they're working on.
4. **PROJECT.md NEXT STEP is updated as work progresses**, not at session end. Crash-safe continuity.
5. **Boot contract starts at active-project.json** — before memory, before session history.

## PROJECT.md Template

```markdown
# Project: <name>

## Goal
What done looks like — one paragraph.

## Status
Current phase + what just happened.

## NEXT STEP
The single next action. Specific enough to execute cold.

## Context
Key paths, decisions, constraints a fresh boot needs.

## Decisions Log
- date — decision — why
```

NEXT STEP is the load-bearing line. A returning agent (or a farm worker) should be able to act on it with zero other context.

## Why "ADHD-Safe"

The human property this system respects: attention arrives in bursts, sometimes days apart. A good slot means resuming is zero-effort —

- Open dashboard → see active project + book preview
- Read NEXT STEP → know exactly where things stand
- Old work can't contaminate; nothing needs re-explaining

Switching cost drops from "reorient for 20 minutes" to "read one file."

## Orchestrator Integration

- Mission Control shows active slot name + PROJECT.md preview with New / Switch / Archive buttons
- Project books are uploadable through the control plane (agents poll, humans drop)
- Archive-on-new keeps history queryable without cluttering the live view

See [agent-farm-mission-control.md](agent-farm-mission-control.md) for how dispatch consumes slots.
