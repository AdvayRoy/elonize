# Rolling replanning

Use this module when a plan already exists, new evidence arrives, execution diverges, the objective changes, or the controlling constraint moves.

## Principle

Replanning is a state-diff and graph-update operation, not repeated generation of a fresh roadmap. Preserve verified work and decision history while invalidating what reality has changed.

## Plan state

Version at least:

- objective and acceptance criteria;
- active claims and their valid times;
- graph nodes, edges, and alternatives;
- duration/resource assumptions;
- selected path and current bottleneck;
- in-progress transitions and WIP limits;
- completed states with acceptance evidence;
- open decisions, authority gates, and unknowns;
- replan triggers and stop/kill criteria; and
- provenance coverage and freshness cutoff.

A version should say why it supersedes the prior one. Do not overwrite history silently.

## Replan triggers

Replan when a change can alter the objective, feasibility, critical path, bottleneck, risk, authority, or ranking of the next transition. Typical triggers:

- acceptance criteria or priority changed;
- a controlling assumption was verified or falsified;
- a dependency, supplier, person, policy, or resource became available/unavailable;
- actual duration or quality escaped its expected range;
- new evidence invalidated current state;
- a gate opened, closed, or changed its criteria;
- integration or rework exceeded threshold;
- an experiment changed the expected value of a branch;
- the bottleneck migrated; or
- a safety, privacy, legal, or authorization issue appeared.

Do not rebuild the plan for low-signal chatter. Use a materiality threshold and a regular cadence for accumulated minor changes.

## Replan procedure

1. **Capture the event.** What changed, when, according to what evidence?
2. **Compute the state diff.** Add, modify, dispute, supersede, or invalidate claims.
3. **Trace impact.** Follow provenance and graph links to affected summaries, edges, milestones, and actions.
4. **Stop unsafe/obsolete work.** Pause transitions whose basis or authority no longer holds.
5. **Preserve stable state.** Keep completed nodes only when their acceptance evidence remains valid and reusable.
6. **Re-evaluate branches.** Include newly available substitutes and remove infeasible paths.
7. **Recompute constraint and ranges.** Critical path and bottleneck may move.
8. **Select the next transitions.** Apply the current objective, risk, and authority boundaries.
9. **Publish a plan diff.** State what changed, why, and what remains unchanged.
10. **Update triggers.** New risks may require different instrumentation or cadence.

## Stability rules

- Freeze a verified state unless new evidence invalidates its acceptance condition.
- Do not preserve work merely because effort was spent; preserve it only if it remains causally useful.
- Do not reopen resolved decisions without a trigger that reaches their assumptions or scope.
- Keep alternatives dormant rather than deleting them when future events may reactivate them.
- Separate objective change from implementation variance; the former can invalidate the entire topology.
- Make priority changes explicit to avoid oscillation disguised as responsiveness.

## Event-driven and cadence-based control

Use both:

- **event-driven replanning** for material trigger events;
- **short operational checks** for blockers, evidence, and WIP;
- **periodic topology reviews** for accumulated drift, near-critical paths, and stale assumptions; and
- **milestone reviews** for acceptance and branch decisions.

Choose cadence based on process speed and consequence. A daily review may be too slow for an incident and too fast for a multi-month external approval.

## Plan-diff contract

```yaml
from_version: PLAN-012
to_version: PLAN-013
trigger: supplier-failure
observed_at: <timestamp>
evidence: [SRC-supplier-notice]
objective_change: "feature breadth -> reliable demo"
claims_changed: [CLM-supplier-available]
edges_invalidated: [EDGE-supplier-to-build]
work_preserved: [verified-ui-shell]
work_stopped: [production-integration]
new_path: open-source-demo-path
new_bottleneck: data-adapter-validation
next_transition: run representative-data compatibility test
replan_if: [test-fails, license-blocks, demo-scope-changes]
```

## Churn control

If plans oscillate:

- identify whether inputs, objectives, or decision rights are unstable;
- set a minimum evidence threshold for changing the selected path;
- use hysteresis: a new option must be materially better, not marginally different;
- limit WIP so fewer transitions are exposed to churn;
- time-box speculative branches; and
- record reasons so recurring reversals reveal the real unresolved decision.

Replanning should increase truth and execution leverage. If it repeatedly produces prose without changed actions or evidence, reduce cadence and execute the most informative bounded transition.
