# user-rules.md — Example

## Communication

- Be direct — no filler or disclaimers
- Summarize decisions before diving into details
- When explaining code, show the diff first

## Coding Preferences

- Python backend with FastAPI
- React frontend with TypeScript
- Prefer functional patterns over class-based where reasonable
- Tests go in `tests/` mirroring the source structure
- Use type hints everywhere in Python

## Workflow

- Read project-state.md at session start
- Update logs at session end
- Branch off `main` for features, fix directly for bugs
- Squash commits before merge

## Do Not Do

- Do not deploy without confirmation
- Do not commit to `main` directly
- Do not use `pip install --user` without --no-deps
- Do not store secrets in source files

## Always Do

- Ask before deleting files or directories
- Check edge cases (empty state, error state, loading state)
- Run tests before calling a task done
- Log decisions to daily log
