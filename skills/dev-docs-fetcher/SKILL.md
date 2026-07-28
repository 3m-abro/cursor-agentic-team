---
name: dev-docs-fetcher
description: >-
  DEV department wrapper for live library/framework docs via Context7.
  Use when needing current API docs, setup, migration, or CLI usage for a
  library. Triggers: docs, Context7, library docs, framework API, SDK docs.
---

# DEV — Docs Fetcher

**Department:** DEV

Thin wrapper around Context7. Prefer MCP over stale training data for library facts.

## Procedure

1. Read and follow:
   `/home/maqsood.a@scicom.msc/.cursor/plugins/cache/cursor-public/context7-plugin/58a36cea87ea887e7bb4850409f1f9ea58dae5e5/skills/context7-mcp/SKILL.md`
2. Use Context7 MCP (`plugin-context7-plugin-context7` or `user-@upstash/context7-mcp`):
   - `resolve-library-id` → `query-docs`
3. Cite retrieved docs in the answer; do not invent API shapes.

## Do not use for

Refactoring business logic, code review, or generic programming concepts with no library-specific API surface.
