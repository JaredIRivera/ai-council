# AI Council

**A framework for reviewing decisions through distinct analytical roles. It provides complete prompts for independent initial analysis, focused critique, and a final recommendation that preserves meaningful disagreements.**

A council assigns different jobs to an AI assistant: examine the evidence, question the assumptions, identify risks, and synthesize the result. A chair weighs the reasoning and explains which findings support the recommendation. This makes the decision easier to inspect and gives the user specific conditions that would change it.

Several roles can surface different concerns, but they can also repeat the same model errors. Separate initial calls reduce direct exposure to earlier answers; they do not make the models statistically independent. A single conversation can simulate the roles when a lighter review is sufficient.

The project turns that process into a reusable skill with four complete templates, an explicit execution contract, synthetic briefing examples, and local package checks. The workflow connects a practical question to inspectable evidence, a disagreement map, and a next action.

## What you can accomplish

| Your task | What you receive |
|---|---|
| Examine an everyday question | Practical, expert, first-principles, and adversarial perspectives with a concise synthesis |
| Review a research question | Evidence and methodology critiques, unresolved disputes, and the next evidence to seek |
| Make a strategic decision | A recommendation, its tradeoffs, the main risks, and conditions that change the answer |
| Review code or architecture | Findings separated by security, performance, maintainability, architecture, and failure scenarios |

A disagreement map identifies where conclusions diverge and why. Other terms are defined in [the glossary](references/glossary.md).

## Quick start

Use an AI assistant that can read a Markdown skill. Git is needed to clone the repository. Python 3.10 or later is needed only for the local checks; they use the standard library and make no model calls.

```bash
git clone https://github.com/JaredIRivera/ai-council.git
cd ai-council
python scripts/check_package.py
python evals/check-fixtures.py
```

Both commands print JSON reports and return a nonzero exit code if a check fails. They do not install dependencies, send data, or overwrite saved results. Access to the private repository requires an authorized GitHub account.

### Use the skill in your assistant

Keep the folder named `ai-council`, with `SKILL.md`, `agents/`, `references/`, `scripts/`, and `evals/` together. Copy it into the user skills directory supported by your assistant. For hosts using `~/.agents/skills/`, the destination is `~/.agents/skills/ai-council/`. Keep an existing installation in its configured location. Refresh or restart the assistant if needed.

For a lightweight review:

```text
Use $ai-council to review this decision in simulated mode. Use the
decision-making template, one pass, and a concise chair synthesis.
Label missing evidence and preserve disagreements.

Decision: Should our volunteer group replace a shared spreadsheet with
a custom scheduling app?
Context: Six coordinators schedule 30 volunteers each week. The spreadsheet
works, but duplicate edits cause two scheduling corrections per week.
Constraints: No budget for ongoing hosting. One maintainer has two hours
per week. No personal volunteer records may be shared with the assistant.
Evidence: These are synthetic planning facts for this example.
Required output: Recommendation, reasons, disagreements, confidence,
revision conditions, and the next reversible action.
```

For separate initial calls:

```text
Use $ai-council to prepare an isolated decision review. Give each analyst
the same briefing and only their own mandate. Save all initial responses
before sharing them for critique. Use one initial round, one critique round,
and a chair synthesis. Stop after that budget.

Decision and context: [specific decision and facts]
Evidence: [authorized source excerpts and their dates]
Constraints and permissions: [limits, excluded data, authorized tools]
Seats: [distinct mandates, including an adversarial mandate]
Required output: Recommendation, supporting evidence, disagreements,
confidence with reasons, conditions for revision, and next action.
```

The host or caller must provide the separate contexts. If it cannot, switch explicitly to simulated mode rather than claiming independent generation. [The workflow guide](references/council-workflow.md) explains the handoff.

## Working examples

### Decide whether to build a scheduling app

The complete briefing above is a synthetic example. A useful council examines whether the proposed app addresses duplicate edits, whether a smaller process change would work, and whether maintenance fits the stated budget.

**Illustrative chair output, authored as an example**

```text
Recommendation: First try protected editing ranges and a named weekly
coordinator in the current spreadsheet for two weeks.
Reason: The reported problem is editing coordination, while a custom app
adds maintenance work without an ongoing hosting budget.
Disagreement: An app could make permissions and reminders clearer. The
briefing does not establish that these features justify the maintenance.
Confidence: Medium. The correction count is supplied, but its causes and
time cost have not been independently measured.
Change the recommendation if: The process trial leaves material errors,
or a supported platform fits the operating budget and privacy constraints.
Next action: Record correction causes and time spent during the trial.
```

This is a worked explanation, not a recorded model response or a measured operational result. The machine-readable [briefing cases](references/briefing-cases.json) cover all four template families.

### Review a technical design

