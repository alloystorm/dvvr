import datetime
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

def is_file_committed_today(file_path):
    """Check if the given file was committed today."""
    commit_date = get_latest_commit_info(file_path)
    # print(f"Comparing {file_path} ({commit_date}) to today {commit_date[:10] == str(datetime.date.today())}")
    return commit_date[:10] == str(datetime.date.today())

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

def correct_file(subdir, file):
    # print(subdir + " " + file)
    _, file_extension = os.path.splitext(file)
    
    # Check if the file is a .md file
    if file_extension.lower() != '.md':
        return
    
    # Construct the file path
    file_path = os.path.join(subdir, file)
    
    # # Translate and save in corresponding directories for each language
    # target_files = []
    # for lang, dst_path in dst_paths.items():
    #     # Construct the destination file path
    #     dst_file_path = os.path.join(dst_path, os.path.relpath(file_path, src_path))

    #     # Check if destination file exists and is newer than source file
    #     # if os.path.exists(dst_file_path) and os.path.getmtime(dst_file_path) >= os.path.getmtime(file_path):
    #     #     print(f"Skipping {dst_file_path} because it is newer than source.")
    #     #     continue
    #     if not is_file_newer_than_translation(file_path, lang):
    #         # print(f"Skipping {dst_file_path} because it is newer than source.")
    #         continue
        
    #     print(dst_file_path)
    #     target_files.append((lang, dst_file_path))
    
    # if target_files:
    if is_file_committed_today(file_path):
        # Read the English content
        print(f"Reading {file_path}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            english_content = f.read()
        corrected = translate_page(english_content)
        with open(file_path, 'w', encoding='utf-8') as f:
           f.write(corrected)
        
def translate_page(english_content):
    # Split the content into chunks and translate each chunk
    front_matter, links, chunks = extract_section(english_content)
    corrected_chunks = []
    print(f"{len(chunks)} chunks to translate.")

    try:
        index = 0
        for chunk in chunks:
            index += 1
            print(f"Correcting grammar for chunk {index}/{len(chunks)} size: {len(chunk)}...")
            chunk = correct(chunk)
            corrected_chunks.append(chunk)
        corrected_content = "\n## ".join(corrected_chunks)
        return corrected_content
    except Exception as e:
        print(f"error: {e}")
        print(f"Skipping due to error...")
        return english_content

correct_file("", "index.md")
# correct_file("", "README.md")
# Iterate through all files in the source path
for subdir, _, files in os.walk(src_path):
    for file in files:
        correct_file(subdir, file)

# print(translate_page("---\ntitle: test page\nsidebar:\n  nav: \"releases\"\n---\n\nThis is a test. \nDanceXR Immersion: Animate any model, anywhere! ", [("zh", None)]))