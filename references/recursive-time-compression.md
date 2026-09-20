# Recursive time compression

Use this module when the objective is to collapse a conventional timeline or find a materially shorter path.

## Start with elapsed-time causes

A baseline can be decomposed conceptually as:

```text
elapsed time = skilled work + waiting + queues + handoffs + decisions
             + feedback latency + coordination + expected rework + external gates
             - valid overlap
```

Do not sum categories that already overlap. Use the execution graph to determine what is sequential, parallel, conditional, or repeated. Calendar duration is the result of this system, not an input to divide.

## Compression search

For each duration on the critical or near-critical path:

1. **Name the cause.** Why does this consume elapsed time?
2. **Test necessity.** Does the output or dependency causally contribute to acceptance?
3. **Move up one level.** What condition makes this cause necessary?
4. **Generate topology changes.** Can it be deleted, substituted, decoupled, overlapped, precomputed, front-loaded, or converted into a faster evidence path?
5. **Specify the mechanism.** What exactly changes duration or probability?
6. **Price the change.** Include acquisition lead time, coordination, integration, risk, and opportunity cost.
7. **Define proof.** What observation would show the lever worked?
8. **Recompute.** Update the graph; identify the new bottleneck and lost/gained options.
9. **Repeat** while the expected value of another decomposition exceeds its cost.

## Lever order

Search roughly in this order because earlier levers often dominate brute force:

1. delete non-causal scope;
2. redefine the artifact while preserving the true outcome;
3. remove or disprove assumed prerequisites;
4. substitute a faster path, interface, supplier, or proof;
5. decouple and parallelize genuinely independent work;
6. move external requests, access, and long-lead items earlier;
7. automate deterministic work and verification;
8. delegate bounded work to capable people or agents;
9. acquire expertise, relationships, compute, capital, data, or authority;
10. shorten feedback and decision cycles;
11. reduce batch size, handoffs, queues, and rework; and
12. increase sustainable intensity only where it acts on the controlling constraint.

This is a search heuristic, not a moral ranking. If a later lever has clearly better evidence and lower cost, use it.

## Compression claim record

```yaml
lever_id: LEVER-08
baseline_cause: six-week external review queue
proposed_change: reserve review slot before implementation completes
mechanism: overlap readiness work with queue wait
prerequisites: reviewable interface and budget approval
gross_time_change: {low: 14, likely: 28, high: 35, unit: days}
interaction_with: [LEVER-03]
acquisition_lead_time: {likely: 3, unit: days}
new_risks: [scope-freeze-too-early]
evidence: [SRC-review-calendar]
validation: confirmed booking and accepted packet
confidence: medium
```

Use ranges. Distinguish gross local savings from net project savings. If two levers remove the same waiting period, do not add both savings.

## Recursive questions

Useful prompts include:

- Why does this step exist?
- What acceptance condition does it satisfy?
- Who or what requires it, and is that current and in scope?
- Could evidence of the outcome replace evidence of the process?
- Can a partial, simulated, sandboxed, or pilot result unlock the next state truthfully?
- What would make this wait disappear?
- What can begin before certainty, while remaining reversible?
- Which interface would make these tasks independent?
- What expertise would eliminate search or rework rather than merely add hands?
- If the target were impossible, which constraint proves it?

## Feasibility bands

After compression, report at least:

- **physical or institutional floor:** cannot credibly be crossed under known constraints;
- **aggressive feasible:** requires named assumptions and favorable execution;
- **defensible target:** mechanism and resources are credible with explicit risk;
- **high-confidence range:** allows likely variance and rework; and
- **requested target:** retained for comparison, not privileged as truth.

If evidence cannot support numeric ranges, state conditional milestones and the measurements needed to estimate them.

## Stop rules

Stop recursive decomposition when any of these is true:

- the next layer cannot change the selected action;
- expected net savings are smaller than analysis, acquisition, or integration cost;
- uncertainty can be resolved faster by a bounded experiment;
- the remaining duration is irreducible under current authority/resources;
- the plan has reached a safety, legal, biological, physical, or external floor;
- further compression would reduce probability of acceptance below the user's risk tolerance; or
- execution now has higher information value than planning.

Record unresolved assumptions, choose the next validated state change, and act or hand off. Compression without a stop rule becomes sophisticated procrastination.

## Invalid compression patterns

- dividing every date by the target ratio;
- increasing working hours while the bottleneck is external;
- counting parallel starts as parallel completions;
- ignoring onboarding, merge, review, or decision cost;
- renaming scope reduction as full outcome completion;
- using speculative automation to justify a committed date;
- collapsing feedback so far that defects surface only at the end; and
- claiming certainty from a detailed schedule.

The compression factor is an output of changed mechanisms and evidence, not an instruction to the calendar.
