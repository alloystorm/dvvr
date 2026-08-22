#!/usr/bin/env python3
"""Audit the Jekyll source for broken internal links and missing content.

Checks:
  1. Markdown / HTML / CSS / YAML internal links resolve to a real file.
  2. Locale parity: every page in dancexr/ exists in jp/zh/tw/kr mirrors.
  3. Extra pages in mirrors that have no English source.

Excludes: _site, .git, .jekyll-cache, .claude, .vscode.
"""
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {"_site", ".git", ".jekyll-cache", ".claude", ".vscode", "node_modules"}

SKIP_PREFIXES = (
    "http://", "https://", "mailto:", "tel:", "javascript:", "data:", "#",
    "ftp://", "discord:", "steam:", "itch:", "steamlink:",
)

# ---------------------------------------------------------------- inventory
all_files = set()
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
    for f in filenames:
        rel = (Path(dirpath) / f).relative_to(ROOT).as_posix()
        all_files.add(rel)

ci_files = {f.lower(): f for f in all_files}  # for case-mismatch detection

def is_candidate(rel: str, is_page_link: bool) -> bool:
    if rel in all_files:
        return True
    if is_page_link:
        if rel + ".md" in all_files:
            return True
        if rel + "/index.md" in all_files:
            return True
        if rel.rstrip("/") + ".md" in all_files:
            return True
    return False

def resolve(target: str, base_dir: str, is_page_link: bool):
    """Return (status, detail) for an internal link target."""
    t = unquote(target.split("#", 1)[0].split("?", 1)[0]).strip()
    if not t:
        return "ok", ""
    if t.startswith("/"):
        p = t.lstrip("/")
    else:
        p = os.path.normpath(os.path.join(base_dir, t)).replace("\\", "/")
    # trailing slash -> directory index
    if p.endswith("/"):
        p = p.rstrip("/")
    if is_candidate(p, is_page_link):
        return "ok", ""
    # case mismatch?
    if p.lower() in ci_files:
        return "case-mismatch", f"{p} -> {ci_files[p.lower()]}"
    return "broken", ""

# ---------------------------------------------------------------- extraction
MD_LINK_RE = re.compile(r"\]\(\s*<?([^)<>\s]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HTML_ATTR_RE = re.compile(r"\b(?:href|src)\s*=\s*[\"']([^\"']+)[\"']", re.I)
CSS_URL_RE = re.compile(r"url\(\s*[\"']?([^\"')]+)[\"']?\s*\)", re.I)
YAML_URL_RE = re.compile(r"^\s*(?:url|icon_url|src|link|permalink)\s*:\s*[\"']?([^\"'\n]+)", re.M)

def extract(path: Path) -> list[tuple[int, str]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    found = []
    lines = text.splitlines()
    if path.suffix in (".md", ".html"):
        for m in MD_LINK_RE.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            found.append((line, m.group(1)))
        for m in HTML_ATTR_RE.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            found.append((line, m.group(1)))
    if path.suffix == ".scss" or path.suffix == ".css":
        for m in CSS_URL_RE.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            found.append((line, m.group(1)))
    if path.suffix in (".yml", ".yaml", ".json"):
        for m in YAML_URL_RE.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            found.append((line, m.group(1)))
    return found

# ---------------------------------------------------------------- link audit
results = {"broken": [], "case": [], "external": [], "skipped_liquid": []}
scanned = 0
for rel in sorted(all_files):
    p = ROOT / rel
    suffix = p.suffix.lower()
    if suffix not in (".md", ".html", ".scss", ".css", ".yml", ".yaml"):
        continue
    if rel.startswith("_data/ui-text"):
        # UI strings may legitimately contain example paths; still check
        pass
    scanned += 1
    base_dir = os.path.dirname(rel)
    for line, url in extract(p):
        u = url.strip()
        if any(u.startswith(s) for s in SKIP_PREFIXES):
            if u.startswith(("http://", "https://")):
                results["external"].append((rel, line, u))
            continue
        if "{{" in u or "{%" in u:
            results["skipped_liquid"].append((rel, line, u))
            continue
        is_page = not u.lower().endswith(
            (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico",
             ".mp4", ".webm", ".mp3", ".ogg", ".json", ".txt", ".xml",
             ".zip", ".zipx", ".vmd", ".pmx", ".bvh", ".xps", ".css",
             ".js", ".woff", ".woff2", ".ttf", ".eot", ".wasm", ".glb",
             ".hdr", ".exr", ".ktx2", ".ktx", ".cube", ".dds"))
        status, detail = resolve(u, base_dir, is_page)
        if status == "broken":
            results["broken"].append((rel, line, url))
        elif status == "case-mismatch":
            results["case"].append((rel, line, url, detail))

# ------------------------------------------------------------ locale parity
LOCALES = {"jp": "Japanese", "zh": "Simplified Chinese", "tw": "Traditional Chinese", "kr": "Korean"}
def page_tree(prefix: str) -> set[str]:
    out = set()
    base = prefix.rstrip("/") + "/"
    for f in all_files:
        if f.startswith(base) and f.endswith(".md"):
            out.add(f[len(base):])
    return out

en = page_tree("dancexr")
parity = {}
for loc, name in LOCALES.items():
    loc_pages = page_tree(f"{loc}/dancexr")
    missing = sorted(en - loc_pages)
    extra = sorted(loc_pages - en)
    parity[name] = {"missing_in": missing, "extra_in": extra}

# ---------------------------------------------------------------- report
out = {
    "scanned_files": scanned,
    "external_links": len(results["external"]),
    "liquid_skipped": len(results["skipped_liquid"]),
    "broken_links": results["broken"],
    "case_mismatches": results["case"],
    "locale_parity": parity,
}
print(json.dumps(out, indent=2, ensure_ascii=False))
