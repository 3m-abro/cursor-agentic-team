# Test checklist

Proof, not vibes. Fill with real commands and expected signals before calling work "done."

## Smoke (every change)

| Command | Expected |
|---------|----------|
| `test -f skills/dev-ai-collab/SKILL.md` | file exists |
| `test -f commands/dev-collab.md` | file exists |
| `test -f templates/ai-collab/HANDOVER.md` | file exists |
| `test -f docs/ai-collab/HANDOVER.md` | dogfood exists |
| `grep -q '1.1.0' .cursor-plugin/plugin.json` | version bumped |
| `grep -q 'dev-ai-collab' rules/ceo-router.mdc AGENTS.md` | wired |

## Feature / bug under test

| Check | How | Pass signal |
|-------|-----|-------------|
| Template pack complete | list `templates/ai-collab/` | 7 core md + traces + README |
| Skill gate language | read SKILL.md | ship/review hard gate table present |
| Parallel ship | AGENTS.md | includes `dev-ai-collab` in Ship/verify |

## Last run

- **When:** 2026-08-17
- **By (model):** Composer (Cursor Auto)
- **Result:** pass
- **Evidence:** files written; grep targets in skill/router/AGENTS; plugin.json 1.1.0
