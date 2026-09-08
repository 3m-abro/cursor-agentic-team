---
name: social-voice-builder
description: >-
  SOCIAL department wrapper for brand voice — tone, do/don't, sample posts.
  Use when defining or auditing social voice for a brand or founder.
  Triggers: brand voice, tone of voice, social voice, voice guide.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# SOCIAL — Voice Builder

**Department:** SOCIAL

Thin wrapper around brand (voice + messaging). No separate voice-framework skill on host.

## Upstream

1. Read and follow:
   `dependency:brand`
2. DESIGN identity systems → also `design-brand` when visual tokens matter.

## Social-specific add-on

After brand voice load:

1. Extract **voice axes** (formal↔casual, playful↔serious, expert↔peer).
2. Write **do / don't** list (10 lines max) for social channels.
3. Produce **3 sample posts** (LinkedIn, X, short-form caption) in-voice.
4. Produce **banned phrases** list (corporate sludge, hype, false urgency).
5. Hand samples to `social-post-writer` for channel adaptation.

## Output

One-page voice card: axes + do/don't + samples + banned list.
