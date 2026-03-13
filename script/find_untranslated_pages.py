import subprocess
import os
import argparse
import json

def get_latest_commit_info(file_path):
    """Get the latest commit date for a given file."""
    cmd = f"git log -1 --pretty=format:%ci -- {file_path}"
    result = subprocess.run(cmd.split(), capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    return ""

def is_file_newer_than_translation(file_path, prefix):
    """Check if the given file is newer than its translated counterpart."""
    dst_path = f"{prefix}/dancexr"
    dst_file_path = os.path.join(dst_path, os.path.relpath(file_path, "dancexr"))

    if not os.path.exists(dst_file_path):
        # If the translated version doesn't exist, it needs translation
        return True
    
    commit_date_original = get_latest_commit_info(file_path)
    commit_date_translated = get_latest_commit_info(dst_file_path)

    # If the original file has no commit history, skip it
    if not commit_date_original:
        return False

    # If the translated version has no commit history, the original is "newer"
    if not commit_date_translated:
        return True

    return commit_date_original > commit_date_translated

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
            langs_needed = []
            
            for lang in target_languages:
                if is_file_newer_than_translation(file_path, lang):
                    langs_needed.append(lang)
            
            if langs_needed:
                untranslated.append({
                    "file": file_path,
                    "languages": langs_needed
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
                print(f"{item['file']} -> {', '.join(item['languages'])}")
