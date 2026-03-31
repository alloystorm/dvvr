---
name: publish-new-release
description: Publishes a new DanceXR release to the documentation website. Creates English release notes from a CHANGELOG, generates all four localized versions, updates navigation for all locales, and updates the homepage release card. Use this when asked to "publish release [version]" or "create release notes for [version]".
---

## Overview

A full release publication touches six areas:

1. Draft the English release notes from the CHANGELOG
2. Create four localized release note pages (JP, ZH, TW, KR)
3. Add the new release to `_data/navigation.yml` for all five nav sections
4. Update the homepage release card in all five `index.md` files
5. Use `layout: release` (not `layout: single`) for all release note pages

The inputs you need before starting:
- The **version string** (e.g., `2026.4`)
- The **CHANGELOG** content — either a file path or pasted inline

---

## Step 1: Draft the English release notes

Read the existing most-recent release file (e.g., `dancexr/releases/2026.3.md`) to understand the writing style and structure.

Create `dancexr/releases/[version].md` with this exact front matter:

```yaml
---
layout: release
title: Release [version]
locale: en-US
nav_links:
  - label: Intro
    url: /dancexr
  - label: Features
    url: /dancexr/features
  - label: Releases
    url: /dancexr/releases
  - label: Download
    url: /dancexr/download
---
```

**No language links line in the body** — the `release` layout renders this automatically.

Writing guidelines for the body:
- Organise content into named sections matching the CHANGELOG groups (new features, improvements, bug fixes).
- Translate internal/technical CHANGELOG language into user-facing prose. Explain *what it means for the user*, not how it was implemented.
- Use `##` for top-level sections and `###` for sub-sections.
- Keep bug fix entries concise — one line each, grouped under a single `### Bug Fixes` section.
- American English, sentence case for headers.

---

## Step 2: Create localized release note pages

For each of the four languages, create the corresponding file under the language prefix directory.

| Language | File path | `locale` | `nav_links` labels | `nav_links` URL prefix |
|---|---|---|---|---|
| Japanese | `jp/dancexr/releases/[version].md` | `ja-JP` | イントロ / 機能 / リリース / ダウンロード | `/jp` |
| Simplified Chinese | `zh/dancexr/releases/[version].md` | `zh-CN` | 简介 / 功能 / 发布 / 下载 | `/zh` |
| Traditional Chinese | `tw/dancexr/releases/[version].md` | `zh-TW` | 簡介 / 功能 / 發布 / 下載 | `/tw` |
| Korean | `kr/dancexr/releases/[version].md` | `ko-KR` | 소개 / 기능 / 출시 / 다운로드 | `/kr` |

Front matter template for each locale (example for Japanese):

```yaml
---
layout: release
title: リリース [version]
locale: ja-JP
nav_links:
  - label: イントロ
    url: /jp/dancexr
  - label: 機能
    url: /jp/dancexr/features
  - label: リリース
    url: /jp/dancexr/releases
  - label: ダウンロード
    url: /jp/dancexr/download
---
```

**No language links line in the body.**

Translate the full body content of the English release notes into each target language. Follow all translation guidelines from the `translate-docs` skill:
- Preserve Markdown structure exactly (same heading hierarchy, same bullet count).
- Never alter URLs.
- Keep code spans, Liquid tags, and HTML untouched.

---

## Step 3: Update `_data/navigation.yml`

Six navigation sections must each have the new release inserted at the top of their 2026 children list. Use `multi_replace_string_in_file` to update all six in a single call.

| Section key | Title format | URL format |
|---|---|---|
| `releases` (main docs nav — inside the `docs` nav entry) | `"[version]"` | `/dancexr/releases/[version]` |
| `releases` (standalone sidebar) | `Release [version]` | `/dancexr/releases/[version]` |
| `releases-zh` | `发布 [version]` | `/zh/dancexr/releases/[version]` |
| `releases-tw` | `發布 [version]` | `/tw/dancexr/releases/[version]` |
| `releases-jp` | `リリース [version]` | `/jp/dancexr/releases/[version]` |
| `releases-kr` | `출시 [version]` | `/kr/dancexr/releases/[version]` |

The main `docs` nav entry is a short list under `- title: Releases` inside the `docs:` key. Insert the new entry as the first child there too, and remove any `(Early Access)` or similar suffixes from the previous release title at the same time.

---

## Step 4: Update the homepage release card

Five `index.md` files each contain a `<div class="release-card">` HTML block. Update all five in a single `multi_replace_string_in_file` call.

The block structure is:

```html
<div class="release-card">
  <p class="release-version">[LATEST_LABEL] — [version]</p>
  <p class="release-headline">[MONTH_YEAR]</p>
  <div class="release-items">
    <div class="release-item">[highlight 1]</div>
    <div class="release-item">[highlight 2]</div>
    <div class="release-item">[highlight 3]</div>
    <div class="release-item">[highlight 4]</div>
  </div>
  <a href="/[locale-prefix]dancexr/releases/[version]" class="btn-ghost">[NOTES_LABEL]</a>
</div>
```

Pick 3–4 user-facing highlights from the release notes (not bug fixes). Keep each item to a short phrase (5–8 words).

Per-language labels:

| File | latest label | notes link label |
|---|---|---|
| `dancexr/index.md` | `Latest` | `Full release notes` |
| `jp/dancexr/index.md` | `最新` | `完全なリリースノート` |
| `zh/dancexr/index.md` | `最新` | `完整版本说明` |
| `tw/dancexr/index.md` | `最新` | `完整版本說明` |
| `kr/dancexr/index.md` | `최신` | `전체 릴리스 노트` |

The English card has no locale prefix in the URL (`/dancexr/releases/[version]`). All others use their locale prefix (`/jp/dancexr/releases/[version]`, etc.).

---

## Constraints

- **Never use `layout: single`** for release note pages. Always use `layout: release`.
- **Never include a language links line** in the body of a release note page — the layout handles this.
- **Never add `toc: true` or a `sidebar:` block** — these are not used by `layout: release`.
- **Never create release note pages for other locales as `layout: single`** even if existing older pages use it — those are legacy.
- Always update all six navigation sections and all five homepage index files in the same session as creating the release notes.
