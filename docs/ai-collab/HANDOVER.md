# Handover

Updated: 2026-09-08

- Done: v1.2.0 portable dependencies, shared routing/roles, preserved Cursor discovery, OpenAI manifest/orchestrator, safe initialization, bundle/reference exports and setup/migration docs.
- Left: maintain the canonical checkout using docs/MAINTENANCE.md; register/install the OpenAI plugin when needed and run manual host smoke checks in docs/SETUP.md.
- Broken / watch: static tests pass; live host/MCP behavior is unverified. Codex lookup lacks 13 upstreams; Cursor lookup resolves all 36 on this machine. External memory mirror not written.
- Avoid: editing deployment/cache copies, copying skills without shared resources, overwriting runtime or consumer records, treating Markdown roles as native subagents.
- Model pin: Codex (GPT-6; exact deployment version not exposed).
