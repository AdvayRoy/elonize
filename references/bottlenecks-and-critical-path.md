# Bottlenecks and critical path

Use this module to find what controls elapsed time or throughput. The calendar critical path and the system bottleneck are related but not identical.

## Definitions

- **Critical path:** the dependency-constrained sequence whose delay currently delays the terminal milestone.
- **Near-critical path:** a path with too little slack to ignore given estimate uncertainty.
- **Bottleneck:** the capacity or constraint limiting system throughput.
- **Gate:** an event or decision that prevents progress regardless of available work capacity.
- **Queue:** elapsed time accumulated while work waits for constrained service.
- **Constraint migration:** the bottleneck moving after the previous one is relieved.

A long task with slack may not matter. A two-day review behind a six-week queue may control the schedule. A reviewer can be the throughput bottleneck even when another path determines the current launch date.

## Duration model

For each transition estimate ranges, not fictional point values:

```yaml
work_time: {low: 2, likely: 4, high: 8, unit: days}
wait_time: {low: 0, likely: 5, high: 20, unit: days}
queue_time: {low: 1, likely: 7, high: 30, unit: days}
feedback_time: {low: 1, likely: 3, high: 7, unit: days}
rework_probability: 0.35
rework_time: {low: 1, likely: 4, high: 12, unit: days}
resource_calendar: counsel-availability
confidence: low
evidence: [SRC-ticket-history]
```

Use historical distributions when comparable. If evidence is absent, label the estimate proposed and test the highest-impact uncertainty. Do not imply that PERT or simulation repairs poor inputs.

## Critical-path procedure

1. Derive an execution graph with typed dependencies.
2. Add resource calendars, approval windows, queues, and external availability.
3. Estimate duration ranges and rework branches.
4. Compute earliest and latest feasible transitions when the graph supports it.
5. Identify zero/low-slack paths and branch probabilities.
6. Stress the result with high-duration values and changed assumptions.
7. Report the controlling path, near-critical alternatives, and evidence quality.

For small plans, reason explicitly. For larger graphs, use deterministic graph tooling and preserve inputs. If resource contention changes ordering, plain CPM is insufficient; use resource-constrained scheduling or scenario comparison.

## Bottleneck procedure

1. Define the flow unit: decisions, validated features, experiments, applications, cases, or another outcome-relevant unit.
2. Measure arrival rate, service rate, work in progress, queue age, blocking, and rework where possible.
3. Locate where work accumulates or where downstream stages starve.
4. Determine whether the constraint is capacity, policy, batch size, variability, missing information, integration, or authority.
5. Exploit the constraint before adding capacity: protect its time, improve input quality, reduce context switching, and remove work that need not reach it.
6. Subordinate upstream work to prevent excess WIP.
7. Add or redesign capacity only when the mechanism supports it.
8. Re-measure because the constraint may move.

Little's Law (`WIP = throughput × cycle time`) can expose impossible claims when the process is stable enough for it to apply. State those conditions; do not use the equation as decoration.

## Hidden elapsed time

Explicitly inspect:

- external response and procurement latency;
- calendars, time zones, and batch windows;
- decision rights and escalation delay;
- setup, onboarding, and access provisioning;
- integration and review queues;
- feedback collection and analysis;
- context switching and handoffs;
- defect discovery and rework loops;
- resource contention across projects; and
- time spent producing artifacts that do not change acceptance state.

These often dominate skilled work time.

## Constraint-focused interventions

Tie every proposed intervention to the controlling mechanism:

```yaml
intervention: Pre-book two legal review windows
targets: queue_time
mechanism: converts uncertain wait into reserved capacity
prerequisites: draft scope stable enough for review
cost: legal budget and earlier specification freeze
failure_mode: material scope change invalidates review
proof: calendar reservation plus accepted review packet
```

Adding people to a non-bottleneck increases inventory, coordination, and review load without improving throughput. Accelerating one path can also create a new integration bottleneck.

## Reporting

Report:

- current critical path with range and confidence;
- throughput bottleneck and why it differs if applicable;
- near-critical paths and common-mode risks;
- queue, external gate, and resource assumptions;
- interventions ranked by credible elapsed-time reduction per cost/risk; and
- the measurement that will reveal constraint migration.

Never name the longest task as the bottleneck solely because it is long. Never promise a schedule from deterministic arithmetic when inputs are disputed or stochastic.
