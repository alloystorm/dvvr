# Support catalogue

Review the proposed questions in [SUPPORT_QUESTIONS.md](SUPPORT_QUESTIONS.md).
The corresponding `support-questions.json` contains stable IDs, categories,
source guides, suggested batches and English answer drafts. Read the first batch
in [SUPPORT_ANSWERS.md](SUPPORT_ANSWERS.md). The first 32 answers have been approved
and added to the published catalogue; 10 later questions remain drafts. These files
are excluded from the site build and are not read by the support-page generator.

Published content lives in `script/support.json`. Add approved questions there
after writing and checking their answers. Entries can be placed under any section
and subsection; the support browser reads all of them into one searchable list.
If a draft has a `replaces` field, update that existing entry while retaining its
public ID, rather than adding a duplicate answer. `review_id`, `source`,
`answer_notes`, `review_notes`, `code_sources`, `batch` and `replaces` are editorial
metadata and do not need to be copied into the published catalogue.
New or changed English answers use the English fallback on localized pages until
translated. Remove stale question/answer translations when changing an answer;
unchanged legacy translations can remain. Updated entries retain their public IDs.

Each entry needs:

- `id`: a unique lowercase slug, used in the permanent `#support-ID` link.
- `category`: an ID from the top-level `categories` array.
- `type`: `how-to`, `troubleshooting` or `known-issue`.
- `question` and `answer`: the English question and Markdown answer.
- `keywords`: optional search aliases, such as HDRI, skybox and panorama.

Optional fields:

- `question_locales`, `answer_locales`, `keywords_locales`: translations keyed
  by `jp`, `zh`, `tw` and `kr`. Missing question/answer translations fall back to English.
  Locale keywords are added to the shared keywords.
- `platforms`, `builds`, `editions`, `versions`: lists shown as applicability notes.
- `related`: a list of `{ "href": "features/sky", "label": "Sky guide" }`
  objects. A relative href resolves within the current language's DanceXR pages.
  Labels may also have `label_locales`. Use `href_locales` when a translated guide
  has different anchors; linking to the translated page without the English
  fragment is a suitable fallback.
- `status`: `published` (default) or `draft`. Drafts are omitted, including those
  without answers. Published entries with missing answers or invalid metadata
  fail generation before any support page is written.

Category labels use `label` and `label_locales`. Filters are generated from
categories with published entries. Search matches all query words across the
question, aliases, answer and visible metadata. Question matches rank first;
ties preserve catalogue order. Category counts respect the search and answer
type, while showing the number available in each category.

The shared include `_includes/support-browser.html` serves all five language
pages. Interface text lives in `_data/support_ui.json`. Without JavaScript,
answers remain accessible as native expandable details; search controls stay hidden.

Generate support pages only:

```sh
python3 script/generate_features.py --support
```

`script/build_site.sh` regenerates features and support before building Jekyll.
To check the support data and browser:

```sh
python3 -m unittest discover -s script -p 'test_support_data.py'
# Build/serve the site first; Playwright must be available to Node.
SUPPORT_BASE_URL=http://localhost:4000 node script/test_support_browser.cjs
```
