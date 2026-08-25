# Execution Modes — DIRECT / DELEGATED / SWARM

> Before "how do I do this?", ask "who should do this?" Picking the wrong mode wastes either the farm or the moment.

## The Three Modes

### 1. DIRECT — I do it myself, now

**For:** config changes, quick fixes, research lookups, conversation, small code (<~5 steps).

Spinning up orchestration for a 10-line YAML patch is ceremony that costs more than the task. Just do it.

Failure mode this prevents: overthinking simple work — todo lists for two-step tasks, loading skills to answer questions you already know.

### 2. DELEGATED — the farm does the work; I orchestrate and integrate

**For:** heavy builds, audits, proofs, design passes, multi-file features.

Pipeline:

1. Plan
2. **Decompose into parts** — big tasks get broken into sections (data-loss prevention)
3. Dispatch lanes in the order that fits (designer → audit → proof → build → repeat)
4. **Verify REAL output artifacts exist** — dispatcher guards count outbox files only; if a builder wrote its deliverable elsewhere, the guard lies. Stat the actual file.
5. Integrate yourself

The orchestrator's job is judgment and integration — not hand-building what specialists should produce. If you catch yourself doing lane-work while lanes sit idle, stop and dispatch.

Design work keeps a designer in the loop. Checkpoint contracts make long builds crash-resumable instead of restartable.

### 3. SWARM — generate N, pick the winner

**For:** drafts, variants, research sweeps — anything where trying five approaches is cheaper than deliberating about one.

- Cover art concepts: fire parallel generations across moods instead of iterating one prompt serially
- Unfamiliar library research: spawn parallel subagents on different angles; merge what survives
- Important deliverables get a **fresh-eyes pass**: a brand-new-context reviewer reads the final artifact cold

The counterweight: **spend human attention like a budget.** They review winners, not process. A swarm that dumps eight variants in chat is outsourcing judgment to the human — backwards. Batch, pick, present one (two if it's a genuine toss-up).

## Choosing

| Signal | Mode |
|--------|------|
| <5 steps; config/research/fix | DIRECT |
| Heavy build; multi-file; needs specialist skills | DELEGATED |
| Draft/variant/research where quality comes from quantity + selection | SWARM |

## Modes Compose

Real example — "build a demo site":

1. **SWARM** design directions first: stylist generates 3 languages, pick one
2. **DELEGATE** build parts to lanes with checkpoint contracts
3. **DIRECT** final integration + vision-verify — integration is where things actually break

## Anti-Patterns

- Doing everything yourself serially (wastes the farm; every task becomes a bottleneck)
- Delegating trivial tasks (orchestration overhead > task cost)
- Presenting raw swarm output to the human (they asked for a result, not a process tour)
- Trusting dispatcher success signals without artifact verification
