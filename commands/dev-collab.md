---
name: dev-collab
description: >-
  Init or refresh AI Collaboration field-guide docs (handover, decisions, flow,
  constraints, test checklist, rollback, traces). Invoke DEV skill dev-ai-collab.
---

# Dev Collab

**Dept:** DEV  
**Skill:** `dev-ai-collab`

1. Read and follow `skills/dev-ai-collab/SKILL.md` in this plugin.
2. Subcommands (infer from user text):
   - **init** — copy `templates/ai-collab/` → `docs/ai-collab/` (no silent overwrite of filled files)
   - **status** — list which of the 9 pack files exist + last-updated hints from HANDOVER
   - **handoff** — refresh `HANDOVER.md` five-line ritual for this session
   - **gate** — run ship/review hard-gate checklist; report pass/fail
3. Report concrete paths + next action.
