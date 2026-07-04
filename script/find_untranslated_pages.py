import subprocess
import os
import re
import argparse
import json

_all_commit_dates = None

def load_all_commit_dates():
    global _all_commit_dates
    _all_commit_dates = {}
    cmd = ["git", "log", "--name-only", "--pretty=format:commit:%ci"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return
    
    current_date = ""
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("commit:"):
            current_date = line[len("commit:"):]
        else:
            # git paths are forward slash, normalize
            if line not in _all_commit_dates:
                _all_commit_dates[line] = current_date

def get_latest_commit_info(file_path):
    """Get the latest commit date for a given file."""
    global _all_commit_dates
    if _all_commit_dates is None:
        load_all_commit_dates()
    
    normalized_path = file_path.replace("\\", "/")
    return _all_commit_dates.get(normalized_path, "")

def is_translation_excluded(file_path):
    """Return True if the file's front matter contains 'translate: false'."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if match:
            return bool(re.search(r'^translate:\s*false\s*$', match.group(1), re.MULTILINE | re.IGNORECASE))
    except Exception:
        pass
    return False


def get_header_count(file_path):
    """Count Markdown headers (# ## ### etc.), excluding front matter."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Strip front matter
        content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
        return sum(1 for line in content.splitlines() if re.match(r'^#{1,6}\s', line))
    except Exception:
        return 0

def check_translation_status(file_path, prefix):
    """Return (needs_translation, reason) for a source file and target language prefix."""
    dst_path = f"{prefix}/dancexr"
    dst_file_path = os.path.join(dst_path, os.path.relpath(file_path, "dancexr"))

    if not os.path.exists(dst_file_path):
        return True, "missing"

    commit_date_original = get_latest_commit_info(file_path)
    commit_date_translated = get_latest_commit_info(dst_file_path)

    # If the original file has no commit history, skip it
    if not commit_date_original:
        return False, ""

    # If the translated version has no commit history, treat as outdated
    if not commit_date_translated:
        return True, "no_history"

    if commit_date_original > commit_date_translated:
        return True, "outdated"

    # Header count comparison: flag if translation has fewer headers than source
    src_headers = get_header_count(file_path)
    dst_headers = get_header_count(dst_file_path)
    if src_headers > 0 and dst_headers < src_headers:
        return True, f"header_count ({src_headers} src vs {dst_headers} dst)"

    return False, ""

def find_untranslated_pages():
    src_path = 'dancexr'
    target_languages = ['jp', 'zh', 'kr', 'tw']
    untranslated = []

    for subdir, _, files in os.walk(src_path):
        for file in files:
            _, file_extension = os.path.splitext(file)
            if file_extension.lower() not in ['.md', '.txt']:
                continue

            file_path = os.path.join(subdir, file)
            if is_translation_excluded(file_path):
                continue
            langs_needed = []
            reasons = {}

            for lang in target_languages:
                needed, reason = check_translation_status(file_path, lang)
                if needed:
                    langs_needed.append(lang)
                    reasons[lang] = reason

            if langs_needed:
                untranslated.append({
                    "file": file_path,
                    "languages": langs_needed,
                    "reasons": reasons
                })

    return untranslated

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find pages that need translation.")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    args = parser.parse_args()

    results = find_untranslated_pages()

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        if not results:
            print("No pages need translation.")
        else:
            for item in results:
                reasons_str = ", ".join(
                    f"{lang}:{item['reasons'].get(lang, '?')}" for lang in item['languages']
                )
                print(f"{item['file']} -> {', '.join(item['languages'])}  [{reasons_str}]")
