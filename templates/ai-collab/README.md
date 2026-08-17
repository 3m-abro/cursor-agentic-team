# AI Collaboration pack

Copy into a project as `docs/ai-collab/`:

```bash
cp -r ~/.cursor/plugins/local/cursor-agentic-team/templates/ai-collab/ /path/to/project/docs/ai-collab/
```

Or run `/dev-collab` init from the Agentic Team plugin.

## Files

| File | Role |
|------|------|
| `HANDOVER.md` | Where things stand |
| `DECISIONS.md` | Why, not just what (+ model pin) |
| `FLOW.md` | Active execution path |
| `ARCHITECTURE.md` | System map |
| `CONSTRAINTS.md` | Never / always / ask first |
| `TEST_CHECKLIST.md` | Commands + expected signals |
| `ROLLBACK.md` | Way back out |
| `traces/` | Per bug / feature start-to-finish |

Enforced by DEV skill `dev-ai-collab` (hybrid: soft mid-session, hard on ship/review).
