#!/usr/bin/env python3
"""
init-agent-brain.py — One-command installer for the Agent Memory System.

Creates a complete agent brain directory with vault, skills, logs, bridge,
scripts, prompts, and templates folders plus starter files.

Usage:
  python init-agent-brain.py                        Interactive setup (~/agent-brain)
  python init-agent-brain.py --path ~/agent-brain   Custom path (Unix/Mac)
  python init-agent-brain.py --path D:/agent-brain  Custom path (Windows)
  python init-agent-brain.py --help                 Show this help text

The script:
  - Creates the full directory structure
  - Writes starter AGENT_PROFILE.md and project-state.md
  - Creates .gitkeep files in empty bridge subdirectories
  - Prints a summary of what was created
  - Warns before overwriting an existing directory

Works on Windows, macOS, and Linux.
Uses only Python stdlib — no dependencies required.
"""

import os
import sys
import shutil
import datetime
from pathlib import Path


def print_help():
    """Print detailed help text and exit."""
    print(__doc__)
    sys.exit(0)


def green(msg):
    print(f"\033[92m{msg}\033[0m")


def yellow(msg):
    print(f"\033[93m{msg}\033[0m")


def red(msg):
    print(f"\033[91m{msg}\033[0m")


def confirm_overwrite(path: Path) -> bool:
    """Ask user before overwriting an existing directory."""
    print(f"\n  Warning: {path} already exists.")
    resp = input("  Overwrite? This will delete the existing directory. [y/N]: ").strip().lower()
    return resp == "y"


def create_structure(base: Path):
    """Create the full agent brain directory structure."""
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
    return dirs


def write_core_files(base: Path):
    """Write starter files into the new agent brain."""
    today = datetime.date.today().isoformat()

    files = {
        "AGENT_PROFILE.md": (
            f"# AGENT_PROFILE.md\n\n"
            f"*Created: {today}*\n\n"
            f"## Agent Identity\n\n"
            f"```yaml\n"
            f"name: \"your-agent\"\n"
            f"creator: \"your-name\"\n"
            f"version: \"1.0.0\"\n"
            f"```\n\n"
            f"## Role\n\n"
            f"[What does this agent do?]\n\n"
            f"## Voice and Tone\n\n"
            f"[How should the agent communicate?]\n\n"
            f"## Core Values\n\n"
            f"- [Value 1]\n"
            f"- [Value 2]\n"
            f"- [Value 3]\n\n"
            f"## Boundaries\n\n"
            f"- [What the agent should not do]\n"
            f"- [When to ask before acting]\n"
        ),
        "MEMORY_RULES.md": (
            f"# MEMORY_RULES.md\n\n"
            f"*Created: {today}*\n\n"
            f"## Core Rule\n\n"
            f"**Memory is for active context. Files are for permanent knowledge.**\n\n"
            f"## What Goes in Memory\n\n"
            f"- User communication preferences\n"
            f"- Critical Do Not Do rules\n"
            f"- Current active project\n"
            f"- Environment facts\n\n"
            f"## What Goes in Files\n\n"
            f"- Project plans → vault/projects/\n"
            f"- Daily logs → logs/daily/\n"
            f"- Skills and workflows → skills/\n"
            f"- Reference docs → vault/references/\n"
        ),
        "project-state.md": (
            f"# project-state.md\n\n"
            f"*Last updated: {today}*\n\n"
            f"## Active Project\n\n"
            f"[Project name]\n\n"
            f"## Current Priority\n\n"
            f"[What to work on next]\n\n"
            f"## Current Status\n\n"
            f"[Where things stand]\n\n"
            f"## Current Blockers\n\n"
            f"- [Blocker 1]\n\n"
            f"## Next Safe Task\n\n"
            f"[The next action to take]\n\n"
            f"## Last Completed Task\n\n"
            f"[Previous task]\n"
        ),
        "user-rules.md": (
            f"# user-rules.md\n\n"
            f"*Created: {today}*\n\n"
            f"## Communication\n\n"
            f"- [How you want to be spoken to]\n\n"
            f"## Preferences\n\n"
            f"- [Workflow preferences]\n"
            f"- [Tool preferences]\n\n"
            f"## Do Not Do\n\n"
            f"- [Things the agent should avoid]\n\n"
            f"## Always Do\n\n"
            f"- [Things the agent should always do]\n"
        ),
    }

    written = []
    for name, content in files.items():
        (base / name).write_text(content, encoding="utf-8")
        written.append(name)

    return written


def write_gitkeep_files(base: Path):
    """Create .gitkeep files in empty directories to preserve folder structure."""
    empty_dirs = [
        "bridge/done",
        "bridge/blocked",
        "bridge/logs",
        "bridge/shared",
        "prompts",
    ]
    for d in empty_dirs:
        path = base / d / ".gitkeep"
        if not path.exists():
            path.write_text("")


def print_summary(base: Path):
    """Print a clean summary of what was created."""
    print()
    green(f"Agent brain initialized at: {base}")
    print()
    print(f"  {base}/")
    print(f"  ├── AGENT_PROFILE.md    # Who the agent is")
    print(f"  ├── MEMORY_RULES.md     # Memory vs files rules")
    print(f"  ├── project-state.md    # Current work state")
    print(f"  ├── user-rules.md       # Your preferences")
    print(f"  ├── vault/              # Long-term knowledge")
    print(f"  ├── skills/             # Reusable workflows")
    print(f"  ├── logs/daily/         # Session history")
    print(f"  ├── bridge/             # Multi-agent handoffs")
    print(f"  ├── scripts/            # Automation tools")
    print(f"  ├── prompts/            # Reusable prompts")
    print(f"  └── templates/          # File templates")
    print()
    print("  Next steps:")
    print(f"  1. Edit AGENT_PROFILE.md with your agent info")
    print(f"  2. Edit user-rules.md with your preferences")
    print(f"  3. Tell your agent: 'Read the files in {base}/'")
    print(f"  4. Start working — the system logs automatically")


def setup(path_str: str):
    """Main setup routine."""
    base = Path(path_str).expanduser().resolve()

    print(f"\nAgent Memory System — Init")
    print(f"  Target: {base}")
    print()

    # Check for overwrite
    if base.exists():
        if not confirm_overwrite(base):
            print("  Aborted.")
            sys.exit(0)
        try:
            shutil.rmtree(base)
        except PermissionError:
            red(f"  Error: Cannot remove {base}. Permission denied.")
            sys.exit(1)
        except OSError as e:
            red(f"  Error: Cannot remove {base}. {e}")
            sys.exit(1)

    # Create structure
    try:
        create_structure(base)
        write_core_files(base)
        write_gitkeep_files(base)
    except PermissionError:
        red(f"  Error: Cannot write to {base}. Permission denied.")
        sys.exit(1)
    except OSError as e:
        red(f"  Error: Failed to create structure. {e}")
        sys.exit(1)

    print_summary(base)
    return base


def main():
    """Parse arguments and run setup."""
    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print_help()

    path = "~/agent-brain"

    if "--path" in args:
        idx = args.index("--path")
        if idx + 1 < len(args):
            path = args[idx + 1]
        else:
            red("  Error: --path requires an argument.")
            print("  Usage: python init-agent-brain.py --path /path/to/agent-brain")
            sys.exit(1)

    setup(path)


if __name__ == "__main__":
    main()
