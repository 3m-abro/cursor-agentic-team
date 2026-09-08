# One source repository, host deployment copies

Keep one editable checkout (recommended: `~/Projects/cursor-agentic-team`) connected
to `https://github.com/3m-abro/cursor-agentic-team.git`. All skills, shared roles,
routing, adapters, packaging, tests and documentation are maintained there.

Cursor's local plugin folder is a deployment copy. It should not contain another
`.git` directory. Its local memory, graph outputs, hook state and private dependency
overrides are runtime data; preserve them, keep them out of commits, and do not
copy them into an OpenAI distributable.

## Change workflow

1. In the canonical checkout, start a feature branch from the reviewed main branch.
2. Edit shared skills/roles once; change platform adapters only when needed.
3. Run `python3 -m unittest discover -s tests -v`, `python3 scripts/validate.py`,
   and `git diff --check`. Use the relevant host's dependency doctor.
4. Review and commit the changes, merge into main, then synchronize with GitHub
   using a normal non-force push or the repository's pull-request workflow.
5. Build a new archive with `python3 scripts/team.py bundle --output dist/RELEASE.zip`.
   Use a new output filename; the helper deliberately refuses overwrites.
6. Update the host deployment from that reviewed archive, preserving runtime data
   and keeping a backup of the previous deployment. Reload the host and smoke-test.

Do not edit an installed Cursor folder or a Codex plugin cache as the source of a
change. If you accidentally edit a deployment, compare and recover the change into
the canonical checkout before updating it.

## Cursor deployment procedure

Extract the archive into a new staging directory. Copy private runtime data from
the current installation into that staging directory: `.cursor/`, `graphify-out/`,
`memory.jsonl`, and `config/dependencies.local.json` when present. Inspect any other
untracked files before replacing an existing installation.

Run the validator on the staged package. Back up the full old installation outside
Cursor's scanned plugin directory, including any old Git metadata. Replace the
installation at its existing path with the staged package. Retain the previous
installation until the interactive smoke checks pass. Record the deployed source
commit locally so it is clear which version is installed. Do not silently overlay
an old directory: removed files could otherwise remain active.

For the first consolidation, archive old source checkouts and their ignored data
before retiring them. An optional symlink from an old work location to the canonical
checkout is only a navigation alias; it is not a second Git repository.

## OpenAI / Codex

Register the canonical plugin folder through the supported plugin-creator flow
when ready to install. Refresh/reinstall through the host when updating; never edit
its managed cache. No additional source checkout or copied skill tree is required.
ChatGPT reference exports are generated artifacts, not independently maintained files.

## Rollback

Restore the previous host deployment from its full backup and reload the host.
Keep the canonical Git history and recover source changes with a reviewed revert.
Preserve runtime records written since the deployment before restoring old data.
