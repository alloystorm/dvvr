import requests
import json
import os
import re

# Function to read API key from a JSON file
def get_api_key_from_file(file_path):
    with open(file_path, 'r') as file:
        credentials = json.load(file)
        return credentials.get("api_key")

# Get the API key
api_key_path = os.path.expanduser("~/.openai/auth.json")
api_key = get_api_key_from_file(api_key_path)
# print(api_key)

translation = {
    'alpha': {
        'zh': '透明度',
        'tw': '透明度',
        'jp': 'アルファ',
        'kr': '알파'
    },
    'stage': {
        'zh': '舞台',
        'tw': '舞台',
        'jp': 'ステージ',
        'kr': '무대'
    },
    'scene bundle': {
        'zh': '场景包',
        'tw': '場景包',
        'jp': 'シーンバンドル',
        'kr': '씬 번들'
    },
    'asset': {
        'zh': '资源',
        'tw': '資源',
        'jp': 'アセット',
        'kr': '에셋'
    },
    'bone': {
        'zh': '骨骼',
        'tw': '骨骼',
        'jp': 'ボーン',
        'kr': '본'
    },
    'procedural': {
        'zh': '程序化',
        'tw': '程序化',
        'jp': 'プロシージャル',
        'kr': '프로시저'
    },
    'release': {
        'zh': '发布',
        'tw': '發布',
        'jp': 'リリース',
        'kr': '출시'
    },
    'version': {
        'zh': '版本',
        'tw': '版本',
        'jp': 'バージョン',
        'kr': '버전'
    },
    'pro': {
        'zh': '专业版',
        'tw': '專業版',
        'jp': 'プロ版',
        'kr': '프로버전'
    },
    'camera': {
        'zh': '摄影机',
        'tw': '攝影機',
        'jp': 'カメラ',
        'kr': '카메라'
    },
    'creator': {
        'zh': '创作版',
        'tw': '創作版',
        'jp': 'クリエイター版',
        'kr': '크리에이터버전'
    },
    'DanceXR Immersion': {
        'zh': 'DanceXR舞动幻境',
        'tw': 'DanceXR舞動幻境',
        'jp': 'ダンスXR幻境',
        'kr': '댄스XR환경'
    },
    'DanceXR Mix': {
        'zh': 'DanceXR舞动幻影',
        'tw': 'DanceXR舞動幻影',
        'jp': 'ダンスXR幻影',
        'kr': '댄스XR환영'
    },
    'Animate any model, anywhere': {
        'zh': '遍地皆是舞台，模型随意动画',
        'tw': '遍地皆是舞台，模型隨意動畫', 
        'jp': 'どこでも舞台、モデルは自由にアニメーション',
        'kr': '어디든 무대가 되고, 모델은 자유롭게 애니메이션',
    },
    'Long Take': {
        'zh': '长镜头',
        'tw': '長鏡頭', 
        'jp': '長回し',
        'kr': '롱 테이크',
    }
}

lang_names = {
    'zh': 'Simplified Chinese',
    'zh-rCN': 'Simplified Chinese',
    'tw': 'Traditional Chinese',
    'zh-rTW': 'Traditional Chinese',
    'jp': 'Japanese',
    'ja': 'Japanese',
    'kr': 'Korean',
    'ko-rKR': 'Korean',
    'de': 'German',
    'es': 'Spanish',
    'it': 'Italian',
    'fr': 'French',
}

gpt_model = "gpt-4o-mini"

def first_last_lines(text, f=5, l=5):
    lines = text.split("\n")
    return "\n".join(lines[:f]) + "\n...\n" + "\n".join(lines[-l:])

# Function to call OpenAI API for translation
def translate(text, target_language):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    with open("script/translate_page_prompt.txt", 'r', encoding='utf-8') as f:
            template = f.read()

    terms = '\n'.join([f"{key}={value[target_language]}" for i, (key, value) in enumerate(translation.items()) if target_language in value])
    prompt = template.format(
        target_language=lang_names[target_language], 
        terms=terms,
        text=text)
    
    # print(first_last_lines(prompt, 25, 5))

    data = {
        "model": gpt_model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0
    }
    response = requests.post(url, json=data, headers=headers)
    #print(first_last_lines(response.text, 20, 20))
    translated_text = response.json()['choices'][0]['message']['content'].strip()
    #translated_text = text
    # print(first_last_lines(translated_text))
    # print(f"Received translation...")
    return translated_text

def correct(text):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    with open("script/correct_page_prompt.txt", 'r', encoding='utf-8') as f:
            template = f.read()
    prompt = template.format(text=text)
    data = {
        "model": gpt_model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0
    }
    response = requests.post(url, json=data, headers=headers)
    # print(response.json())
    print("Received result...")
    return response.json()['choices'][0]['message']['content'].strip()


# Maximum tokens for GPT-3.5-turbo
MAX_TOKENS = 12000
# Roughly estimating 4 characters per token as a heuristic
CHARS_PER_TOKEN = 3
MAX_CHARS = MAX_TOKENS * CHARS_PER_TOKEN

def extract_xml_chunks(content):
    chunks = split_text(content, MAX_CHARS, "\n", prefix="")
    return chunks

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
            print(f"divide at: {paragraph}")
            if current_chunk:  # Avoid appending empty chunks
                chunks.append(current_chunk)
            current_chunk = prefix + paragraph
        else:
            # Prefix with "## " unless it's the very first paragraph
            divider = "" if not current_chunk and not first_paragraph else separator
            current_chunk = current_chunk + divider + paragraph
            #print(f"add to chunk: {paragraph}")
    
    # Don't forget to append the last chunk
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks
        
def correct_page(english_content):
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