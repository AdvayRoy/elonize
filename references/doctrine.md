# Doctrine

This reference defines the architectural invariants shared by all Elonize modules. Use it for system-level work, cross-module conflicts, or audits of an Elonize plan.

## Mission

Elonize turns a changing body of project history into the shortest credible sequence of validated state transitions that makes a terminal outcome true. It does not optimize for a beautiful plan, maximal activity, or adherence to an arbitrary date.

The system has three conceptual engines:

```text
Memory engine       What is or was true, according to what evidence?
Intelligence engine What matters causally, and what controls elapsed time?
Execution engine    What authorized state transition should happen next?
```

They share identifiers and evidence, but they must not collapse into one undifferentiated summary. Memory can retain more than current reasoning needs. Intelligence can model alternatives that are not approved. Execution can act only within authority.

## Core objects

- **Objective:** desired effect, beneficiary, scope, acceptance evidence, horizon, and exclusions.
- **State:** a time-bounded set of claims about the project, each with epistemic status and provenance.
- **Claim:** an atomic proposition that can be supported, contradicted, superseded, inferred, or unknown.
- **Outcome node:** a state that must become true for the objective to be met.
- **Action:** an authorized intervention expected to change one or more state variables.
- **Dependency:** a typed, testable relation; never merely an ordering convention.
- **Constraint:** a limit on feasible states or transitions.
- **Resource:** a capacity, asset, permission, relationship, tool, person, compute budget, or information advantage that can alter a transition.
- **Evidence:** an observation that updates confidence in a claim, edge, or completed state.
- **Plan:** a versioned hypothesis connecting actions to outcomes under explicit assumptions.

## The sufficient-state criterion

An active state is sufficient for a decision when adding more archive material is unlikely to change:

1. the terminal-state definition;
2. the controlling constraint or critical path;
3. the ranking of immediate transitions;
4. a material feasibility or safety judgment; or
5. the authority required for the next action.

This is a decision-relative criterion, not a permanent claim of complete understanding. If coverage is unknown, say so. If a low-probability omitted fact would be catastrophic, retrieve more before acting.

## Compression is topology change

Calendar compression is valid only when a mechanism changes the work graph or its duration distribution. Examples include:

- deleting output that does not contribute to acceptance;
- replacing a supposed prerequisite with a direct proof;
- changing a hard dependency into a soft or conditional one;
- obtaining earlier access or a faster external path;
- isolating interfaces so work can proceed in parallel;
- automating deterministic transformation or verification;
- bringing in expertise that reduces search and rework;
- shortening feedback latency; or
- changing the target while preserving the true objective.

Asking the same system to move faster without changing its mechanism is schedule pressure, not planning.

## Evidence classes

Use these labels consistently:

- **Observed:** directly inspected or measured in the current run, with a source handle.
- **Reported:** asserted by a source or person but not independently verified.
- **Derived:** computed from identified inputs and a reproducible rule.
- **Inferred:** reasoned from evidence, with assumptions exposed.
- **Proposed:** a candidate design, action, estimate, or target.
- **Unknown:** required information not yet established.

Never silently promote reported, inferred, or proposed content to observed fact. Never say all sources were reviewed unless coverage supports that claim.

## Planning priorities

When values conflict, prefer in this order:

1. truth and safety constraints;
2. the actual terminal outcome over its proxies;
3. causal sufficiency over conventional sequence;
4. validated learning and state change over planning volume;
5. elimination and topology changes over brute-force intensity;
6. explicit uncertainty over fake precision;
7. recoverable provenance over elegant but unauditable compression; and
8. reversible probes over consequential bets when evidence is weak.

This order does not imply conservatism. It prevents speed claims from being purchased with hidden risk or fictional certainty.

## Failure conditions

An Elonize plan has failed if it:

- compresses dates without identifying changed elapsed-time causes;
- relies on a decisive claim that cannot be traced or labeled as unknown;
- treats a requested deadline as proof of feasibility;
- converts a cyclic or disputed world state into a clean schedule by omission;
- confuses additional people or agents with usable parallel capacity;
- hides integration, queueing, approval, or feedback latency;
- recommends work that cannot produce acceptance evidence;
- performs or implies authority for consequential actions not granted; or
- remains a plan when an authorized, bounded state transition could be executed.

## System boundary

Elonize is a reasoning and execution-control skill, not a project database, scheduler, or optimizer by itself. Use tools and code when they materially improve retrieval, calculation, graph analysis, or verification. Do not make deterministic software pretend that ambiguous causal judgment has become objective. Conversely, do not use model prose for calculations or transformations that a script can perform more reliably.
