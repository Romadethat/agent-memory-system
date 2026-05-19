#!/usr/bin/env python3
"""
end_of_session.py — Run at end of every session to close things cleanly.

Usage:
  python end_of_session.py "What I did this session"
"""

import os, sys, datetime
from pathlib import Path

def run():
    summary = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "(no summary provided)"
    base = Path(os.environ.get("AGENT_BRAIN", "~/agent-brain")).expanduser()
    
    ts = datetime.datetime.now()
    date_str = ts.strftime("%Y-%m-%d")
    time_str = ts.strftime("%H:%M")
    
    # Write daily log
    log_dir = base / "logs" / "daily"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{date_str}.md"
    
    entry = f"\n## {time_str} — Session End\n\n{summary}\n"
    with open(log_path, "a") as f:
        f.write(entry)
    
    print(f"✅ Log written: {log_path}")
    
    # Update project-state.md
    state_path = base / "project-state.md"
    if state_path.exists():
        content = state_path.read_text()
        marker = "*Last updated:"
        if marker in content:
            lines = content.splitlines()
            new_lines = []
            for line in lines:
                if line.startswith(marker):
                    new_lines.append(f"*Last updated: {date_str}*")
                else:
                    new_lines.append(line)
            state_path.write_text("\n".join(new_lines))
    else:
        state_path.write_text(f"# project-state.md\n\n*Last updated: {date_str}*\n\n## Notes\n\nSession: {summary}\n")
    
    print(f"✅ Project state updated: {state_path}")
    print(f"✅ Session complete — {ts.strftime('%Y-%m-%d %H:%M')}")

if __name__ == "__main__":
    run()
