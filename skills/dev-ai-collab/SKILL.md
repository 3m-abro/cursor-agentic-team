---
name: dev-ai-collab
description: >-
  DEV field-guide continuity: handover, decisions, flow, constraints, test
  checklist, rollback, bug/feature traces. Use for session start/end, handoff,
  ship/review gates, or when user mentions AI collab / field guide / paper trail.
  Triggers: handover, handoff, decisions.md, collab docs, field guide, /dev-collab.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# DEV — AI Collaboration (Field Guide)

**Department:** DEV

Paper trail before / during / after AI edits. Stop blind Allow. Hybrid: soft mid-session, **hard** on ship/review.

Default pack path: `docs/ai-collab/` (override if project AGENTS.md says otherwise).

Templates live at:

[the bundled templates](../../templates/ai-collab/)

## When to skip (YAGNI)

Trivial one-liners / typo fixes: no 9-file theater. Still respect `CONSTRAINTS.md` if present.

## Session start

1. If `docs/ai-collab/` missing → offer init (copy templates) or run `/dev-collab` init.
2. Read `HANDOVER.md` (+ `CONSTRAINTS.md` if exists).
3. Say "Remembering…" from handover; do not re-derive cold.

## Before non-trivial code (habit 11 + 12)

1. Short plan first (why before what). Wait for course-correct if reasoning is bad.
2. One logical change per request. Mega-scope → split or ask.
3. Big / cross-module work → skim `ARCHITECTURE.md` + update `FLOW.md` for the path you will touch.

## During work

1. **Decisions:** append to `DECISIONS.md` when choosing library, pattern, or tradeoff. Include **model / version pin**. Dual-write via `dev-memory-keeper`.
2. **Comments:** intent only — what block is for, callers, assumptions. No restating code.
3. **Flow:** update `FLOW.md` when crossing modules or changing call order.
4. **Bug / feature:** one trace file under `docs/ai-collab/traces/` (copy from BUG/FEATURE templates). Keep start→tried→worked→verified.
5. **Risky edits:** fill `ROLLBACK.md` before large change.

## Session end / handoff (habit 13)

Update `HANDOVER.md` in five lines:

- Done
- Left
- Broken / watch
- Avoid
- Model pin

Optional: gstack `/context-save` as mirror — **repo HANDOVER is source of truth**.

## Ship / review hard gate (hybrid)

Before claiming ready for `/ship`, `/review`, or "LGTM / done shipping":

| Check | Required |
|-------|----------|
| `TEST_CHECKLIST.md` | Last-run section filled with command + pass evidence |
| Architectural / pattern choice | Matching `DECISIONS.md` entry (+ memory dual-write) |
| Risky / large diff | `ROLLBACK.md` filled |
| Human habits | Remind: read real diff; own mental model — do **not** claim human reviewed |

If gate fails → status `BLOCKED` with missing file list. Do not pretend success.

## Init pack

Set `AGENTIC_TEAM_ROOT` to this plugin checkout or installed package root. The helper preserves every existing file, including empty files. Without a shell, copy only missing files with the host file tools.

```bash
python3 "$AGENTIC_TEAM_ROOT/scripts/team.py" init-collab /path/to/project
```

Do not overwrite existing non-empty project files without asking.

## Bridge gstack

| Concern | Owner |
|---------|--------|
| Continuity in repo | this skill + `HANDOVER.md` |
| Optional session mirror | gstack `/context-save` / `/context-restore` |
| QA / review / ship workflows | gstack `/qa` `/review` `/ship` |
| Checklist evidence exists | this skill (gate only) |

## Status line

When finishing collab-aware work, report: files touched under `docs/ai-collab/`, gate pass/fail, handover updated yes/no.
