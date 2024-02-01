import subprocess
import os
import re
from utils import translate
from utils import correct

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

# Maximum tokens for GPT-3.5-turbo
MAX_TOKENS = 8192
# Roughly estimating 4 characters per token as a heuristic
CHARS_PER_TOKEN = 4
MAX_CHARS = MAX_TOKENS * CHARS_PER_TOKEN

def extract_section(content):
    front_matter_pattern = re.compile(r'---.*?---', re.DOTALL)
    front_matter_match = re.search(front_matter_pattern, content)
    if front_matter_match:
        front_matter = front_matter_match.group()
        content = content.replace(front_matter, "")
    else:
        front_matter = ""
    language_links_pattern = re.compile(r'\[.+\]\(.*\) \| \[.+\]\(.*\) \| \[.+\]\(.*\) \| \[.+\]\(.*\) \| \[.+\]\(.*\)\n')
    links_match = re.search(language_links_pattern, content)
    if links_match:
        links = links_match.group()
        content = content.replace(links_match.group(), "")
    else:
        links = ""
    chunks = split_text(content, MAX_CHARS)
    return front_matter, links, chunks

def split_text(text, max_chars, separator="\n## ", prefix = "## "):
    # Split by section headers and ensure each chunk is under the maximum character limit
    paragraphs = text.split(separator)
    print(f"{len(paragraphs)} paragraphs.")
    chunks = []
    
    # Handle the first paragraph separately to avoid undesired prefixing
    first_paragraph = paragraphs[0] if paragraphs else ""
    remaining_paragraphs = paragraphs[1:] if len(paragraphs) > 1 else []
    current_chunk = first_paragraph
    
    # If the first paragraph is too long, make it a separate chunk
    if len(first_paragraph) > max_chars or len(remaining_paragraphs) == 0:
        chunks.append(first_paragraph)
        first_paragraph = ""
        current_chunk = ""
    
    for paragraph in remaining_paragraphs:
        # If adding the next paragraph exceeds the max length, start a new chunk
        if len(current_chunk) + len(paragraph) > max_chars:
            if current_chunk:  # Avoid appending empty chunks
                chunks.append(current_chunk)
            current_chunk = prefix + paragraph
        else:
            # Prefix with "## " unless it's the very first paragraph
            divider = "" if not current_chunk and not first_paragraph else separator
            current_chunk = current_chunk + divider + paragraph
    
    # Don't forget to append the last chunk
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks

def translate_file(subdir, file):
    print(subdir + " " + file)
    _, file_extension = os.path.splitext(file)
    
    # Check if the file is a .md file
    if file_extension.lower() != '.md':
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
        with open(file_path, 'r', encoding='utf-8') as f:
            english_content = f.read()
        corrected = translate_page(english_content, target_files)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(corrected)
        
def translate_page(english_content, target_files):
    # Split the content into chunks and translate each chunk
    front_matter, links, chunks = extract_section(english_content)
    translated_chunks = []
    corrected_chunks = []
    print(f"{len(chunks)} chunks to translate.")

    try:
        index = 0
        for chunk in chunks:
            index += 1
            print(f"Correcting grammar for chunk {index}/{len(chunks)} size: {len(chunk)}...")
            chunk = correct(chunk)
            corrected_chunks.append(chunk)

        for lang, dst_file_path in target_files:
            for chunk in chunks:
                print(f"Translating chunk {index}/{len(chunks)} lang: {lang}...")
                translated_chunks.append(translate(chunk, lang))
            # Combine the translated chunks and save the result
            translated_content = "\n## ".join(translated_chunks)
            corrected_content = "\n## ".join(corrected_chunks)
            if (links):
                translated_content = links + "\n" + translated_content
                corrected_content = links + "\n" + corrected_content
            # print(f"Translated content: {translated_content}")
            if (front_matter):
                corrected_content = front_matter + "\n" + corrected_content
                nav_pattern = re.compile(r'nav: ".*"')
                nav_line = re.search(nav_pattern, front_matter)
                if nav_line:
                    line = nav_line.group()
                    nav = line.replace("nav: ", "").replace('"', "").strip()
                    # print("[nav]" + line + " " + nav)
                    front_matter = front_matter.replace(line, line.replace(nav, nav + "-" + lang))
                    # print(f"[{front_matter}]")
                title_pattern = re.compile(r'title: .*')
                title_line = re.search(title_pattern, front_matter)
                if title_line:
                    line = title_line.group()
                    title = line.replace("title:", "").strip()
                    translated_title = translate(title, lang)
                    # print("[title]" + line + " " + title + " " + translated_title)
                    front_matter = front_matter.replace(title, translated_title)
                    # print(f"[{front_matter}]")
                front_matter = front_matter.replace("permalink: /dancexr/", f"permalink: /{lang}/dancexr/")
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
                existing_locale_match = re.search(locale_pattern, front_matter)
                if existing_locale_match:
                    # Replace the existing locale line with the new line
                    front_matter = front_matter.replace(existing_locale_match.group(), f'locale: {locale}')
                else:
                    # Insert the locale line at the beginning of the front matter
                    front_matter = f'---\nlocale: {locale}' + front_matter[3:]
                translated_content = front_matter + "\n" + translated_content
            
            if dst_file_path:
                print(f"Saving translated content to {dst_file_path}...")
                # Ensure the directory exists
                ensure_dir(dst_file_path)
                # Save the translated content
                with open(dst_file_path, 'w', encoding='utf-8') as f:
                    f.write(translated_content)
            else:
                print(f"Translated content: \n{translated_content}")
        return corrected_content
    except Exception as e:
        print(f"error: {e}")
        print(f"Skipping {target_files} due to error...")
        return english_content

translate_file("", "index.md")
# translate_file("", "README.md")
# Iterate through all files in the source path
for subdir, _, files in os.walk(src_path):
    for file in files:
        translate_file(subdir, file)

# print(translate_page("---\ntitle: test page\nsidebar:\n  nav: \"releases\"\n---\n\nThis is a test. \nDanceXR Immersion: Animate any model, anywhere! ", [("zh", None)]))