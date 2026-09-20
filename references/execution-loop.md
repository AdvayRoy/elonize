# Execution loop

Use this module to convert a plan into controlled state transitions, coordinate people or agents, verify results, and decide when to continue, rework, branch, stop, or escalate.

## Unit of execution

The unit is not a task label; it is a state-transition contract:

```yaml
transition_id: TR-021
from_state: demand-evidence-unverified
to_state: demand-evidence-audited
why_now: controls go/no-go decision
action: inspect interview records and reproduce sample counts
inputs: [SRC-interview-index, SRC-recordings]
owner: research-agent
authority: read-only internal sources
deliverable: claim ledger and audit summary
acceptance_evidence:
  - all sampled claims link to source spans
  - coverage and exclusions are explicit
  - contradictions are preserved
timebox: 90 minutes
stop_conditions:
  - source access is blocked
  - sensitive data cannot be handled within authority
integration_owner: project-lead
replan_if:
  - sample differs materially from memo
```

Use only fields that improve control. The essential elements are expected state change, authority, evidence, stopping, and integration.

## Loop

1. **Observe:** collect current results, failures, blockers, queues, and external changes.
2. **Update truth:** record new evidence and invalidate stale claims.
3. **Orient:** recompute the controlling constraint, critical path, and branch value.
4. **Select:** choose the smallest transition with the highest effect on terminal progress or decision-changing information.
5. **Gate:** verify prerequisites, authority, downside, and acceptance evidence.
6. **Execute:** perform or delegate the bounded action when authorized.
7. **Verify:** inspect the artifact or state against acceptance criteria; do not accept self-reported completion alone when direct evidence is practical.
8. **Integrate:** merge the result into the world model, graph, and dependent work.
9. **Decide:** continue, rework, branch, stop, escalate, or replan.

Every cycle should reduce objective distance or materially reduce uncertainty. If it does neither, stop feeding the loop.

## Transition selection

Prioritize a transition by:

- effect on the controlling constraint or terminal acceptance;
- information value if an assumption can flip the plan;
- elapsed time and acquisition lead time;
- reversibility and downside;
- resource and integration cost;
- readiness and authority; and
- option value created for later paths.

Do not maximize the number of concurrent tasks. Maintain WIP that the verification and integration stages can absorb.

## Evidence of completion

Match proof to the claim:

- code: relevant test, build, runtime observation, or diff review;
- data: reproducible query, checks, coverage, and sample evidence;
- decision: authorized record with scope and effective time;
- external state: read-after-write or independent observation when available;
- research: source-backed claim ledger with uncertainty;
- user outcome: behavior or accepted artifact, not internal completion; and
- learning: demonstrated performance on representative tasks, not time spent.

Static inspection, local tests, staging behavior, production behavior, and external acceptance are different states. Name which one was verified.

## Delegation control

Give each person or agent a bounded mission and the minimum sufficient context. Require progress reports only at material events: completion, blocked state, failed assumption, scope risk, or required decision. Avoid constant status chatter that consumes the bottleneck.

For parallel work:

- version inputs;
- isolate mutable environments;
- define interfaces and ownership;
- reserve integration capacity;
- specify acceptance tests before handoff; and
- cancel obsolete branches promptly.

## Failure behavior

On failure:

1. preserve logs, partial artifacts, and exact error state;
2. distinguish transient failure, false assumption, bad execution, and invalid plan;
3. avoid blind retries when the mechanism is unchanged;
4. update confidence and dependent edges;
5. choose the cheapest discriminating next step; and
6. escalate only the decision or resource actually needed.

Repeated failure without new information should trigger a stop or topology change.

## Authority and safety

Internal planning does not authorize external messages, publishing, purchases, private-data movement, account changes, destructive commands, legal commitments, or irreversible actions. Put gates immediately before consequential transitions. Continue safe internal preparation when it preserves momentum, but never portray a pending action as completed.

## Session termination

A planning session should end with one of:

- an executed and verified state change;
- a delegated transition with acceptance and integration contracts;
- a live bounded experiment;
- a precise approval or access request that names the blocked transition;
- a decision to kill or defer work with rationale; or
- an explicit statement that no credible path is currently known, plus the evidence needed to change that conclusion.

It should not end solely with a larger plan when authorized execution or validation was possible.
