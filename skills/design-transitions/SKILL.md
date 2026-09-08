---
name: design-transitions
description: >-
  DESIGN department skill for motion, scroll, and UI transitions. Wraps GSAP
  ScrollTrigger (+ core) and points at ui-ux-pro-max for motion taste.
  Triggers: transitions, scroll animation, ScrollTrigger, motion, parallax, GSAP.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# DESIGN — Transitions

**Department:** DESIGN

Thin orchestration skill. No full GSAP docs duplicated here.

## Procedure

1. **Scroll / pin / scrub / parallax** — read and follow:
   `dependency:gsap-scrolltrigger`
2. **Tweens / timelines / basics** — also read:
   `dependency:gsap-core`
3. **Motion taste / restraint** — consult ui-ux-pro-max when choosing what to animate:
   `dependency:ui-ux-pro-max`
4. Prefer 2–3 intentional motions over decoration. Respect `prefers-reduced-motion`.

## Fallback

Resolve GSAP dependencies by name. Ambiguous installations require an explicit config override; never edit a wrapper to pin a cache hash.

## Sibling

- UI system: `design-ui-ux-pro-max`
- Frontend impl: `design-frontend`
