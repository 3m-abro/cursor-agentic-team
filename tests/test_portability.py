import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / 'scripts' / 'team.py'

class PortabilityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='team test ')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.env = dict(os.environ, HOME=str(self.base), AGENTIC_TEAM_CONFIG='')

    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(CLI), *map(str, args)],
                              cwd=self.base, env=self.env, capture_output=True, text=True)

    def file(self, path, text='skill'):
        path = self.base / path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def test_resolves_named_skill_outside_repo_from_portable_root(self):
        path = self.file('.agents/skills/brand/SKILL.md')
        result = self.run_cli('resolve', 'brand', '--platform', 'codex')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['path'], str(path))

    def test_cursor_keeps_legacy_preference(self):
        expected = self.file('.claude/skills/frontend-design/SKILL.md')
        self.file('.agents/skills/frontend-design/SKILL.md')
        result = self.run_cli('resolve', 'frontend-design', '--platform', 'cursor')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['path'], str(expected))

    def test_cache_hash_changes_and_multiple_versions_require_pin(self):
        root = '.cursor/plugins/cache/cursor-public/superpowers/'
        path = self.file(root + 'new-revision/skills/using-superpowers/SKILL.md')
        result = self.run_cli('resolve', 'using-superpowers', '--platform', 'cursor')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['path'], str(path))
        self.file(root + 'other-revision/skills/using-superpowers/SKILL.md')
        result = self.run_cli('resolve', 'using-superpowers', '--platform', 'cursor')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stdout)['status'], 'ambiguous')

    def test_config_override_is_relative_to_config_not_cwd(self):
        path = self.file('settings/upstream/SKILL.md')
        config = self.file('settings/config.json', json.dumps({'overrides': {'brand': 'upstream/SKILL.md'}}))
        result = self.run_cli('resolve', 'brand', '--config', config)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['path'], str(path))

    def test_stale_explicit_override_does_not_silently_fallback(self):
        self.file('.agents/skills/brand/SKILL.md')
        config = self.file('config.json', '{"overrides":{"brand":"missing.md"}}')
        result = self.run_cli('resolve', 'brand', '--config', config)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stdout)['status'], 'missing')

    def test_missing_unknown_and_invalid_config_report_failure(self):
        for name in ('brand', '../unknown'):
            result = self.run_cli('resolve', name)
            self.assertEqual(result.returncode, 2)
            self.assertIn(json.loads(result.stdout)['status'], ('missing', 'unknown'))
        config = self.file('bad.json', '{bad')
        result = self.run_cli('resolve', 'brand', '--config', config)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stdout)['status'], 'invalid-config')

    def test_configured_roots_and_codex_authoring_alias(self):
        expected = self.file('custom/copywriting/SKILL.md')
        config = self.file('config.json', '{"roots":["custom"]}')
        result = self.run_cli('resolve', 'copywriting', '--config', config)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['path'], str(expected))
        expected = self.file('.codex/skills/.system/skill-creator/SKILL.md')
        result = self.run_cli('resolve', 'create-skill', '--platform', 'codex')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['path'], str(expected))

    def test_init_preserves_existing_files_and_is_repeatable(self):
        expected = self.file('project/docs/ai-collab/HANDOVER.md', 'keep my work')
        for _ in range(2):
            result = self.run_cli('init-collab', self.base / 'project')
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(expected.read_text(), 'keep my work')
        self.assertTrue(expected.with_name('CONSTRAINTS.md').is_file())

    def test_bundle_contains_single_skill_source_and_all_adapter_targets(self):
        output = self.base / 'team.zip'
        result = self.run_cli('bundle', '--output', output)
        self.assertEqual(result.returncode, 0, result.stderr)
        with zipfile.ZipFile(output) as bundle:
            names = bundle.namelist()
            self.assertIn('.codex-plugin/plugin.json', names)
            self.assertIn('.cursor-plugin/plugin.json', names)
            self.assertIn('shared/ROUTING.md', names)
            self.assertIn('shared/agents/ceo-orchestrator.md', names)
            self.assertIn('skills/team-orchestrator/SKILL.md', names)
            self.assertEqual(len([p for p in names if p.endswith('/SKILL.md')]), 44)
            self.assertFalse(any('local.json' in p or '.git/' in p or '__pycache__' in p for p in names))
            self.assertEqual(bundle.read('skills/design-brand/SKILL.md'), (ROOT / 'skills/design-brand/SKILL.md').read_bytes())
        self.assertEqual(self.run_cli('bundle', '--output', output).returncode, 2)

    def test_chatgpt_export_includes_roles_and_explicit_runtime_limits(self):
        output = self.base / 'team.md'
        result = self.run_cli('chatgpt', '--output', output)
        self.assertEqual(result.returncode, 0, result.stderr)
        text = output.read_text()
        self.assertIn('not an installed plugin', text)
        self.assertIn('LEGAL Department Lead', text)
        self.assertIn('finance-reconciliation', text)
        self.assertEqual(self.run_cli('chatgpt', '--output', output).returncode, 2)


class ValidationTests(unittest.TestCase):
    def test_repository_validation_and_detects_bad_reference(self):
        import shutil
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / 'package'
            shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns('.git', '__pycache__', 'dist'))
            validator = target / 'scripts/validate.py'
            result = subprocess.run([sys.executable, str(validator)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            with (target / 'skills/design-brand/SKILL.md').open('a') as stream:
                stream.write('\n`dependency:nonexistent-provider`\n[broken](../../missing-file.md)\n')
            result = subprocess.run([sys.executable, str(validator)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('nonexistent-provider', result.stdout)
            self.assertIn('missing-file.md', result.stdout)

    def test_cursor_discovery_contract(self):
        baseline = json.loads((ROOT / 'tests/cursor-contract.json').read_text())
        manifest = json.loads((ROOT / '.cursor-plugin/plugin.json').read_text())
        for key, value in baseline['manifest'].items():
            self.assertEqual(manifest[key], value)
        for directory, names in baseline['entries'].items():
            actual = sorted(p.name for p in (ROOT / directory).iterdir() if p.is_file() or directory == 'skills')
            self.assertTrue(set(names) <= set(actual))
        self.assertIn('alwaysApply: true', (ROOT / 'rules/ceo-router.mdc').read_text())
        for name, frontmatter in baseline['agents'].items():
            self.assertEqual((ROOT / 'agents' / name).read_text().split('---', 2)[1], frontmatter)

if __name__ == '__main__':
    unittest.main()
