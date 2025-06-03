import os
import re
import sys
import json
import requests
from script.utils import translate

def ensure_dir(file_path):
    """Ensure the directory exists."""
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(file_path, content):
    """Write content to a file."""
    ensure_dir(file_path)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def read_release_notes(file_path):
    """Read the release notes from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract version from filename or content
    version = os.path.basename(file_path).replace('.md', '')
    
    # Parse the markdown content
    title_pattern = re.compile(r'# DanceXR (.*) Release Notes')
    title_match = re.search(title_pattern, content)
    if title_match:
        version = title_match.group(1)
    
    return content, version

def call_ollama(prompt, model="qwen3"):
    """Call the Ollama API with a prompt and return the response."""
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        print(f"Error calling Ollama API: {e}")
        return None

def generate_all_content_with_ollama(version, base_url, release_notes_content):
    """Generate all content with a single Ollama call."""
    prompt = f"""
Here's the release notes for DanceXR version {version}:

{release_notes_content}

Please help me write the release announcements for Steam and Google Play in the following languages: English, Simplified Chinese, Traditional Chinese, Japanese, and Korean.

For each language, I need:
1. Steam announcement:
   - Title (max 80 characters)
   - Subtitle (max 120 characters)
   - Summary (max 180 characters)
   - Body (concise description including this link at the end: {base_url})

2. Google Play announcement:
   - A concise summary focused on main features and improvements

Please return your response in the following JSON structure:
```json
{{
  "steam": {{
    "en": {{
      "title": "",
      "subtitle": "",
      "summary": "",
      "body": ""
    }},
    "zh-CN": {{
      "title": "",
      "subtitle": "",
      "summary": "",
      "body": ""
    }},
    "zh-TW": {{
      "title": "",
      "subtitle": "",
      "summary": "",
      "body": ""
    }},
    "ja-JP": {{
      "title": "",
      "subtitle": "",
      "summary": "",
      "body": ""
    }},
    "ko-KR": {{
      "title": "",
      "subtitle": "",
      "summary": "",
      "body": ""
    }}
  }},
  "google": {{
    "en-US": "",
    "zh-CN": "",
    "zh-TW": "",
    "ja-JP": "",
    "ko-KR": ""
  }}
}}
```
"""
    
    print("Calling Ollama to generate all content...")
    response = call_ollama(prompt)
    
    if response:
        try:
            # The response should be a JSON string
            content = json.loads(response)
            return content
        except json.JSONDecodeError:
            print("Error parsing JSON response from Ollama")
            return None
    
    return None

def generate_steam_notes(version, base_url, release_notes_content, content=None):
    """Generate XML files for Steam announcements."""
    if not content:
        # Use traditional method with multiple API calls
        lang_mapping = {
            'en': 'English',
            'zh-CN': 'zh',  # Simplified Chinese
            'zh-TW': 'tw',  # Traditional Chinese
            'ja-JP': 'jp',  # Japanese
            'ko-KR': 'kr'   # Korean
        }
        
        for lang_code, lang_short in lang_mapping.items():
            # Create prompts for OpenAI
            prompts = {
                'title': f"Based on the following release notes, create a title for DanceXR {version} announcement, max 80 characters:\n\n{release_notes_content}",
                'subtitle': f"Based on the following release notes, create a subtitle for DanceXR {version} announcement, max 120 characters:\n\n{release_notes_content}",
                'summary': f"Based on the following release notes, create a summary for DanceXR {version} announcement, max 180 characters:\n\n{release_notes_content}",
                'body': f"Based on the following release notes, create a full description for DanceXR {version} announcement, be concise and include this link at the end: {base_url}\n\n{release_notes_content}"
            }
            
            steam_content = {}
            print(f"Generating Steam announcement for {lang_code}...")
            for key, prompt in prompts.items():
                steam_content[key] = translate(prompt, lang_short)
                print(f"Generated {key}: {steam_content[key][:50]}...")
            
            # Generate XML content
            file_path = f'notes/{version}/{lang_code}.xml'
            xml_content = f'''<?xml version="1.0" encoding="UTF-8" ?>
<content>
    <string id="title">{steam_content['title']}</string>
    <string id="subtitle">{steam_content['subtitle']}</string>
    <string id="summary">{steam_content['summary']}</string>
    <string id="body">{steam_content['body']}</string>
</content>'''
            
            write_file(file_path, xml_content)
            print(f"Generated {file_path}")
    else:
        # Use the pre-generated content from Ollama
        for lang_code, lang_content in content['steam'].items():
            file_path = f'notes/{version}/{lang_code}.xml'
            xml_content = f'''<?xml version="1.0" encoding="UTF-8" ?>
<content>
    <string id="title">{lang_content['title']}</string>
    <string id="subtitle">{lang_content['subtitle']}</string>
    <string id="summary">{lang_content['summary']}</string>
    <string id="body">{lang_content['body']}</string>
</content>'''
            
            write_file(file_path, xml_content)
            print(f"Generated {file_path}")

def generate_google_notes(version, release_notes_content, content=None):
    """Generate text file for Google Play release notes."""
    if not content:
        # Map between Google Play language codes and our language codes for translation
        lang_mapping = {
            'en-US': 'English',
            'zh-CN': 'zh',  # Simplified Chinese
            'zh-TW': 'tw',  # Traditional Chinese
            'ja-JP': 'jp',  # Japanese
            'ko-KR': 'kr'   # Korean
        }
        
        google_content_map = {}
        print("Generating Google Play release notes...")
        for lang_code, lang_short in lang_mapping.items():
            prompt = f"Based on the following release notes, create a concise summary for Google Play release notes for DanceXR {version}, focus on the main features and improvements:\n\n{release_notes_content}"
            google_content_map[lang_code] = translate(prompt, lang_short)
            print(f"Generated {lang_code}: {google_content_map[lang_code][:50]}...")
        
        # Generate text content
        file_path = f'notes/{version}/google.txt'
        google_content = '\n\n'.join([f'<{lang}>\n{text}\n</{lang}>' for lang, text in google_content_map.items()])
        write_file(file_path, google_content)
        print(f"Generated {file_path}")
    else:
        # Use the pre-generated content from Ollama
        file_path = f'notes/{version}/google.txt'
        google_content = '\n\n'.join([f'<{lang}>\n{text}\n</{lang}>' for lang, text in content['google'].items()])
        write_file(file_path, google_content)
        print(f"Generated {file_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_steam_google_notes.py <release_name>")
        print("Example: python generate_steam_google_notes.py 2025.6")
        sys.exit(1)
        
    release_name = sys.argv[1]
    release_notes_path = f"dancexr/releases/{release_name}.md"
    
    if not os.path.exists(release_notes_path):
        print(f"Error: Release notes file not found at {release_notes_path}")
        sys.exit(1)
        
    release_notes_content, version = read_release_notes(release_notes_path)
    
    print(f"Generating announcements for version {version}")
    base_url = f'https://vrstormlab.com/dancexr/releases/{version}'
    
    # Try to use Ollama's structured output first
    use_ollama = input("Do you want to use Ollama to generate all content at once? (y/n): ").lower() == 'y'
    content = None
    
    if use_ollama:
        content = generate_all_content_with_ollama(version, base_url, release_notes_content)
    
    # Generate Steam notes
    generate_steam_notes(version, base_url, release_notes_content, content)
    
    # Generate Google Play notes
    generate_google_notes(version, release_notes_content, content)
    
    print(f"All files generated successfully under notes/{version}/")

if __name__ == '__main__':
    main()