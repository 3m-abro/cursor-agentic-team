# Architecture

```text
Cursor manifest → rules/ + agents/ + commands/ ─┐
                                              ├→ shared routing / role instructions
OpenAI manifest → skills/team-orchestrator/ ────┘          ↓
                                                  skills/*/SKILL.md
                                                         ↓
                                       named dependencies + actual host capabilities
```

`skills/` remains the one canonical skill tree. Moving it would risk Cursor
compatibility without improving reuse. Both manifests point there; the new
orchestrator entry is a host-neutral bootstrap, not another department.

| Layer | Ownership |
|---|---|
| `shared/ROUTING.md` | Intent classification, assignment, escalation, parallel patterns |
| `shared/agents/` | CEO and six optional department leads; DEV uses its skill map |
| `shared/TEAM.md` | Org / skill / workflow map |
| `shared/RUNTIME.md` | Dependency and capability contract, unavailable-tool behavior |
| `skills/` | 43 original procedures/wrappers plus routing entry |
| `adapters/cursor/` | Legacy discovery preference, Cursor tool names and destinations |
| `adapters/codex/` | Codex capability mapping and authoring-skill alias |
| `adapters/chatgpt/` | Plugin vs reference-document behavior and local-access boundaries |
| `.cursor-plugin/`, `rules/`, `agents/`, `commands/` | Compatible Cursor discovery surface |
| `.codex-plugin/` | OpenAI manifest referencing the same skills |
| `config/` + `scripts/team.py` | Read-only dependency resolution, safe init and export |
| `templates/` | Consumer instructions and collaboration templates |

Cursor rule and agent adapters load shared files by relative links. They contain
no copied role bodies. Existing command files remain Cursor entry points; the
orchestrator can also interpret their instructions by workflow name. Host-specific
command steps are conditional on the actual host adapter.

The resolver uses declarative JSON, not shell interpolation. It expands `~`, keeps
relative config paths anchored to their config file, and returns an existing path.
It does not load that path into an agent or execute it. The agent must read the
resolved resource through its host tools. Multiple matches within a cache pattern
require a pin. Root order intentionally expresses provider preference.

An installed OpenAI plugin is not an Agents SDK runtime or an MCP server. Shared
role prompts preserve responsibilities; native parallelism depends on the host.
The plain-chat export concatenates source files at build time, with source headings
for lookup. Generated archives/exports are not a second maintained skill source.
