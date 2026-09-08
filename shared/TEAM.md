# AGENTS.md — Agentic Team

CEO routes. Departments execute. Never code without a department assignment.

## Department routing

| Dept | Mission | When |
|------|---------|------|
| DEV | Build, fix, ship, test, docs, skills, MCP, memory, AI collab paper trail | Code, bugs, PRs, QA, CI, APIs, skills, handover |
| DESIGN | UI/UX, visual systems | Layout, brand, mockups, frontend taste |
| MARKETING | Positioning, copy, growth | Landing copy, campaigns, SEO, funnel |
| SOCIAL | Social / community | Posts, threads, reels, profiles, hooks |
| FINANCE | Books / statements / close | P&L, JE, recs, variance, audit, close |
| BIZ | Ops / cash / GTM | Runway, collections, payroll/tax prep, margins, campaigns |
| LEGAL | Risk / compliance | Contracts, NDAs, GDPR/OWASP checks, vendors, signatures |

**Ambiguous?** Ask one clarifying question, then assign primary dept.

## DEV skill map (Phase 1 — cursor-agentic-team plugin)

| Skill | Points at |
|-------|-----------|
| `dev-superpowers` | Superpowers `using-superpowers` + `writing-skills` |
| `dev-docs-fetcher` | Context7 skill + Context7 MCP |
| `dev-mcp-builder` | Claude `build-mcp-server` |
| `dev-skill-creator` | Host `create-skill` + Superpowers `writing-skills` |
| `dev-qa-engineer` | `gstack-qa` |
| `dev-memory-keeper` | claude-mem `mem-search` (fallback: user-memory + codebase-memory MCP) |
| `dev-ai-collab` | Field-guide pack: handover / decisions / flow / constraints / test / rollback / traces |

DEV work: follow gstack router first (`dependency:gstack`), then the matching wrapper.

## AI Collaboration (field guide)

Repo pack (default): `docs/ai-collab/` — copy from `templates/ai-collab/` or `/dev-collab` init.

| Habit layer | Skill / rule |
|-------------|--------------|
| Continuity + ship gate | `dev-ai-collab` |
| Memory dual-write | `dev-memory-keeper` + `DECISIONS.md` |
| Plan before code / small asks | CEO + DEV |
| Read diff / own mental model | Human — agents remind, never fake |

Ship/verify parallel: `dev-qa-engineer` + `dev-docs-fetcher` + `dev-memory-keeper` + `dev-ai-collab`.

## DESIGN skill map (Phase 2)

| Skill | Points at |
|-------|-----------|
| `design-ui-ux-pro-max` | `dependency:ui-ux-pro-max` |
| `design-taste` | `dependency:taste-design` (provider fallback handled by the adapter) |
| `design-frontend` | `dependency:frontend-design` |
| `design-transitions` | GSAP `gsap-scrolltrigger` + `gsap-core` (+ ui-ux-pro-max motion taste) |
| `design-web-artifacts` | `dependency:canvas` + Stitch skills |
| `design-brand` | `dependency:brand` |

## MARKETING skill map (Phase 2)

| Skill | Points at |
|-------|-----------|
| `marketing-copywriting` | `dependency:copywriting` |
| `marketing-ai-seo` | seo-audit + schema-markup + content-strategy |
| `marketing-cro` | `dependency:page-cro` |
| `marketing-ad-creative` | banner-design + ogilvy |
| `marketing-customer-research` | NEW thin procedure (content-strategy + optional startup-analyst role) |
| `marketing-lead-magnets` | NEW thin lead-magnet procedure |

## SOCIAL skill map (Phase 3)

| Skill | Points at |
|-------|-----------|
| `social-post-writer` | hermes-tweet + NEW LinkedIn/posts procedure (+ optional social-publishing) |
| `social-profile-optimizer` | NEW |
| `social-reels-scripting` | NEW |
| `social-hook-generator` | boost-prompt + enhance-prompt + social hooks procedure |
| `social-voice-builder` | `dependency:brand` (voice) |
| `social-youtube-thumbnail` | banner-design + nano-banana-pro-openrouter |

## FINANCE skill map (Phase 3)

| Skill | Role |
|-------|------|
| `finance-financial-statements` | Statement Builder (NEW; canvas; not financial advice) |
| `finance-journal-entry` | Journal Keeper (NEW) |
| `finance-reconciliation` | Reconciler (NEW) |
| `finance-variance-analysis` | Variance Analyst (NEW) |
| `finance-audit-support` | Auditor prep (NEW) |
| `finance-close-management` | The Closer (NEW) |

## BIZ skill map (Phase 3)

| Skill | Points at |
|-------|-----------|
| `biz-cash-flow-snapshot` | startup-financial-modeling + snapshot procedure |
| `biz-invoice-chase` | NEW |
| `biz-plan-payroll` | NEW (not payroll/tax advice) |
| `biz-margin-analyzer` | NEW / startup metrics |
| `biz-tax-prep` | NEW (not tax advice) |
| `biz-run-campaign` | content-marketing agent + content-strategy |

## LEGAL skill map (Phase 3)

| Skill | Points at |
|-------|-----------|
| `legal-review-contract` | NEW Contract Reviewer |
| `legal-triage-nda` | NEW NDA Triage |
| `legal-compliance-check` | gdpr-data-handling + agent-owasp-compliance |
| `legal-risk-assessment` | NEW |
| `legal-vendor-check` | NEW |
| `legal-signature-request` | NEW |

LEGAL hard rules: not a lawyer; HIGH risk → human counsel; never invent jurisdiction-specific law as fact.

## Parallel patterns (host-supported parallel execution)

| Scenario | Parallel tracks |
|----------|-----------------|
| Ship / verify | `dev-qa-engineer` + `dev-docs-fetcher` + `dev-memory-keeper` + `dev-ai-collab` |
| Skill forge | `dev-superpowers` then `dev-skill-creator` (sequential) |
| MCP build | `dev-mcp-builder` (+ `dev-docs-fetcher` for MCP/SDK docs) |
| Landing | `design-frontend` + `marketing-copywriting` + `marketing-cro` |
| Brand campaign | `design-brand` + `marketing-ad-creative` + `marketing-copywriting` |
| SEO content | `marketing-ai-seo` + `marketing-copywriting` (+ `marketing-customer-research`) |
| Social push | `social-post-writer` + `social-hook-generator` + `social-voice-builder` |
| Close week | `finance-close-management` + `finance-reconciliation` + `finance-variance-analysis` |

## Escalation

1. Missing tool/MCP access → stop the dependent step, report what is blocked; use only a documented fallback.
2. Cross-dept conflict → CEO names primary; secondary gets handoff note only.
3. LEGAL HIGH risk → human counsel before sign/rely.
4. Memory write failed → retry once; if still fail, surface in status (external decision mirror not persisted).
5. Ship/review without TEST_CHECKLIST evidence → `dev-ai-collab` gate BLOCKED (no fake "done").

## Commands

- `/team-status` — full org map (7 depts)
- `/dev-qa` — QA wrapper
- `/dev-docs` — Context7 docs
- `/dev-skill-forge` — superpowers + skill creator
- `/dev-collab` — AI collab pack init / handoff / ship gate
- `/design-prototype` — frontend + taste (+ ui-ux-pro-max)
- `/design-brand` — brand identity
- `/marketing-copy` — copywriting
- `/marketing-cro` — page CRO
- `/social-post` — social post writer
- `/finance-statements` — Statement Builder
- `/biz-cash-flow` — cash snapshot
- `/legal-review-contract` — Contract Reviewer
