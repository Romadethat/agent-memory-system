#!/usr/bin/env python3
"""
init-agent-brain.py — One-command installer for the Agent Memory System.

Usage:
  python init-agent-brain.py                        # Interactive setup
  python init-agent-brain.py --path ~/agent-brain   # Custom path
  python init-agent-brain.py --path D:/agent-brain  # Windows D: drive
"""

import os, sys, shutil, datetime
from pathlib import Path

def green(msg):
    print(f"\033[92m{msg}\033[0m")

def yellow(msg):
    print(f"\033[93m{msg}\033[0m")

def setup(path_str: str):
    base = Path(path_str).expanduser().resolve()
    
    print(f"\n🧠 Initializing Agent Memory System")
    print(f"   Target: {base}")
    print()
    
    if base.exists():
        resp = input(f"  ⚠ {base} already exists. Overwrite? [y/N]: ")
        if resp.lower() != "y":
            print("  Aborted.")
            return
        shutil.rmtree(base)
    
    # Create directory structure
    dirs = [
        "vault",
        "skills",
        "logs/daily",
        "bridge/inbox",
        "bridge/outbound",
        "bridge/done",
        "bridge/blocked",
        "bridge/logs",
        "bridge/shared",
        "scripts",
        "prompts",
        "templates",
    ]
    
    for d in dirs:
        (base / d).mkdir(parents=True, exist_ok=True)
    
    # Create core files
    files = {
        "AGENT_PROFILE.md": f"# AGENT_PROFILE.md\n\n*Created: {datetime.date.today()}*\n\n## Agent Identity\n\n```yaml\nname: \"your-agent\"\ncreator: \"your-name\"\n```\n",
        "project-state.md": f"# project-state.md\n\n*Last updated: {datetime.date.today()}*\n\n## Current Focus\n\nNothing yet.\n",
    }
    
    for name, content in files.items():
        (base / name).write_text(content)
    
    # Create .gitkeep files in empty dirs
    for d in ["bridge/done", "bridge/blocked", "bridge/logs", "bridge/shared"]:
        (base / d / ".gitkeep").write_text("")
    
    green(f"\n✅ Agent brain initialized at: {base}")
    print()
    print(f"  📁 {base}/")
    print(f"  ├── AGENT_PROFILE.md    # Your identity card")
    print(f"  ├── project-state.md    # Current work state")
    print(f"  ├── vault/              # Long-term knowledge")
    print(f"  ├── skills/             # Reusable workflows")
    print(f"  ├── logs/daily/         # Session history")
    print(f"  ├── bridge/             # Multi-agent handoffs")
    print(f"  ├── scripts/            # Automation tools")
    print(f"  ├── prompts/            # Reusable prompts")
    print(f"  └── templates/          # File templates")
    print()
    print(f"  Next steps:")
    print(f"  1. Edit AGENT_PROFILE.md with your info")
    print(f"  2. Tell your agent: 'Read {base}/AGENT_PROFILE.md and {base}/project-state.md'")
    print(f"  3. Start working — the system logs automatically")
    
    return base

if __name__ == "__main__":
    path = "~/agent-brain"
    
    if "--path" in sys.argv:
        idx = sys.argv.index("--path")
        if idx + 1 < len(sys.argv):
            path = sys.argv[idx + 1]
    
    setup(path)
