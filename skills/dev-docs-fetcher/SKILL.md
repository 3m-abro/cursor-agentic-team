---
name: dev-docs-fetcher
description: >-
  DEV department wrapper for live library/framework docs via Context7.
  Use when needing current API docs, setup, migration, or CLI usage for a
  library. Triggers: docs, Context7, library docs, framework API, SDK docs.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# DEV — Docs Fetcher

**Department:** DEV

Thin wrapper around Context7. Prefer MCP over stale training data for library facts.

## Procedure

1. Read and follow:
   `dependency:context7-mcp`
2. Discover connected Context7 MCP tools by capability (see host adapter for legacy names):
   - `resolve-library-id` → `query-docs`
3. Cite retrieved docs in the answer; do not invent API shapes.

## Do not use for

Refactoring business logic, code review, or generic programming concepts with no library-specific API surface.

## Fallback

If Context7 is unavailable, retrieve official library documentation with the host web tools and cite it. Report that Context7 was not used. If neither is available, stop the documentation-dependent step.
