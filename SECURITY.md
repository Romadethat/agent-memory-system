# Security Notes — Agent Memory System

This system stores project notes, preferences, logs, and workflow data as plain-text files in a local directory. It is **not** a secure vault or credential manager.

## Do Not Commit Secrets

- Do not store API keys, passwords, tokens, or private keys in any file inside your agent brain.
- Do not commit `.env` files, `secrets/` folders, or `private/` directories to any public repository.
- The `.gitignore` in this repo excludes common secret patterns — verify before every commit.

## Recommended Practices

| Practice | Reason |
|----------|--------|
| Use a `.env` file for secrets | Keeps credentials out of tracked files |
| Add `.env` to `.gitignore` | Prevents accidental commits |
| Use a proper secret manager | For production: HashiCorp Vault, 1Password CLI, or platform-native keychains |
| Review logs before sharing | Daily logs may contain project-sensitive information |
| Isolate agent brains per project | Prevents cross-project data leaks |

## What This System Is Safe For

- Agent identity files
- Workflow procedures and skills
- Project state tracking
- Daily session logs
- Knowledge vault content (non-sensitive)
- Bridge handoff notes (non-sensitive)

## What This System Is NOT Safe For

- Plain-text passwords
- API keys without environment variable indirection
- Client credentials
- Private keys or certificates
- Personal identifying information you wouldn't want public

## Report Issues

If you discover a security concern in this project, open an issue at:

https://github.com/Romadethat/agent-memory-system/issues
