# Cursor adapter

Follow [shared runtime](../../shared/RUNTIME.md). Existing plugin identity,
`skills/`, `agents/`, `rules/` and `commands/` discovery paths are retained.
The always-on `ceo-router` rule loads shared routing; agent files keep their
original names and `model: inherit` and load shared role bodies.

Use `--platform cursor` with the resolver. [dependencies.json](dependencies.json)
retains the old preferred locations and fallback order, with `~` replacing a
personal home directory and `*` replacing mutable cache revisions. A configured
root/override can deliberately supersede those locations. With multiple cache
versions, pin the intended one in local config instead of modifying a skill.

- DEV uses gstack first when installed; use Multitask Mode for supported parallel work.
- Personal skills belong in `~/.cursor/skills/<name>/`; never write to `~/.cursor/skills-cursor/`.
- Context7 legacy MCP names: `plugin-context7-plugin-context7` or `user-@upstash/context7-mcp`.
- claude-mem legacy MCP name: `plugin-claude-mem-mcp-search`; fallbacks remain
  `user-memory` and `user-codebase-memory-mcp`. Discover actual available tools.
- Existing `/dev-collab`, `/dev-qa`, `/team-status` and other commands remain valid.
- Preserve the prior terse/caveman status preference unless the user requests
  another tone. Local workspace-specific re-root shortcuts are not portable APIs.
