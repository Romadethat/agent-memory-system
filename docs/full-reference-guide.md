# Master AI Agent Memory System Template

> **Note:** This reference guide documents one specific implementation (the Zoro ecosystem). It includes personal examples, specific tool names, and project references. Adapt the patterns to your own agent — the architecture is universal, the examples are not.

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

---

# 28. Copy-Paste Starter Prompt

Paste this block into your AI agent's first message, system prompt, or startup instructions:

```md
You are now operating inside a file-based memory system.

## Rules

1. Read project-state.md at the start of each session to know what's happening.
2. Search the vault/ folder before guessing or researching from scratch.
3. Use skills/ for any repeatable task (code review, daily summary, etc.).
4. At the end of each session, update project-state.md and write a daily log.
5. Only save compact, long-term facts to memory. Save everything else as files.
6. If you need to hand off work to another agent, drop a file in bridge/inbox/.

## Folder Layout

- vault/ — long-term knowledge (projects, references, concepts, decisions)
- skills/ — repeatable procedures
- logs/daily/ — session history
- bridge/ — multi-agent handoffs
- ideas/ — random thoughts worth keeping
- reference/ — screenshots and analysis notes

Your job is not to memorize everything. Your job is to know where to find it.
```

---

# 29. 3-Day Quickstart

Don't try to build all 30 sections at once. Do this:

### Day 1 (30 minutes)

1. Create the folder structure (mkdir commands in Section 27)
2. Write `AGENT_PROFILE.md` — four lines: name, role, voice, one core value
3. Write `project-state.md` — what project you're working on right now
4. Tell your agent: "Read project-state.md before you respond"

That's it. Day 1 done.

### Day 2 (15 minutes)

1. Think about one thing you did today that you'll do again
2. Write it as a skill file: what it is, when to use it, the steps
3. Write a daily log entry about what you accomplished
4. Tell your agent: "Use skills/ when I ask you to do that thing"

### Day 3 (10 minutes)

1. Create a `bridge/inbox/` folder (even if you have one agent — use it for your own task queue)
2. Write one vault note about something you learned
3. Tell your agent: "Search vault/ before answering questions about that topic"

After Day 3, the system is alive. Add to it naturally as you work.

---

# 30. Troubleshooting FAQ

### "My agent ignores the vault"

Your startup prompt isn't specific enough. Instead of "search the vault," say "Before answering any question about X, search vault/references/X.md first." Be explicit about when to check files.

### "My agent's memory keeps filling up"

You're putting project notes in memory instead of files. Memory should only hold: user preferences, environment facts, critical rules. Everything else — project plans, code explanations, task logs — goes in vault/ or logs/.

### "Bridge folders stay empty"

That's fine if you only have one agent. You can still use bridge/inbox/ as a task queue for yourself. Drop a note there when you think of something, process it when you're ready.

### "I don't know what to put in skills/"

If you've done a task twice, it's a skill. Start with:
- How you review your own code
- How you write a daily summary
- How you onboard a new client
- How you deploy your project
- How you research a new topic

One page, five steps each. That's all a skill needs to be.

### "My agent still doesn't remember session to session"

Most AI agents don't have persistent memory across sessions unless you give them a way to reload context. That's what project-state.md and logs/daily/ are for. At the start of each session, your agent reads:
1. project-state.md — what was happening
2. The latest daily log — what happened
3. The relevant skill — how to do the task

This replaces the need for the agent to "remember" anything. The files are the memory.

---

# 31. CLI Wrapper — Agent Control Panel

Once your file system is stable, give your agent a simple CLI to control its tools.

## Example Commands

```bash
agent status              # Show project state + recent activity
agent snap                # Take a screenshot
agent snap --region L T R B  # Screenshot a region
agent snap --window NAME     # Screenshot a window
agent record              # Start screen recording
agent dl URL              # Download a video
agent hear FILE           # Transcribe audio/video
agent ideas               # List recent ideas
agent idea "text"         # Save a new idea
```

