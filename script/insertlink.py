import os
import re

# Base path
base_path = "dancexr"

# Regular expression to find the front matter (between two ---)
front_matter_pattern = re.compile(r'---.*?---', re.DOTALL)

# Iterate through all files in the base path
for subdir, _, files in os.walk(base_path):
    for file in files:
        # Check if the file is a .md file
        if file.endswith('.md'):
            file_path = os.path.join(subdir, file)
            
            # Read the file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Generate the URL based on the file path
            # Remove the file extension and base path, and construct the URLs
            url_path = os.path.splitext(file_path.replace('\\', '/'))[0]
            language_links = f"[English](/{url_path}) | [简体中文](/zh/{url_path}) | [日本語](/jp/{url_path})\n"
            
            # Check if the language links line already exists in the file
            if language_links.strip() not in content:
                # Find the front matter
                front_matter_match = re.search(front_matter_pattern, content)
                
                # If front matter is found, insert the language links line after it
                if front_matter_match:
                    # Find the position to insert the language links line
                    insert_pos = front_matter_match.end()
                    
                    # Insert the language links line
                    content = content[:insert_pos] + "\n" + language_links + content[insert_pos:]
                    
                    # Write the modified content back to the file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
