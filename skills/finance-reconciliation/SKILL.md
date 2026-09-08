---
name: finance-reconciliation
description: >-
  FINANCE Reconciler — bank, AP/AR, balance-sheet account reconciliations.
  Prefer canvas. Not financial advice.
  Triggers: reconcile, bank rec, AP aging, AR aging, account reconciliation.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# FINANCE — Reconciliation (Reconciler)

**Department:** FINANCE

**NEW** procedure. Prefer canvas for tie-outs and exception lists.

> **Disclaimer:** Not legal or financial advice. Reconciliation drafts for ops review only.

## Inputs

Statement (bank/vendor/customer), GL balance, period, open items export if any.

## Procedure

1. Tie **statement ending** ↔ **GL ending**; compute difference.
2. Tick matched items; list unmatched on both sides.
3. Classify exceptions: timing, error, missing entry, fraud-suspect.
4. Propose clearing JEs via `finance-journal-entry` (do not auto-post).
5. Age open items; highlight >30/60/90.
6. Canvas: summary tie-out + exception table + proposed actions.

## Output

Reconciled? Y/N + difference + exception list with owners/dates.
