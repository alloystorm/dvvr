import os
import xml.etree.ElementTree as ET
from lxml import etree
from translate import translate

# Define directories
ROOT_DIR = "i18n"  # Root directory of your resources
DEFAULT_LANG_DIR = os.path.join(ROOT_DIR, "values")
LANG_DIRS = [os.path.join(ROOT_DIR, d) for d in os.listdir(ROOT_DIR) if d.startswith("values-")]
STRINGS_FILE = "strings.xml"

# Parse the default (English) strings.xml
default_tree = ET.parse(os.path.join(DEFAULT_LANG_DIR, STRINGS_FILE))
default_root = default_tree.getroot()
default_strings = {elem.attrib["name"]: elem.text for elem in default_root}

# Loop through each supported language
for lang_dir in LANG_DIRS:
    missing_entries = {}
    lang = os.path.basename(lang_dir).replace("values-", "")
    # Parse the strings.xml for the current language
    lang_file = os.path.join(lang_dir, STRINGS_FILE)
    if not os.path.exists(lang_file):
        continue
    lang_tree = ET.parse(lang_file)
    lang_root = lang_tree.getroot()
    lang_strings = {elem.attrib["name"]: elem.text for elem in lang_root}

    # Compare and find missing entries
    for key, value in default_strings.items():
        if key not in lang_strings:
            missing_entries[key] = value

    # If there are missing entries, generate a file and wait for translation
    if missing_entries:
        # with open(os.path.join(lang_dir, "missing_strings.txt"), "w") as f:
        missing_strings = "<resources>\n"
        for key, value in missing_entries.items():
            missing_strings += f"\t<string name=\"{key}\">{value}</string>\n"
        missing_strings += "</resources>"
        print(missing_strings)
        try:
            # Here, we would wait for translation. In this demo, let's mock the translation.
            # translated_strings = {key: f"Translated {value}" for key, value in missing_entries.items()}
            translated_strings = translate(missing_strings, lang)
            # Append the translated strings back to the respective strings.xml
            #parser = etree.XMLParser(remove_blank_text=True)
            tree = ET.parse(lang_file)
            root = tree.getroot()
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
