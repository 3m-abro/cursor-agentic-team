# Architecture

Big picture only — modules, services, data movement. Not implementation detail.

**Updated:** 2026-08-17

## Shape

```text
User → CEO router (rules/ceo-router.mdc) + ceo-orchestrator
         → DEV / DESIGN / MARKETING / SOCIAL / FINANCE / BIZ / LEGAL
              DEV → gstack router → thin wrapper skills
              DEV continuity → docs/ai-collab/ via dev-ai-collab
              memory dual-write → MCP (claude-mem / user-memory)
```

## Modules / packages

| Name | Responsibility | Owns |
|------|----------------|------|
| `rules/` | Always-on routing | Dept assignment |
| `agents/` | Dept leads + CEO | Role prompts |
| `skills/` | Thin wrappers | Procedures |
| `commands/` | Slash entrypoints | User invokes |
| `templates/` | Consumer copyables | AGENTS + ai-collab |
| `docs/ai-collab/` | Dogfood paper trail | Handover / decisions / gates |

## Data movement

- Intent → dept → skill → (optional) gstack / external skill path
- Decisions → `DECISIONS.md` + memory MCP
- Ship claim → TEST_CHECKLIST evidence check (`dev-ai-collab`)

## External deps that matter

- gstack (`~/.cursor/skills/gstack/`)
- Superpowers, Context7, claude-mem (and fallbacks)

## Links

- Graphify: `graphify-out/`
- Field guide templates: `templates/ai-collab/`
