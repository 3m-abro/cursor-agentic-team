# Setup and usage

## Cursor

Keep your existing installation until you have reviewed and tested the migration.
For a fresh source checkout:

```sh
git clone https://github.com/3m-abro/cursor-agentic-team.git ~/Projects/cursor-agentic-team
```

If that directory exists, do not clone over it. Maintain this single source
checkout through your reviewed Git workflow. Deploy a package to
`~/.cursor/plugins/local/cursor-agentic-team` using the
[maintenance procedure](MAINTENANCE.md), preserving runtime data. Reload Cursor / reopen the agent.
This migration branch must be merged or copied into your chosen installation
before these changes are available there. The original `.cursor-plugin/plugin.json`
identity and discovery directories are unchanged.

Run `python3 scripts/team.py doctor --platform cursor` from the installed root.
Resolve missing dependencies separately; multiple cached revisions need an override.
The adapter retains original paths in their original preference order.

Try `/team-status`, `/dev-collab status`, and a relevant department command.
No external service should be marked available until actually discovered.

## Codex and plugin-capable ChatGPT

The repository includes `.codex-plugin/plugin.json` referencing `./skills/`, based
on [OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins).
There are no invented MCP IDs, external-server placeholders or auto-running hooks.

Open this checkout in a compatible local host. Ask its built-in plugin-creator:

> Register this existing cursor-agentic-team folder in my personal marketplace
> without replacing its contents, then validate it for local testing.

This is a separate installation action. This repository change does not modify a
personal marketplace or live plugin cache. Follow the current host's installation
UI and test in a fresh session; see [OpenAI connection/testing guidance](https://developers.openai.com/plugins/deploy/connect-chatgpt).
Do not pass the repository to `marketplace add` as if it already contains a
marketplace catalog. It is a plugin source folder, not a catalog.

Invoke `team-orchestrator` by its installed name/namespace, or ask:

> Use Agentic Team to route this task to the right department. Show missing
> capabilities before attempting dependent steps.

For direct department work invoke, for example, `finance-reconciliation` or
`dev-ai-collab`. These also load the shared runtime contract. For commands such as
`dev-qa`, ask team-orchestrator to run that workflow; native Cursor slash commands
are not registered in Codex/ChatGPT.

Use `python3 scripts/team.py doctor --platform codex` when local shell access
exists. Connect required MCP providers separately in the host. Without a shell,
resolve named upstream skills from the session catalog instead.

## Ordinary ChatGPT reference mode

Generate `python3 scripts/team.py chatgpt --output dist/chatgpt-team.md`, attach the
file in a chat that supports attachments, and ask:

> Use the attached Agentic Team reference. Route my request, execute available
> roles sequentially, and report any missing upstream capabilities.

This does not install a plugin, expose the local filesystem, or create subagents.
Source headings replace internal file navigation. The external skill bodies are
not present. For wrapper-only work, supply the upstream instructions or use an
installed skill on a capable surface. Product availability is not guaranteed by
this repo; no subscription-specific promise is made.

## Consumer project setup

Merge relevant instructions from `templates/AGENTS.md` into the project's existing
instructions, rather than overwriting the file. Initialize collaboration docs:

```sh
python3 /path/to/cursor-agentic-team/scripts/team.py init-collab /path/to/project
```

Every existing file is preserved, including empty files. Re-running is safe. The
helper reports copied and preserved files. It does not update existing templates.

## Manual host smoke checks

1. Cursor: reload; confirm 43 department skills plus orchestrator, seven agents,
   13 commands and always-on routing. Run `/team-status` and `/dev-collab status`.
2. Invoke a wrapper with a known installed upstream. Confirm it reads the resolved
   skill and reports its use. Test a missing upstream without a false success claim.
3. On a disposable project, initialize collaboration docs twice; edited handover
   content must survive. Test the ship gate with missing test evidence.
4. OpenAI host: register/install the plugin, start a fresh task, invoke
   team-orchestrator and a direct department skill. Confirm shared files are accessible.
5. Check connected docs/memory/browser capabilities on the target host. Do not
   count a path-resolution success as an MCP integration test.
6. Plain chat: attach the reference, request a workflow, and confirm unsupported
   filesystem/MCP/delegation operations are reported rather than simulated.
