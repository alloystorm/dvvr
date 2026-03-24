#!/usr/bin/env python3
"""
Sync the slideshows: front matter in dancexr/index.md with the actual
contents of images/slideshows/<section>/ folders.

Usage:
    python script/update_slideshows.py [--dry-run]

- Adds new images found on disk.
- Removes paths whose files no longer exist.
- Preserves the existing order for files that are still present.
- New files are appended at the end of their section list.
- Sections present in the front matter but with no matching folder are
  left as empty lists (not removed).
- Folders on disk that have no matching key in the front matter are
  reported but not auto-added (avoids silently adding stray folders).
"""

import argparse
import re
import urllib.parse
from pathlib import Path

REPO_ROOT   = Path(__file__).parent.parent
SLIDES_ROOT = REPO_ROOT / "images" / "slideshows"

INDEX_FILES = [
    REPO_ROOT / "dancexr" / "index.md",
    REPO_ROOT / "jp" / "dancexr" / "index.md",
    REPO_ROOT / "zh" / "dancexr" / "index.md",
    REPO_ROOT / "tw" / "dancexr" / "index.md",
    REPO_ROOT / "kr" / "dancexr" / "index.md",
]

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def folder_paths(section: str) -> list[str]:
    """Return sorted URL-encoded paths for all images in a section folder."""
    folder = SLIDES_ROOT / section
    if not folder.is_dir():
        return []
    files = sorted(f.name for f in folder.iterdir() if f.suffix.lower() in IMAGE_EXTS)
    return [f"/images/slideshows/{section}/{urllib.parse.quote(f, safe='.-_')}" for f in files]


def parse_slideshows_block(text: str) -> tuple[int, int, dict[str, list[str]]]:
    """
    Find the slideshows: block in the front matter and return
    (start_line_index, end_line_index, {section: [paths]}).
    Line indices are into text.splitlines(), end is exclusive.
    """
    lines = text.splitlines()

    # Locate the front matter (between the two --- markers)
    fm_end = lines.index("---", 1)

    # Find "slideshows:" inside the front matter
    sw_start = None
    for i, line in enumerate(lines[:fm_end]):
        if re.match(r"^slideshows:\s*$", line):
            sw_start = i
            break
    if sw_start is None:
        raise ValueError("No 'slideshows:' key found in front matter")

    # Collect section lines until the next top-level key or end of front matter
    sections: dict[str, list[str]] = {}
    current_section = None
    sw_end = fm_end  # default: runs to end of front matter

    for i in range(sw_start + 1, fm_end):
        line = lines[i]
        # Top-level key (not indented, not a comment) → end of slideshows block
        if line and not line.startswith(" ") and not line.startswith("#"):
            sw_end = i
            break
        # Section key: "  section_name:"
        m = re.match(r"^  (\w+):\s*$", line)
        if m:
            current_section = m.group(1)
            sections[current_section] = []
            continue
        # Path entry: "    - '...'"
        m = re.match(r"^    - '(.+)'", line)
        if m and current_section is not None:
            sections[current_section].append(m.group(1))

    return sw_start, sw_end, sections


def build_slideshows_block(sections: dict[str, list[str]]) -> list[str]:
    lines = [
        "# ── Slideshow image lists ─────────────────────────────────────",
        "# Each key matches a {% include slideshow.html slides=page.slideshows.KEY %} call below.",
        "slideshows:",
    ]
    for section, paths in sections.items():
        if paths:
            lines.append(f"  {section}:")
            for p in paths:
                lines.append(f"    - '{p}'")
        else:
            lines.append(f"  {section}: []")
    return lines


def process_index(index_md: Path, updated_sections: dict[str, list[str]], dry_run: bool) -> None:
    text = index_md.read_text(encoding="utf-8")
    lines = text.splitlines()

    sw_start, sw_end, _ = parse_slideshows_block(text)

    # Walk back from sw_start to remove preceding comment lines
    block_start = sw_start
    while block_start > 0 and lines[block_start - 1].startswith("#"):
        block_start -= 1

    new_block_lines = build_slideshows_block(updated_sections)
    new_lines = lines[:block_start] + new_block_lines + lines[sw_end:]
    new_text = "\n".join(new_lines) + "\n"

    if dry_run:
        print(f"\n--- {index_md.relative_to(REPO_ROOT)} ---")
        print("\n".join(new_block_lines))
        return

    if new_text == text:
        print(f"Already up to date: {index_md.relative_to(REPO_ROOT)}")
        return

    index_md.write_text(new_text, encoding="utf-8")
    print(f"Updated {index_md.relative_to(REPO_ROOT)}")


def main():
    parser = argparse.ArgumentParser(description="Sync slideshow paths in all dancexr index pages")
    parser.add_argument("--dry-run", action="store_true", help="Print diff without writing")
    args = parser.parse_args()

    # Derive updated sections from the primary (English) index
    primary = INDEX_FILES[0]
    text = primary.read_text(encoding="utf-8")
    _, _, old_sections = parse_slideshows_block(text)

    unknown_folders: list[str] = []

    # Check for folders on disk with no matching front matter key
    if SLIDES_ROOT.is_dir():
        known = set(old_sections.keys())
        for folder in sorted(SLIDES_ROOT.iterdir()):
            if folder.is_dir() and folder.name not in known:
                unknown_folders.append(folder.name)

    # For each existing section: keep present files in order, append new ones
    updated_sections: dict[str, list[str]] = {}
    for section, old_paths in old_sections.items():
        disk_paths = set(folder_paths(section))
        kept = [p for p in old_paths if p in disk_paths]
        new = [p for p in sorted(disk_paths) if p not in set(old_paths)]
        updated_sections[section] = kept + new

    # Report & summarise changes
    added = removed = 0
    for section in old_sections:
        old = set(old_sections[section])
        new = set(updated_sections[section])
        added   += len(new - old)
        removed += len(old - new)

    print(f"Sections: {len(updated_sections)}  |  Added: {added}  |  Removed: {removed}")
    if unknown_folders:
        print(f"Unknown folders (not in front matter, skipped): {', '.join(unknown_folders)}")

    for index_md in INDEX_FILES:
        process_index(index_md, updated_sections, args.dry_run)


if __name__ == "__main__":
    main()
