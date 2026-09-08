---
name: biz-run-campaign
description: >-
  BIZ campaign runner — wraps content-marketing agent patterns plus
  content-strategy. Use for GTM / content / launch campaign plans.
  Triggers: run campaign, GTM campaign, content campaign, launch plan.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# BIZ — Run Campaign

**Department:** BIZ

Wrap content-marketing (agent pack; no SKILL.md on host) + content-strategy.

## Upstream

1. Content marketer agent (read and follow patterns):
   `dependency:content-marketer`
2. Content strategy skill:
   `dependency:content-strategy`

## Campaign procedure

1. Goal + KPI (one primary).
2. Audience / offer / proof — pull MARKETING (`marketing-customer-research`, `marketing-copywriting`) as needed.
3. Channel mix + calendar (owned / social / paid / email).
4. Asset list + owners; SOCIAL for posts (`social-post-writer`), DESIGN for creatives.
5. Launch checklist + measurement plan + kill criteria.
6. Compliance claims → LEGAL if regulated.

## Output

Campaign brief + calendar + KPI dashboard stub. Prefer canvas for calendar.
