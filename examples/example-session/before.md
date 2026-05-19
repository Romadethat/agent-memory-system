# Session Before Example

## Context

The agent hasn't loaded session context yet. It knows nothing about what was happening before.

```
Agent starts fresh...
Memory is empty.

What project was I working on?       → Unknown
What was the last priority?          → Unknown
What files matter?                   → Unknown
What happened last session?          → Unknown

Agent has to ask the user or guess.
```

## Solution

With the agent memory system, the agent reads:

1. project-state.md → Knows active project, priority, blockers
2. AGENT_PROFILE.md → Knows identity and role
3. user-rules.md → Knows preferences
4. logs/daily/2026-05-17.md → Knows what happened yesterday

Agent starts productive instantly.
