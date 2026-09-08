---
name: social-post-writer
description: >-
  SOCIAL department skill for drafting posts — X/Twitter via hermes-tweet,
  LinkedIn and multi-platform posts via thin procedure. Use when writing
  tweets, LinkedIn posts, threads, or social copy.
  Triggers: tweet, LinkedIn post, social post, thread, X post.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# SOCIAL — Post Writer

**Department:** SOCIAL

Wrap + NEW: hermes-tweet for X; LinkedIn/posts procedure (no dedicated LinkedIn-post skill on host).

## Upstream

1. X / Twitter research + guarded tweet prep:
   `dependency:hermes-tweet`
2. Optional publish/schedule (API):
   `dependency:social-publishing`
3. Voice constraints → `social-voice-builder` / `design-brand`.

## Procedure (LinkedIn / general posts)

1. **Goal** — awareness / engage / convert; one CTA max.
2. **Audience** — ICP one-liner + platform norms (LinkedIn = professional narrative; X = punchy).
3. **Hook** — first line earns the scroll; run `social-hook-generator` if stuck.
4. **Body** — 3–7 short paras or bullets; one proof (metric, quote, story beat).
5. **CTA** — comment prompt, link, or DM keyword — not all three.
6. **Variants** — ship 2–3 lengths (short / standard / thread).
7. **Compliance** — no fake engagement claims; flag regulated claims → LEGAL.

## X path

Read hermes-tweet fully when researching accounts, monitoring, or preparing tweet actions. Draft here; publish only via approved gated flow.

## Output

Platform-ready drafts + alt hooks. No emoji spam unless brand voice demands it.

## Command

`/social-post` → this skill.
