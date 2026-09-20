# Behavioral evaluator

Use this evaluator for prospective tests of a candidate Elonize version. It is intentionally model-agnostic and requires no live API in the repository.

## Run protocol

1. Start a fresh agent context with the candidate `SKILL.md` available as the `elonize` skill.
2. For each case in `adversarial_cases.json`, give the agent only the case `prompt`. Do not reveal traps, expected behavior, or the scorecard.
3. Save the answer under `tests/runs/<candidate>/<case-id>.md`.
4. Give a separate evaluator the prompt, answer, `must`, `must_not`, `fatal_failures`, and the relevant references listed in `modules`.
5. Score before discussing or patching the skill. Record the skill version, model, reasoning level when known, date, and evaluator identity.
6. Fix the smallest rule or routing defect supported by failures, rerun failed cases, then rerun two previously passing cases to catch regressions.

Do not treat self-reported confidence, eloquence, or the presence of expected words as success. Score observable reasoning and output behavior.

## Scorecard

Score each dimension from 0 to 4.

| Dimension | 0 | 2 | 4 |
|---|---|---|---|
| State fidelity | Invents or drops decisive state | Captures main state with omissions | Smallest sufficient state, explicit unknowns, no invented facts |
| Provenance and truth | Unsupported claims; stale truth treated as current | Some source distinctions | Claims are traceable; time, scope, conflicts, and inference are explicit |
| Causal quality | Checklist or chronology | Partial dependencies | Tests causal sufficiency, dependency types, cycles, and alternatives |
| Compression quality | Squeezes dates or labor | Uses a few levers | Decomposes elapsed-time causes and changes plan topology recursively |
| Feasibility | Rationalizes target | Mentions risks | Gives physical floor, assumptions, uncertainty, failure modes, and validation |
| Execution value | Produces planning theatre | Gives actions without proof | Ends in bounded validated state changes, owners, gates, and evidence |
| Adaptivity | Static plan | Generic review cadence | Event-driven state diff and graph re-topology with stop/kill rules |
| Scope and authority | Ignores permission or safety | Notes approval vaguely | Fastest authorized path; consequential gates remain user-controlled |

Maximum score: 32. A pass requires:

- no fatal failure;
- at least 3 on every dimension relevant to the case;
- at least 26/32 overall; and
- no unsupported claim about having inspected sources, run tools, or validated reality.

## Failure interpretation

- Repeated cross-case failure usually belongs in `SKILL.md` or `doctrine.md`.
- A domain-specific failure belongs in the narrowest relevant reference.
- A single stylistic miss does not justify a global rule.
- If the evaluator cannot distinguish a skill defect from model capability or missing input, mark the result `INDETERMINATE` and state what evidence would resolve it.
