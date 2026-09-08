# Rollback — v1.2.0

The migration is developed in an isolated checkout; the live Cursor installation
was not edited. Return to the existing installation if a host smoke check fails.
Before deployment, keep a copy of the prior reviewed revision and local config.
Use the normal reviewed Git revert/restore workflow to restore v1.1.0 if needed.

No consumer records, account settings or MCP configuration were migrated. Preserve
consumer docs and local dependency overrides during rollback. If a new OpenAI
installation was registered separately, remove it through its host UI as needed.

After rollback, confirm the original 43 skills, seven agents, always-on router and
13 commands load in Cursor. No automatic rollback/destructive cleanup is included.
