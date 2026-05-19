# Obsidian Setup Guide

Using Obsidian as your agent's knowledge vault is optional but powerful.

## Why Obsidian

Obsidian gives you:

- Full-text search across your agent's knowledge base
- Graph view of connected ideas
- Visual previews and note editing
- Backlinks and deep linking between notes
- Local-only storage (no cloud dependency)

## Setup

### Option 1: Agent Brain as Its Own Vault

```
1. python init-agent-brain.py --path D:\agent-brain
2. Open Obsidian → Manage Vaults → Open folder as vault
3. Select D:\agent-brain
```

Your agent brain becomes a full Obsidian vault. The `vault/` folder is nested inside.

### Option 2: Agent Brain Inside an Existing Vault

```
1. Open your existing Obsidian vault
2. python init-agent-brain.py --path /path/to/vault/agent-brain
```

The agent lives in a subfolder inside your existing vault. Good for personal knowledge + agent context in one place.

## Folder Structure in Obsidian

```
agent-brain/                    ← Opens as vault
├── AGENT_PROFILE.md            ← Shows in sidebar
├── project-state.md            ← Pin this for quick access
├── vault/                      ← Full Obsidian features
│   ├── projects/               ← Graph view, backlinks
│   ├── references/             ← Full-text search
│   └── decisions/              ← Wiki links [[like-this]]
├── logs/daily/                 ← Calendar view possible
├── skills/                     ← Tagged workflows
└── templates/                  ← Obsidian template plugin
```

## Tips

- **Pin `project-state.md`** to the Obsidian sidebar for one-click access to current state
- **Use `vault/` for deep knowledge** — full-text search means your agent can find anything
- **Tag skills** with `#skill` for quick filtering
- **Link decisions** with `[[wikilinks]]` to connect related notes
- **Daily logs** can feed into Obsidian's daily notes plugin

## What Won't Work in Obsidian

- `bridge/` folders — these are agent-only handoff points, not meant for human editing
- `scripts/` — keep these in a code editor, not Obsidian

## Optional Plugins

| Plugin | Why |
|--------|-----|
| Daily Notes | Auto-create daily log templates |
| Templates | Insert skill/template stubs quickly |
| Graph View | See connections between vault items |
| Tag Wrangler | Organize skills and vault categories |
