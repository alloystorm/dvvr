import subprocess
import os
import re
import argparse
from utils import translate_local
from utils import correct_page
from utils import extract_section
from find_untranslated_pages import find_untranslated_pages

# Define the path to the English content
src_path = 'dancexr'

# Define the paths for the translated content
dst_paths = {
    'jp': 'jp/dancexr',
    'zh': 'zh/dancexr',
    'kr': 'kr/dancexr',
    'tw': 'tw/dancexr'
}

# Function to create directories if they don't exist
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def translate_file(file_path, langs_needed=None):
    if not langs_needed:
        langs_needed = dst_paths.keys()
        
    print(file_path)
    
    # Translate and save in corresponding directories for each language
    target_files = []
    for lang in langs_needed:
        dst_path = dst_paths[lang]
        # Construct the destination file path
        dst_file_path = os.path.join(dst_path, os.path.relpath(file_path, src_path))

        print(dst_file_path)
        target_files.append((lang, dst_file_path))
    
    if target_files:
        # Read the English content
        with open(file_path, 'r+', encoding='utf-8') as f:
            english_content = f.read()
            translate_page(english_content, target_files)
        
def translate_page(english_content, target_files):
    # Split the content into chunks and translate each chunk
    front_matter, links, chunks = extract_section(english_content)
    print(f"{len(chunks)} chunks to translate.")

    try:
        index = 0
        for lang, dst_file_path in target_files:
            existing_translation = ""
            if dst_file_path and os.path.exists(dst_file_path):
                with open(dst_file_path, 'r', encoding='utf-8') as f:
                    existing_translation = f.read()

            translated_chunks = []
            index = 0
            for chunk in chunks:
                index += 1
                print(f"Translating chunk {index}/{len(chunks)} lang: {lang}...")
                
                max_retries = 3
                translated_chunk = ""
                for attempt in range(max_retries):
                    translated_chunk = translate_local(chunk, lang, existing_translation=existing_translation)
                    
                    # Validation
                    orig_sections = len(re.findall(r'^#+\s', chunk, flags=re.MULTILINE))
                    trans_sections = len(re.findall(r'^#+\s', translated_chunk, flags=re.MULTILINE))
                    orig_bullets = len(re.findall(r'^[\s]*([-*]|\d+\.)\s', chunk, flags=re.MULTILINE))
                    trans_bullets = len(re.findall(r'^[\s]*([-*]|\d+\.)\s', translated_chunk, flags=re.MULTILINE))
                    
                    if orig_sections == trans_sections and orig_bullets == trans_bullets:
                        break
                    else:
                        print(f"Validation failed (Attempt {attempt+1}/{max_retries}). Sections: {orig_sections} vs {trans_sections}, Bullets: {orig_bullets} vs {trans_bullets}. Retrying...")
                
                translated_chunks.append(translated_chunk)
            # Combine the translated chunks and save the result
            translated_content = "\n## ".join(translated_chunks)
            if (links):
                translated_content = links + "\n" + translated_content
            # print(f"Translated content: {translated_content}")
            if (front_matter):
                nav_pattern = re.compile(r'nav: ".*"')
                fm = front_matter
                nav_line = re.search(nav_pattern, fm)
                if nav_line:
                    line = nav_line.group()
                    nav = line.replace("nav: ", "").replace('"', "").strip()
                    # print("[nav]" + line + " " + nav)
                    fm = fm.replace(line, line.replace(nav, nav + "-" + lang))
                    # print(f"[{fm}]")
                title_pattern = re.compile(r'title: .*')
                title_line = re.search(title_pattern, fm)
                if title_line:
                    line = title_line.group()
                    title = line.replace("title:", "").strip()
                    translated_title = translate_local(title, lang)
                    # print("[title]" + line + " " + title + " " + translated_title)
                    fm = fm.replace(title, translated_title)
                    # print(f"[{fm}]")
                fm = fm.replace("permalink: /dancexr/", f"permalink: /{lang}/dancexr/")
                locale_pattern = re.compile(r'locale: .*')
                locale = "en-US"
                if lang == 'zh':
                    locale = "zh-CN"
                elif lang == 'tw':
                    locale = "zh-TW"
                elif lang == 'jp':
                    locale = "ja-JP"
                elif lang == 'kr':
                    locale = "ko-KR"
                existing_locale_match = re.search(locale_pattern, fm)
                if existing_locale_match:
                    # Replace the existing locale line with the new line
                    fm = fm.replace(existing_locale_match.group(), f'locale: {locale}')
                else:
                    # Insert the locale line at the beginning of the front matter
                    fm = f'---\nlocale: {locale}' + fm[3:]
                translated_content = fm + "\n" + translated_content
            
            if dst_file_path:
                print(f"Saving translated content to {dst_file_path}...")
                # Ensure the directory exists
                ensure_dir(dst_file_path)
                # Save the translated content
                with open(dst_file_path, 'w', encoding='utf-8') as f:
                    f.write(translated_content)
            else:
                print(f"Translated content: \n{translated_content}")
    except Exception as e:
        print(f"error: {e}")
        print(f"Skipping {target_files} due to error...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate DanceXR pages.")
    parser.add_argument("--file", type=str, help="Specific file to translate")
    parser.add_argument("--langs", type=str, help="Comma-separated list of languages to translate to")
    args = parser.parse_args()

    if args.file:
        langs = args.langs.split(",") if args.langs else list(dst_paths.keys())
        translate_file(args.file, langs)
    else:
        # Default behavior: translate all outdated pages
        untranslated = find_untranslated_pages()
        for item in untranslated:
            translate_file(item["file"], item["languages"])

# print(translate_page("---\ntitle: test page\nsidebar:\n  nav: \"releases\"\n---\n\nThis is a test. \nDanceXR Immersion: Animate any model, anywhere! ", [("zh", None)]))