---
name: elonize
description: Plan and drive complex, long-running objectives across large distributed histories by building a provenance-backed state model, finding the causal critical path, compressing causes of elapsed time, and continuously replanning. Use for multi-stage objectives where dependencies, uncertainty, resources, or changing state matter; do not use for a simple one-step task or ordinary checklist.
metadata:
  version: "0.1.0"
---

# Elonize

Elonize is an execution-planning operating system for objectives whose history is larger than useful active context. Its job is to identify the shortest **credible** path from current state to a validated terminal state, then keep that path current as reality changes.

## Non-negotiable laws

1. **Compress causes of elapsed time, not dates.** A shorter calendar must come from a changed mechanism: deletion, dependency removal, substitution, overlap, better access, automation, delegation, faster feedback, or another explicit lever.
2. **Reason over the smallest sufficient state representation.** Do not equate more context with better reasoning.
3. **Compress information without compressing away provenance.** Every decision-relevant claim must remain recoverable to source evidence or be labeled as inference or unknown.
4. **Treat the requested deadline as a hypothesis.** Report the physical floor, a defensible target, and uncertainty; never rationalize an impossible date.
5. **Optimize validated state change, not planning volume, task count, or suffering.** Human intensity is a late lever, not the default.
6. **Graphs and plans are hypotheses about reality.** Revise them when evidence, constraints, or the objective changes.
7. **Prediction is not authority.** Keep private data, external commitments, money, destructive changes, and consequential actions behind the applicable approval boundary.

## Choose the operating depth

- **Quick pass:** The state is already clear and the user needs the bottleneck, next transition, or a narrow replan. Read only the directly relevant modules.
- **Full build:** The objective is long-running, context is distributed, or the path is disputed. Build the world model and execution graph before compressing it.
- **Refresh:** A prior plan exists and material state changed. Load the prior state, ingest only deltas, invalidate affected claims and edges, then re-topologize.

Do not load every module by default. Load the minimum set needed for the current decision.

## Kernel procedure

### 1. Define the terminal state

Translate the aspiration into observable acceptance conditions, scope, exclusions, time horizon, stakes, and authority boundaries. Separate the true outcome from proxies such as documents, credentials, meetings, or feature count.

### 2. Build or refresh the state model

Inventory sources before deep reading. Extract objectives, present facts, constraints, assets, decisions, attempts, dependencies, risks, unknowns, and evidence handles. Distinguish observed facts, source assertions, model inferences, and proposals. For very large archives, use hierarchical, query-directed compression and delta ingestion.

Read:

- [Context ingestion and compression](references/context-ingestion-and-compression.md) for large, mixed, or distributed histories.
- [Provenance](references/provenance.md) whenever source quality, traceability, or coverage affects the plan.
- [Temporal truth and contradictions](references/temporal-truth-and-contradictions.md) when claims conflict, become stale, or change by time or scope.

### 3. Model how the outcome becomes true

Construct a causal/dependency graph, not a chronological checklist. Mark hard, soft, assumed, coordination, evidence, and resource dependencies. Preserve cycles in the world graph; break or collapse them before deriving an executable graph.

Read [Causal and dependency graphs](references/causal-and-dependency-graphs.md).

### 4. Establish the baseline and controlling constraint

Estimate ranges for work, waiting, queues, handoffs, decisions, feedback, rework, coordination, and external gates. Identify both the calendar critical path and the throughput bottleneck; they can differ. State what evidence supports each estimate.

Read [Bottlenecks and critical path](references/bottlenecks-and-critical-path.md).

### 5. Recursively attack elapsed-time causes

For every controlling duration ask: **Why does this consume elapsed time? What must be true to remove, substitute, overlap, or shorten that cause?** Apply only levers with an explicit mechanism, prerequisites, cost, side effects, and proof test. Recompute the graph after material changes; do not add overlapping savings as if independent.

Read:

- [Recursive time compression](references/recursive-time-compression.md) for the compression search and stop rules.
- [Resources, parallelization, and automation](references/resources-parallelization-and-automation.md) when people, agents, tools, compute, money, expertise, or access may change the topology.

### 6. Try to falsify the plan

Challenge the objective definition, claimed prerequisites, estimates, resource assumptions, external gates, hidden queues, feedback quality, and integration burden. Distinguish demonstrated, defensible, plausible, speculative, and impossible. If decisive evidence is missing, create the cheapest test that can change the plan.

Read [Anti-delusion and feasibility](references/anti-delusion-and-feasibility.md).

### 7. Commit the next transition and control loop

Convert the chosen path into bounded state transitions with owners or agents, inputs, authority, acceptance evidence, integration points, work-in-progress limits, and stop/kill criteria. Every planning session should terminate in a concrete validated state change when authorized, or in a precise handoff/approval request when action cannot proceed.

Read:

- [Execution loop](references/execution-loop.md) for transition contracts, delegation, evidence, and gates.
- [Rolling replanning](references/rolling-replanning.md) for event triggers, state diffs, and graph updates.
- [Output contracts](references/output-contracts.md) for compact, standard, full, and machine-readable deliverables.

## Default output behavior

Return the smallest output that lets the operator act and audit the decision. At minimum expose:

- terminal state and present-state delta;
- current bottleneck and critical path;
- recommended topology changes and why they reduce elapsed time;
- next validated state changes, owners, and acceptance evidence;
- decisive assumptions, unknowns, feasibility range, and replan triggers; and
- compact provenance handles for claims that control the plan.

Do not dump the archive or every intermediate artifact. Offer drill-down paths. Use the full contract only when the user requests a comprehensive plan or the stakes justify it.

## Shared doctrine

Read [Doctrine](references/doctrine.md) when designing, auditing, or materially revising the Elonize system itself, or when a case spans several modules and their priorities conflict.
