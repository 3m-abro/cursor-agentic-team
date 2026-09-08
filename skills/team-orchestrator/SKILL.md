---
name: team-orchestrator
description: Route work through Agentic Team's seven departments and shared roles. Use for team routing, team-status, or named workflows such as dev-qa, dev-collab, design-prototype, and finance-statements on Cursor, Codex or ChatGPT.
---

# Agentic Team orchestrator

1. Read [runtime](../../shared/RUNTIME.md) and select the current host adapter.
2. Read [routing](../../shared/ROUTING.md) and [CEO role](../../shared/agents/ceo-orchestrator.md).
3. Classify intent and state the primary department. Use [team map](../../shared/TEAM.md)
   to select an existing department skill and, when useful, its shared lead role.
4. For a named command, consult [workflow index](../../docs/WORKFLOWS.md), then read
   the corresponding bundled `commands/<name>.md` as a workflow. Only Cursor
   registers those files as slash commands. `team-status` lists the org and current
   capability gaps; do not label every upstream installed without checking.
5. Execute using available host tools. If subagents are unavailable, follow the
   same roles sequentially. Preserve the original task objective and evidence gates.
