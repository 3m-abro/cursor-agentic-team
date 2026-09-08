---
name: legal-compliance-check
description: >-
  LEGAL compliance check — wraps GDPR data-handling and agent OWASP patterns
  for privacy/security compliance reviews. Not a lawyer.
  Triggers: compliance check, GDPR, privacy review, OWASP agent, data handling.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# LEGAL — Compliance Check

**Department:** LEGAL

Wrap GDPR data-handling + agent-owasp-compliance. Issue-spot only.

## Hard rules

1. **Not a lawyer.** Not legal advice or certification of compliance.
2. **HIGH risk → escalate human counsel / DPO / security owner.**
3. **Never invent jurisdiction-specific law as fact.**

## Upstream

1. GDPR / personal data handling patterns:
   `dependency:gdpr-data-handling`
2. Agent / app security OWASP-oriented checks:
   `dependency:agent-owasp-compliance`

## Procedure

1. Scope: data types, systems, regions (user-stated), processing purposes.
2. Run relevant upstream checklists; map gaps.
3. Separate privacy vs security findings; severity LOW/MED/HIGH.
4. Recommend owners + next evidence to gather.
5. Do not claim "GDPR compliant."

## Output

Gap list + severity + escalation notes.
