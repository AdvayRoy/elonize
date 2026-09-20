# Anti-delusion and feasibility

Use this module before committing a compressed plan, when evidence is weak, when the requested date dominates reasoning, or when failure would be costly.

## Purpose

Aggressive planning becomes delusional when a target is converted into an assumption, uncertainty is hidden by detail, or a shortcut silently changes the outcome. This module tries to falsify the plan while preserving useful ambition.

## Feasibility layers

Separate:

- **demonstrated:** already achieved in sufficiently similar conditions with inspectable evidence;
- **defensible:** mechanism, resources, dependencies, and ranges are supported enough to plan against;
- **plausible:** no known contradiction, but important assumptions remain untested;
- **speculative:** depends on multiple low-evidence or novel assumptions;
- **physically/institutionally blocked:** violates a hard constraint under current conditions; and
- **unknown:** available evidence cannot classify it.

Do not assign numeric probabilities unless there is a basis. Qualitative uncertainty is better than fake precision.

## Falsification pass

Attack the plan in this order:

1. **Outcome integrity:** Does the compressed target satisfy the original acceptance conditions, or did scope quietly change?
2. **Current-state integrity:** Which baseline claims are reported, stale, inferred, or uncovered?
3. **Causal sufficiency:** If every planned action succeeds, does the outcome follow?
4. **Dependency reality:** Which edges are hard, assumed, conventional, disputed, or external?
5. **Duration mechanism:** Does every claimed saving identify an elapsed-time cause and a changed mechanism?
6. **Resource reality:** Are capacity, acquisition lead time, authority, onboarding, and integration included?
7. **Feedback validity:** Will evidence arrive early enough and measure the real outcome?
8. **Common-mode failure:** Can one event invalidate several supposedly independent paths?
9. **Operational safety:** Does the fastest route violate privacy, law, contracts, security, health, or user authority?
10. **Execution transition:** Is there a bounded next action that improves reality or information, rather than another planning artifact?

## Deadline test

Treat a requested deadline as a candidate constraint, not evidence of feasibility.

Report:

```yaml
requested_target: 6 months
known_floor: <range-or-unknown>
aggressive_feasible: <range-or-conditions>
defensible_target: <range-or-conditions>
high_confidence_range: <range-or-unknown>
controlling_assumptions: [<ids>]
target_breakers: [<events>]
evidence_to_narrow_range: [<tests>]
```

If a legal, biological, physical, contractual, or external gate has an irreducible duration, show it. If the floor is unknown, name the source or experiment required instead of inventing a number.

## Assumption register

Track assumptions that can change path selection:

```yaml
assumption_id: ASM-014
statement: "The partner accepts sandbox usage as pilot evidence."
importance: critical
evidence_status: reported
confidence: low
if_false: live-pilot path blocked
test: obtain written acceptance criteria
test_cost: low
test_lead_time: 2-5 days
owner: partnership-lead
```

Prioritize assumptions by impact, uncertainty, and cost/latency to test. Test cheap plan-flipping assumptions early.

## Pre-mortem and reference classes

Ask: if the plan failed, what was the earliest observable reason? Look for historical or external reference classes only when scope is comparable and sources are current enough. Adjust for base rates without treating them as destiny. Novelty increases uncertainty; it does not automatically prove impossibility or justify optimism.

Useful failure categories:

- demand or objective invalid;
- missing permission or stakeholder commitment;
- external queue or supplier failure;
- integration and quality collapse;
- feedback arrives too late or measures a proxy;
- resource cannot be acquired in time;
- compressed scope fails acceptance;
- coordination exceeds predicted savings;
- policy, security, or legal blocker; and
- operator bandwidth or competing priorities.

## Counterfactual checks

- If the proposed resource disappeared, what path remains?
- If the best duration estimate doubled, which milestone breaks first?
- If the key claim is false, what action would now be wasteful or harmful?
- If the deadline moved later, would the recommended topology still be good?
- If the plan had to produce evidence in 48 hours, what would be tested?
- What evidence would cause the system to abandon this plan?

## Anti-rationalization rules

- A detailed plan is not evidence.
- A prominent or repeated source is not necessarily current or independent.
- A simulation is not live proof unless the acceptance gate says it is.
- Starting parallel work does not mean the work can integrate in parallel.
- An AI agent's confidence is not calibration.
- Missing data does not justify using the desired target as the estimate.
- Scope deletion must be explicit; do not relabel a partial outcome as complete.
- Intensity cannot remove external latency, physics, or unavailable authority.

## Decision rule

Accept an aggressive plan when its mechanism is explicit, decisive assumptions have evidence or near-term tests, downside is controlled, and the next transitions produce acceptance evidence or high-value learning. Otherwise branch, probe, reduce commitment, change the target, or report that the requested target is not currently defensible.

The output should be direct: what is supported, what is merely possible, what is blocked, what would change the judgment, and what to do next.
