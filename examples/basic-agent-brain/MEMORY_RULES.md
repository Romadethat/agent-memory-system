# MEMORY_RULES.md — Example

## Core Rule

**Memory is for active context. Files are for permanent knowledge.**

## What Goes in Memory

Memory should only store compact, high-value facts used across every session:

- User's communication preferences
- Current project name and role
- Critical Do Not Do rules
- Environment facts (OS, paths, tools)
- Frequently used conventions

## What Does NOT Go in Memory

Do not store these in memory — use files instead:

| Content | File Location |
|---------|--------------|
| Project plans | `vault/projects/plan.md` |
| Code patterns | `vault/references/` |
| Daily work logs | `logs/daily/YYYY-MM-DD.md` |
| Task procedures | `skills/task-name.md` |
| Long instructions | `user-rules.md` |
| API documentation | `vault/references/api-notes.md` |
| Session decisions | `logs/daily/` or `vault/decisions/` |

## Why This Matters

An agent with too much in memory spends tokens loading stale context. A lean agent reads files on demand — it has the information it needs without carrying everything at once.

## Memory Limits

- If a memory entry would be longer than 2-3 sentences, it belongs in a file
- If you reference it in every session, it might be memory-worthy
- If you reference it once a week or less, it might be a vault document
