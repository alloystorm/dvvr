#!/usr/bin/env python3
"""
generate_features.py
====================
Generates dancexr/features.md and all four localized versions from:
  - script/features.json   (structure, badges, images, grouping)
  - dancexr/features/*.md  (EN titles, via front-matter `title:` field)
  - {locale}/dancexr/features/*.md  (localized titles)

For each tile the title is resolved in priority order:
  1. JSON `title_locales[locale]` (explicit override for this locale)
  2. JSON `title`                  (explicit EN override, also used as fallback)
  3. Markdown front-matter title   (read from {locale}/dancexr/{path}.md)

`image` and `video` fields are injected into feature-page front matters
when --inject-media is passed.

Usage:
  python script/generate_features.py [--inject-media] [--locale LOCALE]
"""

import json
import os
import re
import sys
import argparse

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOCALES = {
    "jp": {"code": "ja-JP",  "title": "機能一覧",   "permalink": "/jp/dancexr/features",
           "prefix": "/jp",
           "hero_title": "機能一覧",
           "hero_cta_label": "今すぐダウンロード",
           "hero_cta_url": "/jp/dancexr/download",
           "nav_links": [
               {"label": "イントロ",       "url": "/jp/dancexr"},
               {"label": "機能",           "url": "/jp/dancexr/features"},
               {"label": "リリース",       "url": "/jp/dancexr/releases"},
               {"label": "ダウンロード",   "url": "/jp/dancexr/download"},
               {"label": "サポート",       "url": "/jp/dancexr/support"},
           ],
           "releases_title": "リリース",
           "releases_hero_title": "リリース",
           "releases_tile_prefix": "リリース",
           "releases_latest_label": "最新リリース",
           "releases_about_title": "リリースについて",
           "releases_permalink": "/jp/dancexr/releases",
           },
    "zh": {"code": "zh-CN",  "title": "功能列表",   "permalink": "/zh/dancexr/features",
           "prefix": "/zh",
           "hero_title": "功能列表",
           "hero_cta_label": "立即下载",
           "hero_cta_url": "/zh/dancexr/download",
           "nav_links": [
               {"label": "介绍",     "url": "/zh/dancexr"},
               {"label": "功能",     "url": "/zh/dancexr/features"},
               {"label": "发布",     "url": "/zh/dancexr/releases"},
               {"label": "下载",     "url": "/zh/dancexr/download"},
               {"label": "支持",     "url": "/zh/dancexr/support"},
           ],
           "releases_title": "发行",
           "releases_hero_title": "发行",
           "releases_tile_prefix": "发布",
           "releases_latest_label": "最新发布",
           "releases_about_title": "关于发布",
           "releases_permalink": "/zh/dancexr/releases",
           },
    "tw": {"code": "zh-TW",  "title": "功能清單",   "permalink": "/tw/dancexr/features",
           "prefix": "/tw",
           "hero_title": "功能清單",
           "hero_cta_label": "立即下載",
           "hero_cta_url": "/tw/dancexr/download",
           "nav_links": [
               {"label": "介紹",     "url": "/tw/dancexr"},
               {"label": "功能",     "url": "/tw/dancexr/features"},
               {"label": "發布",     "url": "/tw/dancexr/releases"},
               {"label": "下載",     "url": "/tw/dancexr/download"},
               {"label": "支援",     "url": "/tw/dancexr/support"},
           ],
           "releases_title": "發布版本",
           "releases_hero_title": "發布版本",
           "releases_tile_prefix": "發布",
           "releases_latest_label": "最新發布",
           "releases_about_title": "關於發布",
           "releases_permalink": "/tw/dancexr/releases",
           },
    "kr": {"code": "ko-KR",  "title": "기능 목록",  "permalink": "/kr/dancexr/features",
           "prefix": "/kr",
           "hero_title": "기능 목록",
           "hero_cta_label": "지금 다운로드",
           "hero_cta_url": "/kr/dancexr/download",
           "nav_links": [
               {"label": "소개",     "url": "/kr/dancexr"},
               {"label": "기능",     "url": "/kr/dancexr/features"},
               {"label": "릴리스",   "url": "/kr/dancexr/releases"},
               {"label": "다운로드", "url": "/kr/dancexr/download"},
               {"label": "지원",     "url": "/kr/dancexr/support"},
           ],
           "releases_title": "출시",
           "releases_hero_title": "출시",
           "releases_tile_prefix": "출시",
           "releases_latest_label": "최신 출시",
           "releases_about_title": "출시 정보",
           "releases_permalink": "/kr/dancexr/releases",
           },
}

