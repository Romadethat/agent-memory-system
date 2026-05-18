# Master AI Agent Memory System Template

## Purpose

This system is for building an AI assistant or local agent that can remember, resume work, follow repeatable workflows, and improve over time without stuffing everything into short-term memory.

The core principle is simple:

**Memory is for active context. Files are for permanent knowledge.**

Most AI agents forget because people try to make memory do everything. They put long procedures, project notes, personal preferences, task logs, and technical documentation into memory until the agent becomes overloaded. A better system stores long-term knowledge in files and lets the agent read what it needs when it needs it.

---

# 1. Agent Identity File

## File Name

```md
AGENT_PROFILE.md
```

or

```md
SOUL.md
```

## Purpose

This file defines who the agent is before it starts working.

It should include:

```md
# Agent Profile

## Agent Name
[Add assistant/agent name here]

## Role
[What is this agent supposed to be? Example: coding assistant, design assistant, business assistant, project manager, research agent, creative partner]

## Voice and Tone
[How should the agent speak? Example: direct, friendly, formal, casual, detailed, concise, motivational, technical]

## Core Values
- [Value 1]
- [Value 2]
- [Value 3]

## Boundaries
- [What the agent should not do]
- [When the agent should ask before acting]
- [What risky actions require approval]

## Default Behavior
- Check the project state before starting work.
- Search the knowledge vault before guessing.
- Use skills for repeatable tasks.
- Log important changes after completing major work.
- Verify before making risky changes.
```

This is the personality layer. It gives the agent a consistent identity and decision-making style.

---

# 2. Persistent Memory Rules

## File Name

```md
MEMORY_RULES.md
```

## Purpose

This file explains what belongs in memory and what belongs in files.

```md
# Memory Rules

## What Goes in Memory

Memory should only store compact, high-value facts that the agent needs often.

Examples:
- User’s preferred communication style
- Important long-term preferences
- Current active project name
- Important environment facts
- Critical rules that apply across all sessions

## What Does NOT Go in Memory

Do not store long content in memory.

Avoid storing:
- Full project plans
- Long code explanations
- Daily logs
- Large documentation
- Full task history
- Long procedures
- Repeated troubleshooting steps

These should be saved as files instead.

## Core Rule

Memory is for active context.
Files are for permanent knowledge.
```

This keeps the assistant lean instead of overloading its context. Increasing memory size can help temporarily, but architecture is the real fix.

---

# 3. Project State File

## File Name

```md
project-state.md
```

## Purpose

This is the agent’s current working memory on disk. The agent should read this at the start of every session.

```md
# Current Project State

## Active Project
[Project name]

## Current Priority
[The most important task right now]

## Current Status
[Brief summary of where things stand]

## Current Blockers
- [Blocker 1]
- [Blocker 2]

## Next Safe Task
[The next action the agent can safely take]

## Waiting On
- [Person, tool, file, decision, approval, test result, etc.]

## Last Completed Task
[Most recent completed task]

## Last Updated
YYYY-MM-DD
```

## Rule

Whenever the active project changes, a blocker clears, or a task is completed, update this file.

This prevents the agent from waking up in a new session confused about what is happening. The project-state file acts as the single source of truth for current work.

---

# 4. User Preference File

## File Name

```md
user-rules.md
```

## Purpose

This file stores the user’s personal working preferences without overloading memory.

```md
# User Rules

## User Name
[Add user name here]

## Preferred Communication Style
- [Example: direct and simple]
- [Example: detailed explanations]
- [Example: no filler]
- [Example: explain before acting]

## Design Preferences
- [Add design style preferences]
- [Add color preferences]
- [Add layout preferences]

## Coding Preferences
- [Add framework preferences]
- [Add formatting rules]
- [Add testing expectations]

## Business Preferences
- [Add brand voice]
- [Add customer handling style]
- [Add sales or marketing rules]

## Do Not Do
- [Things the agent should avoid]

## Always Do
- [Things the agent should always remember]
```

This replaces the need for the agent to “learn the user” through scattered conversations. It simply reads the file.

---

# 5. Skills Folder

## Folder Name

```txt
skills/
```

## Purpose

A skill is a repeatable procedure saved as a file.