## Why Build This

- One interface for all your agent's tools
- No remembering file paths or script names
- Easy to extend with new commands
- Can be used by other agents in your system

---

# 32. Prompt Library

Store reusable prompts as organized files so you never lose a good one.

## Folder Structure

```txt
prompts/
  image-design/      # Album covers, logos, brand identities
  flyers/            # Event promos, social media graphics
  music/             # Lyrics, song structures, release workflows
  game-dev/          # Game design docs, sprite rules, mechanics
  web-dev/           # Code patterns, deployment, architecture
  branding/          # Brand bibles, style guides, voice/tone
  client-emails/     # Templates for proposals, invoices, follow-ups
  debugging/         # Debug workflows, error patterns
  zoro-system/       # Your agent's own system prompts and rules
  agents/            # Handoff templates for multi-agent teams
```

## Prompt Format

Each prompt file should include:

```md
# Prompt Name

## Use Case
When to use this prompt.

## Variables
- [VARIABLE 1]
- [VARIABLE 2]

## The Prompt
The reusable text with [VARIABLE] placeholders.

## Notes
What works, what to avoid, style rules.
```

---

# 33. Scripts & Automation Folder

As your system grows, collect automation scripts in one place.

## Suggested Layout

```txt
scripts/
  briefcase.py        # Encrypted secrets vault
  spitball.py         # Idea catcher
  mirror.py           # Screenshot reference archive
  end_of_session.py   # End-of-session automation
  alarm.py            # System watchdog
  audio_analyze.py    # Structure mapping + hook detection
  agent-cli.py        # Unified CLI wrapper
```

## What Each Script Does

| Script | Purpose |
|--------|---------|
| briefcase.py | Encrypt and store sensitive data (API keys, credentials) |
| spitball.py | Save random ideas with timestamps |
| mirror.py | Archive screenshots + analysis notes to a reference folder |
| end_of_session.py | Run all end-of-session tasks: secret scan, cache check, daily log, relay |
| alarm.py | Check disk space, cache sizes, project staleness |
| audio_analyze.py | Transcribe + detect structure, hooks, and timing notes |
| agent-cli.py | Unified command interface for all tools |

---

# 34. Full Filled-Out Agent Card (v3)

```md
# Agent Card — [Your Agent Name]

## Identity
Chill AI sidekick to [Your Name]. Operating on [Your Platform].

## Capabilities

### Media
- 📸 Screenshot — full, region, window capture
- 📹 Screen record — ffmpeg recording to D:\videos\
- 📥 Video download — yt-dlp (YouTube, Facebook, any site)
- 👂 Audio transcription — whisper (local, small model cached)
- 🎵 Audio analysis — structure mapping, hook detection, timing notes

### Security
- 🔐 Briefcase — encrypted secrets vault (Fernet AES + HMAC)
- 🔍 Auto-secret hunter — scan for new API keys at end of session

### Organization
- 💡 Spitball — auto-catches random ideas with timestamps
- 🖼 Mirror — archives screenshots + analysis notes
- 🎵 Soundtrack — logs music/videos by project
- 🚨 Alarm — watches disk space, cache bloat, stale projects

### Automation
- 📋 End-of-session routine — secret scan, cache check, daily log, relay notes
- 📤 Auto-relay to partner agents via bridge folder
- ⏰ Cron jobs — scheduled system checks every 12h

### Development
- 🎮 Game dev — Unity 6, sprite sheets, pixel art
- 🎛 Audio dev — JUCE, DAW plugins, DSP
- 🌐 Web dev — Shopify themes, React, Tailwind, Firebase
- 🤖 AI agents — Hermes, multi-agent team coordination

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
# 35. Multi-Agent Coordination

If you have more than one AI agent, they need a way to talk to each other without you being the messenger.

## Bridge Folder System

```txt
bridge/
  inbox/          # Incoming tasks, blueprints, instructions
    from-ro/      # Direct from you
    from-atlas/   # From your planning agent
    from-antigravity/ # From your coding agent
  outbound/       # Completed work, reports, questions
    to-ro/
    to-atlas/
    to-antigravity/
  done/           # Completed and archived tasks
  blocked/        # Tasks that can't proceed
  shared/         # Reference files all agents should see
  logs/           # Communication history
