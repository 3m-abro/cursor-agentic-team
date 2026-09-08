# Migration from v1.1.0

Version 1.2.0 preserves plugin name `cursor-agentic-team`, the 43 department skill
names, seven Cursor agent names/frontmatter, `ceo-router.mdc` with `alwaysApply`,
and all 13 command names. The extra `team-orchestrator` skill provides an explicit
routing entry point for other hosts. Both manifests now report 1.2.0.

## Changed internals

- Personal absolute paths became `dependency:NAME` references in shared content.
- Original provider locations moved into `adapters/cursor/dependencies.json`;
  cache revision segments use wildcards. Multiple installed revisions require an
  explicit local override; the resolver never guesses the active version.
- Shared agent bodies and routing moved into `shared/`. Cursor discovery files
  retain metadata and load these bodies by relative links.
- Root `AGENTS.md` now holds contributor guidance; the reusable team map is in
  `shared/TEAM.md`. Consumer template instructions use the installed routing entry.
- Host-specific filesystem and tool mappings live in adapters. Existing gstack,
  Context7, claude-mem and memory fallbacks remain available when installed.
- Missing external memory now leaves a repository decision record and an explicit
  missing-mirror report. Missing gstack permits ordinary shared DEV work, but not
  a claim of gstack QA execution. Other required missing upstreams stop their step.
- Template initialization uses exclusive creation instead of overwriting copies.
- Former scaffold-host status claims and hash-editing advice were removed from
  current documentation. Dependency availability is checked at runtime.

## Upgrade steps

Review the diff in a separate checkout. Back up any local modifications and keep
local dependency config outside version control. Apply the reviewed migration,
run the tests and validator, then run the appropriate `doctor` command. Configure
only the upstreams you need; see [dependencies](DEPENDENCIES.md). Reload the target
host and run the [manual smoke checks](SETUP.md#manual-host-smoke-checks).

Do not install the OpenAI plugin by copying only `skills/`: wrappers need shared
runtime files and the orchestrator needs routing, role and workflow resources.
Use the entire source folder or the generated package. Likewise, do not move only
Cursor agents/rules without their shared targets.

## Rollback

Keep the pre-migration installation or restore the preceding reviewed revision
through your usual Git workflow. No user data, consumer docs, account settings or
MCP configuration are migrated by this change. Remove an optional new host
installation through its UI if necessary. Do not delete consumer collaboration
records as part of rollback. The isolated working branch is safe to retain.

## Limits

Static packaging is validated, but live Cursor/OpenAI loading is a manual check.
Prompt indirection relies on the host reading linked files. Markdown roles are not
native autonomous agents; delegation is conditional. External providers may change
instructions and tools independently. Cache ambiguity deliberately requires a local
pin. Plain ChatGPT cannot use local dependencies without an appropriate capability.