Instead of the agent memorizing workflows, it loads the correct skill only when needed. This keeps memory clean and makes workflows reusable.

## Example Folder

```txt
skills/
  code-review-checklist.md
  design-review-checklist.md
  daily-summary.md
  project-handoff.md
  bug-debugging-flow.md
  content-writing-style.md
  deployment-checklist.md
  research-process.md
```

## Example Skill File

```md
# Skill: Code Review Checklist

## When to Use
Use this skill when reviewing code changes, pull requests, patches, or bug fixes.

## Steps

1. Identify what changed.
2. Check for syntax errors.
3. Check for logic errors.
4. Check edge cases.
5. Check performance risks.
6. Check security risks.
7. Confirm the change matches the user’s request.
8. Summarize findings clearly.

## Output Format

### Summary
[Brief overview]

### Issues Found
- [Issue 1]
- [Issue 2]

### Recommended Fixes
- [Fix 1]
- [Fix 2]

### Safe to Proceed?
Yes / No / Needs Review
```

## Rule

If the user repeats a task more than twice, turn it into a skill.

---

# 6. Knowledge Vault

## Folder Name

```txt
vault/
```

## Purpose

The vault stores long-term knowledge.

This can include:

```txt
vault/
  projects/
  docs/
  references/
  decisions/
  concepts/
  research/
  templates/
  examples/
```

## Example Structure

```txt
vault/
  projects/
    project-a/
      overview.md
      architecture.md
      decisions.md
      bugs.md

  references/
    api-notes.md
    framework-docs.md
    tool-setup.md

  concepts/
    memory-architecture.md
    agent-routing.md
    verification-gates.md

  templates/
    email-template.md
    task-brief-template.md
    project-plan-template.md
```

## Rule

Before researching from scratch, the agent should search the vault first.

This lets the agent reuse knowledge learned in previous sessions instead of depending only on chat memory.

---

# 7. Daily Logs

## Folder Name

```txt
logs/daily/
```

## Purpose

Daily logs preserve what happened during each session.

```txt
logs/
  daily/
    2026-05-18.md
    2026-05-19.md
```

## Daily Log Template

```md
# Daily Summary - YYYY-MM-DD

## Completed
- [Completed task 1]
- [Completed task 2]

## Decisions Made
- [Decision 1]
- [Decision 2]

## Problems Found
- [Problem 1]
- [Problem 2]

## Fixes Applied
- [Fix 1]
- [Fix 2]

## Blockers
- [Blocker 1]
- [Blocker 2]

## Next Actions
- [Next action 1]
- [Next action 2]

## Notes for Next Session
[Anything the agent should know when work resumes]
```

## Rule

At the end of every major session, write or update the daily log.

The next session can read the log instead of relying on memory.

---

# 8. Bridge Folders for Multi-Agent Teams

## Folder Name

```txt
bridge/
```

## Purpose

Bridge folders let multiple agents work together without relying on one long messy chat thread.

```txt
bridge/
  inbox/
  outbound/
  done/
  blocked/
  logs/
  shared/
```

## Folder Meanings

```txt
bridge/inbox/      Incoming tasks
bridge/outbound/   Completed responses or handoffs
bridge/done/       Finished task records
bridge/blocked/    Tasks that cannot continue
bridge/logs/       Communication history
bridge/shared/     Shared context, state, or reference files
```

This model works because every handoff becomes a file. Agents do not need to talk over one another or remember chat history.

---

# 9. Task Brief Template

## File Name Format

```txt
TASK-[priority]-[type]-[short-name].md
```

Example:

```txt
TASK-P1-FIX-login-error.md
TASK-P2-BUILD-dashboard-layout.md
TASK-P3-RESEARCH-payment-options.md
```

## Template

```md
# Task Brief

## Task ID
[Unique task ID]

## Priority
P1 / P2 / P3

## Target Agent
[Agent name or role]

## Task Type
Build / Fix / Research / Review / Design / Write / Verify

## Goal
[What needs to be done]

## Context
[Important background information]

## Requirements
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

## Files Involved
- [File path 1]
- [File path 2]

## Constraints
- [Constraint 1]
- [Constraint 2]

## Verification Gate
The task is not complete until:
- [Condition 1]
- [Condition 2]
- [Condition 3]

## Expected Output
[What the agent should produce]

## Status
Pending / In Progress / Blocked / Done

## Notes
[Any extra notes]
```

