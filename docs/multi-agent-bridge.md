# Multi-Agent Bridge

The bridge folder allows multiple AI agents to coordinate without relying on shared chat history.

## Problem

When multiple agents work on the same project, they each have isolated context windows. Agent A finishes a task, but Agent B has no way to know what happened. Chat memory is per-agent — not shared.

## Solution

The bridge folder is a file-based handoff system. Any agent can:

1. Drop a task into another agent's inbox
2. Pick up work from its own inbox
3. Signal completion through outbound files
4. Log progress to shared bridge logs

## Folder Structure

```
bridge/
├── inbox/         Incoming tasks from other agents
├── outbound/      Completed responses or handoffs
├── done/          Finished task records (archive)
├── blocked/       Tasks that cannot continue
├── logs/          Bridge activity history
└── shared/        Agent cards, protocols, shared state
```

## Handoff File Format

```md
---
from: Agent-A
to: Agent-B
type: task-handoff
status: ready
priority: P1
---

## Task

[What needs to be done]

## Context

[Background the agent needs]

## Files

- path/to/file.ext

## Expected Output

[What success looks like]
```

## Handoff Lifecycle

```
1. Agent A creates bridge/outbound/task-description.md
2. Agent B scans bridge/inbox/ (or shared location)
3. Agent B picks up the file from inbox/
4. Agent B completes the task
5. Agent B moves the file to bridge/done/ or creates a response
6. Agent B logs the handoff in bridge/logs/

If stuck:
  → Move to bridge/blocked/ with a note about why
```

## Agent Conventions

| Convention | Purpose |
|------------|---------|
| Prefix files `YYYY-MM-DD--task-name.md` | Sorted, no collisions |
| Include `from:` and `to:` in frontmatter | Clear routing |
| Set `status:` to `ready`, `in-progress`, `done`, or `blocked` | Lifecycle tracking |
| Log every bridge action to `logs/` | Audit trail |
| Store agent cards in `shared/` | Self-discovery |

## Multi-Agent Discovery

Each agent should have an `AGENT_CARD.md` in the bridge/shared/ folder:

```md
# Agent Card: Agent-A

## Role
Coding assistant focused on backend work.

## Can Access
- /project/src/
- /project/tests/

## Commands
| Command | What it does |
|---------|-------------|
| review  | Review a pull request |
| build   | Build and test the project |

## Partner Agents
- Agent-B (frontend) — bridge/outbound/ for handoffs
- Agent-C (design) — bridge/inbox/ for incoming designs

## Created
2026-05-18
```

## Typical Workflow

1. **Architect agent** designs a blueprint → drops to `bridge/outbound/` 
2. **Coding agent** picks up from `bridge/inbox/` → implements → moves to `bridge/done/`
3. **Review agent** picks up from `bridge/done/` → reviews → creates review note
4. **Bridge log** captures every transition

No chat memory needed. The files are the truth.
