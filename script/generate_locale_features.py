#!/usr/bin/env python3
"""
Generates localized features.md files by:
1. Reading the English features.md YAML front matter (structure, images, badges, links)
2. Reading each locale's HTML body to extract translated tile/section titles and locale links
3. Writing new YAML-only locale features.md files
"""

import re
import sys
import os
from html import unescape

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOCALES = {
    'zh': {'code': 'zh-CN', 'title': '功能列表', 'permalink': '/zh/dancexr/features'},
    'jp': {'code': 'ja-JP', 'title': '機能一覧', 'permalink': '/jp/dancexr/features'},
    'tw': {'code': 'zh-TW', 'title': '功能清單', 'permalink': '/tw/dancexr/features'},
    'kr': {'code': 'ko-KR', 'title': '기능 목록', 'permalink': '/kr/dancexr/features'},
}

def read_front_matter_and_body(filepath):
    """Read a markdown file, split into front matter (as string) and body."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find the closing --- of front matter
    # File starts with ---\n, find the next ---
    match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        fm_str = match.group(1)
        body = content[match.end():]
        return fm_str, body
    return None, content

def parse_locale_html(body, locale_prefix):
    """
    Parse the HTML body of a locale features page.
    Returns: (sections, section_titles, subsection_titles, tile_data)
    where tile_data maps link -> title
    """
    # Extract section titles (h2) and subsection titles (h3)
    # And tile data (link + title pairs)

    sections = []
    current_section = None
    current_subsection = None

    # Process section by section
    # Split on <section tags
    section_blocks = re.split(r'(?=<section class="section)', body)

    for block in section_blocks:
        if not block.strip():
            continue

        section = {}
        # Check if light
        section['light'] = 'section-light' in block.split('\n')[0] if block.startswith('<section') else False

        # Get section title (h2)
        h2_match = re.search(r'<h2>(.*?)</h2>', block)
        if not h2_match:
            continue
        section['title'] = unescape(h2_match.group(1))

        # Find subsections (h3 + feature-grid pairs)
        # Split into subsection blocks by h3 or feature-grid
        subsections = []

        # Find all h3 headers
        h3_positions = [(m.start(), m.group(1)) for m in re.finditer(r'<h3>(.*?)</h3>', block)]

        # Find all feature-grid divs
        grid_pattern = re.compile(r'<div class="feature-grid">(.*?)</div>\s*\n', re.DOTALL)

        if h3_positions:
            # There are subsections
            # Split block into parts around h3 tags
            remaining = block[h2_match.end():]

            # Find all h3+grid pairs - match grid content as everything between the opening
            # <div class="feature-grid"> and the closing </div> on its own line
            h3_iter = list(re.finditer(
                r'<h3>(.*?)</h3>\s*\n<div class="feature-grid">\n((?:.*\n)*?)</div>\n',
                remaining
            ))

            for h3_match in h3_iter:
                sub = {}
                sub['title'] = unescape(h3_match.group(1))
                grid_content = h3_match.group(2)
                sub['tiles'] = parse_tiles(grid_content)
                subsections.append(sub)

            section['subsections'] = subsections
        else:
            # No subsections, just tiles
            grids = re.findall(r'<div class="feature-grid">\n((?:.*\n)*?)</div>\n', block)
            if grids:
                section['tiles'] = parse_tiles(grids[0])

        sections.append(section)

    return sections

def parse_tiles(grid_content):
    """Parse tile HTML into list of tile dicts."""
    tiles = []

    # Match both linked and disabled tiles
    # Linked: <a href="..." class="feature-tile">...</a>
    # Disabled: <div class="feature-tile feature-tile--disabled">...</div>

    tile_pattern = re.compile(
        r'(<a href="([^"]*)" class="feature-tile">|<div class="feature-tile feature-tile--disabled">)'
        r'.*?<div class="feature-tile-img" style="background-image: url\(\'([^\']*)\'\);"></div>'
        r'.*?<span class="feature-tile-name">(.*?)</span>'
        r'(.*?)'
        r'(</a>|</div>)',
        re.DOTALL
    )

    for m in tile_pattern.finditer(grid_content):
        tile = {}
        tag_start = m.group(1)

        if 'feature-tile--disabled' in tag_start:
            tile['link'] = None
        else:
            tile['link'] = m.group(2)

        tile['image'] = m.group(3)
        tile['title'] = unescape(m.group(4))

        # Check for badge
        badge_content = m.group(5)
        badge_match = re.search(
            r'<span class="feature-tile-badge(?:\s+feature-tile-badge--([\w]+))?">(.*?)</span>',
            badge_content
        )
        if badge_match:
            badge_type = badge_match.group(1)  # new, pro, nsfw, or None
            badge_text = badge_match.group(2)
            tile['badge'] = badge_text
            if badge_type:
                tile['badge_type'] = badge_type

        tiles.append(tile)

    return tiles

def sections_to_yaml(sections):
    """Convert sections list to YAML string."""
    lines = ['feature_sections:']

    for section in sections:
        lines.append(f'  - title: {yaml_str(section["title"])}')
        if section.get('light'):
            lines.append(f'    light: true')
        if 'subsections' in section:
            lines.append(f'    subsections:')
            for sub in section['subsections']:
                lines.append(f'      - title: {yaml_str(sub["title"])}')
                lines.append(f'        tiles:')
                for tile in sub['tiles']:
                    lines.extend(tile_to_yaml(tile, '          '))
        elif 'tiles' in section:
            lines.append(f'    tiles:')
            for tile in section['tiles']:
                lines.extend(tile_to_yaml(tile, '      '))

    return '\n'.join(lines)

def yaml_str(s):
    """Format a string for YAML, quoting if necessary."""
    # Need to quote if contains special chars
    special = [':', '#', '{', '}', '[', ']', ',', '&', '*', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`', '"', "'", '\n']
    needs_quote = any(c in s for c in special) or s.startswith(' ')
    if needs_quote:
        # Use double quotes, escape internal double quotes
        escaped = s.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'
    return s

def tile_to_yaml(tile, indent):
    """Convert a tile dict to YAML lines."""
    lines = []
    if tile['link'] is None:
        lines.append(f'{indent}- title: {yaml_str(tile["title"])}')
    else:
        lines.append(f'{indent}- title: {yaml_str(tile["title"])}')
        lines.append(f'{indent}  link: {tile["link"]}')

    lines.append(f'{indent}  image: {yaml_str(tile["image"])}')

    if 'badge' in tile:
        lines.append(f'{indent}  badge: {yaml_str(tile["badge"])}')
    if 'badge_type' in tile:
        lines.append(f'{indent}  badge_type: {tile["badge_type"]}')

    return lines

def build_locale_fm_header(locale, info):
    """Build the front matter header for a locale (without feature_sections, without closing ---)."""
    return f"""locale: {info['code']}
