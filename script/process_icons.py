from PIL import Image, ImageOps
import os

# Folder containing images (set to current directory)
folder_path = "images/source"

# Process images
for filename in os.listdir(folder_path):
    if filename.startswith("ic_") and filename.endswith(".png"):
        img_path = os.path.join(folder_path, filename)
        
        # Open image in RGBA mode
        img = Image.open(img_path).convert("RGBA")
        
        # Split channels
        r, g, b, a = img.split()
        
        # Invert RGB channels
        r, g, b = r, g, ImageOps.invert(b)
        
        # Merge back with original alpha
        inverted_img = Image.merge("RGBA", (r, g, b, a))
        
        # Resize to 32x32
        resized_img = inverted_img.resize((16, 16), Image.LANCZOS)
        
        # Save with modified name
        new_filename = f"{os.path.splitext(filename)[0]}.png"
        new_path = os.path.join("images/icon", new_filename)
        resized_img.save(new_path)

        print(f"Processed: {filename} -> {new_filename}")

print("Done!")
