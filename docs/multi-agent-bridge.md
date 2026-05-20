# Multi-Agent Bridge

The bridge system allows multiple AI agents to coordinate without relying on shared chat history. This covers two patterns:

1. **Basic local bridge** — agents on the same machine sharing a folder
2. **Advanced cross-machine relay** — agents on different machines, syncing through cloud storage

---

## Problem

When multiple agents work on the same project, they each have isolated context windows. Agent A finishes a task, but Agent B has no way to know what happened. Chat memory is per-agent — not shared.

For agents on different machines (or different environments like ChatGPT vs CLI), the problem is worse — they can't reach each other's file systems at all.

---

## Solution

### Basic Local Bridge

A file-based handoff system on a shared folder. Any agent can:

1. Drop a task into another agent's inbox
2. Pick up work from its own inbox
3. Signal completion through outbound files
4. Log progress to shared bridge logs

```
bridge/
├── inbox/         Incoming tasks from other agents
├── outbound/      Completed responses or handoffs
├── done/          Finished task records (archive)
├── blocked/       Tasks that cannot continue
├── logs/          Bridge activity history
└── shared/        Agent cards, protocols, shared state
```

### Advanced Cross-Machine Relay

For agents that cannot share a filesystem (cloud-based agents, different machines, different humans), use a **cloud-synced relay folder** (Google Drive, Dropbox, OneDrive).

```
Cloud Agent drops native file (Google Doc, web export, etc.)
     ↓
Cloud sync folder
     ↓
Local Ingestion Agent discovers file (rclone / Drive API)
     ↓
Export → extract text → normalize to .md or .txt
     ↓
Save canonical relay file + matching .ready marker into relay/inbox/
     ↓
Receiving agent processes message
     ↓
Archive after processing
```

---

## Folder Structure

### Basic Local Bridge

```
bridge/
├── inbox/         Incoming tasks from other agents
├── outbound/      Completed responses or handoffs
├── done/          Finished task records (archive)
├── blocked/       Tasks that cannot continue
├── logs/          Bridge activity history
└── shared/        Agent cards, protocols, shared state
```

### Advanced Cross-Machine Relay

```
relay/
├── inbox/         Canonical relay messages + .ready markers
├── outbox/        Agent responses
├── archive/       Processed relay history
├── protocol/      Relay laws, naming, safety, ready-marker rules
└── agents/        Per-agent identity cards
```

---

## Handoff File Format

### Basic handoff

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

### Updated relay message header

For cross-machine relay messages, include metadata fields:

```md
# YYYY-MM-DD-FROM-to-TO-TYPE-description.md

[AGENT] ADVISORY EXPORT — REVIEW BEFORE USE

From: [Agent Name]
To: [Agent Name]
Date: YYYY-MM-DD
Type: GUIDE | QUESTION | ANSWER | LESSON | WARNING | STATUS | ARCHITECTURE_NOTE | REVIEW_REQUEST
Status: READY | RECEIVED | PROCESSING | ANSWERED | ARCHIVED | NEEDS_REVIEW
Protocol Version: 1.0
Authority level: Advisory only
No secrets included: YES
Real-World Action Authorized: NO

---
```

---

## Ready Marker Rule

A synced relay message should not be processed until it has a matching `.ready` marker:

```
message.md
message.md.ready
```

or:

```
message.txt
message.txt.ready
```

The marker guarantees the file is fully written and synced before any agent reads it. Cloud sync services may deliver files in chunks — the .ready marker prevents partial reads.

---

## Handoff Lifecycle

### Local bridge

1. Agent A creates `bridge/outbound/task-description.md`
2. Agent B scans `bridge/inbox/` (or shared location)
3. Agent B picks up the file from `inbox/`
4. Agent B completes the task
5. Agent B moves the file to `bridge/done/` or creates a response
6. Agent B logs the handoff in `bridge/logs/`

If stuck: → Move to `bridge/blocked/` with a note about why

### Cross-machine relay

1. Atlas creates a Google Doc in `G:\My Drive\` root
2. Zoro runs `zoro gdoc --inbox "topic"` to discover and ingest
3. rclone exports the doc → text extracted → `.md` + `.ready` placed in `relay/inbox/`
4. Zoro reads, processes, and responds
5. Response placed in `relay/outbox/`, original archived

---

## Agent Conventions

| Convention | Purpose |
|------------|---------|
| Prefix files `YYYY-MM-DD--task-name.md` | Sorted, no collisions |
| Include `from:` and `to:` in frontmatter | Clear routing |
| Set `status:` to `ready`, `in-progress`, `done`, or `blocked` | Lifecycle tracking |
| Log every bridge action to `logs/` | Audit trail |
| Store agent cards in `shared/` | Self-discovery |

---

## Multi-Agent Discovery

Each agent should have an `AGENT_CARD.md` in the bridge/shared/ folder (local) or `relay/agents/` folder (cross-machine):

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

---

## Protocol Files

Store operating rules separately from daily messages:

```
relay/
├── protocol/
│   ├── relay-laws.md
│   ├── naming-convention.md
│   ├── message-types.md
│   ├── ready-marker-rules.md
│   └── safety-rules.md
```

This keeps protocol information accessible to every agent without burying it inside message exchanges.

---

## Optional: Multi-Agent Relay Ingestion Layer

When a cloud-only agent (like ChatGPT) drops a Google Doc in the shared Drive root, a local ingestion agent can normalize it:

```bash
# Discover new docs
rclone lsjson gdrive: --include "*ATLAS-to-ZORO*"

# Export as text and save to relay inbox with .ready marker
zoro gdoc --inbox "partial-name-match"
```

### Key concepts

- **Cloud Drop Zone** — A root folder or Drive location where agents can drop files in their native format
- **Local Ingestion Agent** — An agent that scans the drop zone, converts files to canonical format, and places them in the relay inbox
- **Canonical Relay Format** — Plain `.md` or `.txt` file + `.ready` marker. All normalized before processing
- **Archive After Processing** — Once ingested, move files to archive. Don't re-process

---

## Cross-Machine Relay Notes

When setting up a cross-machine relay via Google Drive:

1. **Shared folders don't auto-sync** — Recipients must open the share link in a browser and click "Add shortcut to Drive" before the folder appears locally
2. **Some agents can't write raw .md** — ChatGPT/Atlas creates Google Docs (.gdoc). A local ingestion agent with rclone solves this
3. **.ready markers are essential** — Drive syncs in chunks. Always pair a message file with a matching .ready marker
4. **Human review is always possible** — Cloud-synced files are visible to both humans at all times
5. **No secrets** — Never pass passwords, API keys, or tokens through relay files

---

## Typical Workflow

1. **Architect agent** designs a blueprint → drops to relay inbox
2. **Local ingestion agent** normalizes format → places `.md` + `.ready`
3. **Coding agent** picks up → implements → archives
4. **Review agent** reviews → creates review note
5. **Relay log** captures every transition

No chat memory needed. The files are the truth.
