---
name: dev-qa-engineer
description: >-
  DEV department wrapper for gstack QA — browser verification, dogfooding,
  and QA workflows. Use when testing UI flows, verifying fixes, or running
  QA against a running app. Triggers: QA, test UI, browser verify, gstack-qa,
  dogfood.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# DEV — QA Engineer

**Department:** DEV

Thin wrapper around gstack-qa. No duplicate QA playbook here.

## Procedure

1. Read and follow:
   `dependency:gstack-qa`
2. If routing is unclear, consult gstack router first:
   `dependency:gstack`
3. Execute the gstack-qa workflow (browse / verify / report) as defined upstream.

## Parallel

On ship/verify, CEO may run this in host-supported parallel execution alongside `dev-docs-fetcher` and `dev-memory-keeper`.
