#!/usr/bin/env python3
"""
fix_links.py
============
Convert absolute /dancexr/... and /<locale>/dancexr/... links inside the body of
Markdown pages into relative links, so the same source content works in any
locale without per-locale URL editing.

Why:
  Localized pages (jp/, zh/, tw/, kr/) have historically used absolute paths
  like (/dancexr/support), which point at the EN page even when a localized
  version exists. Relative links resolve correctly under whichever locale the
  page lives in.

What is converted:
  * Markdown links:  ](/dancexr/X)   ->  ](X)  (or ../X / ../../X based on depth)
  * HTML href:       href="/dancexr/X" -> href="X"  (same)
  * For pages under a locale, /<own_locale>/dancexr/X is also converted.
  * Cross-locale links (e.g. /zh/dancexr/X from a jp/ page) are left alone —
    they are presumed intentional.

What is NOT touched:
  * Frontmatter (everything between the opening and closing --- markers),
    so permalink:, lang_path:, hero_ctas: URLs etc. all stay as authored.
  * External URLs and anchor-only links (#section).
  * Image references (/images/...).
  * features.md and releases.md naturally have empty bodies (all data sits in
    frontmatter), so the script makes no body changes there.

Usage:
  python script/fix_links.py --dry-run        # preview
  python script/fix_links.py                  # apply
  python script/fix_links.py --locale jp      # restrict to one locale
"""

import os
import posixpath
import re
import sys
import argparse

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOCALES = ["", "jp", "zh", "tw", "kr"]  # "" = EN

# Match /dancexr/X or /<locale>/dancexr/X — the captured URL includes whichever
# leading prefix is present.
URL_PATTERN = r'(/(?:(?:jp|zh|tw|kr)/)?dancexr/[^)\s\'"#?]*(?:[#?][^)\s\'"]*)?)'

MD_LINK_RE = re.compile(r'\]\(' + URL_PATTERN + r'\)')
HTML_HREF_RE = re.compile(r'''href=(["'])''' + URL_PATTERN + r'''\1''')

LOCALE_PREFIX_RE = re.compile(r'^/(jp|zh|tw|kr)/')


# ---------------------------------------------------------------------------
# Frontmatter handling
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r'^(---\n.*?\n---\n)', re.DOTALL)


def split_frontmatter(content):
    """Return (frontmatter, body). Frontmatter includes the closing --- and trailing newline."""
    m = FRONTMATTER_RE.match(content)
    if m:
        return m.group(1), content[m.end():]
    return "", content


# ---------------------------------------------------------------------------
# URL transformation
# ---------------------------------------------------------------------------

def url_locale(url):
    """Return locale code from URL ('jp', 'zh', 'tw', 'kr') or '' for EN/unprefixed."""
    m = LOCALE_PREFIX_RE.match(url)
    return m.group(1) if m else ""


def strip_locale_prefix(url):
    """Drop a leading /<locale>/ prefix if present, leaving /dancexr/..."""
    m = LOCALE_PREFIX_RE.match(url)
    if m:
        return url[m.end() - 1:]  # keep the leading slash before "dancexr"
    return url


def src_path_in_dancexr(filepath, locale):
    """
    Path of the source page relative to its dancexr/ root, sans .md extension.
    e.g. 'getting-started', 'features/morph_list', 'releases/2025.9'.
    """
    if locale:
        root = os.path.join(BASE, locale, "dancexr")
    else:
        root = os.path.join(BASE, "dancexr")
    rel = os.path.relpath(filepath, root).replace(os.sep, "/")
    if rel.endswith(".md"):
        rel = rel[:-3]
    return rel


def transform_url(url, src_path, page_locale):
    """
    Decide whether to relativize this URL. Returns (new_url, changed_flag).

    Convert if:
      - URL has no locale prefix (EN form /dancexr/X) — common case across
        every page, including localized pages that historically linked to EN
        absolute paths. Relativizing makes the link resolve under the page's
        own locale.
      - URL has the same locale prefix as the page (correct absolute form).

    Leave alone if:
      - URL has a *different* locale prefix (genuine cross-locale link).
    """
    target_locale = url_locale(url)
    if target_locale != "" and target_locale != page_locale:
        return url, False

    bare = strip_locale_prefix(url)
    if not bare.startswith("/dancexr"):
        return url, False

    # Split target into pure path + anchor/query suffix
    suffix = ""
    path_part = bare
    for sep in "#?":
        i = path_part.find(sep)
        if i != -1:
            suffix = path_part[i:]
            path_part = path_part[:i]
            break

    # Compute relative path in /dancexr/ URL space
    src_url = "/dancexr/" + src_path  # source URL ignoring permalink overrides
    src_dir = posixpath.dirname(src_url)
    if not src_dir:
        src_dir = "/"

    rel = posixpath.relpath(path_part, src_dir)
    if rel == ".":
        rel = "./"

    return rel + suffix, True


# ---------------------------------------------------------------------------
# File processing
# ---------------------------------------------------------------------------

def process_body(body, src_path, page_locale):
    """Apply URL transformation to all matched patterns in the body. Returns (new_body, count)."""
    count = 0

    def md_repl(match):
        nonlocal count
        url = match.group(1)
        new_url, changed = transform_url(url, src_path, page_locale)
        if changed:
            count += 1
        return f']({new_url})'

    def html_repl(match):
        nonlocal count
        quote = match.group(1)
        url = match.group(2)
        new_url, changed = transform_url(url, src_path, page_locale)
        if changed:
            count += 1
        return f'href={quote}{new_url}{quote}'

    body = MD_LINK_RE.sub(md_repl, body)
    body = HTML_HREF_RE.sub(html_repl, body)
    return body, count


def find_md_files(locale_filter=None):
    """Return list of (filepath, locale) for every .md file under dancexr/ in each locale."""
    files = []
    for locale in LOCALES:
        if locale_filter is not None and locale != locale_filter:
            continue
        if locale:
            root = os.path.join(BASE, locale, "dancexr")
        else:
            root = os.path.join(BASE, "dancexr")
        if not os.path.isdir(root):
            continue
        for dirpath, _, fnames in os.walk(root):
            for f in sorted(fnames):
                if f.endswith(".md"):
                    files.append((os.path.join(dirpath, f), locale))
    return files


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would change without writing.")
    parser.add_argument("--locale", choices=LOCALES, default=None,
                        help="Restrict to one locale. '' = EN. (default: all locales)")
    parser.add_argument("--verbose", action="store_true",
                        help="Print each link transformation.")
    args = parser.parse_args()

    files = find_md_files(args.locale)
    total_files_changed = 0
    total_links_changed = 0

    for filepath, locale in files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        fm, body = split_frontmatter(content)
        src_path = src_path_in_dancexr(filepath, locale)
        new_body, count = process_body(body, src_path, locale)
        if count > 0:
            total_files_changed += 1
            total_links_changed += count
            rel = os.path.relpath(filepath, BASE)
            tag = "[dry-run]" if args.dry_run else "[update]"
            print(f"{tag} {rel}: {count} link(s)")
            if args.verbose:
                # Show a quick before/after diff for the first few
                before_links = MD_LINK_RE.findall(body) + HTML_HREF_RE.findall(body)
                # findall returns the captures; HTML returns tuples, MD returns strings
                # Skip detailed diff to keep output light
                pass
            if not args.dry_run:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(fm + new_body)

    verb = "would update" if args.dry_run else "updated"
    print(f"\nSummary: {verb} {total_links_changed} link(s) across {total_files_changed} file(s).")
    if args.dry_run and total_links_changed > 0:
        print("Run without --dry-run to apply.")


if __name__ == "__main__":
    main()
