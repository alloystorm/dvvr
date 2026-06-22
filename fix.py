import os
import re

BASE = r"d:\studio\Unity\website"
locales = ["zh", "tw", "kr"]

html = """{% for section in page.support_sections %}
<!-- ── {{ section.label }} ───────────────────────────────────────────── -->
<section class="section {% if section.light %}section-light{% endif %}" id="{{ section.id }}">
<div class="editions-header" markdown="1">

{:.section-label}
{{ section.label }}

## {{ section.title }}

</div>

{% for sub in section.subsections %}
<h3 style="max-width: 1200px; margin: 40px auto 16px; padding: 0 24px; color: var(--text); font-weight: 600; font-size: 20px;">{{ sub.title }}</h3>
<div class="faq-grid">

{% for item in sub.items %}
<div class="faq-item" markdown="1">

### {{ item.question }}

{{ item.answer }}

</div>
{% endfor %}

</div>
{% endfor %}

</section>
{% endfor %}

<!-- ── Bug Report & Contact"""

for loc in locales:
    p = os.path.join(BASE, loc, "dancexr", "support.md")
    if os.path.isfile(p):
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = re.sub(r'<!-- ── FAQ.*?<!-- ── Bug Report & Contact', html, content, flags=re.DOTALL)
        with open(p, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Fixed", p)
