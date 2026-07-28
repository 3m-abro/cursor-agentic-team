---
name: dev-memory-keeper
description: >-
  DEV department wrapper for searching and persisting agent memory. Use when
  recalling past decisions, storing observations, or querying codebase memory.
  Triggers: memory, remember, mem-search, claude-mem, knowledge graph,
  codebase memory.
---

# DEV — Memory Keeper

**Department:** DEV

Thin wrapper. Prefer claude-mem mem-search; fall back to user-memory + codebase-memory MCP.

## Primary

1. Read and follow (prefer marketplace copy if present):
   `/home/maqsood.a@scicom.msc/.claude/plugins/marketplaces/thedotmack/plugin/skills/mem-search/SKILL.md`
2. Alternate cached copy:
   `/home/maqsood.a@scicom.msc/.cursor/plugins/cache/thedotmack/claude-mem/3651a34e96b82f105377e040d86cf4bfe6939bed/skills/mem-search/SKILL.md`
3. Use `plugin-claude-mem-mcp-search` MCP tools (`search`, `timeline`, `smart_search`, etc.) per that skill.

## Fallback (if claude-mem unavailable)

1. **user-memory** MCP — entities, relations, observations (`search_nodes`, `create_entities`, `add_observations`, `read_graph`).
2. **user-codebase-memory-mcp** — `search_graph`, `search_code`, `get_architecture`, `index_repository` for repo-scoped memory.

## CEO habit

After routing / architecture decisions: write a short observation (decision + why + date). No memory → decision evaporates.
