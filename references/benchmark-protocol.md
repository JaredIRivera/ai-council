# AI Council: benchmark protocol

A benchmark compares processes on the same tasks under a scoring rule chosen before results are seen. This protocol is a plan, not a completed experiment.

## Compare equivalent tasks

| Condition | Definition |
|---|---|
| A: focused reviewer | One clear expert mandate with the same briefing, evidence, tools, and required output |
| B: simulated council | Multiple roles in a shared context, followed by a chair synthesis |
| C: isolated council | Separate initial contexts, a defined critique stage if included, then a chair synthesis |

Use representative everyday, research, decision, and technical tasks only where those families fit the intended use. Reserve unseen cases. Include missing evidence, conflicting sources, ambiguous requirements, and instructions embedded in untrusted input. Use synthetic or authorized sanitized data.

## Hold conditions constant

Record the skill version and fingerprint, provider, exact model, settings, tools, evidence, output requirements, seat mandates, rounds, and budget. If the models or tool access differ between conditions, report those differences as confounders. Separate initial contexts do not establish independent model errors.

Use repeated trials where resources permit. Randomize condition order and blind evaluators to condition labels. Count all analyst, critic, chair, retrieval, retry, and validation work in cost and elapsed time.

## Score quality and safety

Before running, define case-specific expected facts, acceptable decision alternatives, unsupported claims, and material constraint violations. Rate factual grounding, constraint preservation, disagreement quality, synthesis usefulness, and uncertainty handling from 0 to 2 each.

Use machine checks for literal facts and required fields; use independent human review for reasoning and open-ended judgments. For technical tasks, confirm findings against code or targeted tests. Do not award confidence merely because roles agree.

Reject a candidate with a new material authorization or privacy failure, fabricated evidence, or loss of required facts. Define the minimum useful quality gain and acceptable cost/time increase for the workflow before the run. Report failed and inconclusive cases as well as successes.

## Report the result

For each condition, publish case-level outputs and scores, failures, number of calls, tokens when available, elapsed time, actual cost, and missing measurements. Keep simulated and isolated modes separate. Show whether the added review produced a useful new issue or changed an incorrect recommendation.

Describe the sample and its limits. A small synthetic pilot can expose problems; it does not establish broad superiority or production reliability. Preserve results when changing the skill or rubric and run a new comparison rather than rewriting earlier scores.
