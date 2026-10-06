#!/usr/bin/env python3
"""Fetch public channel metadata and suggest feature/video matches (never apply them)."""
import argparse
from datetime import date, datetime, timezone
import json
import os
from pathlib import Path
import re
import sys
import time
from urllib.parse import urlencode
from urllib.error import HTTPError
from urllib.request import Request, urlopen

BASE = Path(__file__).resolve().parents[1]
CATALOGUE = BASE / 'script/data/youtube.json'
CHANNEL = 'UC4kSPkrWRR_oE2QMOjFYwBg'
HANDLE = '@dancexr'


def request(url, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = Request(url, data=data, headers={
        'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/json',
    })
    for attempt in range(3):
        try:
            with urlopen(req, timeout=30) as response:
                return response.read().decode('utf-8')
        except Exception:
            if attempt == 2:
                raise
            time.sleep(attempt + 1)


def embedded_json(html, name):
    match = re.search(r'(?:var\s+)?' + re.escape(name) + r'\s*=\s*', html)
    if not match:
        raise ValueError(f'YouTube did not return {name}; try --api with YOUTUBE_API_KEY.')
    return json.JSONDecoder().raw_decode(html[match.end():])[0]


def nodes(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from nodes(child)


def text(value):
    return value.get('simpleText') or ''.join(r['text'] for r in value.get('runs', []))


def public_listing():
    html = request(f'https://www.youtube.com/{HANDLE}/videos')
    data = embedded_json(html, 'ytInitialData')
    channel = data['metadata']['channelMetadataRenderer']['externalId']
    if channel != CHANNEL:
        raise ValueError('Unexpected channel identity')
    version = re.search(r'"INNERTUBE_CLIENT_VERSION":"([^"]+)"', html).group(1)
    tabs = data['contents']['twoColumnBrowseResultsRenderer']['tabs']
    data = next(t['tabRenderer']['content'] for t in tabs
                if t.get('tabRenderer', {}).get('selected'))
    videos, seen_tokens = {}, set()
    while True:
        token = None
        for node in nodes(data):
            if 'lockupViewModel' in node:
                r = node['lockupViewModel']
                if r.get('contentType') != 'LOCKUP_CONTENT_TYPE_VIDEO':
                    continue
                vid = r['contentId']
                title = r['metadata']['lockupMetadataViewModel']['title']['content']
                sources = r['contentImage']['thumbnailViewModel']['image']['sources']
                thumbnail = max(sources, key=lambda x: x.get('width', 0))['url'].split('?')[0]
                videos[vid] = {'id': vid, 'title': title, 'thumbnail': thumbnail}
            elif 'videoRenderer' in node:
                r = node['videoRenderer']
                vid = r['videoId']
                thumbnail = r['thumbnail']['thumbnails'][-1]['url'].split('?')[0]
                videos[vid] = {'id': vid, 'title': text(r['title']), 'thumbnail': thumbnail}
            if 'continuationItemRenderer' in node:
                token = node['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
        print(f'Listed {len(videos)} videos', flush=True)
        if not token:
            return list(videos.values())
        if token in seen_tokens:
            raise ValueError('YouTube repeated a continuation; refusing an incomplete catalogue')
        seen_tokens.add(token)
        response = json.loads(request('https://www.youtube.com/youtubei/v1/browse', {
            'context': {'client': {'clientName': 'WEB', 'clientVersion': version, 'hl': 'en'}},
            'continuation': token,
        }))
        actions = [n['appendContinuationItemsAction'] for n in nodes(response)
                   if 'appendContinuationItemsAction' in n]
        if not actions:
            raise ValueError('YouTube continuation failed; try the official API')
        data = actions
        if not any('lockupViewModel' in n or 'videoRenderer' in n for n in nodes(data)):
            raise ValueError('Unexpected empty continuation; refusing an incomplete catalogue')


def api_listing(key):
    def api(resource, **params):
        return json.loads(request('https://www.googleapis.com/youtube/v3/' + resource + '?' +
                                  urlencode(dict(params, key=key))))
    channel = api('channels', part='contentDetails', forHandle=HANDLE)['items'][0]
    if channel['id'] != CHANNEL:
        raise ValueError('Unexpected channel identity')
    playlist = channel['contentDetails']['relatedPlaylists']['uploads']
    ids, token = [], ''
    while True:
        page = api('playlistItems', part='contentDetails', playlistId=playlist,
                   maxResults=50, pageToken=token)
        ids.extend(i['contentDetails']['videoId'] for i in page['items'])
        token = page.get('nextPageToken')
        if not token:
            break
    videos = []
    for start in range(0, len(ids), 50):
        page = api('videos', part='snippet,status', id=','.join(ids[start:start + 50]))
        for item in page['items']:
            s = item['snippet']
            if s['channelId'] != CHANNEL:
                raise ValueError('Unexpected video owner')
            thumbs = s['thumbnails']
            thumb = next(thumbs[k]['url'] for k in ('maxres', 'standard', 'high', 'medium', 'default') if k in thumbs)
            videos.append({'id': item['id'], 'url': f'https://www.youtube.com/watch?v={item["id"]}',
                           'title': s['title'], 'description': s['description'], 'thumbnail': thumb,
                           'published_at': s['publishedAt'], 'metadata_status': 'complete',
                           'embeddable': item['status'].get('embeddable', False)})
    return videos


def tiles(sections):
    for section in sections:
        yield from section.get('tiles', [])
        yield from tiles(section.get('subsections', []))


def recency_weight(published_at, as_of):
    """Prefer recent uploads with a two-year half-life; unknown dates get no boost."""
    try:
        published = date.fromisoformat(published_at[:10])
    except (TypeError, ValueError):
        return 0.25, None
    age_years = max(0, (as_of - published).days / 365.25)
    return 0.25 + 0.75 * 2 ** (-age_years / 2), age_years


def score_candidate(title_overlap, desc_overlap, existing, image, published_at, as_of):
    relevance = 6 * len(title_overlap) + 2 * len(desc_overlap) + 2 * existing + 0.5 * image
    weight, age = recency_weight(published_at, as_of)
    return {'score': round(relevance * weight, 3), 'relevance_score': relevance,
            'recency_weight': round(weight, 3), 'age_years': round(age, 2) if age is not None else None}


def suggest(catalogue, as_of=None):
    as_of = as_of or datetime.now(timezone.utc).date()
    # Repeated boilerplate descriptions (site links, credits) carry no matching weight.
    frequencies = {}
    for video in catalogue['videos']:
        for line in set(video['description'].splitlines()):
            frequencies[line] = frequencies.get(line, 0) + 1
    stop = set('dancexr dvvr the and with for from this that settings feature features video demo new support options'.split())
    def words(s):
        return set(re.findall(r'[a-z0-9]{3,}', s.lower())) - stop
    sections = json.loads((BASE / 'script/features.json').read_text())['sections']
    results, seen = {}, set()
    for tile in tiles(sections):
        path = tile.get('path')
        if not path or path in seen:
            continue
        seen.add(path)
        page = BASE / 'dancexr' / (path + '.md')
        body = page.read_text() if page.exists() else ''
        title = re.search(r'^title:\s*(.+)', body, re.M)
        query = words(' '.join([path.replace('_', ' '), tile.get('title', ''),
                                title.group(1) if title else '', *tile.get('video_keywords', [])]))
        scores = []
        for video in catalogue['videos']:
            unique_desc = '\n'.join(line for line in video['description'].splitlines()
                                    if frequencies.get(line, 0) <= 3 and not line.startswith(('http', '#')))
            title_overlap = query & words(video['title'])
            desc_overlap = query & words(unique_desc)
            existing = video['id'] in body
            image = video['id'] in tile.get('image', '')
            score = score_candidate(title_overlap, desc_overlap, existing, image,
                                    video.get('published_at', ''), as_of)
            if score['relevance_score']:
                scores.append({'id': video['id'], 'title': video['title'], **score,
                               'published_at': video.get('published_at', ''),
                               'title_terms': sorted(title_overlap), 'description_terms': sorted(desc_overlap),
                               'already_in_page': existing, 'existing_thumbnail': image})
        results[path] = sorted(scores, key=lambda v: -v['score'])[:5]
    out = BASE / '.scratch/feature-media/suggestions.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
    print(f'Suggestions written to {out.relative_to(BASE)}; review before editing features.json')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh', action='store_true', help='Fetch catalogue before suggesting matches')
    parser.add_argument('--api', action='store_true', help='Use official API (YOUTUBE_API_KEY environment variable)')
    parser.add_argument('--as-of', type=date.fromisoformat, help='Reference date for reproducible recency scoring (YYYY-MM-DD)')
    args = parser.parse_args()
    if args.api and not args.refresh:
        parser.error('--api requires --refresh')
    if args.refresh:
        if args.api:
            key = os.environ.get('YOUTUBE_API_KEY')
            if not key:
                parser.error('Set YOUTUBE_API_KEY in your environment; do not put it in a file or command argument')
            videos = api_listing(key)
        else:
            listing = public_listing()
            previous = json.loads(CATALOGUE.read_text()) if CATALOGUE.exists() else {'videos': []}
            previous = {v['id']: v for v in previous['videos']}
            videos = []
            for video in listing:
                old = previous.get(video['id'], {})
                video.update(description=old.get('description', ''),
                             metadata_status=old.get('metadata_status', 'listing-only'),
                             published_at=old.get('published_at', ''),
                             url=f'https://www.youtube.com/watch?v={video["id"]}')
                videos.append(video)
            # Videos tab excludes Shorts/live uploads. Keep API-cached uploads so a
            # public-only refresh cannot erase reviewed mappings to those videos.
            listed_ids = {v['id'] for v in listing}
            videos.extend(dict(v, listing_status='cached-not-in-videos-tab')
                          for vid, v in previous.items() if vid not in listed_ids)
        catalogue = {'channel': CHANNEL, 'handle': HANDLE,
                     'fetched_at': datetime.now(timezone.utc).isoformat(),
                     'source': 'youtube-data-api-v3' if args.api else 'public-videos-tab-with-cached-descriptions',
                     'scope': 'uploads' if args.api else 'videos-tab-and-cached-uploads', 'videos': videos}
        CATALOGUE.parent.mkdir(parents=True, exist_ok=True)
        # Write only once the whole fetch succeeds; preserve the last good catalogue on failure.
        CATALOGUE.write_text(json.dumps(catalogue, ensure_ascii=False, indent=2) + '\n')
    catalogue = json.loads(CATALOGUE.read_text())
    print(f'Catalogue: {len(catalogue["videos"])} videos; '
          f'{sum(bool(v["description"]) for v in catalogue["videos"])} nonempty descriptions')
    suggest(catalogue, args.as_of)


if __name__ == '__main__':
    try:
        main()
    except HTTPError as error:
        print(f'YouTube returned HTTP {error.code}. Existing data is unchanged. '
              'For API mode, check that YouTube Data API v3 is enabled, the key allows this API, '
              'and quota is available. The API key is never printed.', file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        # urllib errors can contain the API key in the URL. Never print raw errors.
        print(f'Catalogue update failed ({type(error).__name__}). Existing data is unchanged. '
              'Check network access or use --api with YOUTUBE_API_KEY.', file=sys.stderr)
        sys.exit(1)
