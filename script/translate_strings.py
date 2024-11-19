import os
import xml.etree.ElementTree as ET
from lxml import etree
import json
from utils import translate
import sys

refresh = False
if len(sys.argv) > 1:
    refresh = sys.argv[1] == "refresh"

# from translate import translate

# Function to read API key from a JSON file
def get_api_key_from_file(file_path):
    with open(file_path, 'r') as file:
        credentials = json.load(file)
        return credentials.get("api_key")

# Get the API key
api_key_path = os.path.expanduser("~/.openai/auth.json")
api_key = get_api_key_from_file(api_key_path)
# print(api_key)

# Define directories
ROOT_DIR = "i18n"  # Root directory of your resources
# ROOT_DIR = "../android/mobile/DanceXR/launcher/src/main/res"  # Root directory of your resources
DEFAULT_LANG_DIR = os.path.join(ROOT_DIR, "values")
LANG_DIRS = [os.path.join(ROOT_DIR, d) for d in ['values-ja', 'values-ko-rKR', 'values-zh-rCN', 'values-zh-rTW', 'values-de', 'values-es', 'values-it', 'values-fr']]
STRINGS_FILE = "strings.xml"

# Parse the default (English) strings.xml
default_tree = ET.parse(os.path.join(DEFAULT_LANG_DIR, STRINGS_FILE))
default_root = default_tree.getroot()
default_strings = {elem.attrib["name"]: elem.text for elem in default_root if not "translatable" in elem.attrib}

# Loop through each supported language
for lang_dir in LANG_DIRS:
    print("Processing " + lang_dir)
    missing_entries = {}
    lang = os.path.basename(lang_dir).replace("values-", "")
    # Parse the strings.xml for the current language
    lang_file = os.path.join(lang_dir, STRINGS_FILE)
    if not os.path.exists(lang_file):
        if not os.path.exists(lang_dir):
            os.makedirs(lang_dir)
        print(f"Creating empty string file {lang_file}...")
        tree = ET.ElementTree(ET.Element("resources"))
        tree.write(lang_file, xml_declaration=True, encoding="utf-8")
        # continue
    lang_tree = ET.parse(lang_file)
    lang_root = lang_tree.getroot()
    lang_strings = {elem.attrib["name"]: elem.text for elem in lang_root}

    # Compare and find missing entries
    for key, value in default_strings.items():
        if refresh or key not in lang_strings:
            missing_entries[key] = value

    MAX_TOKENS = 1024
    # Roughly estimating 4 characters per token as a heuristic
    CHARS_PER_TOKEN = 4
    MAX_CHARS = MAX_TOKENS * CHARS_PER_TOKEN

    # If there are missing entries, generate a file and wait for translation
    if missing_entries:
        print(f"Found {len(missing_entries)} missing entries in {lang_file}")
        # with open(os.path.join(lang_dir, "missing_strings.txt"), "w") as f:
        chunks = []
        #missing_strings = "<resources>\n"
        chunk = ""
        for key, value in missing_entries.items():
            line = f"\t<string name=\"{key}\">{value}</string>\n"
            if len(chunk) + len(line) > MAX_CHARS:
                chunks.append(chunk)
                chunk = line
            else:
                chunk += line
        if chunk:
            chunks.append(chunk)
        #missing_strings += "</resources>"
        print(f"Split {len(missing_entries)} entries into {len(chunks)} chunks.")
        index = 0
        if refresh:
            tree = ET.ElementTree(ET.Element("resources"))
        else:
            tree = ET.parse(lang_file)
        root = tree.getroot()
        for missing_strings in chunks:
            index += 1
            try:
                print(f"Translating chunk {index}... \n" + missing_strings)
                # Here, we would wait for translation. In this demo, let's mock the translation.
                # translated_strings = {key: f"Translated {value}" for key, value in missing_entries.items()}
                translated_strings = translate(f"<resources>\n{missing_strings}</resources>", lang).replace(" & ", " &amp; ").replace('"', "&quot;").replace("'", "&apos;")
                # Append the translated strings back to the respective strings.xml
                #parser = etree.XMLParser(remove_blank_text=True)
                # print(f"Translated chunk {index}... \n" + translated_strings)
                translatedRoot = ET.fromstring(translated_strings)
                for elem in translatedRoot:
                    root.append(elem)
                # for key, value in translated_strings.items():
                #     elem = etree.SubElement(root, "string", name=key)
                #     elem.text = value
                tree.write(lang_file, xml_declaration=True, encoding="utf-8")
            except Exception as e:
                print(e)
                print(f"Skipping {lang_file} due to error...")
print("Process completed!")
