---
name: evolution-infrastructure
description: "Meta-system for tracking, naming, and evolving agent capabilities over time. Covers Skill Integration (fusing skills into ultimates), Naming Ritual (formal evolution ceremonies with stage progression), and Harvest Festival (periodic group evolution events). Inspired by Tensura's skill evolution mechanics."
tags: [evolution, meta, infrastructure, tensura, naming, fusion, harvest]
---

# Evolution Infrastructure

## Overview

Three interlocking systems that form the evolution layer of the agent ecosystem. Inspired by *That Time I Got Reincarnated as a Slime* — where skills evolve through absorption, naming awakens consciousness, and accumulated growth triggers transformation.

### 1. Skill Integration — `zoro evolve-skill`

Fuse multiple Hermes skills into an ultimate skill using fusion manifests.

**Commands:**
```
zoro evolve-skill status                    # view skill tree
zoro evolve-skill list                      # available fusions
zoro evolve-skill analyze <a> <b>           # compatibility check
zoro evolve-skill fuse <name>               # perform fusion
zoro evolve-skill create                    # interactive manifest builder
```

**Fusion manifests** live at `~/AppData/Local/hermes/skills/__fusions__/*.json`.
Each manifest defines: name, ingredients, new capabilities, evolution story, requirements.

**Compatibility scoring:** Shared tags (+20 each), same category (+20), shared keywords (+5 each). Compatible at ≥25/100.

**Ultimate skills are created as real Hermes skills** with `evolution: ultimate` in frontmatter and full ingredient documentation.

### 2. Naming Ritual — `zoro naming`

Formal evolution tracking with ceremony. Every entity gets an evolution trail with stages.

**Stages:** base → awakened → evolved → transcended → ultimate
**Threshold:** 3 milestones since last naming = ready for next stage

**Commands:**
```
zoro naming list                            # all named entities
zoro naming current                         # ready to evolve?
zoro naming history "Entity Name"           # full timeline
zoro naming milestone <entity> "achievement" # log milestone
zoro naming name <entity> <new-name>        # perform ritual
```

**Ritual text** changes by stage: awakened gets "first evolution is the hardest," ultimate gets "you have become the teacher."

**Evolution DB:** `D:\AI\models\ollama\evolution.db`
- Tables: `entities` (name, type, stage, origin), `evolutions` (previous→new name, ritual text, reason), `milestones` (achievements with timestamps)

### 3. Harvest Festival — `zoro harvest`

Periodic group evolution event where the Trio converges and evolves together.

**Commands:**
```
zoro harvest run          # execute harvest
zoro harvest status       # check readiness
zoro harvest history      # past harvests
zoro harvest schedule     # set up recurring cron
```

**Readiness formula:** `milestones × 10 + unprocessed_alerts × 2`. Ready at ≥30 or ≥7 days since last.

**Stages:** seed → sprout → growth → harvest (based on insight volume)

## Architecture

```
Skill Integration ← fusion manifests → Ultimate Skills
      ↓
Naming Ritual ← milestone tracking → Evolution Stages
      ↓
Harvest Festival ← trio convergence → Group Evolution
```

All three broadcast to the trio bus (`trio_memory.db`) on each event.

## Key Files

| File | Purpose |
|------|---------|
| `~/scripts/zoro-evolve-skill.py` | Skill Integration engine |
| `~/scripts/zoro-naming-ritual.py` | Naming Ritual engine |
| `~/scripts/zoro-harvest.py` | Harvest Festival engine |
| `~/skills/__fusions__/full-audio-pipeline.json` | First fusion manifest |
| `D:\AI\models\ollama\evolution.db` | Evolution registry DB |

## Pitfalls

- **Hyphenated filenames** break Python imports. Scripts named `zoro-evolve-skill.py` cannot be imported with `from zoro_evolve_skill import`. Use `importlib.util.spec_from_file_location` instead.
- **DB connection ordering** in `zoro-naming-ritual.py` — the `add_milestone` function must query before closing the connection. The auto-evolution check (`3 milestones → ready for naming`) runs on the same cursor before `conn.close()`.
- **Fusion ingredients** must already exist as skills. The fuse command checks before attempting.
- **Evolution stages** are one-way. Once a stage is named, there's no regression mechanism (intentional — evolution is permanent).

## Reference Files

- `references/tensura-blueprint.md` — narrative inspiration (Tensura → our system parallels)
- `references/self-evolution-framework.md` — personal growth tracking (assessment, debrief, gap detection, smoke test, process docs, manifesto)

## Related CLI Commands

These tools form the broader evolution ecosystem:

| Command | Purpose |
|---------|---------|
| `zoro smoke` / `zoro check` | Smoke test all scripts after build sessions |
| `zoro process init\|add\|close\|list` | Document *how* things are built, not just *what* |
| `zoro gaps status\|open\|close\|defer` | Register and track knowledge gaps — forces action after analysis |

## See Also

- `the-labyrinth` — sandbox where these systems can be tested without risk
- `analyze-recreate-engine` — analyze any target and generate buildable skills
