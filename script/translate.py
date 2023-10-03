import os
import requests
import json

# Function to read API key from a JSON file
def get_api_key_from_file(file_path):
    with open(file_path, 'r') as file:
        credentials = json.load(file)
        return credentials.get("api_key")

# Get the API key
api_key_path = os.path.expanduser("~/.openai/auth.json")
api_key = get_api_key_from_file(api_key_path)
print(api_key)

# Define the path to the English content
src_path = 'dancexr'

# Define the paths for the translated content
dst_paths = {
    'jp': 'jp/dancexr',
    'zh': 'zh/dancexr'
}

# Function to call OpenAI API for translation
def translate(text, target_language):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo-16k",
        "messages": [{"role": "user", "content": f"Translate the following English text to {target_language}:\n{text}"}],
        "max_tokens": len(text) * 2,  # Adjust as needed
        "temperature": 0.7
    }
    response = requests.post(url, json=data, headers=headers)
    print(response.json())
    translated_text = response.json()['choices'][0]['message']['content'].strip()
    return translated_text

# Function to create directories if they don't exist
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

# Iterate through all files in the source path
for subdir, _, files in os.walk(src_path):
    for file in files:
        # Construct the file path
        file_path = os.path.join(subdir, file)
        
        # Read the English content
        with open(file_path, 'r', encoding='utf-8') as f:
            english_content = f.read()
        
        # Translate and save in corresponding directories for each language
        for lang, dst_path in dst_paths.items():
            # Construct the destination file path
            dst_file_path = os.path.join(dst_path, os.path.relpath(file_path, src_path))

            # Check if destination file exists and is newer than source file
            if os.path.exists(dst_file_path) and os.path.getmtime(dst_file_path) >= os.path.getmtime(file_path):
                print(f"Skipping {dst_file_path} because it is newer than source.")
                continue
            
            print(dst_file_path)
            translated_content = translate(english_content, lang)
            
            # Ensure the directory exists
            ensure_dir(dst_file_path)
            
            # Save the translated content
            with open(dst_file_path, 'w', encoding='utf-8') as f:
               f.write(translated_content)