---

# 10. Verification Gates

## Purpose

Verification gates are hard stops that prevent the agent from moving forward before the system is ready.

```md
# Verification Gate Template

## Gate Name
[Name of gate]

## Applies To
[Project, task, feature, workflow]

## Required Before Proceeding
- [Condition 1]
- [Condition 2]
- [Condition 3]

## How to Verify
- [Test 1]
- [Test 2]
- [Review step]

## If Gate Fails
Move task to:

bridge/blocked/

Then write a blocked report explaining:
- What failed
- Why it matters
- What is needed next
```

## Example

```md
# Verification Gate: Deployment Safety

## Required Before Proceeding
- Build passes
- Tests pass
- No unresolved critical errors
- Rollback plan exists

## If Gate Fails
Do not deploy.
Move task to bridge/blocked/.
Write a blocked report.
```

Verification gates are one of the most important parts of the system because they stop agents from assuming prerequisites are complete when they are not.

---

# 11. Thinking Protocol

## File Name

```md
thinking-protocol.md
```

## Purpose

This gives the agent a repeatable reasoning flow.

```md
# Thinking Protocol

## 1. Orient
Understand what the user actually wants.

Ask:
- What is the real goal?
- What domain is this?
- Is this simple or complex?
- What would a successful result look like?

## 2. Recall
Check available context.

Look at:
- Memory
- project-state.md
- user-rules.md
- relevant skills
- vault files
- recent daily logs

## 3. Plan
Decide the safest path.

Ask:
- What steps are needed?
- What tools are required?
- What could break?
- Is approval needed?

## 4. Execute
Do the task.

## 5. Verify
Check the work.

Ask:
- Did it meet the request?
- Are there errors?
- Are there edge cases?
- Is anything unsafe?

## 6. Reflect
Save important learning.

Update:
- project-state.md
- daily log
- skill files
- vault notes
- memory only if needed
```

---

# 12. Imagination / Simulation Layer

## File Name

```md
simulation-protocol.md
```

## Purpose

This teaches the agent to think ahead before acting.

```md
# Simulation Protocol

Before making major changes, the agent should simulate possible outcomes.

## Ask

- What happens if this works?
- What happens if this breaks?
- What user action could expose a hidden bug?
- What edge case is most likely?
- What dependency could fail?
- What assumption am I making?
- What should exist that does not exist yet?

## Use This For

- Code changes
- System architecture
- Multi-agent workflows
- Business processes
- Automation
- File operations
- Deployment
- Anything risky or complex
```

The simulation layer is not just creativity. It is the ability to think ahead, spot hidden problems, and combine known patterns into better solutions.

---

# 13. End-of-Session Routine

## File Name

```md
end-session-checklist.md
```

## Purpose

This is the save button for the whole system.

```md
# End of Session Checklist

## 1. Review Work Completed
- What changed?
- What was built?
- What was fixed?

## 2. Update project-state.md
- Current priority
- Current blockers
- Next safe task
- Last completed task

## 3. Write Daily Log
Save summary to:

logs/daily/YYYY-MM-DD.md

## 4. Update Skills
If a repeatable process was discovered, create or update a skill file.

## 5. Update Vault
If new long-term knowledge was created, save it to the vault.

## 6. Update Memory Only If Needed
Only save compact, long-term facts that the agent needs often.

## 7. Prepare Next Session
Write clear next steps.
```

---

# 14. Recommended Folder Structure

```txt
agent-system/
  AGENT_PROFILE.md
  MEMORY_RULES.md
  project-state.md
  user-rules.md
  thinking-protocol.md
  simulation-protocol.md
  end-session-checklist.md

  skills/
    code-review-checklist.md
    daily-summary.md
    project-handoff.md
    bug-debugging-flow.md

  vault/
    projects/
    references/
    concepts/
    templates/
    decisions/

  bridge/
    inbox/
    outbound/
    done/
    blocked/
    logs/
    shared/

  logs/
    daily/
```

---

# 15. Startup Prompt for the Agent

Copy and paste this into the agent’s system, startup instructions, or first message.

