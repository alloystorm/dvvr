from __future__ import annotations

import argparse
from pathlib import Path
import sys


DEFAULT_ROOTS = [
    "dancexr",
    "jp/dancexr",
    "zh/dancexr",
    "tw/dancexr",
    "kr/dancexr",
]

LOCALE_NAV_LINKS = {
    "en": [
        ("Intro", "/dancexr"),
        ("Features", "/dancexr/features"),
        ("Releases", "/dancexr/releases"),
        ("Download", "/dancexr/download"),
    ],
    "jp": [
        ("イントロ", "/jp/dancexr"),
        ("機能", "/jp/dancexr/features"),
        ("リリース", "/jp/dancexr/releases"),
        ("ダウンロード", "/jp/dancexr/download"),
    ],
    "zh": [
        ("简介", "/zh/dancexr"),
        ("功能", "/zh/dancexr/features"),
        ("发布", "/zh/dancexr/releases"),
        ("下载", "/zh/dancexr/download"),
    ],
    "tw": [
        ("簡介", "/tw/dancexr"),
        ("功能", "/tw/dancexr/features"),
        ("發布", "/tw/dancexr/releases"),
        ("下載", "/tw/dancexr/download"),
    ],
    "kr": [
        ("소개", "/kr/dancexr"),
        ("기능", "/kr/dancexr/features"),
        ("출시", "/kr/dancexr/releases"),
        ("다운로드", "/kr/dancexr/download"),
    ],
}

ORDERED_KEYS = ["layout", "title", "locale", "nav_links"]


def split_front_matter(text: str) -> tuple[list[str] | None, str]:
    if not text.startswith("---\n"):
        return None, text

    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text

    front_matter = text[4:end].splitlines()
    body = text[end + 5 :]
    return front_matter, body


def parse_blocks(front_matter_lines: list[str]) -> list[tuple[str, list[str]]]:
    blocks: list[tuple[str, list[str]]] = []
    index = 0
    comment_index = 0

    while index < len(front_matter_lines):
        line = front_matter_lines[index]
        if not line.strip():
            index += 1
            continue

        if line.lstrip().startswith("#"):
            blocks.append((f"__comment_{comment_index}", [line]))
            comment_index += 1
            index += 1
            continue

        if line.startswith((" ", "\t")):
            raise ValueError(f"Unexpected indented top-level front matter line: {line}")

        key, sep, _ = line.partition(":")
        if not sep:
            raise ValueError(f"Unsupported front matter line: {line}")

        block = [line]
        index += 1

        while index < len(front_matter_lines):
            next_line = front_matter_lines[index]
            if next_line and not next_line.startswith((" ", "\t")):
                break
            block.append(next_line)
            index += 1

        blocks.append((key.strip(), block))

    return blocks


def detect_locale(path: Path) -> str:
    first_part = path.parts[0]
    if first_part in LOCALE_NAV_LINKS:
        return first_part
    return "en"


def build_nav_links_block(locale: str) -> list[str]:
    nav_lines = ["nav_links:"]
    for label, url in LOCALE_NAV_LINKS[locale]:
        nav_lines.append(f"  - label: {label}")
        nav_lines.append(f"    url: {url}")
    return nav_lines


def rewrite_front_matter(path: Path, front_matter_lines: list[str]) -> list[str] | None:
    blocks = parse_blocks(front_matter_lines)
    block_map: dict[str, list[str]] = {}
    preserved_order: list[str] = []
    layout_is_single = False

    for key, lines in blocks:
        if key == "layout" and any(line.strip() == "layout: single" for line in lines):
            layout_is_single = True
        if key in {"toc", "sidebar", "nav_links"}:
            continue
        if key == "layout":
            block_map[key] = ["layout: release"]
        else:
            block_map[key] = lines
        if key not in preserved_order:
            preserved_order.append(key)

    if not layout_is_single:
        return None

    if "layout" not in block_map:
        block_map["layout"] = ["layout: release"]

    locale = detect_locale(path)
    block_map["nav_links"] = build_nav_links_block(locale)

    ordered_keys: list[str] = []
    for key in ORDERED_KEYS:
        if key in block_map:
            ordered_keys.append(key)
    for key in preserved_order:
        if key in block_map and key not in ordered_keys:
            ordered_keys.append(key)

    output_lines: list[str] = []
    for key in ordered_keys:
        output_lines.extend(block_map[key])

    return output_lines


def iter_markdown_files(root: Path, roots: list[str]) -> list[Path]:
    files: list[Path] = []
    for relative_root in roots:
        search_root = root / relative_root
        if not search_root.exists():
            continue
        files.extend(sorted(search_root.rglob("*.md")))
    return files


def process_file(path: Path, repo_root: Path, dry_run: bool) -> bool:
    original_text = path.read_text(encoding="utf-8")
    front_matter_lines, body = split_front_matter(original_text)
    if front_matter_lines is None:
        return False

    relative_path = path.relative_to(repo_root)
    updated_front_matter = rewrite_front_matter(relative_path, front_matter_lines)
    if updated_front_matter is None:
        return False

    updated_text = "---\n" + "\n".join(updated_front_matter) + "\n---\n" + body
    if updated_text == original_text:
        return False

    print(relative_path.as_posix())
    if not dry_run:
        path.write_text(updated_text, encoding="utf-8")
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Convert DanceXR Markdown pages from layout: single to layout: release, "
            "remove toc/sidebar, and add locale-specific nav_links."
        )
    )
    parser.add_argument(
        "--root",
        dest="roots",
        action="append",
        help="Relative docs root to scan. Can be passed multiple times.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write changes in place. Without this flag, the script only prints files that would change.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    roots = args.roots or DEFAULT_ROOTS

    changed_count = 0
    for path in iter_markdown_files(repo_root, roots):
        if process_file(path, repo_root, dry_run=not args.write):
            changed_count += 1

    action = "Would update" if not args.write else "Updated"
    print(f"{action} {changed_count} file(s).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())