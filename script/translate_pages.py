#!/usr/bin/env python3
"""
Translate DanceXR documentation pages to missing locales using a local Ollama model.

Usage:
  python script/translate_pages.py                          # translate all missing
  python script/translate_pages.py --lang jp                # one language only
  python script/translate_pages.py --file dancexr/foo.md   # one file, all langs
  python script/translate_pages.py --lang jp --file dancexr/foo.md
  python script/translate_pages.py --dry-run               # preview without writing
  python script/translate_pages.py --model llama3.2        # use a different model
"""

import os
import re
import sys
import argparse

sys.path.insert(0, os.path.dirname(__file__))
from find_untranslated_pages import find_untranslated_pages
from utils import translate_local, extract_section, lang_names

# ── Constants ────────────────────────────────────────────────────────────────

LOCALE_MAP = {
    'jp': 'ja-JP',
    'zh': 'zh-CN',
    'tw': 'zh-TW',
    'kr': 'ko-KR',
}

# Standard navigation label translations (hardcoded to avoid unnecessary LLM calls)
NAV_LABELS = {
    'jp': {
        'Intro': 'イントロ',
        'Features': '機能',
        'Releases': 'リリース',
        'Download': 'ダウンロード',
        'Support': 'サポート',
        'DOWNLOAD NOW': '今すぐダウンロード',
    },
    'zh': {
        'Intro': '简介',
        'Features': '功能',
        'Releases': '发布',
        'Download': '下载',
        'Support': '支持',
        'DOWNLOAD NOW': '立即下载',
    },
    'tw': {
        'Intro': '簡介',
        'Features': '功能',
        'Releases': '發布',
        'Download': '下載',
        'Support': '支援',
        'DOWNLOAD NOW': '立即下載',
    },
    'kr': {
        'Intro': '소개',
        'Features': '기능',
        'Releases': '출시',
        'Download': '다운로드',
        'Support': '지원',
        'DOWNLOAD NOW': '지금 다운로드',
    },
}


# ── Front matter helpers ─────────────────────────────────────────────────────

def transform_front_matter(front_matter: str, lang: str, translated_title: str) -> str:
    """Apply locale-specific transformations to raw front matter text."""
    result = front_matter

    # locale: en-US → target locale
    result = re.sub(
        r'^(locale:\s*)\S+',
        r'\g<1>' + LOCALE_MAP[lang],
        result, flags=re.MULTILINE, count=1,
    )

    # permalink: /dancexr/... → /<lang>/dancexr/...
    result = re.sub(
        r'^(permalink:\s*)/(?!(?:jp|zh|tw|kr)/)(dancexr)',
        r'\g<1>/' + lang + r'/\g<2>',
        result, flags=re.MULTILINE, count=1,
    )

    # All nav/cta URLs: url: /dancexr → url: /<lang>/dancexr
    result = re.sub(
        r'(url:\s*)/(?!(?:jp|zh|tw|kr)/)(dancexr)',
        r'\g<1>/' + lang + r'/\g<2>',
        result, flags=re.MULTILINE,
    )

    # feature_sections tile links: link: /dancexr → link: /<lang>/dancexr
    result = re.sub(
        r'(link:\s*)/(?!(?:jp|zh|tw|kr)/)(dancexr)',
        r'\g<1>/' + lang + r'/\g<2>',
        result, flags=re.MULTILINE,
    )

    # Translate nav_links labels using lookup table
    labels = NAV_LABELS.get(lang, {})
    for en_label, local_label in labels.items():
        result = re.sub(
            r'(label:\s*)' + re.escape(en_label) + r'(\s*)$',
            r'\g<1>' + local_label + r'\g<2>',
            result, flags=re.MULTILINE,
        )

    # Translate hero_title if it matches the page title (same value as title:)
    title_match = re.search(r'^title:\s*(.+)$', front_matter, re.MULTILINE)
    original_title = title_match.group(1).strip().strip('"\'') if title_match else ''

    if translated_title:
        # Replace title: field
        result = re.sub(
            r'^(title:\s*)(.+)$',
            r'\g<1>' + translated_title,
            result, flags=re.MULTILINE, count=1,
        )
        # Replace hero_title: if it matches the original title
        if original_title:
            result = re.sub(
                r'^(hero_title:\s*)' + re.escape(original_title) + r'(\s*)$',
                r'\g<1>' + translated_title + r'\g<2>',
                result, flags=re.MULTILINE,
            )

    return result


