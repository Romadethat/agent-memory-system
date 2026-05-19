# Windows Setup Guide

This guide covers Windows-specific setup for the Agent Memory System.

## Path Recommendations

Use `D:\` drive for your agent brain to keep data off your system drive.

```cmd
python scripts\init-agent-brain.py --path D:\agent-brain
```

Windows paths can use either forward slashes or backslashes:

```cmd
python scripts/init-agent-brain.py --path D:/agent-brain
```

## Script Path Handling

Both scripts in this repo handle Windows paths correctly:

- `Path.expanduser()` maps `~` to your user directory
- Forward slashes work in most contexts
- Backslashes need escaping in strings (`\\` or raw strings `r"path"`)

## Agent Brain Location

Recommended locations:

| Use Case | Path |
|----------|------|
| Personal (recommended) | `D:\agent-brain` |
| Shared system | `D:\Projects\agent-brain` |
| Testing | `C:\Users\You\agent-brain` |
| Per-project | `D:\Projects\my-app\agent-brain` |

## Environment Variables

Set `AGENT_BRAIN` in your shell profile so the end-of-session script can find your brain automatically:

```powershell
# PowerShell $PROFILE
$env:AGENT_BRAIN = "D:\agent-brain"
```

```cmd
# Command Prompt
setx AGENT_BRAIN D:\agent-brain
```

## Obsidian on Windows

If you use Obsidian on Windows:

1. Create your agent brain with `init-agent-brain.py --path D:\agent-brain`
2. Open Obsidian → Manage Vaults → Open folder as vault
3. Select `D:\agent-brain`

The vault/ folder inside your agent brain works as nested knowledge — Obsidian will index the full tree.

## Known Issues

- Paths with spaces need quotes: `--path "D:/My Agent Brain"`
- MSYS2/Git Bash uses `/c/` prefix — use absolute Windows paths for scripts
