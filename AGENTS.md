# Agentic Team contributor instructions

Read [shared runtime](shared/RUNTIME.md), [team map](shared/TEAM.md), and
[routing](shared/ROUTING.md). Select the actual host adapter: Cursor uses
`adapters/cursor/RUNTIME.md`; Codex uses `adapters/codex/RUNTIME.md`.

Keep `skills/` canonical. Keep Cursor manifest, agent names, rule name/alwaysApply,
and command names compatible. Keep upstream wrappers thin; do not copy external
skill bodies. No new departments. Preserve filled consumer collaboration docs.

Before edits read `docs/ai-collab/HANDOVER.md` and `CONSTRAINTS.md`.
Run `python3 -m unittest discover -s tests -v` and `python3 scripts/validate.py`.
Update decisions, handover, and test evidence; do not claim a human reviewed the diff.
