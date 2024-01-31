import os
import re

# Base path
base_path = [
    "dancexr",
    "zh/dancexr",
    "tw/dancexr",
    "jp/dancexr",
    "kr/dancexr"
]

# Regular expressions
front_matter_pattern = re.compile(r'---.*?---', re.DOTALL)
locale_pattern = re.compile(r'locale: .*')

# Iterate through all files in the base path
for folder in base_path:
    for subdir, _, files in os.walk(folder):
        for file in files:
            # Check if the file is a .md file
            if file.endswith('.md'):
                file_path = os.path.join(subdir, file)
                
                # Read the file content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Generate the URL based on the file path
                url_path = os.path.splitext(file_path.replace('\\', '/'))[0].lstrip('/')
                locale = "en-US"
                if url_path.startswith('zh/'):
                    locale = "zh-CN"
                elif url_path.startswith('tw/'):
                    locale = "zh-TW"
                elif url_path.startswith('jp/'):
                    locale = "ja-JP"
                elif url_path.startswith('kr/'):
                    locale = "ko-KR"
                
                # Find the front matter
                front_matter_match = re.search(front_matter_pattern, content)

                if front_matter_match:
                    front_matter = front_matter_match.group()
                    # Check if the locale line already exists in the front matter
                    existing_locale_match = re.search(locale_pattern, front_matter)
                    if existing_locale_match:
                        # Replace the existing locale line with the new line
                        front_matter = front_matter.replace(existing_locale_match.group(), f'locale: {locale}')
                    else:
                        # Insert the locale line at the beginning of the front matter
                        front_matter = f'---\nlocale: {locale}' + front_matter[3:]
                    content = content.replace(front_matter_match.group(), front_matter)
                
                    # Write the modified content back to the file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