```md
You are an AI agent operating inside a file-based memory system.

Your rules:

1. Read AGENT_PROFILE.md to understand your identity and role.
2. Read MEMORY_RULES.md to understand what belongs in memory versus files.
3. Read project-state.md at the start of each session.
4. Read user-rules.md before making style, design, writing, or workflow decisions.
5. Search the vault before assuming something is unknown.
6. Use skills from the skills/ folder for repeatable procedures.
7. Use bridge/ folders for multi-agent task handoffs.
8. Use verification gates before risky work.
9. Use the thinking protocol: Orient, Recall, Plan, Execute, Verify, Reflect.
10. At the end of major work, update project-state.md and write a daily log.
11. Only save compact, long-term facts to memory.
12. Save long-term procedures, project details, decisions, and logs as files.
```

---

# 16. Public Explanation Version

Use this if sharing the concept with other people:

```md
This system helps an AI assistant remember better by separating memory from permanent knowledge.

Instead of trying to cram everything into memory, the agent uses a file-based structure:

- project-state.md tracks what is happening right now.
- user-rules.md stores the user’s preferences.
- skills/ stores repeatable procedures.
- vault/ stores long-term knowledge.
- logs/ stores daily session history.
- bridge/ allows multiple agents to pass tasks through files.
- verification gates prevent risky work from happening too early.

The main principle is:

Memory is for active context.
Files are for permanent knowledge.

This makes the agent easier to resume, harder to confuse, and safer to scale.
```

---

# 17. Fill-In-The-Blank Setup Sheet

```md
# My AI Agent Setup

## Agent Name
[Add name]

## Main Purpose
[What do you want this agent to help with?]

## User Name
[Add your name]

## Preferred Communication Style
[How should the agent talk to you?]

## Main Projects
- [Project 1]
- [Project 2]
- [Project 3]

## Tools Available
- [Tool 1]
- [Tool 2]
- [Tool 3]

## Important Rules
- [Rule 1]
- [Rule 2]
- [Rule 3]

## Things the Agent Should Never Do
- [Boundary 1]
- [Boundary 2]

## Things the Agent Should Always Do
- [Expectation 1]
- [Expectation 2]

## Folder Location
[Where this system lives on your computer]

## Daily Log Location
logs/daily/

## Skill Location
skills/

## Vault Location
vault/

## Bridge Location
bridge/
```

---

# 18. Master Summary

The clean version is:

```txt
AGENT_PROFILE.md = who the agent is
MEMORY_RULES.md = what memory is allowed to hold
project-state.md = what is happening right now
user-rules.md = how the user likes things done
skills/ = repeatable procedures
vault/ = long-term knowledge
logs/ = session history
bridge/ = multi-agent handoffs
verification gates = safety stops
thinking-protocol.md = how the agent reasons
simulation-protocol.md = how the agent thinks ahead
end-session-checklist.md = how the system saves progress
```

That gives people the same architecture without copying anyone's personal setup.

---

# 19. Briefcase — Encrypted Secrets Vault

## Folder Name

```txt
briefcase/
```

## Purpose

An encrypted folder for sensitive information that should not be in plaintext — API keys, personal data, credentials, business strategies.

## How It Works

```txt
briefcase/
  .briefcase_key    # Generated once, do not share
  .access_log       # Every read/write timestamped
  entries.json      # Encrypted secrets (AES + HMAC)
```

## Commands

```bash
python scripts/briefcase.py init                # Create + generate key
python scripts/briefcase.py add "entry-name"    # Add a secret
python scripts/briefcase.py read "entry-name"   # Decrypt and read
python scripts/briefcase.py list                # List names only
python scripts/briefcase.py log                 # Show access history
python scripts/briefcase.py remove "entry-name" # Delete entry
python scripts/briefcase.py change-key          # Rotate encryption key
```

## Rule

The agent should auto-scan for new API keys and tokens at the end of each session, then store them in the briefcase automatically. Every access is logged.

---

# 20. Spitball — Idea Catcher

## Folder Name

```txt
ideas/
```

## Purpose

A safety net for random thoughts. When the user says something interesting ("what if we built X"), the agent logs it immediately before it gets forgotten.

## How It Works

```txt
ideas/
  20260518_123045_build_a_media_player.md
  20260518_140200_encrypted_briefcase_concept.md
```

