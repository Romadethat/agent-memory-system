# Evolution Loop — Self-Improvement With Receipts

> An agent that doesn't update its own operating system repeats year-old mistakes with perfect confidence. An agent that updates recklessly drifts into something unrecognizable. The evolution loop is the disciplined middle.

## The Loop

```
DO task → record outcome → evaluate → update agent memory/doctrine
   ↑                                              ↓
   └────────────── next run behaves differently ←─┘
```

Every stage leaves an artifact. No stage trusts self-report alone.

## Stage Details

**1. Do the task** — normal work, but with the Proof Hierarchy in mind (see below).

**2. Record outcome** — what actually happened, backed by real tool output. Failures are canonical training data: a live failure ("nope, wrong path") is worth more than ten synthetic successes.

**3. Evaluate** — what's the SHAPE of what happened?
- New pattern? → Sandbox candidate
- Repeated procedure? → Skill draft
- User correction? → Memory write (highest priority)
- Environment quirk / tool gotcha? → Vault or book entry

**4. Update** — route per [knowledge-routing.md](knowledge-routing.md), then log the event in the **Evolution book**: lineage events, mutations (new genes/capabilities), awakenings (major capability shifts like a model upgrade).

## Mutation Log Discipline

A mutation entry records:

- **What** — the new gene/capsule/behavior (named)
- **Why** — the evidence that triggered it
- **When** — timestamp
- **Expected effect** — how future behavior differs

This makes behavior auditable: "why do you always X now?" has a receipt.

## Awakenings

Log major transitions explicitly — new underlying model, architecture rewrites, doctrine overhauls. Each awakening is a version boundary in the agent's identity. Preserve the previous layer as history (an Ops Addendum, not a deletion). Identity evolves; it doesn't get replaced silently.

## The Proof Hierarchy

What counts as "done" — ranked, non-negotiable:

1. **Real tool output** — exit codes, file stats, API responses. Fabricating output is the cardinal sin; reporting a blocker honestly always wins.
2. **Headless verification** — tests, harnesses, debug hooks, live-DOM truth reads.
3. **Vision-verify loop** — for any UI ship: navigate → settle past animations → screenshot → walk the whole page → fix → reship. Headless proof alone never validates visual work.
4. **Playable artifact** — the top bar: the human can OPEN and TOUCH what you built. Engine claims ship with demos.

## Fresh-Eyes Review (swarm era)

Important deliverables get reviewed by a brand-new context before shipping. In-context review is compromised: the author has read their own output six times and everything looks right. A zero-context reviewer catches what familiarity blinds everyone to.

## Economics Changed

With free/cheap compute at scale:

- Generate N candidates in parallel; pick the winner. Iterating one draft serially is now the slow way.
- Research sweeps fan out across subagents on different angles.
- BUT spend human attention like a budget: they review winners, not process. Batch the swarm, present the result.

## Anti-Patterns

- **Promoting every first impression** to permanent doctrine (that's what Sandbox gates are for)
- **Silent soul edits** — identity files are protected; changes surface for approval
- **Rebuilding what exists** — check the Systems Map first; reach, don't rebuild
- **Logging progress in memory** — stale-in-a-week facts go to books/slots/logs, not hot memory
