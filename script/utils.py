import requests
import json
import os

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
    }
}

lang_names = {
    'zh': 'Simplified Chinese',
    'tw': 'Traditional Chinese',
    'jp': 'Japanese',
    'kr': 'Korean'
}

gpt_model = "gpt-3.5-turbo-1106"

# Function to call OpenAI API for translation
def translate(text, target_language):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    with open("script/translate_page_prompt.txt", 'r', encoding='utf-8') as f:
            template = f.read()

    terms = '\n'.join([f"{i+1}. {key}: {value[target_language]}" for i, (key, value) in enumerate(translation.items()) if target_language in value])
    prompt = template.format(
        target_language=lang_names[target_language], 
        terms=terms,
        text=text)
    
    # print(prompt)

    data = {
        "model": gpt_model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0
    }
    response = requests.post(url, json=data, headers=headers)
    # print(response.json())
    print("Received translation...")
    translated_text = response.json()['choices'][0]['message']['content'].strip()
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
