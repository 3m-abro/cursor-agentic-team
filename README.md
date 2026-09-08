# Agentic Team

Portable CEO routing and seven departments: **43 department skills** (DEV × 7,
DESIGN / MARKETING / SOCIAL / FINANCE / BIZ / LEGAL × 6), plus one
`team-orchestrator` entry point. Version **1.2.0** keeps the existing
`cursor-agentic-team` plugin identity and Cursor commands.

Skills are thin wrappers or focused procedures. External skills and MCP tools
must be installed/connected separately. This package does not bundle those
providers, create autonomous agents, or grant ChatGPT product access.

## Start here

- [Setup for Cursor, Codex and ChatGPT](docs/SETUP.md)
- [Architecture and capability boundaries](docs/ARCHITECTURE.md)
- [Migration and rollback notes](docs/MIGRATION.md)
- [Maintaining one source repository](docs/MAINTENANCE.md)
- [Workflow / command index](docs/WORKFLOWS.md)
- [Dependency inventory and configuration](docs/DEPENDENCIES.md)
- [Shared team map](shared/TEAM.md)

## Local checks

Python 3.10+; standard library only. From the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
python3 scripts/team.py doctor --platform cursor
python3 scripts/team.py doctor --platform codex
```

`doctor` reports optional upstream availability, not plugin installation status.
Exit 2 means one or more dependencies are missing or ambiguous; inspect the JSON
and resolve only the capabilities needed for your task.

Build a plugin archive or a plain-chat reference (outputs must not already exist):

```sh
python3 scripts/team.py bundle --output dist/cursor-agentic-team.zip
python3 scripts/team.py chatgpt --output dist/chatgpt-team.md
```

The archive carries both host manifests and a single copy of each shared skill.
The Markdown export can be attached as reference material; it is not an installed
plugin and does not include external upstream instructions or tools.

## Compatibility

| Surface | Entry point | Execution |
|---|---|---|
| Cursor | Existing always-on rule, agents and 13 slash commands | Cursor adapter; legacy dependency lookup retained |
| Codex / plugin-capable OpenAI host | `.codex-plugin/plugin.json`, `team-orchestrator` | Shared skills and host tools; sequential roles if no delegation |
| Ordinary ChatGPT conversation | Generated reference Markdown | Instructions and chat output only; capabilities depend on session |

Static validation and filesystem behavior are tested. Interactive host installation,
MCP integration and Cursor command execution require the manual smoke checks in
[setup](docs/SETUP.md). See [validation evidence](docs/ai-collab/TEST_CHECKLIST.md).

## License

MIT for this repository. External skills/providers retain their own licenses and
installation requirements. No external skill bodies are copied into the package.