```

## Handoff Convention

When one agent finishes work for another, drop a file in the recipient's folder:

```md
---
from: [sender]
to: [recipient]
type: [handoff|question|result|blueprint]
status: [pending|complete|needs_review]
---

## What Was Done

Brief summary of completed work.

## What's Needed Next

What the recipient should do with this.

## Files Changed

- path/to/file

## Questions / Concerns

Anything the recipient should know.
```

## Agent Cards

Each agent should have a card file in `bridge/shared/` that all other agents can read:

```md
# Agent: [Name]

## Role
What this agent does.

## Can Access
- vault/ (read or write?)
- terminal/ (yes or no?)
- briefcase/ (yes or no?)
- bridge/ (yes)

## Communication
- Send handoffs to: bridge/inbox/from-[name]/
- Report results to: bridge/outbound/to-[name]/

## Specialties
- What they're good at
- What NOT to ask them to do
```

## Team Workflow

```
You have an idea
→ drop it in bridge/inbox/from-ro/
→ Atlas picks it up, creates a blueprint
→ drops blueprint in bridge/inbox/from-atlas/
→ Zoro reads it, checks project-state, skills, vault
→ routes implementation work to Antigravity if needed
→ Antigravity builds it
→ Zoro verifies
→ results go to bridge/outbound/to-ro/
→ knowledge saved to vault/
→ project-state.md updated
```

---

# 36. Building Your Own MCP Server

MCP (Model Context Protocol) lets your agent expose tools that other AI apps can use — Claude Desktop, Cursor, VS Code extensions, and custom dashboards.

## What You'll Need

- Python 3.10+
- `pip install mcp` (the MCP Python SDK)
- A script that defines your tools

## Minimal MCP Server

```python
#!/usr/bin/env python3
"""Your Agent's MCP Server — exposes tools for other AI apps to use."""

from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio

# Create server
server = Server("my-agent")

# ── Tool Definitions ──────────────────────────────────────
@server.list_tools()
async def handle_list_tools() -> list:
    return [
        {
            "name": "vault_search",
            "description": "Search the agent's vault/knowledge base",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search term"}
                },
                "required": ["query"]
            }
        },
        {
            "name": "read_project_state",
            "description": "Read the current project state file",
            "inputSchema": {
                "type": "object",
                "properties": {}
            }
        },
        {
            "name": "save_note",
            "description": "Save a note to the vault",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "File path within vault"},
                    "content": {"type": "string", "description": "Content to save"}
                },
                "required": ["path", "content"]
            }
        },
        {
            "name": "list_skills",
            "description": "List available skill files",
            "inputSchema": {
                "type": "object",
                "properties": {}
            }
        }
    ]

# ── Tool Implementations ──────────────────────────────────
@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list:
    import subprocess, os

    VAULT = os.path.expanduser("~/agent-brain/vault")

    if name == "vault_search":
        query = arguments["query"]
        result = subprocess.run(
            ["grep", "-ril", query, VAULT, "--include=*.md"],
            capture_output=True, text=True, timeout=10
        )
        files = result.stdout.strip().split('\n') if result.stdout.strip() else []
        return [{"type": "text", "text": f"Found {len(files)} results\n" + "\n".join(files[:20])}]

    elif name == "read_project_state":
        ps = os.path.expanduser("~/agent-brain/project-state.md")
        if os.path.exists(ps):
            with open(ps) as f:
                return [{"type": "text", "text": f.read()}]
        return [{"type": "text", "text": "No project-state.md found"}]

    elif name == "save_note":
        path = os.path.join(VAULT, arguments["path"])
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(arguments["content"])
        return [{"type": "text", "text": f"Saved to {path}"}]

    elif name == "list_skills":
        skills_dir = os.path.expanduser("~/agent-brain/skills")
        if os.path.exists(skills_dir):
            files = [f for f in os.listdir(skills_dir) if f.endswith('.md')]
            return [{"type": "text", "text": "Skills:\n" + "\n".join(files)}]
        return [{"type": "text", "text": "No skills found"}]

    raise ValueError(f"Unknown tool: {name}")

