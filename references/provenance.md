# Provenance

Use this module whenever source identity, evidence quality, derivation, freshness, or auditability can alter a decision.

## Principle

Compression may reduce active detail but must preserve recoverability. A claim that controls the plan must either resolve to evidence, resolve to an explicit derivation, or remain labeled unsupported/unknown.

## Provenance record

A useful minimum record is:

```yaml
claim_id: CLM-0042
statement: "The pilot environment supports ten concurrent users."
epistemic_status: observed|reported|derived|inferred|proposed|unknown
source_id: SRC-0017
locator: <path-url-record-id>
span: <page-line-timecode-query-or-record-key>
source_kind: measurement|artifact|message|decision|test|external-reference
source_owner: <known-or-unknown>
observed_at: <when-this-system-accessed-it>
valid_time: <when-the-claim-applies>
content_identity: <hash-version-or-revision-if-available>
scope: <population-system-environment-jurisdiction>
extractor: <human-agent-tool-and-version-if-useful>
confidence: <calibrated-value-or-qualitative-band>
supports: [<claim-or-edge-ids>]
contradicts: [<claim-or-edge-ids>]
```

Not every low-stakes detail needs every field. Do not omit source, valid time, or epistemic status for a claim that controls feasibility or execution.

## Derivation chains

Derived and inferred claims require input links:

```text
source spans -> atomic claims -> derived metric -> graph edge -> decision -> action
```

Record the transformation or reasoning rule. For calculations, keep inputs, units, formula, and code or command when practical. For model inference, state the assumptions and alternative explanations. A polished summary is never its own evidence.

## Evidence strength

Evaluate evidence by relevance, directness, freshness, scope match, independence, measurement quality, and incentives—not by document count or formal appearance. A signed decision can be authoritative about what was decided and still stale about current state. A live measurement can be direct but scoped to the wrong environment.

Use statuses such as:

- `verified`: independently checked in the relevant scope;
- `supported`: credible evidence exists but is not independently complete;
- `reported`: source assertion only;
- `disputed`: material evidence conflicts;
- `stale`: valid once, current applicability unestablished;
- `unsupported`: no recoverable basis found; and
- `unknown`: not enough information to make the claim.

Do not turn these labels into decorative confidence. State what verification occurred.

## Coverage ledger

When working over large histories, report:

```yaml
coverage:
  inventoried_sources: 420
  accessible_sources: 371
  inspected_sources: 68
  deeply_reviewed_sources: 14
  blocked_groups: [legal-archive, old-crm]
  time_cutoff: 2026-09-20T14:00:00Z
  sampling_method: risk-weighted plus source-class sampling
  known_blind_spots: [pre-2024 customer interviews]
```

Never call sampled or partial coverage complete. Record changing access separately from changing truth.

## Summary provenance

Every compressed node should include:

- `derived_from`: lower-level item IDs;
- `coverage`: source set and exclusions;
- `generated_at`: timestamp;
- `method`: human, agent, script, or hybrid;
- `uncertainties`: important unresolved items; and
- `invalidated_by`: events or claims that make the summary stale.

If one summary is derived from another, retain the chain to raw evidence. Limit summary-of-summary depth when it creates semantic drift; periodically compare high-impact summaries to representative sources.

## Citations in operator output

Use compact handles near the claims they support. The operator should be able to inspect the basis without receiving the entire archive. Group low-impact sources in a provenance index, but keep decisive evidence adjacent to the recommendation.

Example:

```text
Current bottleneck: security review queue, not implementation [CLM-0042; SRC-0017 §queue-report].
Uncertainty: the queue estimate is reported by one owner and has not been verified against ticket history.
```

## Failure handling

If a source cannot be opened, a citation is broken, or a derivation cannot be reproduced:

1. downgrade the claim;
2. identify decisions that depend on it;
3. retrieve an alternative source or create a validation task;
4. avoid irreversible action if the claim is controlling; and
5. keep the failed handle so the gap is auditable.

Never replace missing evidence with a plausible story. Never claim a tool, file, database, person, or live system was checked unless it actually was.

## Integrity checks

- Can the recommendation be traced backward to source evidence?
- Are quotation, paraphrase, calculation, and inference distinguishable?
- Are source copies and duplicated claims being mistaken for independent support?
- Do scope and valid time match the planned action?
- Is sensitive provenance exposed only to authorized recipients?
- Would the plan change if the weakest controlling claim failed?

If yes to the last question, make validation of that claim part of the critical path.
