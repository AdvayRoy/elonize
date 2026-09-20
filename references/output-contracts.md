# Output contracts

Use this module to return the smallest useful, auditable planning artifact. Match depth to the operator's decision and available attention.

## Contract selection

- **Flash:** one decision or immediate bottleneck; usually under a page.
- **Operator brief:** default for active work; enough to execute and replan.
- **Full plan:** high-stakes or genuinely complex objectives requiring graph, ranges, resources, and branches.
- **Plan diff:** update to an existing plan after material change.
- **Machine-readable state:** for durable tooling, handoff, or repeated replanning.

Do not dump internal chain-of-thought, the entire archive, or every low-impact node. Expose conclusions, assumptions, evidence, calculations, alternatives, and uncertainty at the level needed for audit.

## Flash contract

```markdown
## Outcome
<terminal state and acceptance proof>

## Controlling constraint
<current bottleneck or plan-flipping unknown, with provenance handle>

## Change now
<one to three state transitions, owner/authority, acceptance evidence>

## Why this compresses time
<elapsed-time cause and mechanism changed>

## Could make this wrong
<decisive assumptions, contradiction, or replan trigger>
```

## Operator brief

```markdown
## Decision
<recommended path and confidence/feasibility class>

## State delta
- Terminal state: ...
- Current verified/reported state: ...
- Gap: ...

## Critical path and bottleneck
<controlling subgraph, duration range, queue/resource constraints>

## Compression moves
| Move | Cause removed/changed | Net effect | Preconditions | Risk | Proof |

## Next transitions
| Transition | Owner | Authority | Acceptance evidence | Stop/replan trigger |

## Assumptions and unknowns
<ranked by impact and value of information>

## Provenance
<compact source/claim handles and coverage cutoff>
```

## Full-plan contract

Include only sections that apply:

1. objective, beneficiary, scope, exclusions, and acceptance evidence;
2. current-state model with epistemic statuses and coverage;
3. relevant source and contradiction ledger;
4. outcome/causal graph and alternative paths;
5. baseline elapsed-time decomposition;
6. critical path, near-critical paths, bottleneck, and resource queues;
7. compression lever portfolio with interactions and net ranges;
8. resource, parallelization, automation, and integration design;
9. feasibility bands, assumptions, pre-mortem, and safety/authority gates;
10. milestones expressed as validated states, not activity lists;
11. immediate transition contracts and WIP limits;
12. monitoring, replan triggers, and stop/kill criteria; and
13. provenance index and known coverage gaps.

Use a diagram only when it makes dependency structure or branches materially clearer than prose.

## Machine-readable state

This is an interchange shape, not a mandatory database schema:

```yaml
plan_id: PLAN-013
generated_at: <timestamp>
freshness_cutoff: <timestamp>
objective:
  statement: <outcome>
  acceptance: [<observable conditions>]
  exclusions: [<not included>]
  authority_boundaries: [<gates>]
state:
  claims: [<claim ids>]
  contradictions: [<claim pairs>]
  unknowns: [<unknown ids>]
graph:
  selected_path: [<node ids>]
  alternatives: [<path ids>]
  critical_path: [<node ids>]
  bottleneck: <constraint id>
feasibility:
  class: demonstrated|defensible|plausible|speculative|blocked|unknown
  ranges: <supported ranges or null>
  controlling_assumptions: [<assumption ids>]
execution:
  active_transitions: [<transition ids>]
  wip_limit: <number or null>
  next_decision: <decision id or null>
control:
  replan_triggers: [<events>]
  stop_conditions: [<conditions>]
provenance:
  source_manifest: <locator>
  coverage: <summary>
```

Keep identifiers stable across revisions. Use null or unknown rather than invented values.

## Plan-diff contract

State:

- trigger and source evidence;
- objective/state changes;
- claims and edges added, invalidated, disputed, or superseded;
- work preserved, stopped, or made obsolete;
- old versus new critical path and bottleneck;
- changed feasibility range;
- new immediate transitions; and
- updated replan triggers.

## Quality bar

Before delivery verify that the output:

- distinguishes observed, reported, inferred, proposed, and unknown;
- names the mechanism behind every material time saving;
- shows the current constraint rather than an exhaustive checklist;
- gives executable state transitions with acceptance evidence;
- preserves recoverable provenance and coverage limits;
- exposes feasibility and authority boundaries;
- avoids fake precision and unsupported completion claims; and
- stops after the operator has enough to act and audit.

A concise output is successful only if it preserves decisive signal. A comprehensive output is successful only if its added detail changes execution, auditability, or risk control.
