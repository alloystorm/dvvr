# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this site is

A Jekyll-based documentation website for **DanceXR** — a VR character model viewer (PMX/MMD, XNALara/XPS models; VMD/BVH motions). Hosted via GitHub Pages using the `alloystorm/minimal-mistakes` remote theme. There is no local build step; content is all Markdown + YAML.

## Site structure

- `dancexr/` — English source documentation (features, releases, menus)
  - `features/` — one `.md` file per feature topic
  - `features.md` — master feature index (Markdown table)
  - `releases/` — monthly release notes (e.g., `2026.3.md`)
- `jp/dancexr/`, `zh/dancexr/`, `tw/dancexr/`, `kr/dancexr/` — localized mirrors of `dancexr/`
- `_data/navigation.yml` — sidebar nav hierarchy (releases grouped by year, feature nav)
- `_data/ui-text.yml` — theme UI string translations
- `_config.yml` — Jekyll config (theme, plugins, analytics, footer links)
- `script/` — Python utilities for translation automation

## Page anatomy

Every content page has three mandatory regions in this order:

```markdown
---
layout: single
title: Page Title
toc: true
locale: en-US
sidebar:
  nav: "docs"
---

[Eng](/dancexr/<path>) | [繁中](/tw/dancexr/<path>) | [日本語](/jp/dancexr/<path>) | [한국어](/kr/dancexr/<path>) | [简中](/zh/dancexr/<path>)

Body content here...
```

**Never alter** YAML front matter fields (except `title`, `locale`, `permalink`, `sidebar.nav` when translating), the language links block, or Jekyll Liquid tags.

## Localization

| Language | Directory prefix | Locale | Nav suffix |
|---|---|---|---|
| Japanese | `jp/dancexr/` | `ja-JP` | `-jp` |
| Simplified Chinese | `zh/dancexr/` | `zh-CN` | `-zh` |
| Traditional Chinese | `tw/dancexr/` | `zh-TW` | `-tw` |
| Korean | `kr/dancexr/` | `ko-KR` | `-kr` |

Translation detection uses `git log -1 --pretty=format:%ci` on both source and destination files; if the source commit date is newer, the translation is outdated. See `script/translate_pages.py` and `script/utils.py` for the implementation.

**Language links block** is identical in every language version — never translate it, never alter URLs.

When translating an outdated page, prefer updating only the changed sections rather than rewriting the whole file.

## GitHub Skills (AI workflows)

Two skills under `.github/skills/` define step-by-step AI workflows:

- **`translate-docs`** — translates missing or outdated pages into all four languages (full spec in `.github/skills/translate-docs/SKILL.md`)
- **`update-feature-docs`** — merges release note updates into feature pages and the master `features.md` index (spec in `.github/skills/update-feature-docs/SKILL.md`)

For update-feature-docs: never create a new feature page without explicit user permission; always ask first if a release note introduces a feature with no matching file in `dancexr/features/`.

## Writing style

- American English, sentence case for headers (except proper nouns)
- Descriptions concise and user-centric (how to use, not implementation detail)
- Integrate new content naturally into existing sections; avoid appending "Recent Updates" lists unless necessary
