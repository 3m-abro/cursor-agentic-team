# Validation evidence — 2026-09-08

Model: Codex (GPT-6; exact deployment version not exposed).

| Check | Command / method | Result |
|---|---|---|
| Automated behavior and compatibility | `python3 -m unittest discover -s tests -v` | 12 tests pass |
| References and package structure | `python3 scripts/validate.py` | Pass: 44 skills, manifests, dependencies, adapters, links |
| OpenAI manifest | Bundled plugin-creator `scripts/validate_plugin.py` against repo | Pass |
| All skill metadata | Bundled skill-creator `scripts/quick_validate.py` for each skill | 44 pass |
| Cursor upstream lookup | `python3 scripts/team.py doctor --platform cursor` | 36 resolved, 0 missing on this machine |
| Codex upstream lookup | `python3 scripts/team.py doctor --platform codex` | 23 resolved, 13 missing on this machine (expected exit 2) |
| Whitespace / diff | `git diff --check` | Pass |

Tests cover relocated lookup, legacy Cursor preference, mutable cache versions,
ambiguous caches, relative config paths, missing explicit pins, unknown dependency,
invalid JSON, configured roots, Codex authoring alias, preservation/idempotence of
collab initialization, bundle contents, exclusive output creation, ChatGPT export,
original Cursor manifest/name/frontmatter contract and invalid-link detection.

## Not verified automatically

Live Cursor discovery/command execution, OpenAI installation/skill activation,
external MCP execution and actual native delegation. Run the manual smoke checks
in [setup](../SETUP.md). A resolved path is not an upstream integration test.
Human diff review has not been claimed. External memory mirror was not written.

## Gate

Local implementation and static package validation: PASS.
Live deployment/integration gate: PENDING the target-host manual smoke checks.
