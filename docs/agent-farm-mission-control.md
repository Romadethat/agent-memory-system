# Agent Farm + Mission Control — Orchestrated Multi-Agent Work

> One agent working serially is a hobby. A farm of specialists with a control plane, dispatch discipline, and receipts is infrastructure.

## The Shape

```
Mission Control (web dashboard)
     │  sees everything, controls anything
     ▼
Control Plane daemon (line-JSON over localhost socket)
     │  agents / status / send / events verbs
     ▼
Dispatcher (claim → boot → receipt loop)
     │  injects project context + checkpoint contract into every brief
     ▼
Specialist Lanes (auditor · builder · proof · stylist · smith · scout …)
     │  each lane = isolated agent profile + inbox/outbox
     ▼
Personal Memory Books (every specialist owns one)
```

## Lane Anatomy

Each specialist is an isolated agent profile with:

- **ROLE.md** — its identity, scope, and non-negotiables (no ROLE = stays out of rotation)
- **config.yaml** — model/provider binding, swappable at runtime from Mission Control
- **inbox/** — tasks arrive as files; nothing moves until the tree is right
- **outbox/** — deliverables land here; the dispatcher's success guard counts NEW outbox files
- **processed/** — consumed task receipts
- **books/\<name\>-memory.inkbook** — personal Run Log + Lessons chapters, append-only

## The Dispatch Loop

1. Task lands in a lane inbox (dropped by orchestrator or another agent)
2. Dispatcher claims it atomically (rename-claim prevents double-dispatch on crash)
3. Agent boots with a brief that includes: the task, the active PROJECT context, and the CHECKPOINT CONTRACT
4. Agent works, appending progress after each major sub-step
5. On completion: receipt event closes the task; watcher routes notifications to the ORCHESTRATOR agent, not the human
6. On timeout/crash mid-work: progress file survives → task marked PartialProgress → next boot gets a RESUME DIRECTIVE (continue from last uncompleted step; never redo completed gates)

## Checkpoint Contract

Long tasks must decompose into parts. Each part completion appends a checkpoint:

```markdown
## Progress — task-name
- [x] Step 1: survey existing files (2026-08-20 14:02)
- [x] Step 2: draft module skeleton (14:19)
- [ ] Step 3: implement core logic   ← crash happened here
- [ ] Step 4: verify + write receipt
```

This is the data-loss prevention layer. A 30-minute build that dies at minute 29 resumes at minute 29's frontier, not zero.

## False-Success Guard

`exit code 0` proves NOTHING. Receipts require evidence:

- Outbox must GROW (a build that wrote its deliverable elsewhere reads as failure — route heavy outputs through outbox or verify real artifacts directly)
- Watchers parse notification grammar; malformed notices are rejected and preserved for debugging
- Claim-before-append semantics prevent duplicate events from double instances

## Mission Control Dashboard Rules

Hard-won UI laws for any live ops view:

- Anything that accumulates lines MUST be size-locked — fixed-height panel, internal scroll, never grows the page
- New rows append; panel auto-pins to bottom until the user scrolls up (then it stays put)
- Derive per-agent activity from the event stream (dispatch opens a task window; receipt/error/timeout closes it) — don't poll processes for state you already logged
- Bind services to 127.0.0.1 explicitly; some browser harnesses block `localhost` but pass the literal IP

## Provider Flexibility

Lanes read provider/model from config at boot. A good control plane can rewrite that file live:

- Keep a registry of providers (base_url + model presets per provider)
- Switching = rewrite one config block; next dispatch picks it up
- Free-tier reality: models flake upstream sometimes. Retry later is a valid strategy; distinguish config bugs from upstream outages by probing the endpoint directly

## Personal Books Law

Every farm agent keeps its own memory book — NEVER shared:

> The vault is the shared world. Books are personal experience.

Append-only Run Log + Lessons & Gotchas chapters. The orchestrator may READ them; only the owner writes. At scale this is how you audit why a lane keeps failing without interrogating chat logs.
