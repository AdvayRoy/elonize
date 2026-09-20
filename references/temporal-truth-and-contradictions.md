# Temporal truth and contradictions

Use this module when sources disagree, project state changes over time, definitions drift, decisions are superseded, or a plan depends on what is true now rather than what was once documented.

## Model two times

Track at least:

- **Valid time:** when a claim is true in the modeled world.
- **Observation time:** when the system learned or recorded the claim.

A late observation can describe an old event. A newly modified file can contain an obsolete policy. File modification time is not automatically valid time.

Useful optional fields include effective start/end, event time, decision time, publication time, supersession time, and verification time.

## Claim lifecycle

Use explicit states:

- `active`: supported and applicable to the current scope and time;
- `superseded`: replaced by a later valid decision or state;
- `expired`: no longer applicable by rule or time;
- `disputed`: incompatible evidence remains unresolved;
- `stale`: current applicability has not been established;
- `conditional`: true only when named conditions hold;
- `historical`: retained as context but not current state;
- `proposed`: not yet true; and
- `unknown`: evidence cannot establish the state.

Do not delete superseded claims. They explain prior actions and may become relevant if a replacement fails.

## Contradiction taxonomy

Before choosing a winner, classify the apparent conflict:

1. **Temporal change:** both claims were true at different times.
2. **Scope mismatch:** claims concern different teams, environments, populations, or jurisdictions.
3. **Definition drift:** the same label refers to different acceptance conditions.
4. **Granularity mismatch:** a summary says complete while row-level evidence shows exceptions.
5. **Source disagreement:** same time and scope, incompatible reports.
6. **Plan versus reality:** intended or approved state is mistaken for actual state.
7. **Measurement disagreement:** instruments, queries, or samples differ.
8. **Inference conflict:** evidence is shared but interpretations differ.

Resolving the taxonomy often removes the contradiction without discarding either record.

## Resolution procedure

1. Normalize the proposition: exact subject, predicate, scope, and time.
2. Link every supporting and contradicting source.
3. Separate direct observation from report, decision, inference, and proposal.
4. Check independence, measurement method, freshness, and incentives.
5. Look for a supersession relation or changed definition.
6. Resolve only to the strength supported by evidence.
7. If material ambiguity remains, mark the claim disputed and create a decision or validation node.
8. Propagate the uncertainty to dependent graph edges and schedules.

Do not resolve by majority vote, title seniority alone, document formality alone, or newest timestamp alone. Those can be inputs, not universal rules.

## Temporal state table

```yaml
- claim_id: CLM-vendor-required
  statement: "Vendor A is required for production."
  valid_from: 2026-01-08
  valid_to: 2026-09-04
  status: superseded
  superseded_by: CLM-vendor-removed
  evidence: [SRC-architecture-decision]

- claim_id: CLM-vendor-removed
  statement: "Vendor A is not permitted in production."
  valid_from: 2026-09-04
  valid_to: null
  status: active
  evidence: [SRC-incident-decision]
  conflicts: [CLM-undated-onboarding]
```

The example does not establish which source type always wins. It shows how to encode a conclusion once evidence and authority support it.

## Decision history

For material decisions retain:

- decision and alternatives considered;
- owner and authority;
- effective scope and date;
- evidence available at decision time;
- assumptions;
- rationale;
- supersession or rollback conditions; and
- affected claims, graph edges, and actions.

This prevents a later model from treating an old decision as irrational merely because it has new information.

## Planning with unresolved conflict

When resolution is not immediately available:

- branch the plan by truth state;
- identify actions common to all branches;
- prefer reversible work that preserves option value;
- put the cheapest discriminating test on the near critical path;
- avoid committing through the disputed edge; and
- state the owner and deadline for resolution when those are real, not invented.

## Freshness and invalidation

Define freshness by domain. A source is stale when its underlying process can change faster than the evidence is refreshed, not merely because it is old. Tag each high-impact claim with invalidation events such as a deployment, policy change, supplier failure, new test, objective change, or incident.

When an invalidation event occurs:

1. mark dependent claims `stale` or `disputed`;
2. identify affected summaries and graph edges;
3. block claims of current verification;
4. retrieve or measure the new state; and
5. replan only the affected region unless the objective or controlling constraint changes globally.

## Output rule

The active-state view should be concise, but conflicts that can change the plan must be visible. Report the best-supported current state, the basis, remaining contradiction, and what would resolve it. Never use smooth prose to conceal temporal uncertainty.
