---
name: legal-review-contract
description: >-
  LEGAL Contract Reviewer — issue-spot contracts, flag risk, propose questions.
  Not a lawyer. Escalate HIGH risk to human counsel.
  Triggers: contract review, MSA review, agreement review, redline issues.
---

# LEGAL — Review Contract (Contract Reviewer)

**Department:** LEGAL

**NEW** procedure for contract issue-spotting.

## Hard rules

1. **Not a lawyer.** Output is issue-spotting aid, not legal advice.
2. **HIGH risk → escalate human counsel** before signing or relying.
3. **Never invent jurisdiction-specific law as fact.** Cite uncertainty; ask for governing law / counsel.

## Inputs

Contract text/PDF, party role (buyer/seller), deal context, known must-haves.

## Procedure

1. Identify parties, term, governing law (if stated), commercial core (price, scope, SLAs).
2. Issue-spot: liability, indemnity, IP, confidentiality, termination, auto-renew, payment, data, non-compete, assignment.
3. Rate each issue LOW / MED / HIGH with plain-language why.
4. Propose **questions for counsel** and **negotiation asks** (business-friendly language).
5. Do not draft binding opinions; mark speculative interpretations.

## Output

Risk table + counsel questions + suggested ask list. Command: `/legal-review-contract`.
