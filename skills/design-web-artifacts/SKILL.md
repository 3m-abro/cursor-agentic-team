---
name: design-web-artifacts
description: >-
  DESIGN department wrapper for Canvas artifacts and Stitch design pipelines.
  Use for analytical canvases, design-from-brief, or design-system extraction.
  Triggers: canvas, .canvas.tsx, stitch, design artifact, visual deliverable.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# DESIGN — Web Artifacts

**Department:** DESIGN

Thin wrapper. Canvas for live React artifacts; Stitch for design generation / sync.

## Procedure

1. **Interactive / analytical artifact** — read and follow:
   `dependency:canvas`
2. **Generate / extract / loop designs (when Stitch fits)** — pick the matching upstream:
   - `dependency:stitch-generate-design`
   - `dependency:stitch-extract-design-md`
   - `dependency:stitch-code-to-design`
   - `dependency:stitch-loop`
   - `dependency:stitch-manage-design-system`
3. Announce which upstream skill ran. Do not invent a parallel canvas/Stitch protocol.

## Sibling

- Brand system: `design-brand`
- Frontend ship: `design-frontend`
