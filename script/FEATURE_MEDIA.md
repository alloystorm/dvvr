# Feature thumbnails and videos

`script/features.json` is the source of truth. Each tile can have:

```json
{
  "path": "features/discovery",
  "image": "/images/features/youtube/bMtgN0cNJm8.webp",
  "video": "https://www.youtube.com/watch?v=bMtgN0cNJm8",
  "videos": ["https://www.youtube.com/watch?v=ANOTHER_ID"],
  "video_keywords": ["asset discovery"]
}
```

`video` is the primary video; `videos` optionally adds more. `video_keywords` only helps produce suggestions. These links must point to videos in the cached channel catalogue. Suggestions never overwrite reviewed mappings. Omit videos when no clear demonstration exists. When the same page occurs in several sections, its page videos are combined and deduplicated; tile images can remain specific to their sections.

After editing the mapping, run:

```sh
python3 script/generate_features.py --features-only
```

This regenerates the five feature indexes and `_data/feature_media.json`. Jekyll's `feature` and `release` layouts read that lookup at build time and add linked video cards. Localized pages share the same mapping and have localized section headings. Existing embedded or linked videos are suppressed from the extra cards. No feature guide Markdown is edited. The old `--inject-media` flag is accepted for compatibility and no longer writes guide front matter.

An explicit `image` wins; otherwise a matched video poster is used, followed by the existing logo fallback. The reviewed primary thumbnails are stored locally in `images/features/youtube/`; the catalogue retains YouTube thumbnail URLs for secondary cards and provenance. Poster filenames for video IDs starting with `_` must use a `video-` prefix (for example, `video-_ojV5x37FlU.webp`), since Jekyll excludes files that start with an underscore.

## Refresh the channel catalogue

```sh
python3 script/youtube_catalogue.py --refresh
```

Public mode paginates the channel's **Videos tab** (not Shorts or live streams), fetches titles and thumbnail URLs, and preserves any descriptions previously fetched. Previously cached uploads outside that tab are retained with `listing_status: cached-not-in-videos-tab`, so a public refresh cannot erase mappings to Shorts. Use API mode to verify those uploads again. It does not sign in, download video files, or request hundreds of watch pages. YouTube's public page format can change; use the official API if that happens. Description availability is reported explicitly.

For full titles, descriptions, upload dates and thumbnails via the official YouTube Data API v3:

1. Create/select a project in [Google Cloud Console](https://console.cloud.google.com/).
2. Enable **YouTube Data API v3** in APIs & Services → Library.
3. In Credentials, create an **API key** and restrict it to **YouTube Data API v3**. Use a suitable application restriction for the machine running the script (for example, a stable IP address restriction).
4. Set `YOUTUBE_API_KEY` locally in your shell or secret manager. Do not commit it or paste it into chat. An API key is sufficient for public data; OAuth account authorization is not required.
5. Run:

```sh
python3 script/youtube_catalogue.py --refresh --api
```

The API mode resolves the channel's uploads playlist and paginates it, then requests video details in batches of 50. It includes public Shorts and live uploads present in that playlist. API mode does not require channel ownership. See the official [getting started guide](https://developers.google.com/youtube/v3/getting-started) and [playlistItems.list reference](https://developers.google.com/youtube/v3/docs/playlistItems/list).

Without `--refresh`, the script uses the offline cache and only generates ranked suggestions in `.scratch/feature-media/suggestions.json`. Review titles, descriptions and page context before applying any suggestion to `features.json`. The current selection and unresolved pages are documented in `.scratch/feature-media/README.md`.

## Prefer recent coverage

Suggestions weight upload age as well as topic relevance. Each shared title term contributes 6 points and each shared description term contributes 2. An existing guide embed adds only 2 points, and a matching tile image adds 0.5; these are supporting evidence rather than reasons to keep an old selection.

The relevance score is multiplied by `0.25 + 0.75 × 2^(-age_in_years / 2)`. The recency boost halves every two years, with a 0.25 floor so an older exact tutorial can still beat a broad recent upload. Missing or invalid dates use the floor; future dates are treated as zero age. Suggestions include the upload date, age, relevance score and age multiplier to make the ranking reviewable.

The current date is used by default. To reproduce a review from the same catalogue without another API request:

```sh
python3 script/youtube_catalogue.py --as-of 2026-10-06
```

Prefer the newer video when it demonstrates the same feature or its current workflow, update its tile poster, and remove redundant older previews. Keep older companions when they explain distinct useful controls. Do not replace an exact tutorial with an unrelated recent showcase, or assign Native renderer videos to Unity settings pages. The dated review in `.scratch/feature-media/recency-changes.json` records selection changes and their rationale. Existing guide embeds remain as authored; JSON changes control the generated cards and thumbnails.

## Checks and site build

```sh
python3 -m unittest discover -s script -p 'test_feature_media.py'
sh script/build_site.sh
```

`build_site.sh` always reads the current `features.json` before generating HTML; it forwards arguments to `jekyll build`. A plain `jekyll build` uses the last generated lookup, so regenerate first if using that command directly.

Commit `features.json`, the catalogue, local thumbnails, generated indexes and lookup together. Catalogue refresh is a manual step; the Jekyll build itself makes no YouTube API requests and needs no credentials.
