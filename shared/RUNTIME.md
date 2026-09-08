# Shared runtime contract

Read this before using any Agentic Team skill or role. The plugin root is the
folder containing this `shared/` folder, `skills/`, and the plugin manifests.
Resolve Markdown links relative to their file. Paths such as `skills/...` in role
and command instructions are relative to the plugin root; `docs/ai-collab/...`
refers to the consumer project. Never assume the current directory is the plugin.

## Host selection

Use the actual host: [Cursor](../adapters/cursor/RUNTIME.md),
[Codex](../adapters/codex/RUNTIME.md), or [ChatGPT](../adapters/chatgpt/RUNTIME.md).
On another host, use the capability rules below without Cursor defaults. Platform
adapters specialize tool names and discovery; they do not override user authority,
project constraints, department responsibilities or verification requirements.

## Named dependencies

`dependency:NAME` is an instruction reference, not a filesystem path or a URI to
open. Resolve it to an installed skill/agent, then read and follow that resource.
The inventory is [config/dependencies.json](../config/dependencies.json).

With a local shell, run (replace ROOT with the actual package path):

```sh
python3 ROOT/scripts/team.py resolve NAME --platform cursor
python3 ROOT/scripts/team.py doctor --platform codex
```

Use your actual platform flag. Lookup order: explicit config override; configured
roots in order; selected adapter's legacy/host paths in order; portable default
skill roots. All personal paths expand against the current user's home directory.
Relative config paths resolve against the config file's directory, not the cwd.
Pass `--config FILE`, set `AGENTIC_TEAM_CONFIG`, or use the ignored
`config/dependencies.local.json`. Overrides are exact files (or skill directories).
The helper only reports paths; it never executes, downloads, or installs anything.

If a cache pattern matches several versions, resolution fails with candidates.
Select the intended version using a local override. Never select an arbitrary hash
or silently fall back from a missing explicit pin. The helper reports JSON and
exits 0 on success, 2 on missing/ambiguous/invalid configuration. `doctor` checks
all optional upstream capabilities, so a nonzero result need not block unrelated work.

Without a shell, use the host skill catalog by name (including its namespace),
or a connected resource the user supplied. Config JSON is a local resolver input,
not an automatically loaded host setting. Never pretend ChatGPT can read a local path.
If needed, ask for the missing upstream resource or connection.

Required upstream unavailable: stop that dependent step and report the dependency.
Optional upstream unavailable: skip it and disclose the gap. Use fallbacks only
where explicitly documented (for example official docs in dev-docs-fetcher and
repository decisions in dev-memory-keeper). Do not invent missing upstream instructions.
These are thin wrappers, not bundled copies of external skills.

## Capabilities and workflow semantics

- Route using [shared routing](ROUTING.md); roles are [shared role instructions](agents/ceo-orchestrator.md).
- Resolve gstack for DEV on hosts where configured. If unavailable, retain the
  department assignment and proceed with the requested shared procedure and host
  development tools; report gstack unavailable. A gstack-specific QA request still
  requires its upstream dependency. This is not a claim of equivalent gstack execution.
- Delegation means use supported subagents only when available and authorized.
  Otherwise execute assigned roles sequentially in the current session. No adapter
  creates autonomous agents merely by loading Markdown.
- MCP names are discovered capabilities, not guaranteed tools. Check connected
  tools before use. Never fabricate retrieval, a memory write, browser QA, or publishing.
- Preserve claude-mem/user-memory/codebase-memory preference when connected. When
  no external memory exists, persist decisions to consumer `docs/ai-collab/DECISIONS.md`
  and report the external mirror unavailable. If file access is absent, return a
  copyable decision/handover and state it is not persisted. Failed external writes:
  retry once and report failure; do not discard the repository record.
- Prefer the host's canvas for relevant deliverables. If unavailable, provide
  Markdown tables or an available file artifact, and disclose the different format.
- Slash names identify workflows; only Cursor registers `commands/`. Other hosts
  can read those files as instructions via team-orchestrator, not native slash tools.
- Consumer files must not be overwritten by initialization. Tests and evidence
  remain required for ship/review claims. Human diff review is never implied.
