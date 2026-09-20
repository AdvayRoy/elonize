# Causal and dependency graphs

Use this module to represent how an outcome becomes true, test whether claimed prerequisites are real, and derive an executable sequence without hiding cycles or uncertainty.

## Graphs answer different questions

Maintain distinct views when useful:

- **World graph:** claims about causal, resource, evidence, and constraint relations. It may contain cycles, conflicts, and alternatives.
- **Outcome graph:** the minimal conditions jointly sufficient for the terminal state.
- **Execution graph:** authorized state transitions that can currently be scheduled. It should be acyclic for the selected planning horizon or explicitly contain a bounded iterative loop.
- **Evidence graph:** observations that validate or falsify nodes and edges.

Do not force the world graph into a DAG simply because scheduling software expects one. First detect cycles, then break, collapse, or bound them to derive an execution graph.

## Node types

- objective or outcome;
- state condition;
- action or experiment;
- artifact;
- decision;
- resource or capacity;
- constraint or external gate;
- assumption or unknown;
- evidence; and
- risk or failure mode.

Each high-impact node should have an identifier, status, acceptance condition, provenance, owner when real, and valid time.

## Edge types

Use typed relations rather than one generic `depends_on`:

- `requires`: target cannot be valid without source;
- `enables`: source increases feasibility but is not strictly necessary;
- `blocks`: source prevents target while active;
- `validates` / `invalidates`: evidence changes confidence in target;
- `produces`: action changes a state or creates an artifact;
- `consumes`: action uses capacity or inventory;
- `substitutes_for`: one path can replace another under conditions;
- `competes_with`: nodes share a constrained resource;
- `amplifies`: source increases rate or impact;
- `feeds_back_to`: outcome changes an upstream variable; and
- `authorized_by`: transition requires a permission or decision.

For scheduling, classify dependencies further:

- **hard:** physically, legally, logically, or contractually required;
- **soft:** preferred order with a stated cost of reversal;
- **assumed:** treated as required but not yet established;
- **coordination:** imposed by ownership, interface, or synchronization;
- **resource:** caused by shared capacity rather than causal necessity;
- **evidence:** action should wait for information because downside exceeds option value; and
- **conventional:** historical sequence with no demonstrated causal need.

## Edge record

```yaml
edge_id: EDGE-031
from: STATE-access-granted
to: ACTION-live-pilot
relation: requires
dependency_class: hard
condition: "Production customer data is used"
evidence: [CLM-contract-clause, CLM-security-policy]
confidence: high
alternatives: [ACTION-synthetic-pilot]
invalidation_events: [policy-change, sandbox-approval]
```

Do not call an edge hard without naming the mechanism. If the mechanism is unknown, mark the edge assumed and test it.

## Build procedure

1. Start from the terminal-state acceptance conditions.
2. Ask what must be true immediately before each condition.
3. Continue backward until nodes are already true, directly controllable, externally gated, or genuinely unknown.
4. Link each relation to evidence or label it as a planning assumption.
5. Add actions that can change false or unknown states.
6. Add resources, decisions, and authority gates that constrain those actions.
7. Search for substitutes, shared constraints, and cycles.
8. Prune nodes that do not causally contribute to acceptance, risk reduction, or necessary learning.
9. Project the selected authorized path into an execution graph.

## Causal sufficiency tests

For every proposed path ask:

- If every node on this path succeeds, does the terminal state actually become true?
- Is any necessary condition missing because it is socially assumed or hard to measure?
- Is a proxy being mistaken for the outcome?
- Is the action expected to cause the state change, or merely correlated with teams that succeed?
- What evidence would falsify the edge?
- Does the relation hold in the actual environment and scope?
- Could a substitute path produce the same acceptance evidence faster?

## Cycle handling

Use strongly connected components conceptually or with graph tooling. For each cycle choose one of these treatments:

- **break:** introduce a substitute, pilot, simulation, escrow, conditional approval, or minimum proof that removes an edge;
- **bootstrap:** define a small initial state that creates enough output to unlock the next round;
- **collapse:** model a tightly coupled iterative loop as one bounded component with exit criteria;
- **buffer:** decouple timing with inventory, interface contracts, or staged data;
- **escalate:** obtain a decision or resource that removes the circular gate; or
- **reject:** declare the path infeasible under current constraints.

Synthetic or simulated evidence must remain labeled. A cycle-breaking proxy is useful only if the downstream gate accepts it.

## Alternative-path analysis

Represent OR branches explicitly. Compare paths by expected elapsed time, probability of satisfying acceptance, resource demand, downside, reversibility, evidence gain, and integration burden. The fastest individual path is not always the best portfolio: a cheap parallel probe can preserve options while the main path proceeds.

## Graph hygiene

- Keep facts separate from graph assumptions.
- Version the graph and record why edges changed.
- Remove an edge only when its mechanism is disproved or made irrelevant; retain history.
- Propagate disputed claims to dependent edges.
- Do not assign dates until dependencies and resource constraints are credible.
- Do not add nodes merely to make a diagram look complete.

The output should usually show only the controlling subgraph, alternative route, and unresolved edges. Preserve the full graph as an inspectable artifact when the project warrants it.
