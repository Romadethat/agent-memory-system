# Agent Memory System — Architecture

## Flow Diagram

```
User sends request
       │
       ▼
  ┌─────────────┐
  │   Read      │◄──── AGENT_PROFILE.md (identity)
  │  project-   │◄──── project-state.md (current state)
  │  state.md   │
  └─────┬───────┘
        │
        ▼
  ┌─────────────┐
  │  Search     │◄──── vault/ (long-term knowledge)
  │  vault/     │
  └─────┬───────┘
        │
        ▼
  ┌─────────────┐
  │  Load skill │◄──── skills/ (reusable workflows)
  │  if needed  │
  └─────┬───────┘
        │
        ▼
  ┌─────────────┐
  │  Check      │◄──── MEMORY_RULES.md (memory constraints)
  │  memory     │
  │  rules      │
  └─────┬───────┘
        │
        ▼
  ┌─────────────┐
  │  Execute    │     Use the best approach
  │  task       │     (direct, tool, or skill)
  └─────┬───────┘
        │
        ▼
  ┌─────────────┐
  │  Update     │────► logs/daily/YYYY-MM-DD.md
  │  logs +     │────► project-state.md
  │  state      │
  └─────┬───────┘
        │
        ▼
  ┌─────────────┐
  │  Bridge     │────► bridge/outbound/ (to other agents)
  │  handoff    │────► bridge/inbox/ (from other agents)
  │  if needed  │
  └─────────────┘
```

## Directory Structure

```
agent-brain/
├── AGENT_PROFILE.md      # Who the agent is
├── MEMORY_RULES.md       # What goes in memory vs files
├── project-state.md      # Current work — source of truth
├── user-rules.md         # Your preferences
├── thinking-protocol.md  # How to approach tasks
│
├── vault/                # Long-term knowledge (4095+ pages)
├── skills/               # Reusable workflows
├── logs/daily/           # Session history
│
├── bridge/
│   ├── inbox/            # Incoming relays from other agents
│   ├── outbound/         # Outgoing relays to other agents
│   ├── done/             # Completed handoffs
│   ├── blocked/          # Stuck items
│   ├── logs/             # Bridge activity log
│   └── shared/           # Agent cards, shared protocols
│
├── scripts/              # Automation (setup, EOS, CLIs)
├── prompts/              # Reusable prompt templates
└── templates/            # File templates for new items
```

## Key Principle

**Memory is for active context. Files are for permanent knowledge.**
