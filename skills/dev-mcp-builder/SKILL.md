---
name: dev-mcp-builder
description: >-
  DEV department wrapper for designing and building MCP servers. Use when
  creating MCP integrations, exposing tools/APIs to agents, or choosing
  stdio vs remote HTTP vs MCPB. Triggers: build MCP, create MCP server,
  MCP integration, Model Context Protocol.
---

# DEV — MCP Builder

**Department:** DEV

Thin wrapper. Discovery first — do not scaffold until use-case questions are answered.

## Procedure

1. Read and follow:
   `/home/maqsood.a@scicom.msc/.claude/plugins/marketplaces/claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`
2. Follow that skill's interrogation → deployment model → tool-design → handoff flow.
3. For Cursor local plugins that ship MCP config, also respect create-plugin quality gates (relative paths, valid manifest).

## Fallback

If the path above is missing on another machine: use Context7 / official MCP docs and Cursor MCP server templates; still interrogate use case before coding.
