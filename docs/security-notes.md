# Security Notes — Reference Guide

## Overview

The Agent Memory System stores information in plain-text markdown files in a local directory. This makes it transparent, searchable, and easy to work with — but also means sensitive information needs special handling.

## What NOT to Store in Your Agent Brain

- API keys, tokens, or secrets
- Passwords or login credentials
- Private keys or certificates
- Client PII or confidential documents
- Session tokens or refresh tokens
- Database connection strings
- Any value you would put in a `.env` file

## Safe Alternatives for Secrets

| Secret Type | Safe Storage |
|-------------|-------------|
| API keys | Environment variables sourced from `.env` (which is gitignored) |
| Database credentials | `.env` file excluded by `.gitignore` |
| Private keys | Dedicated key management, never in agent brain |
| OAuth tokens | Short-lived, stored in memory only, refreshed per session |
| Client data | Outside the agent brain entirely |

## Recommended `.gitignore`

```gitignore
# Secrets
.env
.env.*
secrets/
private/
*.key
*.pem

# Databases (may contain user data)
*.sqlite
*.db

# Python artifacts
__pycache__/
*.pyc
*.pyo

# OS artifacts
.DS_Store
Thumbs.db
```

## Script Safety

Both scripts in this repo (`init-agent-brain.py` and `end_of_session.py`):

- Only write to the path you explicitly specify
- Warn before overwriting existing directories
- Never access environment variables named `SECRET`, `TOKEN`, `KEY`, or `PASSWORD`
- Never make network requests
- Only use Python stdlib (no external dependencies)

## Logging Safety

Daily logs may contain:

- What you worked on
- Decisions made
- Blockers encountered

They should NOT contain:

- Plain-text credentials
- Secrets or passwords
- Client PII

Review logs before sharing them outside your environment.

## Bridge Safety

Bridge handoff files are shared between agents. Treat them like internal memos:

- Include task context, not secrets
- Reference configuration values by name, not by value
- Store agent cards with capabilities, not credentials

## Audit

Run `git diff --name-only` before every commit to catch unintended file inclusions.

```bash
# Check what's about to be committed
git diff --cached --name-only

# Check for known secret patterns
git diff --cached | grep -iE "(api.?key|secret|token|password|-----BEGIN)"
```
