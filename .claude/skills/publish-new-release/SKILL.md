---
name: publish-new-release
description: Publishes a new DanceXR release to the documentation website. Creates English release notes from a CHANGELOG, generates all four localized versions, adds the release to the releases index, updates the homepage release card for every locale, and prepares platform-specific release notes for Steam, Google Play, and itch.io. Use this when asked to "publish release [version]" or "create release notes for [version]".
---

## Overview

A full release publication touches five areas, in order:

1. Draft the English release notes from the CHANGELOG
2. Create four localized release note pages (JP, ZH, TW, KR)
3. Add the release to the releases index (`releases.md`, all five locales)
4. Update the homepage release card in all five `index.md` files
5. Prepare platform-specific release notes under `notes/[version]/`

Related work that is handled by *other* skills, not this one:
- Merging release highlights into feature pages and `features.md` → `update-feature-docs`
- Re-translating any pages that changed as a result → `translate-docs`

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

| Language | File path | `locale` | Translated `title` prefix |
|---|---|---|---|
| Japanese | `jp/dancexr/releases/[version].md` | `ja-JP` | リリース [version] |
| Simplified Chinese | `zh/dancexr/releases/[version].md` | `zh-CN` | 发布 [version] |
| Traditional Chinese | `tw/dancexr/releases/[version].md` | `zh-TW` | 發布 [version] |
| Korean | `kr/dancexr/releases/[version].md` | `ko-KR` | 출시 [version] |

Front matter template for each locale (example for Japanese):

```yaml
---
layout: release
title: リリース [version]
locale: ja-JP
---
```

**No language links line in the body.**

Translate the full body content of the English release notes into each target language. Follow all translation guidelines from the `translate-docs` skill:
- Preserve Markdown structure exactly (same heading hierarchy, same bullet count).
- Never alter URLs.
- Keep code spans, Liquid tags, and HTML untouched.
- The `# ...` page title heading is conventionally left in English (e.g. `# Release [version]`); match the existing localized release notes.

---

## Step 3: Add the release to the releases index

Five `releases.md` index pages list every release as year-grouped tiles: `dancexr/releases.md` plus `jp/`, `zh/`, `tw/`, `kr/` prefixed copies.

In **every** locale's `releases.md`, add a new tile as the **first** entry under the current year section (newest first). The tile title uses the locale's translated "Release" label:

```yaml
  - title: "20XX"
    light: true
    tiles:
      - title: "Release [version]"          # EN
        link: "/dancexr/releases/[version]"
```

| Locale | Tile title | Link |
|---|---|---|
| en-US | `Release [version]` | `/dancexr/releases/[version]` |
| ja-JP | `リリース [version]` | `/jp/dancexr/releases/[version]` |
| zh-CN | `发布 [version]` | `/zh/dancexr/releases/[version]` |
| zh-TW | `發布 [version]` | `/tw/dancexr/releases/[version]` |
| ko-KR | `출시 [version]` | `/kr/dancexr/releases/[version]` |

In the **English** `dancexr/releases.md` only, also update the hero block to point at the new release:
- `hero_title: Latest Release - [version]`
- `hero_sub:` a one-line headline for the release
- the "Full Release Notes" CTA `url: /dancexr/releases/[version]`

The four localized index pages use a compact hero with no `hero_sub` or CTA — add only the tile there.

---

## Step 4: Update the homepage release card

Five `index.md` files each contain a `<div class="release-card">` HTML block. Update all five.

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
  <a href="releases/[version]" class="btn-ghost">[NOTES_LABEL]</a>
</div>
```

Pick 3–4 user-facing highlights from the release notes (not bug fixes). Keep each item to a short phrase (3–8 words), translated per locale.

The notes link is **relative** — `releases/[version]` — in all five files (each `index.md` already lives under its locale directory, so no locale prefix is added).

Per-language labels:

| File | latest label | headline format | notes link label |
|---|---|---|---|
| `dancexr/index.md` | `Latest` | `Month YYYY` | `Full release notes` |
| `jp/dancexr/index.md` | `最新` | `YYYY年M月` | `完全なリリースノート` |
| `zh/dancexr/index.md` | `最新` | `YYYY年M月` | `完整版本说明` |
| `tw/dancexr/index.md` | `最新` | `YYYY年M月` | `完整版本說明` |
| `kr/dancexr/index.md` | `최신` | `YYYY년 M월` | `전체 릴리스 노트` |

---

## Step 5: Prepare platform-specific release notes

Create a `notes/[version]/` directory and generate all 7 files in it. Study the most recent existing folder (e.g. `notes/2026.5/`) as the reference for format and tone.

### 5a — Google Play (`google.txt`)

Android audience only. **Omit any feature that is Windows/VR/PC/DX12-exclusive** (e.g. desktop VR mode, VR hand control, DX12, Steam-specific functionality). Focus on physics, character, and general simulation features that also run on Android.

Format: one short paragraph per language (≈500 characters), wrapped in language tags. All five languages in one file in this order:

```
<en-US>
…
</en-US>

<zh-CN>
…
</zh-CN>

<zh-TW>
…
</zh-TW>

<ja-JP>
…
</ja-JP>

<ko-KR>
…
</ko-KR>
```

Each paragraph ends with a localized link to the full release notes URL:
`https://vrstormlab.com/[locale-prefix]dancexr/releases/[version]`
(no prefix for English: `https://vrstormlab.com/dancexr/releases/[version]`)

### 5b — itch.io (`itchio.txt`)

No language-specific pages on itch.io — brief, all languages in one plain-text file in the order en-US, ja-JP, zh-CN, zh-TW, ko-KR. One short paragraph per language, separated by `---`. Each paragraph starts with `DanceXR [version]` as a heading and ends with a localized link to the full release notes. Keep each paragraph to 3–5 sentences maximum.

### 5c — Steam (5 separate XML files)

One XML file per language, named:
- `steam_english.xml`
- `steam_japanese.xml`
- `steam_schinese.xml`
- `steam_tchinese.xml`
- `steam_korean.xml`

Each file follows this exact XML structure:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<content>
    <string id="title">[Localised title]</string>
    <string id="subtitle">[Localised subtitle — key features, ≤120 chars]</string>
    <string id="summary">[Localised summary — 1-2 sentences, ≤300 chars]</string>
    <string id="body">[Localised body — 3-5 paragraphs of prose]

For full details, visit: [link text](https://vrstormlab.com/[locale-prefix]dancexr/releases/[version])</string>
</content>
```

Steam notes cover the full PC + VR feature set. The body should be engaging prose (not a bullet list), written as a product announcement. Escape `&` as `&amp;` in XML attributes and content.

Per-language title formats:
| File | Title format |
|---|---|
| `steam_english.xml` | `DanceXR Version [version] Released` |
| `steam_japanese.xml` | `DanceXR バージョン [version] をリリース` |
| `steam_schinese.xml` | `DanceXR 版本 [version] 发布` |
| `steam_tchinese.xml` | `DanceXR 版本 [version] 發布` |
| `steam_korean.xml` | `DanceXR 버전 [version] 출시` |

---

## Constraints

- **Never use `layout: single`** for release note pages. Always use `layout: release`.
- **Never include a language links line** in the body of a release note page — the layout handles this.
- **Never add `toc: true` or a `sidebar:` block** — these are not used by `layout: release`.
- **Never create release note pages for other locales as `layout: single`** even if existing older pages use it — those are legacy.
- Always update all five `releases.md` index pages and all five homepage `index.md` files in the same session as creating the release notes.
