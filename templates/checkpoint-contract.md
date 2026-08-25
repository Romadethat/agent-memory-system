# Checkpoint Contract — Progress File

> Farm-dispatched agents append to this file after EACH major sub-step. The dispatcher reads it on boot (resume briefs) and after timeouts (partial-progress detection). Copy per task: `progress-<task>.md` in the lane outbox.

## Task

<task id / one-line description>

## Contract

- Append a line after each completed step. Never delete or rewrite previous lines.
- On resume: continue from the last uncompleted step. Do NOT redo completed gates.
- If blocked >2 attempts: write a BLOCKED note with what was tried + hypothesis, then stop.

## Progress

Format: `- [x] Step N: <name> — <timestamp> (<one-line result>)`

- [x] Step 1: survey existing files — 2026-08-25 14:02 (found 3 modules, conventions noted)
- [x] Step 2: draft skeleton — 14:19 (module X created)
- [ ] Step 3: implement core logic
- [ ] Step 4: verify + deliver artifact to outbox

## Blocked Notes (only when blocked)

<what was tried / error received / current hypothesis>
