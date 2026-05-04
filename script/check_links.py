#!/usr/bin/env python3
"""Dead-link checker and orphan-page detector for DanceXR docs.

Usage: python3 check_links.py BASE_URL SITE_DIR [--external]

Crawls BASE_URL, reports internal pages that return HTTP >= 400,
and reports pages present in SITE_DIR that were never reached from the home page.
"""
import sys
import re
from collections import deque
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
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


def main() -> None:
    check_external = "--external" in sys.argv
    pos_args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(pos_args) < 2:
        print("Usage: check_links.py BASE_URL SITE_DIR [--external]", file=sys.stderr)
        sys.exit(2)

    base_url = pos_args[0].rstrip("/")
    site_dir = Path(pos_args[1])
    base_netloc = urlparse(base_url).netloc

    # path -> HTTP status int, error string, or None (queued but not yet fetched)
    visited: dict[str, object] = {}
    # path -> canonical path of first page that linked here
    first_referrer: dict[str, str] = {}
    # external URL -> status
    ext_checked: dict[str, object] = {}

    queue: deque[tuple[str, str, str | None]] = deque()
    start = canonical_path("/")
    visited[start] = None
    queue.append((start, base_url + "/", None))

    print(f"Checking links starting from {queue[0]} ...")

    while queue:
        path, fetch_url, ref = queue.popleft()
        print(f"Checking {fetch_url} ...", end="\r")
        if should_skip(path):
            visited[path] = 200
            continue

        if ref is not None and path not in first_referrer:
            first_referrer[path] = ref

        # Fetch
        try:
            req = Request(fetch_url, headers={"User-Agent": "DanceXR-link-checker/1.0"})
            with urlopen(req, timeout=15) as resp:
                status = resp.status
                ct = resp.headers.get("Content-Type", "")
                body = resp.read().decode("utf-8", errors="ignore")
            visited[path] = status
            print(f"Checked {path} → {status}    ")
        except HTTPError as e:
            visited[path] = e.code
            continue
        except Exception as e:
            visited[path] = f"ERR:{e}"
            continue

        if "text/html" not in ct:
            continue

        # Extract hrefs
        for raw_href in re.findall(r'href=["\']([^"\']+)["\']', body):
            href = raw_href.split("#")[0].strip()
            if not href or href.startswith(("mailto:", "javascript:")):
                continue
            abs_url = urljoin(fetch_url, href)
            p = urlparse(abs_url)
            if p.netloc == base_netloc:
                norm = canonical_path(p.path)
                if norm not in visited:
                    visited[norm] = None  # mark queued to avoid duplicates
                    queue.append((norm, abs_url.split("#")[0], path))
            elif check_external:
                url_no_frag = abs_url.split("#")[0]
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

    # ── Dead internal links ──────────────────────────────────────────────────
    dead = sorted(
        (p, s) for p, s in visited.items()
        if isinstance(s, int) and s >= 400
    )
    if dead:
        print(f"\nDead links — internal ({len(dead)}):")
        for path, status in dead:
            ref = first_referrer.get(path, "?")
            print(f"  [{status}] {path}  ← {ref}")
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
    reachable = {p for p, s in visited.items() if s is not None}

    file_pages: set[str] = set()
    for p in site_dir.rglob("*.html"):
        rel = "/" + str(p.relative_to(site_dir))
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
