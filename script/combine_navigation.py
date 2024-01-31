import os
import re

# Base path
base_path = {
    "dancexr/navigation.md": "",
    "zh/dancexr/navigation.md": "zh",
    "tw/dancexr/navigation.md": "tw",
    "jp/dancexr/navigation.md": "jp",
    "kr/dancexr/navigation.md": "kr"
}

combined = ""
for file, suffix in base_path.items():
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        if (len(suffix) > 0):
            content = content.replace("docs:", "docs-" + suffix + ":").replace("releases:", "releases-" + suffix + ":").replace("/dancexr", "/" + suffix + "/dancexr")
        # remove the last 2 lines from the content
        # content = "\n".join(content.split("\n")[:-2])
        combined += content + "\n\n"
with open("_data/navigation.yml", 'w', encoding='utf-8') as f:
    f.write(combined)