EN_NAV_LINKS = [
    {"label": "Features",  "url": "/dancexr/features"},
    {"label": "Releases",  "url": "/dancexr/releases"},
    {"label": "Download",  "url": "/dancexr/download"},
    {"label": "Support",   "url": "/dancexr/support"},
]


# ---------------------------------------------------------------------------
# Front-matter helpers
# ---------------------------------------------------------------------------

def read_front_matter(filepath):
    """Return a dict of front-matter key→value (strings only, shallow parse)."""
    if not os.path.isfile(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    m = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^(\w[\w_]*):\s*(.*)", line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip().strip('"').strip("'")
    return fm


def write_front_matter_field(filepath, key, value):
    """
    Inject or update a single scalar field in a file's YAML front matter.
    Creates the field before the closing --- if it doesn't exist.
    """
    if not os.path.isfile(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    m = re.match(r"^(---\n)(.*?)(\n---\n)", content, re.DOTALL)
    if not m:
        return
    head, body_after = m.group(0), content[m.end():]
    fm_text = m.group(2)

    # Replace existing value
    pattern = re.compile(r"^" + re.escape(key) + r":.*$", re.MULTILINE)
    if pattern.search(fm_text):
        new_fm = pattern.sub(f"{key}: {value}", fm_text)
    else:
        # Append before closing ---
        new_fm = fm_text + f"\n{key}: {value}"

    new_content = f"---\n{new_fm}\n---\n{body_after}"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)


# ---------------------------------------------------------------------------
# Title resolution
# ---------------------------------------------------------------------------

def page_filepath(path, locale=None):
    """Return absolute path to the markdown file for `path` in the given locale."""
    if locale:
        return os.path.join(BASE, locale, "dancexr", path + ".md")
    return os.path.join(BASE, "dancexr", path + ".md")


def resolve_title(tile, locale=None):
    """
    Return the display title for a tile in the given locale.
    Priority:
      1. tile["title_locales"][locale]
      2. tile["title"]
      3. front-matter title of the locale markdown
      4. front-matter title of the EN markdown
      5. path basename as last resort
    """
    if locale and "title_locales" in tile and locale in tile["title_locales"]:
        return tile["title_locales"][locale]
    if "title" in tile:
        return tile["title"]
    if "path" in tile:
        # Try locale markdown first, then EN
        fp = page_filepath(tile["path"], locale)
        fm = read_front_matter(fp)
        if fm.get("title"):
            return fm["title"]
        fp_en = page_filepath(tile["path"])
        fm_en = read_front_matter(fp_en)
        if fm_en.get("title"):
            return fm_en["title"]
        return os.path.basename(tile["path"])
    raise ValueError(f"Cannot resolve title for tile: {tile}")


def resolve_section_title(section_or_sub, locale=None):
    """Return localized section/subsection title."""
    if locale and "title_locales" in section_or_sub and locale in section_or_sub["title_locales"]:
        return section_or_sub["title_locales"][locale]
    return section_or_sub["title"]


# ---------------------------------------------------------------------------
# Link building
# ---------------------------------------------------------------------------

def resolve_link(tile, locale_prefix=""):
    """Build the URL for a tile."""
    if "path" not in tile:
        return None  # no link
    suffix = tile.get("link_suffix", "")
    return f"{locale_prefix}/dancexr/{tile['path']}{suffix}"


# ---------------------------------------------------------------------------
# YAML serialisation helpers
# ---------------------------------------------------------------------------

def yaml_str(s):
    """Quote a string for YAML if it contains special characters."""
    if s is None:
        return "null"
    # Quote if contains: : { } [ ] , & * # ? | - < > = ! % @ `
    needs_quote = any(c in s for c in ':{}[]|>&*#?!@')
    if needs_quote:
        escaped = s.replace('"', '\\"')
        return f'"{escaped}"'
    return s


def build_tile_dict(tile, locale=None, locale_prefix=""):
    """Return an ordered dict of YAML fields for a single tile."""
    result = {}
    title = resolve_title(tile, locale)
    result["title"] = title

    link = resolve_link(tile, locale_prefix)
    if link:
        result["link"] = link

    if "image" in tile:
        result["image"] = tile["image"]

    if "video" in tile:
        result["video"] = tile["video"]

    if "badge" in tile:
        result["badge"] = tile["badge"]

    if "badge_type" in tile:
        result["badge_type"] = tile["badge_type"]

    return result


def serialize_tile(tile_dict, indent=10):
    """Serialize a tile dict to indented YAML lines."""
    pad = " " * indent
    pad2 = " " * (indent + 2)
    lines = []
    for i, (k, v) in enumerate(tile_dict.items()):
        v_str = yaml_str(str(v))
        if i == 0:
            lines.append(f"{pad}- {k}: {v_str}")
        else:
            lines.append(f"{pad2}{k}: {v_str}")
    return "\n".join(lines)


def build_sections_yaml(sections_data, locale=None, locale_prefix=""):
    """Build the feature_sections YAML block as a string."""
    lines = ["feature_sections:"]
    for idx, section in enumerate(sections_data):
        sec_title = yaml_str(resolve_section_title(section, locale))
        lines.append(f"  - title: {sec_title}")
        if idx % 2 == 0:
            lines.append(f"    light: true")
        if "subsections" in section:
            lines.append(f"    subsections:")
            for sub in section["subsections"]:
                sub_title = yaml_str(resolve_section_title(sub, locale))
                lines.append(f"      - title: {sub_title}")
                lines.append(f"        tiles:")
                for tile in sub["tiles"]:
                    td = build_tile_dict(tile, locale, locale_prefix)
                    lines.append(serialize_tile(td, indent=10))
        else:
            lines.append(f"    tiles:")
            for tile in section["tiles"]:
                td = build_tile_dict(tile, locale, locale_prefix)
                lines.append(serialize_tile(td, indent=6))
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# features.md front matter templates
# ---------------------------------------------------------------------------

EN_FRONT_MATTER_TEMPLATE = """\
---
locale: en-US
layout: home
title: Feature List
toc: false
permalink: /dancexr/features
hero_compact: true
hero_title: Features
hero_image: /images/hero.png
hero_ctas:
  - label: DOWNLOAD NOW
    url: /dancexr/download
    style: neon
nav_links:
  - label: Features
    url: /dancexr/features
  - label: Releases
    url: /dancexr/releases
  - label: Download
    url: /dancexr/download
  - label: Support
    url: /dancexr/support
{sections}
---
"""

LOCALE_FRONT_MATTER_TEMPLATE = """\
---
locale: {locale_code}
layout: home
title: {title}
toc: false
permalink: {permalink}
hero_compact: true
hero_title: {hero_title}
hero_image: /images/hero.png
hero_ctas:
  - label: {hero_cta_label}
    url: {hero_cta_url}
    style: neon
nav_links:
{nav_links}
{sections}
---
"""


def build_nav_links_yaml(nav_links, indent=2):
    """Serialize nav_links list for YAML front matter."""
    pad = " " * indent
    lines = []
    for nl in nav_links:
        lines.append(f"{pad}- label: {nl['label']}")
        lines.append(f"{pad}  url: {nl['url']}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File generation
# ---------------------------------------------------------------------------

def generate_en(sections_data):
    sections_yaml = build_sections_yaml(sections_data, locale=None, locale_prefix="")
    content = EN_FRONT_MATTER_TEMPLATE.format(sections=sections_yaml)
    out_path = os.path.join(BASE, "dancexr", "features.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {os.path.relpath(out_path, BASE)}")


def generate_locale(sections_data, locale_key):
    info = LOCALES[locale_key]
    prefix = info["prefix"]
    sections_yaml = build_sections_yaml(sections_data, locale=locale_key, locale_prefix=prefix)
    nav_yaml = build_nav_links_yaml(info["nav_links"])
    content = LOCALE_FRONT_MATTER_TEMPLATE.format(
        locale_code=info["code"],
        title=info["title"],
        permalink=info["permalink"],
        hero_title=info["hero_title"],
        hero_cta_label=info["hero_cta_label"],
        hero_cta_url=info["hero_cta_url"],
        nav_links=nav_yaml,
        sections=sections_yaml,
    )
    out_path = os.path.join(BASE, locale_key, "dancexr", "features.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {os.path.relpath(out_path, BASE)}")


# ---------------------------------------------------------------------------
# Optional: inject media into feature page front matters
# ---------------------------------------------------------------------------

def count_page_lines(path):
    """Return the number of lines in the EN markdown page for `path`, or None if missing."""
    if not path:
        return None
    fp = page_filepath(path)
    if not os.path.isfile(fp):
        return None
    with open(fp, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def generate_outline(sections_data, out_path=None):
    """
    Write a concise indented list of sections and tiles (title + path + line count).
    Each section/subsection is one line; each tile is one indented line.
    Output goes to `out_path` if given, otherwise stdout.
    """
    lines = []
    for section in sections_data:
        lines.append(f"[{section['title']}]")
        if "subsections" in section:
            for sub in section["subsections"]:
                lines.append(f"  [{sub['title']}]")
                for tile in sub["tiles"]:
                    title = resolve_title(tile)
                    path = tile.get("path", "")
                    n = count_page_lines(path)
                    suffix = f"  ({n}L)" if n is not None else ""
                    lines.append(f"    - {title}  {path}{suffix}")
        else:
            for tile in section["tiles"]:
                title = resolve_title(tile)
                path = tile.get("path", "")
                n = count_page_lines(path)
                suffix = f"  ({n}L)" if n is not None else ""
                lines.append(f"  - {title}  {path}{suffix}")

    text = "\n".join(lines) + "\n"
    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Written: {os.path.relpath(out_path, BASE)}")
    else:
        print(text, end="")


def inject_media(sections_data):
    """
    For every tile that has `image` or `video`, inject those values into the
    feature page's front matter (all locales + EN).
    """
    seen = set()
    all_locales = [""] + list(LOCALES.keys())

    def inject_tile(tile):
        if "path" not in tile:
            return
        path = tile["path"]
        # Deduplicate: same path injected multiple times (e.g. camera tiles)
        key = path
        if key in seen:
            return
        seen.add(key)

        for locale in all_locales:
            fp = page_filepath(path, locale if locale else None)
            if not os.path.isfile(fp):
                continue
            if "image" in tile:
                write_front_matter_field(fp, "feature_image", tile["image"])
            if "video" in tile:
                write_front_matter_field(fp, "feature_video", tile["video"])

    def walk(sections):
        for section in sections:
            if "subsections" in section:
                for sub in section["subsections"]:
                    for tile in sub["tiles"]:
                        inject_tile(tile)
            else:
                for tile in section["tiles"]:
                    inject_tile(tile)

    walk(sections_data)
    print("Media injection complete.")


# ---------------------------------------------------------------------------
# Releases list generation
# ---------------------------------------------------------------------------

def version_sort_key(ver):
    """Return a sort key tuple for a release version string (e.g. '2026.5', '1.5.1')."""
    parts = ver.split(".")
    try:
        return tuple(int(p) for p in parts)
    except ValueError:
        return (0,)


def version_year_group(ver):
    """Return the year group label for a version string."""
    major = int(ver.split(".")[0])
    if major >= 2024:
        return str(major)
    # Legacy versioning (1.x.x) all belong to 2023
    return "2023"


def collect_releases():
    """
    Scan dancexr/releases/ for .md files and return:
      - releases_by_year: OrderedDict {year_str: [version, ...]} newest-first
      - latest_version: str
    """
    releases_dir = os.path.join(BASE, "dancexr", "releases")
    versions = []
    for fname in os.listdir(releases_dir):
        if fname.endswith(".md"):
            versions.append(fname[:-3])  # strip .md

    # Sort newest first
    versions.sort(key=version_sort_key, reverse=True)

    # Group by year
    from collections import OrderedDict
    releases_by_year = OrderedDict()
    for ver in versions:
        yr = version_year_group(ver)
        releases_by_year.setdefault(yr, []).append(ver)

    latest = versions[0] if versions else None
    return releases_by_year, latest


def extract_release_subtitle(version):
    """
    Return the first notable heading from the release file (excluding the title/version line).
    Returns empty string if nothing found.
    """
    fp = os.path.join(BASE, "dancexr", "releases", version + ".md")
    if not os.path.isfile(fp):
        return ""
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    for line in content.splitlines():
        m = re.match(r"^#{1,4}\s+(.*)", line)
        if m:
            heading = m.group(1).strip()
            # Skip headings that are just the release title or version number
            if version in heading or re.match(r"^[Rr]elease\s+\d", heading):
                continue
            return heading
    return ""


def build_releases_sections_yaml(releases_by_year, locale_prefix="", tile_prefix="Release"):
    """Build the feature_sections YAML block for a releases page."""
    lines = ["feature_sections:"]
    for idx, (year, versions) in enumerate(releases_by_year.items()):
        lines.append(f'  - title: "{year}"')
        if idx % 2 == 0:
            lines.append(f"    light: true")
        lines.append(f"    tiles:")
        for ver in versions:
            title = f"{tile_prefix} {ver}"
            link = f"{locale_prefix}/dancexr/releases/{ver}"
            lines.append(f'      - title: "{title}"')
            lines.append(f'        link: "{link}"')
    return "\n".join(lines)


EN_RELEASES_TEMPLATE = """\
---
locale: en-US
layout: home
title: Releases
toc: false
permalink: /dancexr/releases
hero_compact: true
hero_title: Latest Release - {latest_version}
hero_sub: {hero_sub}
hero_image: /images/hero.png
hero_ctas:
  - label: Full Release Notes
    url: /dancexr/releases/{latest_version}
    style: neon
  - label: DOWNLOAD NOW
    url: /dancexr/download
    style: neon
nav_links:
  - label: Features
    url: /dancexr/features
  - label: Releases
    url: /dancexr/releases
  - label: Download
    url: /dancexr/download
  - label: Support
    url: /dancexr/support
{sections}
about:
  - title: About Releases
    url: /dancexr/releases

---
"""

LOCALE_RELEASES_TEMPLATE = """\
---
locale: {locale_code}
layout: home
title: {title}
toc: false
permalink: {permalink}
hero_compact: true
hero_title: {hero_title}
hero_image: /images/hero.png
nav_links:
{nav_links}
{sections}
about:
  - title: {about_title}
    url: {permalink}

---

<section class="section">
<div class="section-inner">
<div class="edition-card" markdown="1">

{{% include nav_list nav="releases" %}}

</div>
</div>
</section>"""


def generate_releases_en(releases_by_year, latest_version):
    hero_sub = extract_release_subtitle(latest_version) if latest_version else ""
    sections_yaml = build_releases_sections_yaml(releases_by_year, locale_prefix="", tile_prefix="Release")
    content = EN_RELEASES_TEMPLATE.format(
        latest_version=latest_version,
        hero_sub=hero_sub,
        sections=sections_yaml,
    )
    out_path = os.path.join(BASE, "dancexr", "releases.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {os.path.relpath(out_path, BASE)}")


def generate_releases_locale(releases_by_year, locale_key):
    info = LOCALES[locale_key]
    prefix = info["prefix"]
    tile_prefix = info["releases_tile_prefix"]
    sections_yaml = build_releases_sections_yaml(releases_by_year, locale_prefix=prefix, tile_prefix=tile_prefix)
    nav_yaml = build_nav_links_yaml(info["nav_links"])
    content = LOCALE_RELEASES_TEMPLATE.format(
        locale_code=info["code"],
        title=info["releases_title"],
        permalink=info["releases_permalink"],
        hero_title=info["releases_hero_title"],
        about_title=info["releases_about_title"],
        nav_links=nav_yaml,
        sections=sections_yaml,
    )
    out_path = os.path.join(BASE, locale_key, "dancexr", "releases.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {os.path.relpath(out_path, BASE)}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate features.md files from features.json")
    parser.add_argument(
        "--inject-media",
        action="store_true",
        help="Also inject feature_image / feature_video into feature page front matters",
    )
    parser.add_argument(
        "--locale",
        choices=list(LOCALES.keys()) + ["en"],
        default=None,
        help="Generate only this locale (default: all)",
    )
    parser.add_argument(
        "--outline",
        nargs="?",
        const="-",
        metavar="FILE",
        help="Print a concise indented outline (title + path). "
             "Optionally write to FILE; omit FILE to print to stdout.",
    )
    parser.add_argument(
        "--releases",
        action="store_true",
        help="Generate releases.md (EN + all locales) from dancexr/releases/ directory",
    )
    parser.add_argument(
        "--features-only",
        action="store_true",
        help="Generate only features pages (skip releases generation)",
    )
    args = parser.parse_args()

    # -----------------------------------------------------------------------
    # Releases generation
    # -----------------------------------------------------------------------
    gen_releases = args.releases or (not args.features_only and not args.outline)
    gen_features = not args.releases or args.features_only or (not args.releases and not args.features_only)
    # Default: generate both unless a specific flag limits scope
    if not args.releases and not args.features_only:
        gen_features = True
        gen_releases = False  # keep backward-compatible default: features only unless --releases given

    if args.releases:
        releases_by_year, latest = collect_releases()
        locales_to_gen = list(LOCALES.keys())
        gen_en = True
        if args.locale:
            if args.locale == "en":
                locales_to_gen = []
                gen_en = True
            else:
                locales_to_gen = [args.locale]
                gen_en = False
        if gen_en:
            generate_releases_en(releases_by_year, latest)
        for locale_key in locales_to_gen:
            generate_releases_locale(releases_by_year, locale_key)

    # -----------------------------------------------------------------------
    # Features generation
    # -----------------------------------------------------------------------
    if not args.releases or args.features_only:
        json_path = os.path.join(BASE, "script", "features.json")
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        sections = data["sections"]

        if args.outline is not None:
            out = None if args.outline == "-" else os.path.join(BASE, args.outline)
            generate_outline(sections, out)
            return

        locales_to_gen = list(LOCALES.keys())
        gen_en = True
        if args.locale:
            if args.locale == "en":
                locales_to_gen = []
                gen_en = True
            else:
                locales_to_gen = [args.locale]
                gen_en = False

        if gen_en:
            generate_en(sections)
        for locale_key in locales_to_gen:
            generate_locale(sections, locale_key)

        if args.inject_media:
            inject_media(sections)


if __name__ == "__main__":
    main()
