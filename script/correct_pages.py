import datetime
import subprocess
import os
from utils import correct_page

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
        corrected = correct_page(english_content)
        with open(file_path, 'w', encoding='utf-8') as f:
           f.write(corrected)

correct_file("", "index.md")
# correct_file("", "README.md")
# Iterate through all files in the source path
for subdir, _, files in os.walk(src_path):
    for file in files:
        correct_file(subdir, file)

# print(translate_page("---\ntitle: test page\nsidebar:\n  nav: \"releases\"\n---\n\nThis is a test. \nDanceXR Immersion: Animate any model, anywhere! ", [("zh", None)]))