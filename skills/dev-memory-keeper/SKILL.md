---
name: dev-memory-keeper
description: >-
  DEV department wrapper for searching and persisting agent memory. Use when
  recalling past decisions, storing observations, or querying codebase memory.
  Triggers: memory, remember, mem-search, claude-mem, knowledge graph,
  codebase memory.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# DEV — Memory Keeper

**Department:** DEV

Thin wrapper. Prefer claude-mem mem-search; fall back to user-memory + codebase-memory MCP.

## Primary

1. Read and follow (prefer marketplace copy if present):
   `dependency:mem-search`
2. Alternate provider locations are handled by the selected adapter.
3. Discover connected claude-mem MCP tools (`search`, `timeline`, `smart_search`, etc.) per that skill.

## Fallback (if claude-mem unavailable)

1. **user-memory** MCP — entities, relations, observations (`search_nodes`, `create_entities`, `add_observations`, `read_graph`).
2. **user-codebase-memory-mcp** — `search_graph`, `search_code`, `get_architecture`, `index_repository` for repo-scoped memory.

## CEO habit

After routing / architecture decisions: write a short observation (decision + why + date). Persist to repository DECISIONS.md even if external memory is unavailable. Report external dual-write as unavailable or failed; never claim it succeeded.
