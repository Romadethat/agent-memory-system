# Master AI Agent Memory System Template

> **Memory is for active context. Files are for permanent knowledge.**

![Version](https://img.shields.io/badge/version-v5.3.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow)
![Status](https://img.shields.io/badge/status-starter--kit--ready-brightgreen)

---

## What This Is

A file-based operating structure for AI assistants and local agents. It gives an agent:

- A consistent identity
- Persistent project state
- User preferences
- Reusable skills
- Vault-based knowledge
- Daily logs
- Multi-agent handoff folders
- Optional cross-machine relay ingestion
- One-command setup scripts

## What Problem It Solves

Without structure, agents forget what project they're on, what rules to follow, what files matter, what happened last session, and what other agents already did.

This system fixes that by putting long-term knowledge in files the agent can search, read, and update when needed — instead of cramming everything into short-term memory.

For multi-agent setups, it also gives agents a file-based bridge so they can exchange handoffs without relying on shared chat history. Advanced users can extend that bridge into a cloud-synced relay where one agent drops files in a shared Drive folder and another local agent normalizes them into `.md`/`.txt` messages with `.ready` markers.

## Who This Is For

- Local AI agent builders
- Developers building assistant workflows
- Multi-agent experimenters
- Obsidian vault users who want AI context
- Anyone tired of restarting from zero every session

---

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/Romadethat/agent-memory-system.git
cd agent-memory-system
```

### 2. Create your agent brain

```bash
# Default location (~/agent-brain)
python scripts/init-agent-brain.py

# Custom path (Linux/Mac)
python scripts/init-agent-brain.py --path ~/my-brain

# Custom path (Windows — keep off C: drive)
python scripts/init-agent-brain.py --path D:/agent-brain
```

### 3. Tell your agent

```
Read ~/agent-brain/AGENT_PROFILE.md and ~/agent-brain/project-state.md
```

### 4. Start working

The system auto-logs. At the end of each session:

```bash
python scripts/end_of_session.py "What I built and learned today"
```

---

## Example Workflow

Here's what a typical session looks like with the system:

```
1. You say: "Build a login page"
2. Agent reads project-state.md → sees active project
3. Agent searches vault/ for past login designs or auth patterns
4. Agent loads a skill from skills/ for the task type
5. Agent builds the login page
6. Session ends → agent runs end_of_session.py
7. Agent writes daily log, updates project-state.md
8. Next session, agent reads project-state.md and picks up where it left off
```

---

## How to Customize

The system is designed to grow with you. Here's how to make it yours:

### 1. Replace the examples
- Edit `AGENT_PROFILE.md` with your agent's name and personality
- Edit `user-rules.md` with your preferences (communication style, tools, projects)
- Update `project-state.md` with your actual project

### 2. Add your own skills
Turn any task you do more than once into a skill file in `skills/`:
- How you review code
- How you deploy your project
- How you research a topic
- How you onboard a client

### 3. Fill your vault
As you learn things, save them to `vault/`:
- `vault/projects/` — project plans and architecture notes
- `vault/references/` — research, links, examples
- `vault/concepts/` — patterns, principles, ideas
- `vault/decisions/` — why you built things a certain way

### 4. Add agents
When you have multiple agents (or want to), create a `bridge/` folder for task handoffs. Each agent gets an agent card in `bridge/shared/agent-cards/`.

### 5. What NOT to customize (keep these generic)
- `docs/` — the documentation should stay reusable so others can benefit
- `templates/` — starter files that work for anyone
- `scripts/` — automation tools that should work across setups

---

## What Gets Created

```
agent-brain/
├── AGENT_PROFILE.md      # Who the agent is
├── MEMORY_RULES.md       # Memory vs files guide
├── project-state.md      # Current work — source of truth
├── session-state.md      # Session continuity (survives drops)
├── user-rules.md         # Your preferences
├── thinking-protocol.md  # How the agent reasons
├── simulation-protocol.md# How the agent thinks ahead
├── end-session-checklist.md # Save button
├── boot-protocol.md      # Session startup sequence
│
├── vault/                # Long-term knowledge
├── skills/               # Reusable workflows
├── thoughts/             # Auto-captured learning (raw → consolidated → patterns)
├── logs/daily/           # Session history
│
├── index/                # Navigation maps (projects, skills, templates)
├── templates/            # Reusable file blueprints
├── prompts/              # Reusable prompt templates
│
├── bridge/               # Multi-agent handoffs
│   ├── inbox/            # Incoming tasks
│   ├── outbound/         # Completed responses
│   ├── done/             # Archived tasks
│   ├── blocked/          # Stuck items
│   ├── logs/             # Bridge activity
│   ├── shared/           # Agent cards, protocols
│   └── signals/          # Agent ping files
│
├── crew-agents/          # Agent cards for every capability
├── scripts/              # Setup + session tools
├── briefcase/            # Encrypted secrets
├── ideas/                # Random thought catcher
└── reference/            # Screenshot + analysis archive
```
For advanced multi-agent setups, an optional relay structure can be added:

```
relay/
├── inbox/                # Canonical relay messages
├── outbox/               # Agent responses
├── archive/              # Processed relay history
├── protocol/             # Relay laws, naming, safety, ready-marker rules
└── agents/               # Per-agent cards
```

---

## System Flow

```
User Request
     │
     ▼
Read AGENT_PROFILE.md + project-state.md
     │
     ▼
Search vault/ for relevant knowledge
     │
     ▼
Load skill from skills/ if needed
     │
     ▼
Follow MEMORY_RULES.md (memory vs files)
     │
     ▼
Execute task
     │
     ▼
Update logs/daily/ + project-state.md
     │
     ▼
Create bridge/ handoff if needed
```

See [docs/architecture.md](docs/architecture.md) for the full diagram.

---

## Multi-Agent Relay Bridge

The basic [bridge folder](docs/multi-agent-bridge.md) works on one machine with shared folders. For cross-machine or cloud-to-local agent setups, use the optional relay ingestion pattern:

```
Cloud Drop Zone
     ↓
Local Ingestion Agent
     ↓
Canonical .md/.txt relay file + matching .ready marker
     ↓
Relay inbox processing
     ↓
Archive after processing
```

This pattern is useful when an agent can only create Google Docs, web exports, or other native files. A local ingestion agent can convert those files into plain text relay messages before another agent processes them.

See [docs/multi-agent-bridge.md](docs/multi-agent-bridge.md) and [docs/full-reference-guide.md](docs/full-reference-guide.md) for the full relay protocol.

---

## Examples

| Example | What it shows |
|---------|--------------|
| [basic-agent-brain](examples/basic-agent-brain/) | Complete solo agent setup with profile, rules, state, and preferences |
| [multi-agent-bridge](examples/multi-agent-bridge/) | Multi-agent handoff workflow with inbox/outbound/done lifecycle |
| [example-session](examples/example-session/) | Before/after comparison of a session with the system |
| [zoro-style-agent-card](examples/zoro-style-agent-card.md) | Agent card for multi-agent discovery |

---

## Documentation

| Doc | What's inside |
|-----|--------------|
| [docs/architecture.md](docs/architecture.md) | System flow diagram and directory structure |
| [docs/full-reference-guide.md](docs/full-reference-guide.md) | Deep 58-section reference, including thought pipeline, agent crew system, session state, index system, boot protocol, meta-rules, and cross-machine relay patterns |
| [docs/windows-setup.md](docs/windows-setup.md) | Windows-specific path and env setup |
| [docs/obsidian-setup.md](docs/obsidian-setup.md) | Using your agent brain as an Obsidian vault |
| [docs/multi-agent-bridge.md](docs/multi-agent-bridge.md) | Multi-agent coordination and relay ingestion patterns |
| [docs/security-notes.md](docs/security-notes.md) | Safe usage guidance |

---

## Security

This system stores project notes, preferences, and logs as plain-text files. Do not commit secrets, API keys, or passwords to any public repo.

### What to Commit
- `docs/` — documentation
- `templates/` — starter files
- `examples/` — sample setups
- `scripts/` — automation tools
- `skills/` — reusable procedures (use placeholders, not real data)

### What NOT to Commit
- `AGENT_PROFILE.md` — your agent's identity (keep private)
- `project-state.md` — your active project details
- `user-rules.md` — your personal preferences
- `logs/` — session history (daily logs stay local)
- `vault/` — your private knowledge
- `bridge/` — inter-agent conversations
- `briefcase/` — encrypted secrets (by design)
- `ideas/` — random thoughts
- `thoughts/` — captured learning

The `.gitignore` file is pre-configured to protect these folders. If you fork or clone, check that it's in place before committing.

Relay files are advisory only. Do not let an agent auto-execute relay content, and do not pass secrets through shared relay folders.

See [SECURITY.md](SECURITY.md) for details.

## Contributing

Contributions welcome — skills, templates, docs, scripts, examples.

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Roadmap

- Demo GIF showing agent startup flow
- More example skills (design review, deployment, research)
- MCP server example for agent tool integration
- CLI wrapper for quicker initialization
- Obsidian setup walkthrough video
- Testing script for generated agent brains
- Package installer (pip, homebrew)

## License

MIT — see [LICENSE](LICENSE).
