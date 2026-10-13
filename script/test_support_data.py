"""Support publishing rules and multilingual serialization checks."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

import yaml
from generate_features import inject_support_sections
from support_data import prepare_support, support_yaml

BASE = Path(__file__).resolve().parent.parent


class SupportDataTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((BASE / 'script/support.json').read_text())

    def test_all_current_answers_preserved_in_every_locale(self):
        categories, sections = prepare_support(self.data)
        for locale in (None, 'jp', 'zh', 'tw', 'kr'):
            generated = yaml.safe_load(support_yaml(sections, locale, categories))
            original = [item for section in sections for sub in section['subsections'] for item in sub['items']]
            output = [item for section in generated['support_sections'] for sub in section['subsections'] for item in sub['items']]
            self.assertEqual(len(output), 39)
            for before, after in zip(original, output):
                self.assertEqual(after['answer'], before.get('answer_locales', {}).get(locale) or before['answer'])
                self.assertEqual(after['id'], before['id'])

    def test_unanswered_draft_omitted_and_empty_groups_removed(self):
        self.data['sections'].append({'id': 'drafts', 'subsections': [{'items': [{'status': 'draft'}]}]})
        _, sections = prepare_support(self.data)
        self.assertEqual(len(sections), 3)

    def test_invalid_published_data_rejected(self):
        for field, value in [('answer', ''), ('question', ''), ('category', 'unknown'),
                             ('type', 'unknown'), ('id', 'Bad ID'), ('status', 'unknown')]:
            data = copy.deepcopy(self.data)
            data['sections'][0]['subsections'][0]['items'][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                prepare_support(data)
        data = copy.deepcopy(self.data)
        data['sections'][0]['subsections'][0]['items'].append(copy.deepcopy(data['sections'][0]['subsections'][0]['items'][0]))
        with self.assertRaisesRegex(ValueError, 'Duplicate support ID'):
            prepare_support(data)

    def test_regeneration_is_idempotent_and_keeps_page_body(self):
        categories, sections = prepare_support(self.data)
        with tempfile.TemporaryDirectory() as folder:
            page = Path(folder) / 'support.md'
            page.write_text('---\ntitle: Support\n---\nBody remains.\n')
            inject_support_sections(sections, str(page), categories=categories)
            first = page.read_text()
            inject_support_sections(sections, str(page), categories=categories)
            self.assertEqual(page.read_text(), first)
            self.assertTrue(first.endswith('Body remains.\n'))
            self.assertEqual(first.count('support_categories:'), 1)
            self.assertEqual(first.count('support_sections:'), 1)

    def test_locale_aliases_related_guides_and_applicability_survive(self):
        item = self.data['sections'][0]['subsections'][0]['items'][0]
        item.update(keywords_locales={'jp': ['空']}, platforms=['Windows'], builds=['HD'],
                    editions=['Creator'], related=[{'href': 'features/sky#mode', 'href_locales': {'jp': 'features/sky'}, 'label': 'Sky', 'label_locales': {'jp': '空'}}])
        categories, sections = prepare_support(self.data)
        generated = yaml.safe_load(support_yaml(sections, 'jp', categories))['support_sections'][0]['subsections'][0]['items'][0]
        self.assertIn('空', generated['keywords'])
        self.assertEqual(generated['related'][0]['label'], '空')
        self.assertEqual(generated['related'][0]['href'], 'features/sky')
        self.assertEqual(generated['editions'], ['Creator'])

    def test_review_ids_and_source_pages_are_valid(self):
        data = json.loads((BASE / 'script/support-questions.json').read_text())
        self.assertEqual(len({q['id'] for q in data['questions']}), len(data['questions']))
        self.assertEqual(len({q['review_id'] for q in data['questions']}), len(data['questions']))
        categories = {category['id'] for category in data['categories']}
        for question in data['questions']:
            self.assertIn(question['category'], categories)
            self.assertEqual(question['status'], 'published' if question.get('answer') else 'draft')
            self.assertTrue((BASE / 'dancexr' / (question['source'].split('#')[0] + '.md')).is_file())

    def test_approved_answers_published_once_and_later_questions_excluded(self):
        review = json.loads((BASE / 'script/support-questions.json').read_text())
        _, sections = prepare_support(self.data)
        entries = {item['id']: item for section in sections for sub in section['subsections'] for item in sub['items']}
        approved = [question for question in review['questions'] if question['status'] == 'published']
        self.assertEqual(len(approved), 32)
        for question in approved:
            identifier = question.get('replaces') or question['id']
            self.assertEqual(entries[identifier]['answer'], question['answer'])
            self.assertEqual(entries[identifier]['question'], question['question'])
            if question.get('replaces'):
                self.assertNotIn(question['id'], entries)
        for question in review['questions']:
            if question['status'] == 'draft':
                self.assertNotIn(question['id'], entries)


if __name__ == '__main__':
    unittest.main()
