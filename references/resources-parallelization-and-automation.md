# Resources, parallelization, and automation

Use this module when people, agents, expertise, access, capital, compute, tools, data, relationships, or authority might alter the plan.

## Resources change graphs, not just capacity

Model a resource by what transition it enables or accelerates, when it becomes available, what it costs to acquire and coordinate, and what new constraint it introduces.

```yaml
resource: security-specialist
capability: produce accepted threat model and resolve review questions
availability: two half-days next week
acquisition_lead_time: 3 days
integration_owner: product-lead
required_inputs: [system-boundary, data-flow, deployment-target]
expected_effect: reduce review rework and queue turns
new_constraints: [limited-calendar, preparation-quality]
proof: reviewer accepts package without major rework
```

Headcount, agent count, or compute volume alone does not establish useful capacity.

## Resource strategy

For each controlling constraint, consider:

- eliminate demand on the resource;
- protect and exploit existing capacity;
- improve input quality to reduce service time and rework;
- reserve capacity earlier;
- substitute another accepted resource or path;
- split work at a stable interface;
- add capacity with onboarding and integration cost included; or
- change the objective or acceptance mechanism.

Estimate the net effect on project elapsed time, not the local task speedup.

## Parallelization test

Parallelize work only when:

1. inputs are available or can be versioned;
2. ownership boundaries are explicit;
3. outputs have stable interfaces or can be integrated cheaply;
4. concurrent work will not consume the same bottleneck unnoticed;
5. acceptance tests are independent enough to run early;
6. shared mutable state is isolated or controlled;
7. integration ownership and timing are explicit; and
8. the value of earlier completion exceeds coordination cost.

Otherwise first decouple the work or keep the coupled region under sequential ownership.

## Parallel portfolio patterns

- **Independent branches:** distinct outputs with no shared mutable surface.
- **Interface-first:** agree on contract and tests, then implement components concurrently.
- **Main path plus probes:** execute the likely path while cheap experiments test alternatives.
- **Red-team parallelism:** one stream builds while another attacks assumptions or validates evidence.
- **Pipeline overlap:** downstream preparation begins on stable partial outputs.
- **Speculative branch:** reversible work starts before a decision, with a strict loss cap.

Avoid parallelism that merely creates more work in progress, duplicate exploration, or a late integration cliff.

## Delegation packet

Every human or agent workstream should receive:

```yaml
mission: <single bounded outcome>
why_now: <relation to bottleneck or learning>
inputs: [<versioned sources>]
allowed_actions: [<authority boundary>]
forbidden_actions: [<explicit exclusions>]
deliverable: <artifact or state transition>
acceptance_evidence: [<tests-observations-review>]
interfaces: [<owners-contracts>]
deadline_or_trigger: <real constraint, not invented urgency>
stop_conditions: [<failure-cost-scope conditions>]
integration_owner: <person-or-agent>
reporting: <compact progress and blocker protocol>
```

Delegation is incomplete until someone owns integration and acceptance. A subtask marked done without usable evidence is untrusted inventory.

## Automation test

Automate when the transformation is repeated, sufficiently specified, observable, and cheaper to verify than to redo manually. Separate:

- deterministic collection, transformation, calculation, checking, and routing;
- judgment under ambiguous objectives or policy;
- consequential action requiring authority; and
- exceptions that need escalation.

Good automation makes inputs, decisions, failures, and fallbacks visible. It does not launder unresolved judgment into code.

Before automating, define:

- decision or transformation contract;
- source and freshness requirements;
- success and failure outputs;
- exception path and human/agent owner;
- idempotency or retry behavior when relevant;
- audit log and provenance;
- rollback or disable mechanism; and
- proof that automation improves the bottleneck rather than a non-controlling task.

## Coordination economics

Account for:

- onboarding and context transfer;
- communication paths and synchronization;
- interface negotiation;
- duplicated exploration;
- environment and data contention;
- code/content merge and conflict resolution;
- review and decision load;
- quality variance; and
- integration testing and rework.

Adding resources late to tightly coupled work can increase elapsed time. Use new capacity on separable preparation, testing, documentation required for acceptance, independent risk reduction, or work that removes load from the bottleneck.

## Work-in-progress control

Set a WIP limit at constrained review and integration stages. Starting more tasks is not progress if completed work cannot be validated or absorbed. Track age of blocked work and stop feeding a queue when the bottleneck is saturated.

## Resource acquisition priority

Rank candidate resources by:

- expected net reduction in terminal elapsed time;
- probability of actually acquiring and integrating the resource;
- acquisition lead time;
- effect on acceptance probability and risk;
- option value and reversibility;
- opportunity cost; and
- whether the resource continues to matter after the bottleneck moves.

Do not request money, people, or tools generically. Tie each ask to a mechanism, transition, and proof.
