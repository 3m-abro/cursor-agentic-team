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


### 2026-09-08 — Shared workflows with host adapters (v1.2.0)
- **Decision:** Keep the canonical skills directory and original Cursor discovery surface; move role/routing bodies to shared resources and add the OpenAI manifest plus a routing skill.
- **Why:** Avoid skill duplication and preserve existing Cursor names, metadata and relative discovery paths.
- **Dependency resolution:** Named references with platform-specific lookup preferences, explicit overrides and ambiguity errors; never pick a cache revision arbitrarily.
- **Capabilities:** Delegate only when supported; no native-agent claims. Retain existing providers where present; report missing mirrors and required upstreams honestly.
- **Validation:** Standard-library resolver/export/init tests, static reference validation, original Cursor discovery contract checks, and bundled OpenAI validators.
- **Model / version:** Codex (GPT-6; exact deployment version not exposed).
- **External memory:** No external memory write performed in this task; this repository entry is persisted, external mirror unavailable/unverified.
- **Touched:** shared/, adapters/, config/, scripts/, tests/, both manifests, skills, Cursor adapters and documentation.


### 2026-09-08 — Centralize source and retain deployment copies
- **Decision:** One canonical Git checkout, recommended at `~/Projects/cursor-agentic-team`; Cursor remains a deployment at its existing discovery path without a second Git repository.
- **Why:** Shared files must have one edit location while installed hosts retain compatible paths and private runtime state.
- **Preservation:** Archive legacy source/Git metadata, local memory, graph outputs and hook state before replacement. Preserve runtime data in the Cursor deployment. Keep machine-specific paths out of tracked configuration.
- **Migration:** Merge the tested portability changes into main. Ordinary non-force Git synchronization only; no history rewriting.
- **Model / version:** Codex (GPT-6; exact deployment version not exposed).
- **External memory:** Not connected for this task; decision persisted in this repository only.