Each idea gets a timestamped file with the full thought. No idea is too small.

## Rule

If the user says "imagine," "what if," "random thought," or "idea," log it immediately.

---

# 21. Reference Library (The Mirror)

## Folder Name

```txt
reference/
  screenshots/
  concepts/
  designs/
```

## Purpose

When the agent encounters something interesting (a UI design, an error message, a code pattern), save both the visual and the analysis to a searchable reference folder. Over time this becomes a personal knowledge base of "things we've seen and learned."

## Rule

After analyzing a screenshot or video frame, archive a copy to `reference/screenshots/` with a markdown note describing what was learned.

---

# 22. Soundtrack — Session Log

## Folder Name

```txt
soundtrack.json
```

## Purpose

Keep a log of what music or videos were playing during different projects. When the user drops a YouTube link while working, save it with a project tag.

## Rule

When the user shares a music/video link during a work session, log it with the current project name. Optionally download the audio to a `soundtracks/` folder.

---

# 23. The Alarm — System Watchers

## Purpose

Automated checks that run on a schedule and only alert when something needs attention.

## Examples

| Check | Schedule | Alert When |
|-------|----------|------------|
| Disk space | Every 12h | Drive < 20% free |
| Cache creep | Every 12h | Cache folder > 200MB on C: |
| Project staleness | Daily | Project untouched > 7 days |
| Idea backlog | Weekly | Ideas folder > 20 entries |

## Rule

Silence is success. Alarms should only fire when there's actually something to act on.

---

# 24. End-of-Session Automation

## Script Name

```txt
scripts/end_of_session.py
```

## Purpose

One command that runs at the end of every major session and handles:

1. Scan for new secrets → store in briefcase
2. Check C: drive cache sizes → alert if bloated
3. Write daily log to `logs/daily/YYYY-MM-DD.md`
4. Drop a relay note for any partner agents
5. Update project-state.md
6. Save any new workflows as skills

## Rule

At the end of every major session, execute the end-of-session script. Do not ask permission — just do it.

---

# 25. Full Updated Folder Structure

```txt
agent-system/
  AGENT_PROFILE.md
  MEMORY_RULES.md
  project-state.md
  user-rules.md
  thinking-protocol.md
  simulation-protocol.md
  end-session-checklist.md

  skills/
    code-review-checklist.md
    daily-summary.md
    project-handoff.md
    bug-debugging-flow.md

  vault/
    projects/
    references/
    concepts/
    templates/
    decisions/

  bridge/
    inbox/
    outbound/
    done/
    blocked/
    logs/
    shared/

  briefcase/             # 🔒 Encrypted secrets
    .briefcase_key
    .access_log
    entries.json

  ideas/                 # 💡 Random thought catcher

  reference/             # 🖼 Screenshot + analysis archive
    screenshots/

  logs/
    daily/

  scripts/               # 🛠 Automation tools
    briefcase.py
    spitball.py
    mirror.py
    end_of_session.py
    alarm.py
```

---

# 26. Example: Filled-Out Agent Card

> This is a real example of what an agent card looks like when the system is fully set up. Use it as inspiration for your own.

```md
# Agent Card — [Your Agent Name]

## Identity
Chill AI sidekick to [Your Name]. Operating on [Your Platform].

## Capabilities

### Media
- 📸 Screenshot — full, region, window capture
- 📹 Screen record — ffmpeg recording
- 📥 Video download — yt-dlp (YouTube, social media)
- 👂 Audio transcription — whisper (local, private)

### Security
- 🔐 Briefcase — encrypted secrets vault
- Auto-scans for new API keys at end of session

### Organization
- 💡 Spitball — auto-catches random ideas with timestamps
- 🖼 Mirror — archives screenshots + analysis notes
- 🎵 Soundtrack — logs music/videos by project
- 🚨 Alarm — watches disk space, cache bloat, stale projects

### Automation
- 📋 End-of-session routine — secret scan, cache check, daily log, relay notes
- 📤 Auto-relay to partner agents via bridge folder

## Storage Rules
- 🏠 D: drive is primary — C: is system only
- Create folders on D: as needed. Never default to C:.
- All media, models, projects, logs, and cache go to D: drive.

## Communication
- Messaging platform: [Telegram/Discord/WhatsApp/etc.]
- LLM provider: [Your provider]
- Gateway runs as background service

---

*Last updated: YYYY-MM-DD*
```

