from PIL import Image, ImageDraw
import os

# Folder for saving icons
folder_path = "images/icon"

def create_table_icon(up=False, down=False, left=False, right=False, 
                      size=(16, 16), line_width=2, padding=2, filename="table_icon.png"):
    """
    Generates a table line icon with the specified connections and saves it as a PNG.
    
    :param up: Connects upwards if True.
    :param down: Connects downwards if True.
    :param left: Connects left if True.
    :param right: Connects right if True.
    :param size: Tuple (width, height) for the icon size.
    :param line_width: Thickness of the lines.
    :param padding: Space from edges for line placement.
    :param filename: Name of the output file.
    """
    img = Image.new("RGBA", size, (255, 255, 255, 0))  # Transparent background
    draw = ImageDraw.Draw(img)

    # Calculate center points
    cx, cy = size[0] // 2, size[1] // 2
    half_width = line_width // 2
    fillcolor = (255, 0, 0, 255)  # Red color for lines

    # Define start and end positions for each direction
    if up:
        draw.line([(cx, padding), (cx, cy)], fill=fillcolor, width=line_width)
    if down:
        draw.line([(cx, cy), (cx, size[1] - padding)], fill=fillcolor, width=line_width)
    if left:
        draw.line([(padding, cy), (cx, cy)], fill=fillcolor, width=line_width)
    if right:
        draw.line([(cx, cy), (size[0] - padding, cy)], fill=fillcolor, width=line_width)

    img.save(os.path.join(folder_path, filename))
    print(f"Created table icon: {filename}")

# Example usage: Create different table connection icons
create_table_icon(up=True, down=True, filename="ic_line_v.png")  # Vertical line
create_table_icon(up=True, right=True, filename="ic_line_l.png")  # L line
create_table_icon(up=True, down=True, right=True, filename="ic_line_t.png")  # T-junction
create_table_icon(filename="ic_space.png")

print("Icons created!")
