# Agentic Team (cursor-agentic-team)

CEO + 7 departments (**43 roles**: DEV×7 + 6×6). **Phase 3 complete — v1.1.0** (AI collab field guide).

## Install

Auto-loads from:

```text
~/.cursor/plugins/local/cursor-agentic-team/
```

No marketplace install step. Reload Cursor / reopen agent if skills don't show immediately.

Optional: copy project template:

```bash
cp ~/.cursor/plugins/local/cursor-agentic-team/templates/AGENTS.md /path/to/project/AGENTS.md
```

Optional: AI Collaboration pack (field guide docs):

```bash
cp -r ~/.cursor/plugins/local/cursor-agentic-team/templates/ai-collab/ /path/to/project/docs/ai-collab/
```

Or `/dev-collab` init inside a project.

## Org chart

```text
                    CEO (ceo-orchestrator + ceo-router)
    ┌───────┬─────────┬──────────┬─────────┬──────┬───────┐
   DEV   DESIGN   MARKETING   SOCIAL   FINANCE  BIZ   LEGAL
   ×7      ×6        ×6         ×6       ×6     ×6     ×6
```

## Phase status

| Phase | Scope | Status |
|-------|-------|--------|
| 1 | CEO + DEV (7 skills; +`dev-ai-collab` in 1.1.0) | Done |
| 2 | DESIGN + MARKETING (6 + 6) | Done |
| 3 | SOCIAL + FINANCE + BIZ + LEGAL (24) | Done (`1.0.0`) |
| 1.1 | AI Collaboration field-guide pack + hybrid ship gates | Done (`1.1.0`) |

## Components

| Component | What |
|-----------|------|
| Rule | `rules/ceo-router.mdc` (alwaysApply) |
| Agents | CEO + DESIGN/MARKETING/SOCIAL/FINANCE/BIZ/LEGAL leads |
| Skills | 43 thin wrappers / NEW procedures |
| Commands | team-status, DEV quartet (+ collab), design×2, marketing×2, social-post, finance-statements, biz-cash-flow, legal-review-contract |
| Template | `templates/AGENTS.md` + `templates/ai-collab/` |

## Wrapper → target (verified on scaffold host)

All wrappers are **thin markdown** (not symlinks).

### DEV (Phase 1)

| Wrapper | Target(s) | Status |
|---------|-----------|--------|
| `dev-superpowers` | Superpowers `using-superpowers` + `writing-skills` | OK |
| `dev-docs-fetcher` | Context7 skill + Context7 MCP | OK |
| `dev-mcp-builder` | Claude `build-mcp-server` | OK |
| `dev-skill-creator` | Cursor `create-skill` + Superpowers `writing-skills` | OK |
| `dev-qa-engineer` | `gstack-qa` (+ gstack router) | OK |
| `dev-memory-keeper` | claude-mem `mem-search` | OK |
| `dev-ai-collab` | Field-guide pack + hybrid ship/review gates (NEW) | OK |

### DESIGN (Phase 2)

| Wrapper | Target(s) | Status |
|---------|-----------|--------|
| `design-ui-ux-pro-max` | `~/.cursor/skills/ui-ux-pro-max/` | OK |
| `design-taste` | `~/.agents/skills/taste-design/` (+ claude fallback) | OK |
| `design-frontend` | `~/.claude/skills/frontend-design/` | OK |
| `design-transitions` | GSAP `gsap-scrolltrigger` + `gsap-core` (+ ui-ux-pro-max) | OK (cache hash) |
| `design-web-artifacts` | canvas + Stitch skills | OK |
| `design-brand` | `~/.claude/skills/brand/` | OK |

### MARKETING (Phase 2)

| Wrapper | Target(s) | Status |
|---------|-----------|--------|
| `marketing-copywriting` | `~/.claude/skills/copywriting/` | OK |
| `marketing-ai-seo` | seo-audit + schema-markup + content-strategy | OK |
| `marketing-cro` | `~/.claude/skills/page-cro/` | OK |
| `marketing-ad-creative` | banner-design + ogilvy | OK |
| `marketing-customer-research` | NEW procedure; content-strategy + optional Task `startup-analyst` | OK |
| `marketing-lead-magnets` | NEW thin procedure | OK (new) |

### SOCIAL (Phase 3)

| Wrapper | Target(s) | Status |
|---------|-----------|--------|
| `social-post-writer` | hermes-tweet + NEW LinkedIn/posts (+ optional social-publishing) | OK wrap + NEW |
| `social-profile-optimizer` | NEW | OK (new) |
| `social-reels-scripting` | NEW | OK (new) |
| `social-hook-generator` | boost-prompt + enhance-prompt + hooks procedure | OK wrap |
| `social-voice-builder` | `~/.claude/skills/brand/` (no voice-framework skill) | OK wrap |
| `social-youtube-thumbnail` | banner-design + nano-banana-pro-openrouter | OK wrap |

### FINANCE (Phase 3)

| Wrapper | Target(s) | Status |
|---------|-----------|--------|
| `finance-*` (6) | NEW procedures; canvas preferred; not financial advice | OK (new) |

### BIZ (Phase 3)

| Wrapper | Target(s) | Status |
|---------|-----------|--------|
| `biz-cash-flow-snapshot` | startup-financial-modeling + snapshot | OK wrap |
| `biz-invoice-chase` | NEW | OK (new) |
| `biz-plan-payroll` | NEW (+ disclaimer) | OK (new) |
| `biz-margin-analyzer` | NEW | OK (new) |
| `biz-tax-prep` | NEW (+ disclaimer) | OK (new) |
| `biz-run-campaign` | content-marketing agent + content-strategy | OK wrap |

### LEGAL (Phase 3)

| Wrapper | Target(s) | Status |
|---------|-----------|--------|
| `legal-review-contract` | NEW | OK (new) |
| `legal-triage-nda` | NEW | OK (new) |
| `legal-compliance-check` | gdpr-data-handling + agent-owasp-compliance | OK wrap |
| `legal-risk-assessment` | NEW | OK (new) |
| `legal-vendor-check` | NEW | OK (new) |
| `legal-signature-request` | NEW | OK (new) |

**Not found on host (documented):** dedicated LinkedIn-post skill, voice-framework skill, content-marketing `SKILL.md` (agent pack only).

**Memory fallback:** if claude-mem MCP missing → `user-memory` + `user-codebase-memory-mcp`.

**Cache path caveat:** marketplace / Superpowers / Context7 / GSAP / claude-mem hashes under `~/.cursor/plugins/cache/` or marketplaces can change. If a wrapper 404s, re-resolve with `find` and update the absolute path in that `SKILL.md`.

## Commands

| Command | Invokes |
|---------|---------|
| `team-status` | Full 7-dept map |
| `dev-qa` | `dev-qa-engineer` |
| `dev-docs` | `dev-docs-fetcher` |
| `dev-skill-forge` | `dev-superpowers` + `dev-skill-creator` |
| `dev-collab` | `dev-ai-collab` (init / handoff / ship gate) |
| `design-prototype` | `design-frontend` + `design-taste` (+ ui-ux-pro-max) |
| `design-brand` | `design-brand` |
| `marketing-copy` | `marketing-copywriting` |
| `marketing-cro` | `marketing-cro` |
| `social-post` | `social-post-writer` |
| `finance-statements` | `finance-financial-statements` |
| `biz-cash-flow` | `biz-cash-flow-snapshot` |
| `legal-review-contract` | `legal-review-contract` |

## Symlinked vs wrapped

- **Wrapped / NEW:** all 43 skills — explicit "Read and follow" or focused procedure.
- **Symlinks:** none.

## License

MIT