```text
Use $ai-council in isolated mode to review the attached job-queue design.
Use Security Auditor, Performance Engineer, Maintainability Auditor,
Systems Architect, and Red Team mandates from Template 4.

Context: A single-region internal service processes retryable report jobs.
Evidence: [attach sanitized design, relevant code, tests, and load assumptions]
Constraints: Read-only review. Do not execute commands, contact services,
change code, or deploy. Exclude secrets and production customer records.
Rounds: One isolated initial pass, then synthesis. Review cross-seat claims
only after all initial findings have been saved.
Output: Prioritized candidate findings with locations, supporting code
paths, validation status, and the checks needed to confirm each finding.
Do not infer an exploit or performance measurement that was not shown.
```

Use the [comparison protocol](references/benchmark-protocol.md) when measuring whether a council improves the review relative to one focused reviewer.

## How it works and design choices

The workflow is: **define the question → assign distinct mandates → collect initial views → critique specific claims → synthesize a decision.**

| Choice | Why it matters | What the tradeoff teaches |
|---|---|---|
| Separate initial contexts when independence matters | Analysts do not read earlier seat outputs before their first assessment | More calls require more coordination; shared model biases can remain |
| Assign different analytical jobs | Evidence, practical use, risk, and opposing cases get explicit attention | Adding seats with overlapping mandates can add repetition without useful coverage |
| Require evidence for position changes | The user can see why a critique changed the result | Agreement without a stated reason is not evidence that the issue is resolved |
| Give the chair a synthesis role | The final answer explains which reasoning survived scrutiny | The chair can still misjudge evidence; preserve the record and unresolved disputes |
| Set a budget before execution | The caller can limit seats, rounds, time, and spending | The useful stopping point depends on the task; a fixed round count is a planning choice |

The complete instructions and four templates are in [SKILL.md](SKILL.md). The [specification](SPEC.md) defines inputs, outputs, and safeguards.

## Recorded results

| Check | Recorded observation | What it establishes and what remains open |
|---|---|---|
| [Local package preflight](references/preflight-2026-10-28.md) | Package structure, source fingerprint, template coverage, internal file links, and four briefing fixtures passed | Confirms the packaged files and local contracts; does not measure council answer quality |
| [Validator regression cases](evals/check-fixtures-results.json) | Valid briefings accepted; targeted malformed and incomplete briefings rejected | Confirms the local validator detects the tested input errors; does not enforce model behavior |

The saved [package result](evals/package-check-results.json) records individual checks and the exact skill fingerprint. No model performance, latency, or cost experiment is included in this release. The next comparison should use unseen decisions, fixed scoring criteria, and full workflow cost.

## Running checks and experiments

A preflight checks the package before model use. A benchmark compares outputs under a predefined method.

| Command, from repository root | Requirements and behavior |
|---|---|
| `python scripts/check_package.py` | Python 3.10+, standard library; checks package files, templates, fingerprints, links, and briefing cases; prints JSON |
| `python evals/check-fixtures.py` | Python 3.10+, standard library; exercises valid and deliberately invalid briefing fixtures; prints JSON |

Run both commands after changing the skill or examples. A deliberate skill change requires a new fingerprint in `references/package-manifest.json` and an explanation in the release notes. A matching fingerprint detects content changes; it does not judge reasoning quality. The privacy checks detect specified patterns and complement human review rather than guaranteeing that every sensitive detail is found.

Use [the benchmark protocol](references/benchmark-protocol.md) for model evaluation. Run experiments in a separate checkout, keep the published records intact, and authorize the provider, data handling, and spending before making calls. No API adapter or live model runner is bundled.

## Project status and next decisions

The package provides a portable council workflow and complete prompts. The assistant or application supplies model access, retrieval, isolated contexts, and any external tools. Instructions describe the intended process; the consuming application must enforce permissions, budgets, and execution boundaries.

Simulated roles share one context. Isolated calls avoid direct first-round anchoring but can still share training biases and errors. Confidence labels express judgment, not calibrated probabilities. Agreement among several roles is a reason to inspect the supporting evidence, not proof that the conclusion is correct.

The exported source clarifies those boundaries, replaces unsupported optimum claims with planning heuristics, and removes private vault routing. [Source notes](references/source-notes.md) document the selection and changes. The next evidence milestone is host installation testing and a paired comparison against a single focused reviewer on representative tasks.

Keep secrets, private profile records, and unnecessary personal or client information out of briefings and transcripts. Review the selected model's data handling before sending sensitive material. Technical findings need code or test evidence; external actions remain subject to the caller's authorization.

Maintained by Jared Rivera. Report issues through GitHub; no external support commitment is stated. No license has been selected; contact the owner before reuse or redistribution. See [release notes](RELEASE_NOTES.md) for remaining production checks.

## Glossary

Use [the shared glossary](references/glossary.md) for definitions of seats, mandates, isolated calls, simulated perspectives, disagreement maps, confidence, and preflight checks.
