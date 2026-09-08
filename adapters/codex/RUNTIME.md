# Codex adapter

Follow [shared runtime](../../shared/RUNTIME.md). The `.codex-plugin/plugin.json`
manifest points to the same `skills/` as Cursor. Invoke `team-orchestrator` (using
the installed namespace if required) to load shared routing and role instructions.
No Cursor rule, slash command, or native agent registration is implied.

Use `--platform codex` for local resolution. `create-skill` maps to the installed
Codex `skill-creator` where available. Personal portable skills conventionally live
under `~/.agents/skills/`; do not modify managed `.system` skills. Use the host's
skill installation mechanism and supported discovery locations for your version.

Read `shared/agents/<role>.md` for role behavior. Use supported delegation tools
only when available and authorized; otherwise execute sequentially. Discover MCP,
web, file, browser and memory tools from the current session. No API key or MCP
server is included or required to read the instruction package.

For project-wide routing, merge `templates/AGENTS.md` into the consumer's existing
instructions. Do not overwrite them. Installing a skill does not make it an
always-on rule; explicit invocation is the reliable entry point.
