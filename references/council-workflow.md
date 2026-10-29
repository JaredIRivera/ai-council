# AI Council: execution guide

## Prepare the briefing

Record the decision or question, context, supplied evidence and dates, constraints, permissions, required output, and resource budget. Choose one of the four complete templates in [SKILL.md](../SKILL.md). Remove overlapping analyst mandates while retaining an adversarial review and a chair.

The source templates contain cross-seat questions. In isolated mode, those questions belong in the critique stage. An initial call receives only the shared briefing and the seat's own mandate; it cannot truthfully comment on another seat it has not seen.

## Choose execution mode

| Mode | Procedure | Boundary |
|---|---|---|
| Simulated | Ask one assistant to produce the template's roles and synthesis in one context | The perspectives are sequential and can influence one another |
| Isolated | Create a fresh initial context for each analyst, collect all responses, then share the record for critique and synthesis | The host provides isolation; shared training and model assumptions can still correlate answers |

No provider-specific API code is included. Follow the host's current interface and permission model. A role label does not create another model, new context, or tool permission.

## Collect and critique

1. Preserve each initial response with its mandate and evidence references.
2. Give every critic the same complete initial record.
3. Ask for specific supported and unsupported claims, not generic agreement.
4. Require an explanation for any position change.
5. Stop at the declared budget or when no new material evidence or unresolved question appears.

For a one-pass review, omit the critique round and label that choice. Do not describe omitted stages as completed.

## Synthesize and verify

Give the chair the full record. Request a recommendation, evidence, disagreements, confidence with reasons, revision conditions, and next action. The chair should identify missing evidence and distinguish a values tradeoff from a factual dispute.

For code reviews, verify claimed locations and code paths, and label tests as run, not run, or unavailable. Multiple reviewers repeating a concern is not confirmation. Do not execute code, contact services, edit files, send messages, or deploy unless the user has authorized those actions.

## Keep a useful record

Save the exact skill fingerprint, model and settings, mode, seat mandates, source material, round count, outputs, tool use, time, cost, failures, and final decision. Exclude secrets and unnecessary personal data. See [the comparison protocol](benchmark-protocol.md) before making improvement claims.