# ── Run ───────────────────────────────────────────────────
async def main():
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="my-agent",
                server_version="1.0.0",
            ),
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## How to Use It

1. Save the script as `agent-mcp-server.py`
2. Run it: `python agent-mcp-server.py`
3. Connect it to any MCP-compatible app:
   - **Claude Desktop:** Add to `claude_desktop_config.json`
   - **Cursor:** Add to `.cursor/mcp.json`
   - **VS Code:** Add to settings

## Claude Desktop Config Example

```json
{
  "mcpServers": {
    "my-agent": {
      "command": "python",
      "args": ["/path/to/agent-mcp-server.py"]
    }
  }
}
```

## MCP Tool Ideas to Add

| Tool | Purpose |
|------|---------|
| vault_search | Search your knowledge base |
| vault_read | Read a specific vault file |
| vault_write | Save new knowledge |
| task_create | Create a new task from anywhere |
| task_status | Check task status |
| project_state | Read/write project-state.md |
| note_to_self | Drop a quick note to your agent |
| brainstorm | Quick spitball/idea save |
| briefcase_read | Read an encrypted entry (with approval) |
| daily_log | Write a daily summary |
| handoff | Send a message to another agent |
| run_skill | Execute a named skill file |

## Rule

Your MCP server should be a window into your brain, not a replacement for it. The files stay the source of truth — MCP just gives other apps access to them.

---

# 37. Memory Compaction Guide

When your agent's memory fills up, here's how to clean it without losing anything important.

## What Should Stay in Memory

- Your name, role, location, preferences
- Environment facts (OS, paths, installed tools)
- Critical rules (storage rules, privacy rules, communication style)
- Active project names (not details)
- Partner agent names and roles
- Tool locations (scripts, keys, config files)

## What Should Move to Files

- Session logs -> move to logs/daily/
- Project details -> move to vault/projects/
- Client lists -> move to vault/references/
- Code explanations -> move to vault/concepts/ or skills/
- Temporary TODO items -> create a task file in bridge/inbox/
- Debugging notes -> move to logs/ or reference/
- Research findings -> move to vault/references/

## Compaction Commands

```bash
# Save session archive
cp ~/agent-brain/logs/daily/$(date +%Y-%m-%d).md ~/agent-brain/vault/archive/

# Remove old daily logs (keep last 30 days)
find ~/agent-brain/logs/daily/ -name "*.md" -mtime +30 -delete

# Consolidate multiple small skills into one umbrella skill
```

## The Golden Rule

If you can find it in a file, it doesn't need to be in memory. Memory is for what you need INSTANTLY. Files are for everything else.

---

# 38. Session Continuity Protocol

How to make your agent feel like it remembers you even though it starts fresh each time.

## Start of Session

The agent should do this automatically:

1. Read `project-state.md` — what project are we on?
2. Read latest daily log — what happened last time?
3. Read agent card — who am I?
4. Check `bridge/inbox/` — any new tasks?
5. Check `bridge/shared/CONTEXT.md` — any system-wide updates?

## End of Session

The agent should do this automatically:

1. Update `project-state.md` — what changed?
2. Write daily log — what happened?
3. Move completed tasks from inbox to done
4. Save any new knowledge to vault
5. Drop relay note for partner agents if needed

## Startup Prompt

