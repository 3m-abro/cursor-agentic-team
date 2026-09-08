---
name: legal-signature-request
description: >-
  LEGAL NEW signature request workflow — packet checklist, signer order,
  e-sign hygiene. Not a lawyer. Escalate HIGH risk before send.
  Triggers: signature request, send for signature, e-sign, DocuSign prep.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# LEGAL — Signature Request

**Department:** LEGAL

**NEW** procedure for preparing signature packets.

## Hard rules

1. **Not a lawyer.** Not legal advice; does not authorize signing.
2. **HIGH risk → escalate human counsel** before sending for signature.
3. **Never invent jurisdiction-specific law as fact** (e.g. e-sign validity rules).

## Inputs

Final(ish) docs, parties, signers + roles, deadline, known must-fix issues.

## Procedure

1. Confirm version freeze; list exhibits/schedules attached.
2. Signer matrix: who signs, order, capacity (corp title).
3. Pre-flight: blanks filled, dates, counterparties correct, exhibits complete.
4. If prior review incomplete → run `legal-review-contract` / `legal-triage-nda` first.
5. Draft send message + reminder cadence; note e-sign platform of choice (user's).
6. Stop if HIGH unresolved risks remain.

## Output

Signature checklist + signer order + send email draft. Explicit: human must approve send.
