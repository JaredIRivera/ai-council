# AI Council: release notes

Technical terms are defined in [the glossary](references/glossary.md).

## 1.0.1: portable council workflow and inspectable checks

Review questions through distinct roles and synthesize a recommendation that preserves useful disagreement.

- Packages all four templates from the available AI Council source: everyday, research, decision-making, and technical review.
- Adds explicit simulated and isolated execution modes, evidence boundaries, resource limits, and permission safeguards.
- Replaces unsupported optimum statements with planning heuristics and separates agreement from justified confidence.
- Removes vault-only routing and metadata from the export while retaining the source installation unchanged.
- Adds setup instructions, complete examples, a specification, workflow guidance, glossary, and source provenance.
- Adds standard-library package and briefing-validation checks with saved results.

Local checks cover package structure and selected briefing errors. Model answer quality, installation discovery, latency, and cost are separate checks for the consuming environment.

## Historical 1.0 source

The available source was a self-contained vault skill with four templates and no executable dependencies. Installed Codex skill and plugin searches found no matching AI Council package. The export uses that source rather than substituting Prompt Hivemind or another multi-agent workflow. See [source notes](references/source-notes.md) for the fingerprint and adaptations.

## Before a production release

- [ ] Test installation and skill discovery in the intended assistant.
- [ ] Confirm separate initial contexts when claiming isolated execution.
- [ ] Choose representative tasks, a baseline reviewer, and scoring rules before model evaluation.
- [ ] Record model, settings, source versions, calls, failures, time, and full workflow cost.
- [ ] Check evidence grounding, disagreement preservation, and technical finding validity on unseen cases.
- [ ] Verify the host's permissions, spending limits, data handling, and external action controls.
- [ ] Select a license and support expectations before wider distribution.

Preserve historical results. Add a regression case when a real failure is confirmed rather than changing the scoring rule after seeing the answer.
