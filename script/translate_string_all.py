import subprocess
import os
import re
from utils import translate
from utils import extract_xml_chunks

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
src_path = 'i18n/values'

# Define the paths for the translated content
dst_paths = {
    #'jp': 'i18n/values-ja',
    'zh': 'i18n/values-zh-rCN',
    #'tw': 'i18n/values-zh-rTW',
    #'kr': 'i18n/values-ko-rKR'
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
    if file_extension.lower() != '.txt':
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
        
import concurrent.futures
import time  # For simulating delays or retries

def translate_chunk(chunk, lang, index, total_chunks):
    success = False
    counter = 0
    if index > 1:
        chunk = "# " + chunk
    while not success and counter < 3:
        first_line = chunk.split("\n")[0]
        lines = len(chunk.split("\n"))
        print(f"Translating chunk {index}/{total_chunks} {first_line} of {lines} lines to {lang}... Attempt {counter+1}")
        translated = translate(chunk, lang)
        translatedLines = len(translated.split("\n"))
        success = lines == translatedLines
        counter += 1
        if success:
            return index, translated
    print(f"Failed to translate chunk. {first_line} {lines} vs {translatedLines} {counter}")
    print(f"Original: {chunk}")
    print(f"Translated: {translated}")
    return index, None  # Returning None if it fails after 3 attempts

def translate_page(english_content, target_files): 
    # Split the content into chunks
    chunks = english_content.split("\n# ")
    print(f"{len(chunks)} chunks to translate.")
    translated = chunks.copy()

    try:
        # Iterate through each target language and destination file
        for lang, dst_file_path in target_files:
            total_chunks = len(chunks)
            
            # Using ThreadPoolExecutor to translate chunks concurrently
            with concurrent.futures.ThreadPoolExecutor() as executor:
                # Submit translation tasks for each chunk
                futures = [
                    executor.submit(translate_chunk, chunk, lang, index + 1, total_chunks)
                    for index, chunk in enumerate(chunks)
                ]
                
                # Collect results as they complete
                for future in concurrent.futures.as_completed(futures):
                    index, result = future.result()
                    if result is None:
                        print(f"Translation failed for chunk.")
                        return  # Exit if any chunk translation fails
                    print(f"Translated chunk {index}/{total_chunks} to {lang}.")
                    translated[index - 1] = result
            # Combine the translated chunks and save the result
            if dst_file_path:
                print(f"Saving translated content to {dst_file_path}...")
                # Ensure the directory exists
                ensure_dir(dst_file_path)
                # Save the translated content
                with open(dst_file_path, 'w', encoding='utf-8') as f:
                    for chunk in translated:
                        f.write(chunk + "\n")
                
    except Exception as e:
        print(f"error: {e}")
        print(f"Skipping {target_files} due to error...")


# Iterate through all files in the source path
for subdir, _, files in os.walk(src_path):
    for file in files:
        translate_file(subdir, file)

# print(translate_page("---\ntitle: test page\nsidebar:\n  nav: \"releases\"\n---\n\nThis is a test. \nDanceXR Immersion: Animate any model, anywhere! ", [("zh", None)]))