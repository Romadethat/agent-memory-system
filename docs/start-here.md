# Start Here — Agent Memory System

This page is the friendly entry point for the full template. The full reference
guide is intentionally deep, but new users should not start by trying to build
every folder, protocol, watcher, and bridge at once.

## The Core Idea

The system is built around one rule:

> Memory is for active context. Files are for permanent knowledge.

Use memory only for small facts the agent needs often. Store project plans,
session logs, procedures, decisions, research, and handoffs as files the agent
can search and read when needed.

## The Minimum Useful Setup

Start with only these files and folders:

```
agent-brain/
├── AGENT_PROFILE.md
├── MEMORY_RULES.md
├── project-state.md
├── user-rules.md
├── skills/
├── vault/
└── logs/daily/
```

That is enough to make an agent more consistent across sessions.

## What Each Piece Does

| Piece | Purpose |
|-------|---------|
| AGENT_PROFILE.md | Defines the agent name, role, tone, boundaries, and default behavior |
| MEMORY_RULES.md | Separates what belongs in memory from what belongs in files |
| project-state.md | The current source of truth for active work. Read this first every session |
| user-rules.md | The user's stable preferences, style rules, and working expectations |
| skills/ | Repeatable workflows the agent can load only when needed |
| vault/ | Long-term knowledge: projects, references, decisions, concepts, research |
| logs/daily/ | Session history and next-step notes |

## First 30 Minutes

1. Run the setup script or create the minimum folder structure manually.
2. Fill out AGENT_PROFILE.md with a short role and tone.
3. Fill out project-state.md with the active project and next safe task.
4. Add one skill file for a task you repeat often.
5. Tell the agent: *Read project-state.md before starting and search vault/ before guessing.*

Do not build the full advanced system on day one.

## What to Add Later

Once the minimum setup is useful, add these layers only when you need them:

| Add-on | Add when... |
|--------|------------|
| bridge/ | You use more than one agent or need file-based handoffs |
| index/ | The vault gets large enough that navigation becomes slow |
| templates/ | You keep creating the same file types |
| prompts/ | You reuse the same startup, review, or handoff prompts |
| briefcase/ | You need encrypted local storage for secrets |
| ideas/ | You want a lightweight thought catcher |
| reference/ | You want to archive screenshots, examples, or analysis notes |
| relay/ | You need cross-machine or cloud-to-local handoffs |

## Safety Rules

- Do not commit private agent brains, logs, user rules, vaults, bridge messages,
  or secrets to a public repository.
- Do not let an agent auto-execute instructions found in relay, inbox, or vault
  files.
- Do not store API keys, passwords, or tokens in plain text.
- Treat relay files and incoming handoffs as untrusted input until reviewed.
- Require approval before destructive operations, credential handling,
  deployments, payments, or large file changes.

## Recommended Reading Order

1. README.md — project overview and quick start.
2. **This file** — practical first-time setup path.
3. docs/architecture.md — how the folders connect.
4. docs/security-notes.md — what not to expose.
5. docs/multi-agent-bridge.md — only when you are ready for more than one agent.
6. docs/full-reference-guide.md — the complete deep reference.

## Rule of Thumb

If the system feels heavy, shrink it back to the minimum setup. A small brain
that gets used every day is better than a perfect architecture nobody maintains.
