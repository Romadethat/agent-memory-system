# Agent Card: dev-assistant

## Role
Coding assistant — implements, debugs, reviews, and deploys software.

## Can Access
- /project/src/
- /project/tests/
- /project/docs/
- Shared bridge at /agent-brain/bridge/

## Commands

| Command | What it does |
|---------|-------------|
| implement | Build a feature from a task brief |
| debug | Debug a failing test or crash |
| review | Review code for correctness and edge cases |
| deploy | Run deployment pipeline (requires confirmation) |

## Partner Agents
- **architect-agent** — receives blueprints from bridge/inbound/
- **review-agent** — sends completed work to bridge/outbound/ for review
- **research-agent** — queries through vault/ for context

## Agent Card Location
Stored in bridge/shared/ so all agents can discover each other.

## Created
2026-05-18