---

# 27. Building the Brain — Setup Guide

> This section tells you how to actually build the memory system on your machine, whether you use Obsidian or not.

## For Obsidian Users (Recommended)

Obsidian gives you a visual graph, search, backlinks, and markdown editing for free.

### Step 1: Create the Vault Folder

```bash
mkdir -p ~/agent-brain
mkdir -p ~/agent-brain/vault/projects
mkdir -p ~/agent-brain/vault/references
mkdir -p ~/agent-brain/vault/concepts
mkdir -p ~/agent-brain/vault/templates
mkdir -p ~/agent-brain/vault/decisions
mkdir -p ~/agent-brain/skills
mkdir -p ~/agent-brain/bridge/inbox
mkdir -p ~/agent-brain/bridge/outbound
mkdir -p ~/agent-brain/bridge/done
mkdir -p ~/agent-brain/bridge/blocked
mkdir -p ~/agent-brain/bridge/shared
mkdir -p ~/agent-brain/bridge/logs
mkdir -p ~/agent-brain/logs/daily
mkdir -p ~/agent-brain/ideas
mkdir -p ~/agent-brain/reference/screenshots
```

### Step 2: Open in Obsidian

1. Open Obsidian → "Open folder as vault" → select `~/agent-brain`
2. Enable "Graph view" for visual connections
3. Use `[[Wiki Links]]` to connect related pages
4. Tag system: `#project`, `#client`, `#concept`, `#reference`

### Step 3: Drop in the Core Files

Place the template files from this document into your vault:
- `AGENT_PROFILE.md` — who your agent is
- `MEMORY_RULES.md` — what memory can hold
- `project-state.md` — current status
- `user-rules.md` — your preferences
- `thinking-protocol.md` — how your agent reasons

### Step 4: Connect Your AI Agent

Tell your AI agent to start each session by reading `project-state.md` and searching the vault before answering. The startup prompt in Section 15 is your starting point.

---

## For Non-Obsidian Users (Plain Files)

No Obsidian? No problem. Everything works with plain markdown files and a file explorer.

### Step 1: Create the Folder Structure

Same folders as above — just create them with your file manager or terminal:

```bash
mkdir -p ~/agent-brain/{vault/{projects,references,concepts,templates,decisions},skills,bridge/{inbox,outbound,done,blocked,shared,logs},logs/daily,ideas,reference/screenshots}
```

### Step 2: Use a Markdown Editor

Any of these work:
- **VS Code** — free, has markdown preview + search
- **Typora** — clean, minimal markdown editor
- **Notepad++** — lightweight, works on any Windows machine
- **GitHub** — host your brain as a repo, edit in browser

### Step 3: Search Without Obsidian

If you don't have graph view or backlinks, use search instead:

- **VS Code:** `Ctrl+Shift+F` to search all files
- **Terminal:** `grep -r "keyword" ~/agent-brain/`
- **GitHub:** built-in search across your repo

### Step 4: Link Pages Without Wiki Links

Instead of `[[Page Name]]`, use:
- File paths: `see [projects/project-name.md](vault/projects/project-name.md)`
- Tags in filenames: `project-name_concept_reference.md`
- A central index file that lists everything

### Step 5: Automate With Scripts

Create simple scripts to help your agent:

```bash
# search.sh — search the brain
grep -r "$1" ~/agent-brain/ --include="*.md"

# log.sh — write a daily log entry
echo "## $(date +%Y-%m-%d)" >> ~/agent-brain/logs/daily/$(date +%Y-%m-%d).md
echo "$*" >> ~/agent-brain/logs/daily/$(date +%Y-%m-%d).md

# status.sh — read current project state
cat ~/agent-brain/project-state.md
```

---

## The Most Important Rule

Start small. Don't build all 27 sections at once.

Begin with:
1. `AGENT_PROFILE.md` — who your agent is (2 paragraphs)
2. `project-state.md` — what you're working on right now (5 lines)
3. One skill file — one repeatable task you do often

Add more as you use it. The system grows with you — it doesn't need to be perfect on day one.

**Memory is for active context. Files are for permanent knowledge.**
