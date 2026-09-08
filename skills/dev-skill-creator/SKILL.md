---
name: dev-skill-creator
description: >-
  DEV department wrapper for authoring Agent Skills. Use when creating
  or restructuring SKILL.md files, skill frontmatter, or skill packages.
  Triggers: create skill, new skill, SKILL.md, skill authoring, forge skill.
---

Read [the shared runtime contract](../../shared/RUNTIME.md) before this workflow.

# DEV — Skill Creator

**Department:** DEV

Thin wrapper. Structure from create-skill; craft from Superpowers writing-skills.

## Procedure

1. Read and follow the host skill-authoring dependency:
   `dependency:create-skill`
2. For skill quality / writing craft, also read and follow:
   `dependency:writing-skills`
3. Use the selected host adapter for the skill installation destination; never write into host-managed bundled skill directories.
4. Pair with `dev-superpowers` when process discipline is the main ask.

## Required frontmatter

- `name` — lowercase kebab-case, ≤64 chars
- `description` — third person, WHAT + WHEN, trigger terms
