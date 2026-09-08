# Dependencies

External skill bodies are not bundled. Install them through their provider or
supply a trusted path; the resolver never installs or executes them. Only a
workflow's required capabilities block that workflow. Optional steps remain optional.

## Configuration

Copy `config/dependencies.example.json` to ignored `config/dependencies.local.json`,
or pass `--config /path/to/config.json`. `AGENTIC_TEAM_CONFIG` is another option.

```json
{
  "roots": ["../external-skills", "~/.agents/skills"],
  "overrides": {"brand": "../brand/SKILL.md"}
}
```

These are example paths; replace them with actual resources. Relative paths are
based on the config directory. A missing explicit override fails without fallback.
Configured roots precede adapter defaults. Root order is meaningful. No config
file is automatically interpreted by the host; it is input to `scripts/team.py`.
Use file paths in overrides for agents; skills also accept a directory containing SKILL.md.

Lookup: overrides → configured roots → selected adapter paths → portable roots
(`~/.agents/skills`, `~/.codex/skills`, `~/.claude/skills`). The Cursor adapter
preserves the legacy preference order. Cache wildcards never select between
multiple revisions automatically. Review the candidates, then set an override.

```sh
python3 scripts/team.py resolve using-superpowers --platform cursor
python3 scripts/team.py resolve create-skill --platform codex
python3 scripts/team.py doctor --platform portable
```

Exit 0 means resolved; 2 means missing, ambiguous, unknown or invalid config.
`doctor` inventories all dependencies; it does not test MCP availability or execute skills.
Without a shell, use the session skill catalog by name as described in the
[runtime contract](../shared/RUNTIME.md).

## Inventory

| Dependency | Kind | Referencing department skills |
|---|---|---|
| `agent-owasp-compliance` | skill | legal-compliance-check |
| `banner-design` | skill | marketing-ad-creative, social-youtube-thumbnail |
| `boost-prompt` | skill | social-hook-generator |
| `brand` | skill | design-brand, social-voice-builder |
| `build-mcp-server` | skill | dev-mcp-builder |
| `canvas` | skill | design-web-artifacts |
| `content-marketer` | agent | biz-run-campaign |
| `content-strategy` | skill | biz-run-campaign, marketing-ai-seo, marketing-customer-research |
| `context7-mcp` | skill | dev-docs-fetcher |
| `copywriting` | skill | marketing-copywriting |
| `create-skill` | skill | dev-skill-creator |
| `enhance-prompt` | skill | social-hook-generator |
| `frontend-design` | skill | design-frontend |
| `gdpr-data-handling` | skill | legal-compliance-check |
| `gsap-core` | skill | design-transitions |
| `gsap-scrolltrigger` | skill | design-transitions |
| `gstack` | skill | dev-qa-engineer |
| `gstack-qa` | skill | dev-qa-engineer |
| `hermes-tweet` | skill | social-post-writer |
| `mem-search` | skill | dev-memory-keeper |
| `nano-banana-pro-openrouter` | skill | social-youtube-thumbnail |
| `ogilvy` | skill | marketing-ad-creative |
| `page-cro` | skill | marketing-cro |
| `schema-markup` | skill | marketing-ai-seo |
| `seo-audit` | skill | marketing-ai-seo |
| `social-publishing` | skill | social-post-writer |
| `startup-financial-modeling` | skill | biz-cash-flow-snapshot |
| `stitch-code-to-design` | skill | design-web-artifacts |
| `stitch-extract-design-md` | skill | design-web-artifacts |
| `stitch-generate-design` | skill | design-web-artifacts |
| `stitch-loop` | skill | design-web-artifacts |
| `stitch-manage-design-system` | skill | design-web-artifacts |
| `taste-design` | skill | design-taste |
| `ui-ux-pro-max` | skill | design-transitions, design-ui-ux-pro-max |
| `using-superpowers` | skill | dev-superpowers |
| `writing-skills` | skill | dev-skill-creator, dev-superpowers |

Original provider discovery locations: [Cursor configuration](../adapters/cursor/dependencies.json).
Codex authoring alias: [Codex configuration](../adapters/codex/dependencies.json).
The thin wrappers do not guarantee equivalent behavior across different providers.
