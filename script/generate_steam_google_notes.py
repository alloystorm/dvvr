import os
import re
import sys
import json
import requests
from typing import Dict, Optional
from pydantic import BaseModel, Field

# Define Pydantic models for structured data
class SteamContent(BaseModel):
    title: str = Field(..., max_length=80)
    subtitle: str = Field(..., max_length=120)
    summary: str = Field(..., max_length=180)
    body: str

class SteamLanguages(BaseModel):
    english: SteamContent
    schinese: SteamContent
    tchinese: SteamContent
    japanese: SteamContent
    korean: SteamContent

class GooglePlayContent(BaseModel):
    en_US: str = Field(..., alias="en-US")
    zh_CN: str = Field(..., alias="zh-CN")
    zh_TW: str = Field(..., alias="zh-TW")
    ja_JP: str = Field(..., alias="ja-JP")
    ko_KR: str = Field(..., alias="ko-KR")

class AnnouncementContent(BaseModel):
    steam: SteamLanguages
    google: GooglePlayContent

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
        "format": AnnouncementContent.model_json_schema()
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
    # Create model schema for Ollama to follow
    
    prompt = f"""
Here's the release notes for DanceXR version {version}:

{release_notes_content}

Please help me write the release announcements for Steam and Google Play in the following languages: English, Simplified Chinese, Traditional Chinese, Japanese, and Korean.

For each language, I need:
1. Steam announcement:
   - Title (max 80 characters)
   - Subtitle (max 120 characters)
   - Summary (max 180 characters)
   - Body (description with this link at the end: {base_url})

2. Google Play announcement:
   - A concise summary focused on main features and improvements
"""
    
    print("Calling Ollama to generate all content...")
    response = call_ollama(prompt, "phi4")
    
    if response:
        try:
            # The response should be a JSON string
            content_json = json.loads(response)
            # Validate with Pydantic model
            content = AnnouncementContent.model_validate(content_json)
            # Return the model as a dictionary
            return content.model_dump(by_alias=True)
        except json.JSONDecodeError:
            print("Error parsing JSON response from Ollama")
            return None
        except Exception as e:
            print(f"Error validating response: {e}")
            return None
    
    return None

def generate_steam_notes(version, content=None):
    """Generate XML files for Steam announcements."""
    
    itchio_body = f'DanceXR {version}\n\n'

    # Use the pre-generated content from Ollama
    for lang_code, lang_content in content['steam'].items():
        file_path = f'notes/{version}/steam_{lang_code}.xml'
        xml_content = f'''<?xml version="1.0" encoding="UTF-8" ?>
<content>
    <string id="title">{lang_content['title']}</string>
    <string id="subtitle">{lang_content['subtitle']}</string>
    <string id="summary">{lang_content['summary']}</string>
    <string id="body">{lang_content['body']}</string>
</content>'''
        itchio_body += f"{lang_content['body']}\n\n"
        write_file(file_path, xml_content)
        print(f"Generated {file_path}")
    # Write the Itch.io body content
    itchio_file_path = f'notes/{version}/itchio.txt'
    write_file(itchio_file_path, itchio_body.strip())

def generate_google_notes(version, content=None):
    """Generate text file for Google Play release notes."""
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
    # use_ollama = input("Do you want to use Ollama to generate all content at once? (y/n): ").lower() == 'y'
    content = None
    
    # if use_ollama:
    content = generate_all_content_with_ollama(version, base_url, release_notes_content)
    
    # Generate Steam notes
    generate_steam_notes(version, content)
    
    # Generate Google Play notes
    generate_google_notes(version, content)
    
    print(f"All files generated successfully under notes/{version}/")

if __name__ == '__main__':
    main()