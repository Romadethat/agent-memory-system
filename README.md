# Master AI Agent Memory System Template

**Memory is for active context. Files are for permanent knowledge.**

---

## Starter Kit — v5.0

This repo now includes a ready-to-use starter kit in addition to the full reference guide below.

### Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Romadethat/agent-memory-system.git

# 2. Run the one-command installer
python agent-memory-system/scripts/init-agent-brain.py --path ~/agent-brain

# 3. Tell your agent:
#    "Read ~/agent-brain/AGENT_PROFILE.md and ~/agent-brain/project-state.md"

# 4. Start working. The system auto-logs.
```

**Windows users:** Use `--path D:/agent-brain` to keep data off your system drive.

### What You Get

```
agent-brain/
├── AGENT_PROFILE.md      # Who the agent is — fill in your info
├── MEMORY_RULES.md       # What goes in memory vs files
├── project-state.md      # Current work — source of truth
├── user-rules.md         # Your preferences
├── thinking-protocol.md  # How to approach tasks
├── vault/                # Long-term knowledge
├── skills/               # Reusable workflows
├── logs/daily/           # Session history
├── bridge/               # Multi-agent handoffs
├── scripts/              # Automation (setup, EOS)
├── prompts/              # Reusable prompt templates
└── templates/            # File templates for new items
```

### Starter Kit Files

| File | What it does |
|------|-------------|
| `templates/AGENT_PROFILE.md` | Identity card template |
| `templates/MEMORY_RULES.md` | Memory vs file rules |
| `templates/project-state.md` | Current work tracker |
| `templates/user-rules.md` | User preferences |
| `templates/thinking-protocol.md` | Agent thinking flow |
| `templates/SKILL.md` | New skill template |
| `scripts/init-agent-brain.py` | One-command installer |
| `scripts/end_of_session.py` | Session closer |
| `skills/code-review-checklist.md` | Example skill |
| `skills/daily-summary.md` | Example skill |
| `skills/project-handoff.md` | Example skill |
| `skills/debugging-flow.md` | Example skill |
| `assets/architecture.md` | Architecture diagram |

### Agent Card for MCP/Antigravity

Every plugin and agent needs an AGENT_CARD.md for multi-agent discovery:

```md
# Agent Card: your-agent-name
## Role
What this agent does.
## Can Access
- paths/it/can/read
## Commands
| Command | What it does |
|---------|-------------|
## Partner Agents
How other agents can use this plugin.
## Created
YYYY-MM-DD
```

---

### Full Reference (43 sections)

The complete reference guide follows below. It covers every component in detail:

1. [Agent Identity](templates/AGENT_PROFILE.md) — Who the agent is
2. [Memory Rules](templates/MEMORY_RULES.md) — What to remember vs save as files
3. [Project State](templates/project-state.md) — Current work tracking
4. [User Rules](templates/user-rules.md) — Your preferences
5. [Thinking Protocol](templates/thinking-protocol.md) — How the agent thinks
6. Vault — Long-term knowledge base
7. Skills — Reusable workflows
8. Daily Logs — Session history
9. Bridge — Multi-agent handoffs
10-43. Advanced patterns (CLI, Plugins, API, Signals, etc.)

*[The original 43-section reference continues below — see the full document for complete details]*