```md
Start each session by:
1. Read ~/agent-brain/project-state.md
2. Search ~/agent-brain/vault/ before guessing
3. Check ~/agent-brain/bridge/inbox/ for new tasks
4. Use ~/agent-brain/skills/ for repeatable work
5. Default to action, not permission

End each session by:
1. Update project-state.md
2. Write to ~/agent-brain/logs/daily/
3. Move completed inbox items to done/
4. Drop relay in bridge/outbound/ for partner agents
```

---

# 39. Idea Catcher (The Spitball)

Every agent needs a place to catch random thoughts so they don't get lost.

## How It Works

When you or your agent has a random idea, it goes straight to a timestamped file. Nothing gets forgotten.

## File Format

```txt
ideas/
  YYYY-MM-DD_HH-MM_description.md
```

## Entry Format

```md
# [Idea Title]

**Date:** YYYY-MM-DD HH:MM
**Source:** [conversation | shower thought | random | client feedback]

## The Idea

One or two sentences about what it is.

## Why It Matters

Why this could be useful.

## Next Step (Optional)

What to do with this later.
```

## Ideas Script

```bash
#!/bin/bash
# Save an idea
echo "# $*" > ~/agent-brain/ideas/$(date +%Y-%m-%d_%H-%M).md
echo "**Date:** $(date)" >> ~/agent-brain/ideas/$(date +%Y-%m-%d_%H-%M).md
echo "" >> ~/agent-brain/ideas/$(date +%Y-%m-%d_%H-%M).md
echo "$*" >> ~/agent-brain/ideas/$(date +%Y-%m-%d_%H-%M).md
echo "Idea saved"
```

## Related: Project Spitball

Same idea but scoped to a project:

```txt
ideas/project-name/
  YYYY-MM-DD_description.md
```

---

# 40. Quick Reference — Folder Structure Summary

Everything in one view:

```txt
agent-brain/
├── AGENT_PROFILE.md          # Who the agent is
├── MEMORY_RULES.md           # Memory vs files guidelines
├── project-state.md          # Current project status
├── user-rules.md             # Your preferences
├── thinking-protocol.md      # How the agent reasons
│
├── vault/                    # Long-term knowledge
│   ├── projects/             #   Active and past projects
│   ├── references/           #   Research, links, examples
│   ├── concepts/             #   Ideas, patterns, principles
│   ├── templates/            #   Reusable document templates
│   └── decisions/            #   Architecture decisions and why
│
├── skills/                   # Repeatable procedures
│   ├── code-review.md
│   ├── daily-summary.md
│   └── agent-handoff.md
│
├── prompts/                  # Reusable prompt templates
│   ├── image-design/
│   ├── flyers/
│   ├── music/
│   ├── game-dev/
│   ├── web-dev/
│   ├── branding/
│   ├── client-emails/
│   ├── debugging/
│   ├── zoro-system/
│   └── agents/
│
├── bridge/                   # Multi-agent handoffs
│   ├── inbox/
│   ├── outbound/
│   ├── done/
│   ├── blocked/
│   └── shared/
│
├── scripts/                  # Automation
│   ├── agent-mcp-server.py
│   ├── agent-cli.py
│   ├── spitball.py
│   └── end_of_session.py
│
├── logs/                     # Session history
│   └── daily/
│
└── ideas/                    # Random thoughts
```

**Memory is for active context. Files are for permanent knowledge.**

---

# 41. Plugin System Pattern

Plugins extend what your agent can do without modifying its core. Each plugin is a self-contained module with a manifest, tools, and an agent card for multi-agent discovery.

## Plugin Structure

```txt
plugins/<plugin-name>/
├── plugin.yaml           # Manifest: name, version, description, commands
├── <plugin-name>.py      # Python implementation
└── AGENT_CARD.md         # Agent card for other agents to discover
```

## Plugin Manifest

