# Feature: AI Collaboration field guide in agentic team

**ID / link:** plan ai_collab_field_guide  
**Opened:** 2026-08-17  
**Model / version:** Composer (Cursor Auto)  
**Status:** shipped / verified (smoke)

## Scope

- In: templates, `dev-ai-collab`, `/dev-collab`, CEO wire-up, dogfood `docs/ai-collab/`, v1.1.0
- Out: Cursor Allow hook; 8th department; always-strict on typos

## Plan (why before what)

1. Consumer stubs under `templates/ai-collab/`
2. DEV skill + command with hybrid ship gates
3. Wire CEO / AGENTS / README / team-status
4. Dogfood + version bump

## Decisions (link DECISIONS.md entries)

- 2026-08-17 — Field guide as DEV skill + templates (hybrid)

## Implementation notes

- DEV skill count 6 → 7; org roles 42 → 43

## Verification

- Checklist items run: `docs/ai-collab/TEST_CHECKLIST.md`
- Evidence: smoke shell PASS

## Rollback note

- See `docs/ai-collab/ROLLBACK.md`
