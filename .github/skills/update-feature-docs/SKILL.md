---
name: update-feature-docs
description: Updates DanceXR feature documentation pages and the master feature index based on a given release notes file. Use this when asked to "update feature documentation based on release [version] notes".
---

When asked to "Update feature documentation based on release [version] notes", follow this step-by-step process.

#### Step 1: Read the source file
- Read the specified release notes file located in `dancexr/releases/[version].md`.
- Identify the core updates in the "What's New" and "Improvements & Bug Fixes" sections. Ignore minor bug fixes that do not change user-facing behavior.

#### Step 2: Map features to existing files
- List the Markdown files inside `dancexr/features/` to understand the available feature topics (e.g., `camera.md`, `material_skin.md`).
- Analyze the contents of `dancexr/features.md`, which is a master index that lists all features.
- Map the updates from the release notes to the corresponding existing files in `dancexr/features/` based on their subject matter.
- **IMPORTANT**: If a release note introduces a completely new feature that does not clearly map to an existing file in `dancexr/features/`, STOP and explicitly ask the user if they want you to create a new feature page. **Never create a new feature page without the user's permission.**

#### Step 3: Update feature pages
- Read the content of the matched `dancexr/features/[feature].md` file.
- **Strict constraints**:
  - Never alter the YAML Front Matter (`--- ... ---`).
  - Never alter the localized translation links block (e.g., `[Eng] | [繁中] ...`).
  - Never break or remove Jekyll Liquid tags (e.g., `{% include video list="..." %}`).
- Identify the best location to merge the new information from the release notes. Prefer updating the main description under `## Overview` or adding a new section if it makes logical sense. Do not just append a "Recent Updates" list unless necessary.
- Integrate the changes smoothly and naturally into the existing documentation voice.
- Use tools to edit the `dancexr/features/[feature].md` file with your additions.

#### Step 4: Update the master feature map
- Open `dancexr/features.md`.
- Locate the row in the Markdown table corresponding to the feature you just updated.
- Update the "Version" or "Introduced" column to include or update to the new version (e.g., `[2026.1](releases/2026.1)`).
- Use tools to edit the `dancexr/features.md` file.

#### Formatting guidelines
- The default language is American English.
- Use sentence case for headers (except for proper nouns).
- Keep descriptions concise and user-centric, focusing on how to use the feature.
