#!/usr/bin/env python3
"""
Sync the 'layout' front matter field from English source pages to all
localized counterparts (jp/, zh/, tw/, kr/).

Usage:
  python script/sync_layout.py               # update all localized pages
  python script/sync_layout.py --dry-run     # preview without writing
  python script/sync_layout.py --file dancexr/features/accessory.md
"""

import os
import re
import sys
import argparse

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCALES   = ['jp', 'zh', 'tw', 'kr']

FRONT_MATTER_RE = re.compile(r'^(---\s*\n)(.*?)(---\s*\n)', re.DOTALL)
LAYOUT_LINE_RE  = re.compile(r'^(layout:\s*)(\S+)', re.MULTILINE)


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(path, content):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)


def get_layout(content):
    """Return the layout value from front matter, or None."""
    m = FRONT_MATTER_RE.match(content)
    if not m:
        return None
    fm = m.group(2)
    lm = LAYOUT_LINE_RE.search(fm)
    return lm.group(2) if lm else None


def set_layout(content, layout_value):
    """Replace the layout value in front matter. Returns new content."""
    m = FRONT_MATTER_RE.match(content)
    if not m:
        return None  # no front matter — skip
    fm = m.group(2)
    if LAYOUT_LINE_RE.search(fm):
        new_fm = LAYOUT_LINE_RE.sub(lambda x: x.group(1) + layout_value, fm)
    else:
        # No layout line at all — insert after the first line of front matter
        new_fm = f'layout: {layout_value}\n' + fm
    return m.group(1) + new_fm + m.group(3) + content[m.end():]


def iter_english_pages(src_file=None):
    """Yield relative paths (from repo root) for English source .md files."""
    if src_file:
        # Normalise to relative path
        rel = os.path.relpath(os.path.abspath(src_file), REPO_ROOT).replace('\\', '/')
        yield rel
        return
    for dirpath, _, filenames in os.walk(os.path.join(REPO_ROOT, 'dancexr')):
        for fname in filenames:
            if fname.endswith('.md'):
                full = os.path.join(dirpath, fname)
                yield os.path.relpath(full, REPO_ROOT).replace('\\', '/')


def main():
    parser = argparse.ArgumentParser(description='Sync layout front matter to localized pages.')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without writing')
    parser.add_argument('--file', metavar='PATH', help='Only process this English source file')
    args = parser.parse_args()

    updated = 0
    skipped = 0
    missing = 0

    for eng_rel in iter_english_pages(args.file):
        eng_path = os.path.join(REPO_ROOT, eng_rel)
        if not os.path.isfile(eng_path):
            print(f'  [WARN] Source not found: {eng_rel}')
            continue

        eng_content = read_file(eng_path)
        eng_layout  = get_layout(eng_content)
        if not eng_layout:
            skipped += 1
            continue

        for locale in LOCALES:
            loc_rel  = f'{locale}/{eng_rel}'
            loc_path = os.path.join(REPO_ROOT, loc_rel)
            if not os.path.isfile(loc_path):
                missing += 1
                continue

            loc_content = read_file(loc_path)
            loc_layout  = get_layout(loc_content)

            if loc_layout == eng_layout:
                continue  # already correct

            new_content = set_layout(loc_content, eng_layout)
            if new_content is None:
                print(f'  [SKIP] No front matter: {loc_rel}')
                skipped += 1
                continue

            action = 'would update' if args.dry_run else 'updated'
            print(f'  [{action}] {loc_rel}  ({loc_layout!r} → {eng_layout!r})')
            updated += 1

            if not args.dry_run:
                write_file(loc_path, new_content)

    print(f'\nDone. {updated} file(s) {"would be " if args.dry_run else ""}updated, '
          f'{skipped} skipped (no layout), {missing} locale files not found.')


if __name__ == '__main__':
    main()
