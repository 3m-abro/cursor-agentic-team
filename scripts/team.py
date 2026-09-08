#!/usr/bin/env python3
"""Portable, standard-library-only helpers. Never install or execute dependencies."""
import argparse
import glob
import json
import os
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROOTS = ['~/.agents/skills', '~/.codex/skills', '~/.claude/skills']
PACKAGE_DIRS = ['.codex-plugin', '.cursor-plugin', 'skills', 'shared', 'adapters',
                'agents', 'rules', 'commands', 'templates', 'scripts', 'config', 'tests']


def expanded(value, base):
    path = Path(os.path.expanduser(value))
    return path if path.is_absolute() else base / path


def configuration(path):
    selected = path or os.environ.get('AGENTIC_TEAM_CONFIG')
    config_path = Path(selected).expanduser().resolve() if selected else ROOT / 'config/dependencies.local.json'
    data = json.loads(config_path.read_text()) if selected or config_path.exists() else {}
    if not isinstance(data, dict) or set(data) - {'roots', 'overrides'}:
        raise ValueError('Config must be an object with roots and/or overrides')
    roots, overrides = data.get('roots', []), data.get('overrides', {})
    if not isinstance(roots, list) or not all(isinstance(v, str) and v for v in roots):
        raise ValueError('roots must be a list of nonempty paths')
    if not isinstance(overrides, dict) or not all(isinstance(k, str) and isinstance(v, str) and v for k, v in overrides.items()):
        raise ValueError('overrides must map dependency names to nonempty paths')
    return roots, overrides, config_path.parent


def resolve(name, platform, config):
    catalog = json.loads((ROOT / 'config/dependencies.json').read_text())
    if name not in catalog:
        return {'status': 'unknown', 'dependency': name}
    roots, overrides, base = config
    if name in overrides:
        path = expanded(overrides[name], base)
        if path.is_dir() and catalog[name]['kind'] == 'skill':
            path /= 'SKILL.md'
        return {'status': 'resolved' if path.is_file() else 'missing',
                'dependency': name, 'path': str(path.resolve()), 'source': 'override'}
    suffix = f'{name}/SKILL.md' if catalog[name]['kind'] == 'skill' else f'{name}.md'
    candidates = [(str(expanded(r, base) / suffix), 'configured-root') for r in roots]
    adapter = ROOT / 'adapters' / platform / 'dependencies.json'
    if adapter.is_file():
        candidates += [(p, platform) for p in json.loads(adapter.read_text()).get(name, [])]
    candidates += [(str(expanded(r, ROOT) / suffix), 'default-root') for r in DEFAULT_ROOTS]
    for pattern, source in candidates:
        matches = sorted({str(Path(p).resolve()) for p in glob.glob(str(expanded(pattern, ROOT))) if Path(p).is_file()})
        if len(matches) > 1:
            return {'status': 'ambiguous', 'dependency': name, 'candidates': matches,
                    'message': 'Set an explicit overrides entry; no version was selected.'}
        if matches:
            return {'status': 'resolved', 'dependency': name, 'path': matches[0], 'source': source}
    return {'status': 'missing', 'dependency': name,
            'message': 'Install the upstream capability or configure its path; see shared/RUNTIME.md.'}


def package_files():
    # Explicit allowlist excludes local overrides, user data, caches and Git metadata.
    for directory in PACKAGE_DIRS:
        for path in sorted((ROOT / directory).rglob('*')):
            if not path.is_file() or path.is_symlink():
                continue
            if '__pycache__' in path.parts or path.suffix == '.pyc' or path.name.endswith('.local.json'):
                continue
            if directory == 'config' and path.name not in {'dependencies.json', 'dependencies.example.json'}:
                continue
            yield path
    for name in ['README.md', 'LICENSE', 'AGENTS.md']:
        yield ROOT / name
    for path in sorted((ROOT / 'docs').rglob('*.md')):
        yield path


def init_collab(project):
    target = Path(project).expanduser().resolve() / 'docs/ai-collab'
    copied, skipped = [], []
    for source in sorted((ROOT / 'templates/ai-collab').rglob('*')):
        if not source.is_file():
            continue
        destination = target / source.relative_to(ROOT / 'templates/ai-collab')
        destination.parent.mkdir(parents=True, exist_ok=True)
        try:
            with destination.open('xb') as stream:
                stream.write(source.read_bytes())
            copied.append(str(destination))
        except FileExistsError:
            skipped.append(str(destination))
    return {'status': 'ok', 'copied': copied, 'preserved': skipped}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for command in ('resolve', 'doctor'):
        p = sub.add_parser(command)
        if command == 'resolve':
            p.add_argument('dependency')
        p.add_argument('--platform', choices=['portable', 'cursor', 'codex', 'chatgpt'], default='portable')
        p.add_argument('--config')
    p = sub.add_parser('init-collab')
    p.add_argument('project')
    for command in ('bundle', 'chatgpt'):
        p = sub.add_parser(command)
        p.add_argument('--output', required=True)
    args = parser.parse_args()
    try:
        if args.command in ('resolve', 'doctor'):
            try:
                config = configuration(args.config)
            except (ValueError, OSError) as exc:
                print(json.dumps({'status': 'invalid-config', 'message': str(exc)}))
                return 2
            if args.command == 'resolve':
                result = resolve(args.dependency, args.platform, config)
                ok = result['status'] == 'resolved'
            else:
                names = json.loads((ROOT / 'config/dependencies.json').read_text())
                results = [resolve(name, args.platform, config) for name in names]
                ok = all(r['status'] == 'resolved' for r in results)
                result = {'status': 'ok' if ok else 'incomplete', 'dependencies': results}
        elif args.command == 'init-collab':
            result, ok = init_collab(args.project), True
        else:
            output = Path(args.output).expanduser()
            output.parent.mkdir(parents=True, exist_ok=True)
            if args.command == 'bundle':
                files = list(package_files())
                with zipfile.ZipFile(output, 'x', compression=zipfile.ZIP_DEFLATED) as archive:
                    for path in files:
                        archive.write(path, path.relative_to(ROOT).as_posix())
            else:
                paths = [ROOT / 'adapters/chatgpt/RUNTIME.md', ROOT / 'shared/RUNTIME.md',
                         ROOT / 'shared/ROUTING.md', ROOT / 'shared/TEAM.md',
                         ROOT / 'docs/WORKFLOWS.md', ROOT / 'docs/DEPENDENCIES.md']
                paths += sorted((ROOT / 'shared/agents').glob('*.md'))
                paths += sorted((ROOT / 'skills').glob('*/SKILL.md'))
                paths += sorted((ROOT / 'commands').glob('*.md'))
                with output.open('x', encoding='utf-8') as stream:
                    stream.write('# Agentic Team — ChatGPT reference export\n\nThis is not an installed plugin. It supplies instructions, not tools or external upstream skill bodies.\n\n')
                    for path in paths:
                        stream.write(f'\n\n---\n\n## Source: {path.relative_to(ROOT).as_posix()}\n\n{path.read_text()}')
            result, ok = {'status': 'ok', 'output': str(output.resolve())}, True
        print(json.dumps(result, indent=2))
        return 0 if ok else 2
    except (OSError, ValueError) as exc:
        print(json.dumps({'status': 'error', 'message': str(exc)}))
        return 2

if __name__ == '__main__':
    sys.exit(main())