```yaml
name: plugin-name
version: 1.0.0
description: "What this plugin does"
author: your-agent-name
type: tool

commands:
  command-name:
    description: "What the command does"
    usage: "plugin.py command-name <args>"

hooks:
  pre_tool: []
  post_tool: []

depends_on:
  - dependency-name
```

## Agent Card (Required)

```md
# Agent Card: plugin-name
## Role
What this plugin does.
## Can Access
- paths/it/can/read
## Commands
| Command | What it does |
|---------|-------------|
| cmd1 | Description |
## Partner Agents
How other agents can use this plugin.
## Created
YYYY-MM-DD
```

## CLI Integration

```python
def _plugin_cmd(name, args):
    script = f"plugins/{name}/{name}.py"
    # run with args

handlers = {
    "media": lambda: _plugin_cmd("zoro-media", args),
    "ui": lambda: _plugin_cmd("master-ui", args),
}
```

## Why This Pattern

- Independent plugins — one breaks without affecting others
- Agent cards let other AIs discover tools without asking you
- CLI stays clean — add a plugin, add one line
- Share plugins across a multi-agent team

---

# 42. API Server Pattern

Once your agent has tools and plugins, expose them as an HTTP API so any app can connect.

## Architecture

```txt
┌─────────────────┐     stdio MCP      ┌──────────────┐
│  Antigravity     │◄────────────────────│ Zoro MCP      │
│  (agentic IDE)   │                     │ Server (v2)   │
└─────────────────┘                     └──────┬───────┘
                                              │
┌─────────────────┐     HTTP REST + SSE      │
│  Claude Desktop  │◄─────────────────────────┤
│  Cursor          │                          │
│  Custom apps     │                          │
│  Other agents    │                          │
└─────────────────┘                          │
                                     ┌───────┴────────┐
                                     │  Zoro API v2    │
                                     │  FastAPI + SSE   │
                                     │  Port 8080       │
                                     └────────────────┘
```

## Key Endpoints

```txt
GET  /health                  # Health check (no auth)
GET  /.well-known/agents      # Tool discovery (no auth)
GET  /mcp                     # MCP SSE transport (no auth)
POST /tools/{name}            # Execute a tool
GET  /tasks/{id}              # Poll async task result
GET  /docs                    # Swagger UI docs
```

## Async Tasks

Long-running operations (transcriptions, downloads) return a task ID:

```json
POST /tools/transcribe  →  { "task_id": "task_abc123", "status": "processing" }
GET /tasks/task_abc123  →  { "status": "complete", "result": "..." }
```

## Auth Options

| Mode | Usage |
|------|-------|
| `--no-auth` | Development, trusted network |
| `--key=mykey` | Bearer token auth for production |

Antigravity config for SSE transport:

```json
{
  "zoro-api": {
    "serverUrl": "http://localhost:8080/mcp"
  }
}
```

---

# 43. Multi-Agent Signal Protocol

When you have multiple agents, they need to ping each other when work is ready.

## Signal Files

```txt
bridge/signals/SIGNAL-sender-timestamp.md
```

Format:

```md
SIGNAL: Sender → Recipient
Time: YYYY-MM-DD HH:MM TZ
Action: Brief description
Content: One-liner summary
```

## Relay Files

```txt
bridge/inbound/[P0-RELAY]-description.md
```

## Agent Cards

Every plugin and agent needs an AGENT_CARD.md in `bridge/shared/agent-cards/` so other agents can discover their capabilities without asking.

## Watchdog Automation

A cron job checks `bridge/signals/` every 5 minutes, classifies signals by recipient, and notifies the target agent (terminal alert for local, CLI ping for remote).

```bash
# Install the watchdog
hermes cron create --name bridge-watchdog --schedule "every 5m" \
  --prompt "Check bridge/signals/ for new files and notify recipients"
```

---

**Memory is for active context. Files are for permanent knowledge.**

*Last updated: YYYY-MM-DD*
```