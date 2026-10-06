"""Focused checks for URL validation, duplicate tiles and thumbnail fallback."""
import json
from datetime import date
from contextlib import redirect_stdout
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import feature_media
from youtube_catalogue import api_listing, recency_weight, score_candidate


class FeatureMediaTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.patch = patch.object(feature_media, 'BASE', self.base)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        (self.base / 'script/data').mkdir(parents=True)
        (self.base / 'script/data/youtube.json').write_text(json.dumps({'videos': [
            {'id': 'bMtgN0cNJm8', 'title': 'Discovery', 'thumbnail': 'https://i.ytimg.com/vi/bMtgN0cNJm8/hqdefault.jpg'},
            {'id': 'RtMze-_g8SM', 'title': 'Pose', 'thumbnail': 'https://i.ytimg.com/vi/RtMze-_g8SM/hqdefault.jpg'},
            {'id': '_ojV5x37FlU', 'title': 'Wet textures', 'thumbnail': 'https://i.ytimg.com/vi/_ojV5x37FlU/hqdefault.jpg'},
        ]}))

    def test_watch_and_short_links_normalize(self):
        for url in ('https://www.youtube.com/watch?v=bMtgN0cNJm8', 'https://youtu.be/bMtgN0cNJm8'):
            self.assertEqual(feature_media.video_id(url), 'bMtgN0cNJm8')

    def test_invalid_and_lookalike_urls_rejected(self):
        for url in ('javascript:alert(1)', 'https://youtube.com.evil/watch?v=bMtgN0cNJm8',
                    'https://www.youtube.com/watch?v=bad', '//youtu.be/bMtgN0cNJm8'):
            with self.subTest(url=url), self.assertRaises(ValueError):
                feature_media.video_id(url)

    def test_nested_duplicate_tiles_share_ordered_unique_videos(self):
        media = feature_media.build_media([{'tiles': [
            {'path': 'features/pose', 'video': 'https://youtu.be/RtMze-_g8SM'}], 'subsections': [
            {'tiles': [{'path': 'features/pose', 'video': 'https://youtu.be/RtMze-_g8SM',
                        'videos': ['https://youtu.be/bMtgN0cNJm8']}]}]}])
        self.assertEqual([v['id'] for v in media['features/pose']['videos']], ['RtMze-_g8SM', 'bMtgN0cNJm8'])
        self.assertEqual(media['features/pose']['image'], 'https://i.ytimg.com/vi/RtMze-_g8SM/hqdefault.jpg')

    def test_explicit_thumbnail_wins_over_video_poster(self):
        (self.base / 'demo image.jpg').touch()
        media = feature_media.build_media([{'tiles': [{'path': 'features/pose',
            'image': '/demo%20image.jpg', 'video': 'https://youtu.be/RtMze-_g8SM'}]}])
        self.assertEqual(media['features/pose']['image'], '/demo%20image.jpg')

    def test_missing_thumbnail_and_unknown_video_fail(self):
        for fields in ({'image': '/missing.png'}, {'video': 'https://youtu.be/aaaaaaaaaaa'}):
            with self.subTest(fields=fields), self.assertRaises(ValueError):
                feature_media.build_media([{'tiles': [dict(path='features/pose', **fields)]}])

    def test_no_video_has_no_invented_match(self):
        self.assertEqual(feature_media.build_media([{'tiles': [{'path': 'features/operator'}]}]),
                         {'features/operator': {'videos': []}})

    def test_underscore_video_id_uses_jekyll_safe_local_poster(self):
        poster = '/images/features/youtube/video-_ojV5x37FlU.webp'
        local = self.base / poster.lstrip('/')
        local.parent.mkdir(parents=True)
        local.touch()
        media = feature_media.build_media([{'tiles': [{'path': 'features/skin',
            'video': 'https://youtu.be/_ojV5x37FlU'}]}])
        self.assertEqual(media['features/skin']['videos'][0]['thumbnail'], poster)
        self.assertEqual(media['features/skin']['image'], poster)

    def test_api_paginates_uploads_and_uses_full_descriptions(self):
        from youtube_catalogue import CHANNEL
        responses = [
            {'items': [{'id': CHANNEL, 'contentDetails': {'relatedPlaylists': {'uploads': 'UU-test'}}}]},
            {'items': [{'contentDetails': {'videoId': 'bMtgN0cNJm8'}}], 'nextPageToken': 'page2'},
            {'items': [{'contentDetails': {'videoId': 'RtMze-_g8SM'}}]},
            {'items': [{'id': 'bMtgN0cNJm8', 'snippet': {'channelId': CHANNEL, 'title': 'Discovery',
                'description': 'Full description', 'publishedAt': '2025-06-01',
                'thumbnails': {'high': {'url': 'https://i.ytimg.com/vi/bMtgN0cNJm8/hqdefault.jpg'}}},
                'status': {'embeddable': True}}]},
        ]
        with patch('youtube_catalogue.request', side_effect=[json.dumps(r) for r in responses]) as req:
            videos = api_listing('test-key')
        self.assertIn('pageToken=page2', req.call_args_list[2].args[0])
        self.assertEqual(videos[0]['description'], 'Full description')

    def test_public_refresh_preserves_cached_shorts_and_descriptions(self):
        import youtube_catalogue
        cache_file = self.base / 'script/data/youtube.json'
        cache_file.write_text(json.dumps({'videos': [
            {'id': 'bMtgN0cNJm8', 'title': 'Discovery', 'description': 'Full API description',
             'thumbnail': 'https://i.ytimg.com/vi/bMtgN0cNJm8/hqdefault.jpg'},
            {'id': 'RtMze-_g8SM', 'title': 'A cached Short', 'description': '',
             'thumbnail': 'https://i.ytimg.com/vi/RtMze-_g8SM/hqdefault.jpg'},
        ]}))
        (self.base / 'script/features.json').write_text('{"sections": []}')
        listing = [{'id': 'bMtgN0cNJm8', 'title': 'Updated Discovery title',
                    'thumbnail': 'https://i.ytimg.com/vi/bMtgN0cNJm8/hq720.jpg'}]
        with patch.object(youtube_catalogue, 'BASE', self.base), \
             patch.object(youtube_catalogue, 'CATALOGUE', cache_file), \
             patch.object(youtube_catalogue, 'public_listing', return_value=listing), \
             patch('sys.argv', ['youtube_catalogue.py', '--refresh']), redirect_stdout(io.StringIO()):
            youtube_catalogue.main()
        videos = {v['id']: v for v in json.loads(cache_file.read_text())['videos']}
        self.assertEqual(videos['bMtgN0cNJm8']['description'], 'Full API description')
        self.assertEqual(videos['bMtgN0cNJm8']['title'], 'Updated Discovery title')
        self.assertEqual(videos['RtMze-_g8SM']['listing_status'], 'cached-not-in-videos-tab')

    def test_recent_equivalent_beats_an_old_embedded_video(self):
        as_of = date(2026, 10, 6)
        old = score_candidate({'cloth'}, set(), True, True, '2021-01-01', as_of)
        new = score_candidate({'cloth'}, set(), False, False, '2025-01-01', as_of)
        self.assertGreater(new['score'], old['score'])

    def test_relevance_still_beats_an_unrelated_recent_upload(self):
        as_of = date(2026, 10, 6)
        old = score_candidate({'bone', 'mapper'}, {'mapping'}, False, False, '2023-01-01', as_of)
        broad = score_candidate({'model'}, set(), False, False, '2026-10-01', as_of)
        unrelated = score_candidate(set(), set(), False, False, '2026-10-01', as_of)
        self.assertGreater(old['score'], broad['score'])
        self.assertEqual(unrelated['score'], 0)

    def test_unknown_and_future_dates_do_not_inflate_recency(self):
        as_of = date(2026, 10, 6)
        for value in ('', 'not-a-date', None):
            self.assertEqual(recency_weight(value, as_of), (0.25, None))
        self.assertEqual(recency_weight('2027-01-01', as_of), (1.0, 0))


if __name__ == '__main__':
    unittest.main()
