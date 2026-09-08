---
name: biz-margin-analyzer
description: >-
  BIZ NEW / startup metrics skill — gross margin, contribution, unit economics.
  Prefer canvas. Use for pricing and margin diagnostics.
  Triggers: margin analysis, gross margin, contribution margin, unit economics.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# BIZ — Margin Analyzer

**Department:** BIZ

**NEW** procedure (+ startup metrics patterns). Prefer canvas.

## Inputs

Revenue, COGS/variable costs, fixed costs if relevant, units, pricing tiers.

## Procedure

1. Compute gross margin and contribution margin; state formulas used.
2. Segment by product / customer / channel when data exists.
3. Identify margin killers (discounts, returns, support load, COGS creep).
4. Sensitivity: ±price / ±cost impact on margin.
5. Optional: pair with upstream modeling via `biz-cash-flow-snapshot` / startup-financial-modeling path.
6. Canvas: margin table + waterfall + recommendations (ops, not accounting opinion).

## Output

Margins with drivers + 2–3 levers. Label estimates vs book figures.
