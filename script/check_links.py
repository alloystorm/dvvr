#!/usr/bin/env python3
"""Dead-link checker and orphan-page detector for DanceXR docs.

Usage: python3 check_links.py SITE_DIR [--external [BASE_URL]]

Crawls SITE_DIR HTML files directly (no HTTP server needed), reports internal
pages that cannot be resolved to a file, and reports pages present in SITE_DIR
that were never reached from the home page.

When --external is given, BASE_URL is used to identify internal vs external
links for HTTP HEAD checks (e.g. http://localhost:4000).
"""
import sys
import re
from collections import deque
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.parse import urljoin, urlparse

SKIP_PREFIXES = ("/assets/",)
SKIP_EXACT = frozenset({
    "/feed.xml", "/sitemap.xml", "/robots.txt",
    "/404", "/redirect",
})


def canonical_path(path: str) -> str:
    """Normalise a URL path: strip index.html, .html extension, trailing slash."""
    path = re.sub(r"/index\.html$", "/", path)
    path = path.replace("\\", "/")
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")
    if path.endswith(".html"):
        path = path[:-5]
    return path or "/"


def should_skip(path: str) -> bool:
    return path in SKIP_EXACT or any(path.startswith(p) for p in SKIP_PREFIXES)


def path_to_file(site_dir: Path, url_path: str) -> Path | None:
    """Resolve a URL path to an HTML file inside site_dir, or None if missing."""
    rel = url_path.lstrip("/").replace("/", "/")
    candidates = [
        site_dir / rel,                        # exact
        site_dir / rel / "index.html",         # directory index
        Path(str(site_dir / rel) + ".html"),   # .html extension
    ]
    for c in candidates:
        if c.is_file():
            return c
    return None


def main() -> None:
    check_external = "--external" in sys.argv
    pos_args = [a for a in sys.argv[1:] if not a.startswith("--")]

    # Accept both old-style "BASE_URL SITE_DIR" and new-style "SITE_DIR"
    if len(pos_args) == 0:
        print("Usage: check_links.py SITE_DIR [--external [BASE_URL]]", file=sys.stderr)
        sys.exit(2)
    if len(pos_args) >= 2:
        # Old-style: first arg looks like a URL
        site_dir = Path(pos_args[1])
        base_netloc = urlparse(pos_args[0]).netloc
    else:
        site_dir = Path(pos_args[0])
        base_netloc = ""

    if not site_dir.is_dir():
        print(f"Error: SITE_DIR '{site_dir}' does not exist.", file=sys.stderr)
        sys.exit(2)

    # path -> True (ok) | False (missing) | None (queued)
    visited: dict[str, object] = {}
    # path -> canonical path of first page that linked here
    first_referrer: dict[str, str] = {}
    # external URL -> status
    ext_checked: dict[str, object] = {}

    queue: deque[tuple[str, str | None]] = deque()
    start = canonical_path("/")
    visited[start] = None
    queue.append((start, None))

    total = 0
    print(f"Crawling {site_dir} ...")

    while queue:
        path, ref = queue.popleft()

        if ref is not None and path not in first_referrer:
            first_referrer[path] = ref

        if should_skip(path):
            visited[path] = True
            continue

        # Resolve to file
        html_file = path_to_file(site_dir, path)
        if html_file is None:
            visited[path] = False   # broken link
            continue

        visited[path] = True
        total += 1
        print(f"  {total} pages crawled\r", end="")

        body = html_file.read_text(encoding="utf-8", errors="ignore")

        # Extract hrefs
        for raw_href in re.findall(r'href=["\']([^"\']+)["\']', body):
            href = raw_href.split("#")[0].strip()
            if not href or href.startswith(("mailto:", "javascript:")):
                continue

            parsed = urlparse(href)
            if parsed.scheme in ("http", "https"):
                # External link
                if check_external and (not base_netloc or parsed.netloc != base_netloc):
                    url_no_frag = href.split("#")[0]
                    if url_no_frag not in ext_checked:
                        ext_checked[url_no_frag] = None
                        try:
                            req = Request(
                                url_no_frag, method="HEAD",
                                headers={"User-Agent": "DanceXR-link-checker/1.0"},
                            )
                            with urlopen(req, timeout=10) as r:
                                ext_checked[url_no_frag] = r.status
                        except HTTPError as e:
                            ext_checked[url_no_frag] = e.code
                        except Exception as e:
                            ext_checked[url_no_frag] = f"ERR:{e}"
                elif check_external and base_netloc and parsed.netloc == base_netloc:
                    # Treat as internal by path
                    norm = canonical_path(parsed.path)
                    if norm not in visited:
                        visited[norm] = None
                        queue.append((norm, path))
            elif not parsed.scheme:
                # Relative or absolute-path link — internal
                if parsed.path.startswith("/"):
                    norm = canonical_path(parsed.path)
                else:
                    # Relative: resolve against current file's directory path
                    base = str(html_file.relative_to(site_dir)).replace("\\", "/")
                    base_dir = "/" + base.rsplit("/", 1)[0] + "/" if "/" in base else "/"
                    norm = canonical_path(urljoin(base_dir, parsed.path))
                if norm not in visited:
                    visited[norm] = None
                    queue.append((norm, path))

    print(f"  {total} pages crawled")

    # ── Dead internal links ──────────────────────────────────────────────────
    dead = sorted(p for p, ok in visited.items() if ok is False)
    if dead:
        print(f"\nDead links — internal ({len(dead)}):")
        for path in dead:
            ref = first_referrer.get(path, "?")
            print(f"  [404] {path}  ← {ref}")
    else:
        print("\nNo dead internal links.")

    # ── Dead external links ──────────────────────────────────────────────────
    if check_external:
        dead_ext = sorted(
            (u, s) for u, s in ext_checked.items()
            if isinstance(s, int) and s >= 400
        )
        if dead_ext:
            print(f"\nDead links — external ({len(dead_ext)}):")
            for url, status in dead_ext:
                print(f"  [{status}] {url}")
        else:
            print("No dead external links.")

    # ── Orphan pages ─────────────────────────────────────────────────────────
    reachable = {p for p, ok in visited.items() if ok is True}

    file_pages: set[str] = set()
    for p in site_dir.rglob("*.html"):
        rel = "/" + p.relative_to(site_dir).as_posix()
        norm = canonical_path(rel)
        if should_skip(norm) or norm in ("/404", "/redirect"):
            continue
        file_pages.add(norm)

    orphans = sorted(file_pages - reachable)
    if orphans:
        print(f"\nOrphan pages ({len(orphans)}) — not reachable from home:")
        for page in orphans:
            print(f"  {page}")
    else:
        print("\nNo orphan pages.")

    if dead or orphans:
        sys.exit(1)


if __name__ == "__main__":
    main()
