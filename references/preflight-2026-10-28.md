# AI Council: local preflight

This record covers the portable 1.0.1 package. The filename follows the original October 28, 2026 work session. Final continuation checks ran on October 29, 2026 after punctuation normalization; exact execution timestamps are saved in UTC in the linked JSON reports.

## Scope

The package check inspects required files, skill metadata and fingerprint, all four template families, execution safeguards, README heading order, agent invocation, local file links, code fences, specified private-data patterns, punctuation, and four synthetic briefings.

The regression script checks acceptance of the four valid briefings and rejection of targeted malformed cases. These include missing decisions or chairs, unsupported execution modes, duplicate mandates, absent adversarial review, invalid budgets, and missing output requirements.

## Results

The final local run passed **18/18 package checks** and **15/15 briefing-validator cases** on Python 3.11.15. The validator cases include four valid briefings and eleven targeted invalid inputs. No model calls were made.

See [the package report](../evals/package-check-results.json) and [the fixture report](../evals/check-fixtures-results.json) for individual checks, counts, timestamps, and the exact checked skill fingerprint. Both commands use Python's standard library and make no model calls.

## Reproduction

```bash
python scripts/check_package.py
python evals/check-fixtures.py
```

Run from the repository root. The commands print reports and return nonzero on failure; they do not overwrite the saved records. Deliberate source edits require a fingerprint update and a new recorded preflight.

## Interpretation

The results establish local package consistency and the behavior of the briefing validator on the included cases. They do not establish model answer quality, independence, confidence calibration, installation discovery, performance, or cost savings. Pattern scans complement human privacy review; they cannot detect every possible sensitive detail.

The next evaluation should follow [the benchmark protocol](benchmark-protocol.md) and compare the current council against a focused reviewer on unseen tasks with predefined scoring.
