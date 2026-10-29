# AI Council: source notes

## Source selection

The requested source order was installed Codex skills or plugins first, then the vault skills index. Bounded filename and skill/plugin title searches found no installed AI Council package. The skills index identified a self-contained `ai-council.md` source, version 1.0, which was selected. This is distinct from Prompt Hivemind and the AI Loop Skill.

Source SHA-256: `023fd689a8c3f1fe2e3936a4a046bdfc87d1fcf2bbd431cbad95394849399751`.

No private absolute source path, profile record, client content, or vault index is included. The original source remains unchanged. No supporting files were referenced beyond the removed vault navigation link.

## Export adaptations

- Retained all four complete templates, role reference, failure modes, evaluation criteria, and usage notes.
- Removed the vault's `type`, `status`, and `dependencies` metadata and parent-index wiki link. The dependencies are documented in the README and specification.
- Preserved the `ai-council` name and source author metadata; incremented the export version to 1.0.1.
- Added execution boundaries for simulated versus isolated calls, source handling, authorization, privacy, budgets, and validation.
- Replaced unsupported claims of optimal seat or round counts with explicit planning heuristics.
- Replaced automatic high confidence from convergence with evidence-based confidence, and clarified technical findings as candidates until supported by code or tests.
- Replaced em dash punctuation with colons for consistent presentation.
- Added repository documentation, examples, agent metadata, standard-library checks, and saved local results. These are package additions, not recovered source artifacts.

## Formatting reference

The requested `JaredIRivera/prompt-optimizer` URL returned 404 during reference inspection. The current matching project was accessible as [Prompt & Cache-Readiness Optimizer](https://github.com/JaredIRivera/prompt-and-cache-readiness-optimizer). Its README, file tree, specification, release notes, benchmark protocol, and preflight documentation supplied the presentation reference.

This export follows that README's H2 order and root conventions: `SKILL.md`, `README.md`, `SPEC.md`, `RELEASE_NOTES.md`, `agents/`, `references/`, `scripts/`, and `evals/`. It adapts the experiments and supporting filenames to council work. No reference experiment results or model-performance claims were copied.

## Evidence limits

The local checks verify files and example contracts. They do not measure the effect of a council on decision quality, prove independent reasoning, or verify installation in a host. The source's qualitative seat and round guidance remains task-dependent. The package includes a protocol for measuring those questions.
