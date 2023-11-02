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
language_links_pattern = re.compile(r'\[.+\]\(.*\) \| \[.+\]\(.*\) \| \[.+\]\(.*\) \| \[.+\]\(.*\) \| \[.+\]\(.*\)\n')

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
                if url_path.startswith('zh/'):
                    url_path = url_path[3:]
                elif url_path.startswith('jp/'):
                    url_path = url_path[3:]
                language_links = f"[Eng](/{url_path}) | [繁中](/tw/{url_path}) | [日本語](/jp/{url_path}) | [한국어](/kr/{url_path}) | [简中](/zh/{url_path})\n"
                
                # Check if the language links line already exists in the file
                existing_links_match = re.search(language_links_pattern, content)
                
                # Find the front matter
                front_matter_match = re.search(front_matter_pattern, content)
                
                if existing_links_match:
                    # Replace the existing language links line with the new line
                    content = content.replace(existing_links_match.group(), language_links)
                elif front_matter_match:
                    # Insert the language links line after the front matter
                    insert_pos = front_matter_match.end()
                    content = content[:insert_pos] + "\n" + language_links + content[insert_pos:]
                
                # Write the modified content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
