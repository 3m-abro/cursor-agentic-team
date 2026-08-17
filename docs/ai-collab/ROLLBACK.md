# Rollback

Safety net for risky or large edits. Keep short.

**Active risk:** low (markdown plugin pack)  
**Updated:** 2026-08-17

## Revert target

- Commit / branch / tag: revert the v1.1.0 collab commit(s) if committed
- Or files to restore: remove `skills/dev-ai-collab/`, `commands/dev-collab.md`, `templates/ai-collab/`, `docs/ai-collab/`; restore prior `AGENTS.md`, CEO files, `plugin.json` to 1.0.0

## After revert — re-check

1. `/team-status` still lists 42 roles / v1.0.0 wording
2. No broken skill path references to `dev-ai-collab`

## Data / migrations

- Forward-only? N/A (docs only). How to undo: git revert / delete paths above.
