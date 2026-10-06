"""Resolve reviewed feature media to Jekyll data without editing feature Markdown."""
import json
from pathlib import Path
import re
from urllib.parse import parse_qs, unquote, urlparse

BASE = Path(__file__).resolve().parents[1]


def tiles(sections):
    for section in sections:
        yield from section.get('tiles', [])
        yield from tiles(section.get('subsections', []))


def video_id(url):
    parsed = urlparse(url)
    if parsed.scheme != 'https':
        raise ValueError(f'Use an HTTPS YouTube watch URL: {url}')
    if parsed.netloc in ('youtube.com', 'www.youtube.com') and parsed.path == '/watch':
        vid = parse_qs(parsed.query).get('v', [''])[0]
    elif parsed.netloc == 'youtu.be':
        vid = parsed.path.lstrip('/')
    else:
        raise ValueError(f'Unsupported video URL: {url}')
    if not re.fullmatch(r'[A-Za-z0-9_-]{11}', vid):
        raise ValueError(f'Invalid YouTube video ID: {url}')
    return vid


def build_media(sections):
    catalogue_file = BASE / 'script/data/youtube.json'
    catalogue = json.loads(catalogue_file.read_text()) if catalogue_file.exists() else {'videos': []}
    catalogue = {v['id']: v for v in catalogue['videos']}
    media = {}
    for tile in tiles(sections):
        image = tile.get('image')
        if image:
            parsed = urlparse(image)
            if image.startswith('/'):
                if not (BASE / unquote(image).lstrip('/')).is_file():
                    raise ValueError(f'Missing thumbnail: {image}')
            elif parsed.scheme != 'https':
                raise ValueError(f'Use a site path or HTTPS thumbnail: {image}')
        path = tile.get('path')
        if not path:
            continue
        entry = media.setdefault(path, {'videos': []})
        if image and 'image' not in entry:
            entry['image'] = image
        urls = ([tile['video']] if tile.get('video') else []) + tile.get('videos', [])
        seen = {v['id'] for v in entry['videos']}
        for url in urls:
            vid = video_id(url)
            if vid in seen:
                continue
            if vid not in catalogue:
                raise ValueError(f'{path}: {vid} missing from catalogue; refresh it first')
            video = catalogue[vid]
            poster = video['thumbnail']
            # Jekyll omits files whose names begin with an underscore.
            poster_name = f'video-{vid}' if vid.startswith('_') else vid
            local_poster = f'/images/features/youtube/{poster_name}.webp'
            if (BASE / local_poster.lstrip('/')).is_file():
                poster = local_poster
            elif image and vid in image:
                poster = image
            entry['videos'].append({'id': vid, 'url': f'https://www.youtube.com/watch?v={vid}',
                                    'title': video['title'], 'thumbnail': poster,
                                    'published_at': video.get('published_at', '')})
            seen.add(vid)
    for entry in media.values():
        if 'image' not in entry and entry['videos']:
            entry['image'] = entry['videos'][0]['thumbnail']
    return media


def generate_media(sections):
    media = build_media(sections)
    out = BASE / '_data/feature_media.json'
    out.write_text(json.dumps(media, ensure_ascii=False, indent=2) + '\n')
    print(f'Written: {out.relative_to(BASE)}')
    return media
