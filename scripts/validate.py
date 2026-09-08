#!/usr/bin/env python3
"""Validate portable references, shared skill metadata and host discovery layout."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def validate():
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    catalog = json.loads((ROOT / 'config/dependencies.json').read_text())
    cursor = json.loads((ROOT / '.cursor-plugin/plugin.json').read_text())
    codex = json.loads((ROOT / '.codex-plugin/plugin.json').read_text())
    for manifest in (cursor, codex):
        require(manifest.get('name') == 'cursor-agentic-team', 'Plugin identity changed')
        require(manifest.get('skills') == './skills/', 'Manifests must share skills/')
        require(bool(re.fullmatch(r'\d+\.\d+\.\d+', manifest.get('version', ''))), 'Invalid version')
        for field in ('skills', 'rules', 'agents', 'commands'):
            if field in manifest:
                require((ROOT / manifest[field]).is_dir(), f'Missing manifest target {field}')
    require(cursor['version'] == codex['version'], 'Host versions differ')
    skills = list((ROOT / 'skills').glob('*/SKILL.md'))
    require(len(skills) == 44, 'Expected 43 department skills + orchestrator')
    names = []
    for path in skills:
        text = path.read_text()
        front = text.split('---', 2)
        require(len(front) == 3 and not front[0].strip(), f'{path}: missing frontmatter')
        if len(front) != 3:
            continue
        match = re.search(r'^name:\s*([a-z0-9-]+)\s*$', front[1], re.M)
        name = match[1] if match else ''
        require(name == path.parent.name and len(name) <= 64, f'{path}: invalid name')
        require(bool(re.search(r'^description:\s*\S', front[1], re.M)), f'{path}: missing description')
        names.append(name)
    require(len(names) == len(set(names)), 'Duplicate skill name')
    paths = [ROOT / 'AGENTS.md', ROOT / 'README.md']
    for directory in ('shared', 'skills', 'adapters', 'agents', 'rules', 'commands', 'templates', 'docs'):
        paths.extend(p for p in (ROOT / directory).rglob('*') if p.suffix in ('.md', '.mdc', '.json'))
    for path in paths:
        text = path.read_text()
        require(not re.search(r'/home/[^/\s]+/|/Users/[^/\s]+/', text), f'{path}: personal absolute path')
        require(not re.search(r'/(?:cache|marketplaces)/[^\s`]*[a-f0-9]{40}', text), f'{path}: pinned cache revision')
        for dependency in re.findall(r'dependency:([a-z][a-z0-9-]+)', text):
            require(dependency in catalog, f'{path}: unknown dependency {dependency}')
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if re.match(r'[a-z]+:', link) or link.startswith('#'):
                continue
            target = link.split('#')[0]
            require((path.parent / target).exists(), f'{path}: broken link {target}')
    for platform in ('cursor', 'codex'):
        adapter = json.loads((ROOT / 'adapters' / platform / 'dependencies.json').read_text())
        for name, values in adapter.items():
            require(name in catalog, f'{platform}: unknown dependency {name}')
            require(isinstance(values, list) and all(isinstance(v, str) for v in values), f'{platform}: invalid paths')
    require('alwaysApply: true' in (ROOT / 'rules/ceo-router.mdc').read_text(), 'Cursor router no longer alwaysApply')
    for path in (ROOT / 'agents').glob('*.md'):
        require((ROOT / 'shared/agents' / path.name).is_file(), f'Missing shared role {path.name}')
    return errors

if __name__ == '__main__':
    try:
        errors = validate()
    except (OSError, ValueError, KeyError) as exc:
        errors = [str(exc)]
    print('\n'.join(errors) if errors else 'PASS: 44 shared skill entries, manifests, dependency names, adapters and Markdown links')
    sys.exit(bool(errors))
