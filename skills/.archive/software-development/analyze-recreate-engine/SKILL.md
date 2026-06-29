---
name: analyze-recreate-engine
description: "Formal reverse-engineering pipeline: study a target (file, app, codebase, pattern), extract its architecture, and generate a buildable skill or implementation plan. Inspired by Great Sage's core loop — analyze anything, understand it perfectly, recreate it better."
tags: [analysis, reverse-engineering, recreation, pipeline, study]
---

# Analyze & Recreate Engine

## Overview

A formal pipeline for turning study into capability. When you analyze a target, the output isn't just notes — it's a buildable skill or implementation plan ready to hand to a build agent.

## Pipeline

```
Target → Analyze → Extract Architecture → Generate Plan → (Optional) Build Skill
```

### Step 1: Analyze

```
zoro analyze ./target                          # quick analysis + recreation plan
zoro analyze ./target --depth deep             # thorough analysis
zoro analyze ./target --build                  # analyze + generate buildable skill
zoro analyze list                              # past analyses
```

**Target types auto-detected:**
- `unity_project` — has .unity files
- `node_project` — has package.json
- `python_project` — has setup.py/pyproject.toml
- `csharp_project` — has .sln/.vcxproj
- `cmake_project` — has CMakeLists.txt
- `web_project` — has .html/.css files
- Plus individual files: python_script, web_file, document, config_file, binary

### Step 2: Architecture Extraction

The analyzer detects:
- **Patterns** — class-based, async, event/callback, pipeline, factory, singleton, observer, plugin architecture, state machine, CLI, middleware
- **Dependencies** — from requirements.txt, package.json, import statements
- **Structure** — file count, directory layout, extension distribution
- **Size** — total bytes, line count

### Step 3: Recreation Plan

A markdown plan is generated with:
- Objective
- Architecture summary
- Key patterns to implement
- Dependencies
- Implementation steps (scaffold → core → interfaces → test → polish)

### Step 4: Build Skill (Optional)

With `--build`, the analysis generates a full Hermes skill at `software-development/recreated-{slug}/` containing the complete recreation plan and extracted knowledge.

## Key Files

| File | Purpose |
|------|---------|
| `~/scripts/zoro-analyze.py` | Analysis engine |
| `D:\Memory Brain\Zoro Index\06_ANALYSES\` | Analysis history (JSON) |

## Pitfalls

- **File permission errors** on binaries — the analyzer reads with `errors="ignore"` for text files, but binary files will return empty pattern analysis
- **Deep analysis** on large directories (>1000 files) may be slow — prefer `quick` for initial reconnaissance
- **The build flag** creates a SKILL.md, not executable code. The recreation plan is meant to be handed to a build agent (Codex/Dex) for actual implementation

## See Also

- `evolution-infrastructure` — naming and skill fusion system for evolving from analysis results
- `software-reverse-engineering` — methodology for studying installed software
