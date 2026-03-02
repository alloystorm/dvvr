---
name: translate-docs
description: Translates DanceXR documentation pages into the localized website versions (Japanese, Korean, Traditional Chinese, Simplified Chinese). Use this when asked to translate pages, find missing translations, or update outdated translations.
---

## Overview

Source English pages live under `dancexr/`. Localized counterparts mirror that structure under language prefixes:

| Language | Prefix | Locale | Nav suffix |
|---|---|---|---|
| Japanese | `jp/dancexr/` | `ja-JP` | `-jp` |
| Simplified Chinese | `zh/dancexr/` | `zh-CN` | `-zh` |
| Traditional Chinese | `tw/dancexr/` | `zh-TW` | `-tw` |
| Korean | `kr/dancexr/` | `ko-KR` | `-kr` |

---

## Step 1: Identify pages to translate

For each `.md` file found by walking the `dancexr/` source tree:

1. For every language prefix (`jp`, `zh`, `tw`, `kr`), derive the destination path by replacing the `dancexr/` root with `<lang>/dancexr/`.
2. **Missing page**: if the destination file does not exist, it must be translated.
3. **Outdated page**: if both files exist, use the same logic as `is_file_newer_than_translation` in `script/translate_pages.py`:
   - Run `git log -1 --pretty=format:%ci -- <file>` for both the source and the destination.
   - If the source has a more recent commit date than the destination, the translation is outdated and must be updated.
   - If the source has no commit history, skip it.
   - If the destination has no commit history, treat it as needing translation.

Only proceed to the following steps for files that are missing or outdated.

---

## Step 2: Read the source file

Read the full content of the source English `.md` file. Identify and separate these three regions:

- **Front matter**: the YAML block between the opening and closing `---` delimiters.
- **Language links block**: the single line immediately after the front matter that contains the language switcher links (e.g., `[Eng](/dancexr/...) | [繁中](/tw/dancexr/...) | ...`).
- **Body content**: everything after the language links block.

---

## Step 3: Translate the body content

- Translate the body content into the target language.
- **Never translate** the language links block — keep it exactly as it appears in the source file.
- Preserve all Markdown formatting: headings, bullet lists, numbered lists, tables, bold/italic, and code spans.
- Preserve all Jekyll Liquid tags exactly (e.g., `{% include video list="..." %}`).
- Preserve all Markdown links: translate only the visible link text if it is a natural-language phrase; never alter URLs.
- Keep the same number of headings and bullet/numbered list items as the source. If a translation validation check (section count, bullet count) fails, retry up to 3 times.

---

## Step 4: Build the front matter for the translated file

Start from the source front matter and apply these transformations only — do not translate any other fields:

1. **`title`**: translate the value into the target language.
2. **`locale`**: set to the locale code for the target language (see table above).
3. **`permalink`**: replace `/dancexr/` with `/<lang>/dancexr/` (e.g., `/jp/dancexr/`).
4. **`sidebar.nav`**: append the language suffix to the nav value (e.g., `"docs"` → `"docs-jp"`).

Do not alter any other front matter keys or values.

---

## Step 5: Verify language links

The language links block must follow this exact format and appear immediately after the closing `---` of the front matter, separated by a blank line:

```
[Eng](/dancexr/<path>) | [繁中](/tw/dancexr/<path>) | [日本語](/jp/dancexr/<path>) | [한국어](/kr/dancexr/<path>) | [简中](/zh/dancexr/<path>)
```

- The links in this block are identical in every language version of the page.
- If the source page is missing any language link (e.g., a locale page does not yet exist), add the link anyway — it will resolve once that page is created.
- Verify that each URL path matches the actual file path relative to the language root.

---

## Step 6: Assemble and save the translated file

Combine the translated content in this order:

1. Translated front matter (between `---` delimiters)
2. Blank line
3. Language links block (unchanged)
4. Blank line
5. Translated body content

Create any missing directories, then write the file to the destination path. Use UTF-8 encoding.

---

## Constraints

- **Never modify the source English files.**
- **Never translate front matter fields other than `title`.**
- **Never alter the language links block.**
- **Never alter Jekyll Liquid tags.**
- When translating an outdated page (not missing), prefer translating only the sections that changed rather than rewriting the entire file, to minimize unintended drift from prior translations.