layout: studio-home
title: {info['title']}
toc: false
permalink: {info['permalink']}
hero_compact: true
hero_title: The Ultimate Multi-Platform Character Viewer
hero_image: /images/hero.png
hero_ctas:
  - label: DOWNLOAD NOW
    url: /dancexr/download
    style: neon
nav_links:
  - label: Intro
    url: /{locale}/dancexr
  - label: Features
    url: /{locale}/dancexr/features
  - label: Releases
    url: /{locale}/dancexr/releases
  - label: Download
    url: /dancexr/download"""

def process_locale(locale, info):
    filepath = os.path.join(BASE, locale, 'dancexr', 'features.md')
    print(f'Processing {filepath}...')

    fm_str, body = read_front_matter_and_body(filepath)

    # Parse the HTML body
    sections = parse_locale_html(body, locale)

    if not sections:
        print(f'  ERROR: No sections found for {locale}!')
        return

    print(f'  Found {len(sections)} sections')
    for s in sections:
        tile_count = sum(len(sub.get('tiles', [])) for sub in s.get('subsections', [])) + len(s.get('tiles', []))
        print(f'    Section: {s["title"]} ({tile_count} tiles, {len(s.get("subsections", []))} subsections)')

    # Build new file content
    header = build_locale_fm_header(locale, info)
    sections_yaml = sections_to_yaml(sections)

    new_content = f'---\n{header}\n{sections_yaml}\n---\n'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'  Written: {len(new_content.splitlines())} lines')

def main():
    for locale, info in LOCALES.items():
        process_locale(locale, info)
    print('\nDone!')

if __name__ == '__main__':
    main()
