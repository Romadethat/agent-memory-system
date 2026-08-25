#!/usr/bin/env python3
"""
end_of_session.py — Close a session cleanly with logging and state updates.

Writes a daily log entry and updates project-state.md with the current date.

Usage:
  python end_of_session.py "What I did this session"
  python end_of_session.py --help

Environment:
  AGENT_BRAIN — path to the agent brain directory (default: ~/agent-brain)

The script:
  - Appends a session summary to logs/daily/YYYY-MM-DD.md
  - Updates the Last Updated date in project-state.md
  - Creates files if they don't exist yet
  - Works on Windows, macOS, and Linux
  - Uses only Python stdlib — no dependencies
"""

import os
import sys
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


def get_agent_brain() -> Path:
    """Resolve the agent brain path from env var or default."""
    path_str = os.environ.get("AGENT_BRAIN", "~/agent-brain")
    return Path(path_str).expanduser().resolve()


def write_daily_log(base: Path, summary: str, timestamp: datetime.datetime):
    """Append a session entry to the daily log file."""
    date_str = timestamp.strftime("%Y-%m-%d")
    time_str = timestamp.strftime("%H:%M")

    log_dir = base / "logs" / "daily"
    log_dir.mkdir(parents=True, exist_ok=True)

    log_path = log_dir / f"{date_str}.md"

    entry = f"\n## {time_str} — Session End\n\n{summary}\n"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(entry)

    return log_path


def update_project_state(base: Path, date_str: str):
    """Update the Last Updated date in project-state.md."""
    state_path = base / "project-state.md"

    if state_path.exists():
        content = state_path.read_text(encoding="utf-8")
        marker = "*Last updated:"
        if marker in content:
            lines = content.splitlines()
            new_lines = []
            for line in lines:
                if line.strip().startswith(marker.strip()):
                    new_lines.append(f"*Last updated: {date_str}*")
                else:
                    new_lines.append(line)
            state_path.write_text("\n".join(new_lines), encoding="utf-8")
        else:
            # No date marker found — append one
            with open(state_path, "a", encoding="utf-8") as f:
                f.write(f"\n*Last updated: {date_str}*\n")
    else:
        # Create project-state.md if it doesn't exist
        state_path.write_text(
            f"# project-state.md\n\n"
            f"*Last updated: {date_str}*\n\n"
            f"## Notes\n\n"
            f"Session: (no summary provided)\n",
            encoding="utf-8",
        )

    return state_path


def touch_active_slot(base: Path, summary: str, timestamp: datetime.datetime):
    """v6: append the session note to the active project slot's PROJECT.md log.

    Reads projects/active-project.json; if a slot is live and its PROJECT.md
    exists, appends a dated one-liner under '## Session Log'. Best-effort:
    missing files or malformed JSON are silently skipped.
    """
    import json

    ap = base / "projects" / "active-project.json"
    try:
        data = json.loads(ap.read_text(encoding="utf-8"))
        project_md = data.get("project_md")
        if not project_md or not data.get("id"):
            return None
        project_md = Path(project_md)
        if not project_md.exists():
            return None
        time_str = timestamp.strftime("%Y-%m-%d %H:%M")
        with open(project_md, "a", encoding="utf-8") as f:
            f.write(f"\n- {time_str} — {summary}\n")
        return project_md
    except (OSError, ValueError):
        return None


def run():
    """Main session close routine."""
    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print_help()

    summary = " ".join(args) if args else "(no summary provided)"
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")

    base = get_agent_brain()

    # Verify the agent brain exists
    if not base.exists():
        yellow(f"  Note: {base} does not exist yet.")
        yellow(f"  Run init-agent-brain.py first to create it.")
        resp = input("  Create it now? [y/N]: ").strip().lower()
        if resp != "y":
            print("  Aborted.")
            sys.exit(0)
        base.mkdir(parents=True, exist_ok=True)

    # Write daily log
    try:
        log_path = write_daily_log(base, summary, now)
        green(f"  Log written: {log_path}")
    except PermissionError:
        red(f"  Error: Cannot write log to {base / 'logs'}. Permission denied.")
        sys.exit(1)
    except OSError as e:
        red(f"  Error: Failed to write log. {e}")
        sys.exit(1)

    # Update project state
    try:
        state_path = update_project_state(base, date_str)
        green(f"  State updated: {state_path}")
    except PermissionError:
        red(f"  Error: Cannot update {base / 'project-state.md'}. Permission denied.")
        sys.exit(1)
    except OSError as e:
        red(f"  Error: Failed to update project state. {e}")
        sys.exit(1)

    # v6: append session note to the active project slot (if one is live)
    slot_path = touch_active_slot(base, summary, now)
    if slot_path:
        green(f"  Slot updated: {slot_path}")

    # v6: evolution reminder — unlogged sessions are lost lessons
    evo = base / "books" / "evolution.md"
    if evo.exists():
        yellow("  Reminder: log anything new in books/evolution.md")
        yellow("  (mutations, corrections, gotchas — failures are canonical entries)")

    print(f"  Session complete — {now.strftime('%Y-%m-%d %H:%M')}")


if __name__ == "__main__":
    run()
