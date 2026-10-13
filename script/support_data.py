"""Validate and serialize the support catalogue, leaving review drafts unpublished."""
import copy
import json
import re


def prepare_support(data):
    data = copy.deepcopy(data)
    categories = data.get('categories', [])
    category_ids = [category['id'] for category in categories]
    if len(set(category_ids)) != len(category_ids):
        raise ValueError('Duplicate support category ID')
    seen = set()
    sections = []
    for section in data.get('sections', []):
        subsections = []
        for sub in section.get('subsections', []):
            items = []
            for item in sub.get('items', []):
                if item.get('status', 'published') == 'draft':
                    continue
                if item.get('status', 'published') != 'published':
                    raise ValueError('Support status must be draft or published')
                identifier = item.get('id', '')
                if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', identifier):
                    raise ValueError(f'Invalid support ID: {identifier!r}')
                if identifier in seen:
                    raise ValueError(f'Duplicate support ID: {identifier}')
                seen.add(identifier)
                if item.get('category') not in category_ids:
                    raise ValueError(f'Unknown support category for {identifier}')
                if item.get('type') not in ('how-to', 'troubleshooting', 'known-issue'):
                    raise ValueError(f'Invalid answer type for {identifier}')
                if not item.get('question', '').strip() or not item.get('answer', '').strip():
                    raise ValueError(f'Published entry needs a question and answer: {identifier}')
                items.append(item)
            if items:
                sub['items'] = items
                subsections.append(sub)
        if subsections:
            section['subsections'] = subsections
            sections.append(section)
    return categories, sections


def localized(record, field, locale):
    return record.get(field + '_locales', {}).get(locale) or record.get(field, '')


def support_yaml(sections, locale=None, categories=None):
    # JSON scalars are valid YAML and preserve backslashes, quotes and Unicode.
    scalar = lambda value: json.dumps(value, ensure_ascii=False)
    lines = ['support_categories:']
    for category in categories or []:
        lines += [f"  - id: {scalar(category['id'])}",
                  f"    label: {scalar(localized(category, 'label', locale))}"]
    lines.append('support_sections:')
    for section in sections:
        lines += [f"  - id: {scalar(section['id'])}",
                  f"    label: {scalar(localized(section, 'label', locale))}",
                  f"    title: {scalar(localized(section, 'title', locale))}",
                  '    subsections:']
        for sub in section.get('subsections', []):
            lines += [f"      - title: {scalar(localized(sub, 'title', locale))}", '        items:']
            for item in sub['items']:
                lines += [f"          - id: {scalar(item['id'])}",
                          f"            category: {scalar(item['category'])}",
                          f"            type: {scalar(item['type'])}",
                          f"            question: {scalar(localized(item, 'question', locale))}"]
                keywords = item.get('keywords', []) + item.get('keywords_locales', {}).get(locale, [])
                lines.append(f"            keywords: {scalar(keywords)}")
                for field in ('platforms', 'builds', 'editions', 'versions'):
                    if item.get(field):
                        lines.append(f"            {field}: {scalar(item[field])}")
                if item.get('related'):
                    related = [{'href': localized(link, 'href', locale), 'label': localized(link, 'label', locale)}
                               for link in item['related']]
                    lines.append(f"            related: {scalar(related)}")
                # Use a scalar rather than hand-built indentation, preserving Markdown exactly.
                lines.append(f"            answer: {scalar(localized(item, 'answer', locale))}")
    return '\n'.join(lines)
