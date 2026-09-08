---
name: social-hook-generator
description: >-
  SOCIAL department skill for scroll-stopping hooks — wraps boost/enhance
  prompt craft plus a social-hooks procedure. Use for openers, thumb-stoppers,
  subject lines for social.
  Triggers: hook, scroll stopper, reel hook, post opener, attention grabber.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# SOCIAL — Hook Generator

**Department:** SOCIAL

Wrap + procedure: prompt refinement upstream + social-specific hook craft.

## Upstream

1. Interactive prompt refinement (when brief is vague):
   `dependency:boost-prompt`
2. Specificity / structure polish (adapt patterns; Stitch-oriented but useful for sharpening briefs):
   `dependency:enhance-prompt`

## Social hooks procedure

1. **Frame** — platform, ICP pain, promised outcome, constraint (chars / 3s spoken).
2. **Generate 10 hooks** across patterns:
   - Contrarian claim
   - Specific number / result
   - Curiosity gap (incomplete story)
   - Direct "you" pain callout
   - Myth-bust
   - Before → after
3. **Score** each 1–5 on: clarity, novelty, specificity, brand-safe.
4. **Pick top 3** — rewrite to brand voice (`social-voice-builder`).
5. **Pair** — hand winning hooks to `social-post-writer` or `social-reels-scripting`.

## Output

Ranked hook list + why top 3 win. No clickbait that the body can't pay off.
