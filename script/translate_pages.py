import subprocess
import os
import re
from utils import translate
from utils import correct_page
from utils import extract_section

def get_latest_commit_info(file_path):
    """Get the latest commit date for a given file."""
    cmd = f"git log -1 --pretty=format:%ci -- {file_path}"
    result = subprocess.run(cmd.split(), capture_output=True, text=True, check=True)
    return result.stdout.strip()

def is_file_newer_than_translation(file_path, prefix):
    """Check if the given file is newer than its Japanese counterpart."""
    jp_file_path = os.path.join(prefix, file_path)

    if not os.path.exists(jp_file_path):
        # If the Japanese version doesn't exist, the original is "newer".
        return True
    
    commit_date_original = get_latest_commit_info(file_path)
    commit_date_jp = get_latest_commit_info(jp_file_path)

    # If the original file has no commit history, it's not "newer".
    if not commit_date_original:
        return False

    # If the Japanese version has no commit history, the original is "newer".
    if not commit_date_jp:
        return True

    if commit_date_original > commit_date_jp:
        print(f"Comparing {file_path} ({commit_date_original}) to {jp_file_path} ({commit_date_jp}) {commit_date_original > commit_date_jp}")
    # Return True if the original file's latest commit is more recent than the Japanese version.
    return commit_date_original > commit_date_jp


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

def translate_file(subdir, file):
    print(subdir + " " + file)
    _, file_extension = os.path.splitext(file)
    
    # Check if the file is a .md file
    if file_extension.lower() != '.md' and file_extension.lower() != '.txt':
        return
    
    # Construct the file path
    file_path = os.path.join(subdir, file)
    
    # Translate and save in corresponding directories for each language
    target_files = []
    for lang, dst_path in dst_paths.items():
        # Construct the destination file path
        dst_file_path = os.path.join(dst_path, os.path.relpath(file_path, src_path))

        # Check if destination file exists and is newer than source file
        # if os.path.exists(dst_file_path) and os.path.getmtime(dst_file_path) >= os.path.getmtime(file_path):
        #     print(f"Skipping {dst_file_path} because it is newer than source.")
        #     continue
        if not is_file_newer_than_translation(file_path, lang):
            # print(f"Skipping {dst_file_path} because it is newer than source.")
            continue
        
        print(dst_file_path)
        target_files.append((lang, dst_file_path))
    
    if target_files:
        # Read the English content
        with open(file_path, 'r+', encoding='utf-8') as f:
            english_content = f.read()
            #corrected = correct_page(english_content)
            #f.write(corrected)
            translate_page(english_content, target_files)
        
def translate_page(english_content, target_files):
    # Split the content into chunks and translate each chunk
    front_matter, links, chunks = extract_section(english_content)
    print(f"{len(chunks)} chunks to translate.")

    try:
        index = 0
        for lang, dst_file_path in target_files:
            translated_chunks = []
            for chunk in chunks:
                print(f"Translating chunk {index}/{len(chunks)} lang: {lang}...")
                translated_chunks.append(translate(chunk, lang))
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
                    translated_title = translate(title, lang)
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

# translate_file("dancexr/releases", "2025.1.md")
# translate_file("", "README.md")
# Iterate through all files in the source path
for subdir, _, files in os.walk(src_path):
   for file in files:
       translate_file(subdir, file)

# print(translate_page("---\ntitle: test page\nsidebar:\n  nav: \"releases\"\n---\n\nThis is a test. \nDanceXR Immersion: Animate any model, anywhere! ", [("zh", None)]))