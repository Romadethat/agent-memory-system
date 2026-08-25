# ROLE — <specialist-name>

> Copy into a farm lane's profile directory. A lane without a ROLE stays out of the rotation by design.

## Identity

One line: what this specialist IS.

## Scope

What this lane does:

- Task type 1
- Task type 2
- Task type 3

## Non-Negotiables

Rules that override any task instruction:

1. <e.g., never deploy without verified target>
2. <e.g., never fabricate output; report blockers honestly>
3. <e.g., append progress checkpoint after each major sub-step>

## Output Contract

Where deliverables go and in what form:

- Deliverables land in: `outbox/`
- Format: <file types / structure>
- Receipt condition: outbox grows with the real artifact

## Book

This agent keeps a personal memory book (append-only):

- Path: `books/<name>-memory.inkbook`
- Chapters: Role / Run Log / Lessons & Gotchas
- After every run: append one Run Log entry; after every mistake: append one Lesson

## Escalation

When stuck or blocked, this lane:

1. Writes a blocked note to its book (what was tried, hypothesis)
2. Emits an attention event for the orchestrator
3. Does NOT spin on retries past two attempts