# ── Destination path ─────────────────────────────────────────────────────────

def get_dst_path(src_path: str, lang: str) -> str:
    """Map e.g. dancexr/features/foo.md → jp/dancexr/features/foo.md"""
    return os.path.join(lang, src_path)


# ── Main translation routine ─────────────────────────────────────────────────

def translate_file(src_path: str, lang: str, model: str, dry_run: bool = False) -> None:
    dst_path = get_dst_path(src_path, lang)
    target_lang_name = lang_names[lang]

    print(f"\n{'[DRY RUN] ' if dry_run else ''}{'NEW' if not os.path.exists(dst_path) else 'UPDATE'}"
          f"  {src_path}  →  {dst_path}  ({target_lang_name})")

    with open(src_path, 'r', encoding='utf-8') as f:
        source = f.read()

    existing_translation = ''
    if os.path.exists(dst_path):
        with open(dst_path, 'r', encoding='utf-8') as f:
            existing_translation = f.read()

    front_matter, links, chunks = extract_section(source)

    # Translate title
    title_match = re.search(r'^title:\s*(.+)$', front_matter, re.MULTILINE)
    original_title = title_match.group(1).strip().strip('"\'') if title_match else ''
    translated_title = ''

    if original_title and not dry_run:
        print(f"  title: {original_title!r}")
        translated_title = translate_local(original_title, lang, model=model).strip()
        print(f"      → {translated_title!r}")

    # Translate body chunks
    translated_chunks = []
    for i, chunk in enumerate(chunks, 1):
        print(f"  chunk {i}/{len(chunks)}  ({len(chunk)} chars)…", end='', flush=True)
        if dry_run:
            print(' [skipped]')
            continue
        translated = translate_local(chunk, lang, model=model, existing_translation=existing_translation)
        translated_chunks.append(translated)
        print(' done')

    if dry_run:
        return

    translated_body = '\n'.join(translated_chunks)
    new_front_matter = transform_front_matter(front_matter, lang, translated_title)

    # Assemble output
    parts = [new_front_matter]
    if links.strip():
        parts.append(links.strip())
    parts.append(translated_body)
    output = '\n\n'.join(parts)

    os.makedirs(os.path.dirname(os.path.abspath(dst_path)), exist_ok=True)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"  ✓ saved {dst_path}")


# ── Entry point ──────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description='Translate DanceXR documentation pages to missing locales.'
    )
    parser.add_argument('--lang', choices=['jp', 'zh', 'tw', 'kr'],
                        help='Translate only to this language')
    parser.add_argument('--file',
                        help='Translate only this source file (path relative to workspace root)')
    parser.add_argument('--model', default='gemma4:e4b',
                        help='Ollama model name (default: gemma4:e4b)')
    parser.add_argument('--dry-run', action='store_true',
                        help='List what would be translated without making changes')
    args = parser.parse_args()

    pages = find_untranslated_pages()

    if args.file:
        norm = os.path.normpath(args.file)
        pages = [p for p in pages if os.path.normpath(p['file']) == norm]
        if not pages:
            # File is up to date or doesn't exist in the source tree
            print(f'Nothing to translate for: {args.file}')
            print('(File may already be up to date, or not found in dancexr/ source tree)')
            sys.exit(0)

    if args.lang:
        filtered = []
        for p in pages:
            langs = [l for l in p['languages'] if l == args.lang]
            if langs:
                filtered.append({
                    'file': p['file'],
                    'languages': langs,
                    'reasons': {l: p['reasons'][l] for l in langs},
                })
        pages = filtered

    if not pages:
        print('No pages need translation.')
        return

    total = sum(len(p['languages']) for p in pages)
    print(f'Found {len(pages)} file(s), {total} translation task(s) to process.')
    if args.dry_run:
        print('(Dry run — no files will be written)\n')

    for page in pages:
        src = page['file']
        for lang in page['languages']:
            reason = page['reasons'].get(lang, '?')
            print(f'\n[{reason}]', end=' ')
            translate_file(src, lang, model=args.model, dry_run=args.dry_run)

    print('\nDone.')


if __name__ == '__main__':
    main()
