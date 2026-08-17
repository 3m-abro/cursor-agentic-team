# Decisions

Why, not just what. Append only — never rewrite history. Dual-write important ones to memory (`dev-memory-keeper`).

## Entry format

```markdown
### YYYY-MM-DD — short title
- **Decision:** 
- **Why:** 
- **Rejected:** 
- **Model / version:** 
- **Touched:** paths or modules
```

---

### 2026-08-17 — Field guide as DEV skill + templates (hybrid)
- **Decision:** Implement AI Collaboration Field Guide as `dev-ai-collab` + `templates/ai-collab/` → `docs/ai-collab/`, hybrid gates on ship/review only; no new department.
- **Why:** Guide is DEV process discipline; maps onto CEO → DEV → gstack. Soft mid-session avoids 9-file theater on typos; hard gate on ship catches blind "done."
- **Rejected:** 8th department; always-strict every edit; auto-hook Cursor Allow UI (can't).
- **Model / version:** Composer (Cursor Auto)
- **Touched:** `skills/dev-ai-collab/`, `commands/dev-collab.md`, `templates/ai-collab/`, `docs/ai-collab/`, CEO router/orchestrator, AGENTS.md, README, plugin.json
