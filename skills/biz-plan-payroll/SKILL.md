---
name: biz-plan-payroll
description: >-
  BIZ NEW skill for payroll planning — headcount cost, schedule, cash impact.
  Not legal/tax/payroll advice.
  Triggers: payroll plan, headcount cost, salary budget, payroll run.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# BIZ — Plan Payroll

**Department:** BIZ

**NEW** procedure for payroll ops planning.

> **Disclaimer:** Not legal, tax, or payroll advice. Planning aid only — confirm with payroll provider / counsel for jurisdiction rules.

## Inputs

Headcount roster (comp, start/end, location if known), pay calendar, benefits/employer burdens if known, cash position.

## Procedure

1. Build gross payroll by period; add known employer costs (mark unknowns).
2. Map pay dates vs cash (`biz-cash-flow-snapshot` handoff).
3. Flag new hires / terminations / bonuses / contractors separately.
4. Checklist: timesheets, approvals, tax filings calendar (placeholders — do not invent local law).
5. Escalate jurisdiction-specific questions to human + LEGAL/tax pro.

## Output

Payroll calendar + cost table + cash-risk notes. Never invent statutory rates as fact.
