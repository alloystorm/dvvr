from translate import translate, split_text, ensure_dir

# Maximum tokens for GPT-3.5-turbo
MAX_TOKENS = 1024
# Roughly estimating 4 characters per token as a heuristic
CHARS_PER_TOKEN = 4
MAX_CHARS = MAX_TOKENS * CHARS_PER_TOKEN

languages = ["ja", "ko-rKR", "zh-rCN", "zh-rTW"]

with open("i18n/values/strings.xml", 'r', encoding='utf-8') as f:
    english_content = f.read()
    
    # Split the content into chunks and translate each chunk
    chunks = split_text(english_content, MAX_CHARS, "\n", "")
    translated_chunks = []
    print(f"{len(chunks)} chunks to translate.")

    for lang in languages:
        dst_file_path = f"i18n/values-{lang}/strings.xml"
        try:
            index = 0
            for chunk in chunks:
                index += 1
                print(f"Translating chunk {index}/{len(chunks)} size: {len(chunk)}...")
                translated_chunks.append(translate(chunk, lang))
                print("Done.")
            
            # Combine the translated chunks and save the result
            translated_content = "\n".join(translated_chunks)
            print(f"Saving translated content to {dst_file_path}...")
            
            # Ensure the directory exists
            ensure_dir(dst_file_path)
            
            # Save the translated content
            with open(dst_file_path, 'w', encoding='utf-8') as f:
                f.write(translated_content)
        except Exception as e:
            print(e)
            print(f"Skipping {dst_file_path} due to error...")
            continue