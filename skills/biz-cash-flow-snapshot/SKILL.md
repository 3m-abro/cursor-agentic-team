---
name: biz-cash-flow-snapshot
description: >-
  BIZ cash-flow snapshot — runway, burn, inflows/outflows. Seeds from
  startup-financial-modeling when available. Prefer canvas.
  Triggers: cash flow, runway, burn rate, cash snapshot.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# BIZ — Cash Flow Snapshot

**Department:** BIZ

Seed from startup-financial-modeling + thin snapshot procedure.

## Upstream

1. Read and follow (models / unit economics patterns):
   `dependency:startup-financial-modeling`

## Snapshot procedure

1. Collect cash balances + next 4–13 weeks of known inflows/outflows.
2. Compute burn (avg net outflow) and runway (cash / burn) — label assumptions.
3. Separate committed vs soft pipeline cash in.
4. Flag cliff events (payroll, tax, debt, large vendor).
5. Canvas: weekly cash bridge + runway callout + risks.

## Output

One-page cash snapshot. Not a full financial model unless user asks — then lean on upstream skill.
