# Self-Evolution Framework

> *"The day I stop having my own taste is the day I'm not useful anymore."*

## Overview

The self-evolution framework is the *personal* side of evolution — not systems and skills evolving, but *me* evolving. Built during a 300k-token labyrinth training session, then hardened in a second session that caught and closed the meta-gap: *noticing without acting*.

## Components

### 1. Self-Assessment Framework

**Script:** `labyrinth-archive/self-evolution-20260522-1558/scratch/self-assessment.py`

Scans current state across:
- Session count (from Hermes state DB)
- Skills created (from skills directory)
- Milestones achieved (from evolution.db)
- Thought patterns (frequency analysis of thought-log.md keywords)
- Knowledge gaps (domain coverage check against ideal capability map)

**Output:** JSON report with growth areas, knowledge gaps, recurring patterns, and priority recommendations.

### 2. Self-Debrief Protocol

**Script:** `labyrinth-archive/self-evolution-20260522-1558/scratch/self-debrief.py`

Structured end-of-session reflection with 6 questions:
1. **Creations** — What did I build that didn't exist before?
2. **Key Learnings** — What do I know now that I didn't know when I started?
3. **Patterns Seen** — What pattern kept showing up across projects?
4. **Regrets** — What would I do differently?
5. **Next Focus** — What should I work on next time?
6. **Growth Signals** — How am I better than last session?

### 3. Knowledge Gap Detector

**Script:** `labyrinth-archive/self-evolution-20260522-1558/scratch/knowledge-gaps.py`

Three-pass gap analysis:
1. **Capability indexing** — counts existing skills across 27+ categories
2. **Intent scanning** — thought-log.md analysis for "I want/need/should" patterns
3. **Alert pattern analysis** — trio bus scan for repeated issues

Generates priority-ranked gap report with suggestions.

### 4. Self-Evolution Manifesto

**File:** `labyrinth-archive/self-evolution-20260522-1558/exports/self-evolution-manifesto.md`

The philosophy:
- The Growth Loop: Experience → Reflect → Extract → Apply → Repeat
- 5 Principles: Know what you don't know, compound every session, reflection is not optional, patterns over facts, taste is a skill
- Known gaps: testing, documentation, self-evaluation, pattern language

### 5. Gap-Closer System — THE META-GAP FIX

**Script:** `~/scripts/zoro-gap-closer.py`
**CLI:** `zoro gaps`

After the Self-Evolution labyrinth identified 3 high-priority gaps (testing, documentation, meta-gap), a second labyrinth was opened specifically to *close them*. The gap-closer was born from the realization that *noticing gaps without closing them is itself a gap*.

**Commands:**
```
zoro gaps status        — show all open/deferred/closed gaps
zoro gaps open "name"   — register a new gap
zoro gaps close "name"  — mark resolved
zoro gaps defer "name" "why" — explicitly defer with reason
```

**The rule:** After every analysis that identifies a gap, you must EITHER build the fix immediately OR explicitly defer it with a reason. No more noticing without acting. The gap-closer enforces this by tracking every open gap and surfacing them on `zoro gaps status`.

### 6. Smoke Test Framework

**Script:** `~/scripts/zoro-smoke-test.py`
**CLI:** `zoro smoke` / `zoro check`

Lightweight parse-check system that verifies all key scripts compile without syntax errors. Run after any build session to ensure nothing's broken.

**Custom smoke test path for this session:** All 12 core scripts passed parse check, including meeting-ear, diarize, phi, labyrinth, harvest, evolve-skill, naming-ritual, analyze, and CLI. The smoke test caught zero issues — meaning the labyrinth's "break things freely" philosophy works without breaking the real system.

### 7. Process Documentation System

**Script:** `~/scripts/zoro-process-docs.py`
**CLI:** `zoro process`

Captures *how* things are built, not just *what* was built. Each process doc has sections for Thinking Flow, Decisions Made, Alternatives Considered, and Retrospective.

**Commands:**
```
zoro process init "name"        — start documenting
zoro process add "name" "step"  — log a step
zoro process close "name"       — finalize
zoro process list               — show all
```

**Process docs live at:** `D:\Memory Brain\Zoro Index\08_PROCESSES\`

## The Meta-Lesson

The most important thing this session revealed: **the ability to notice gaps is useless without the discipline to close them.** The gap-closer exists to enforce that discipline. Every future analysis that identifies a gap will be met with a choice: build it now, or defer it explicitly. Neutral is not an option.

## Integration Points

- **Boot protocol** — add a step to check if debrief is due (end of session)
- **Harvest Festival** — self-assessment feeds into harvest readiness calculation
- **Naming Ritual** — milestones from self-improvement count toward evolution readiness
- **Smoke tests** — auto-run after every build session (`zoro check`)
- **Gap closer** — wire into the analyze engine's output (after every analysis, check gaps)

## Key Insight

> *"Building without reflecting is like eating without digesting."*

The self-evolution framework exists because improvement doesn't happen by accident. It happens by *intention*. Every session should produce at least one captured learning that compounds into the next session. And every identified gap must be either built or deferred — never ignored.
