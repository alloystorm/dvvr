import tkinter as tk
from tkinter import filedialog
import time
import threading
import sys
import os

class Teleprompter:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="black")
        
        # Create borderless window
        self.root.overrideredirect(True)
        
        # Window size and position settings
        self.root.geometry("1440x300+20+20")  # Default size and position
        self.root.minsize(400, 200)  # Minimum window size
        self.root.attributes("-topmost", True)  # Always on top by default
        
        # Create custom title bar
        self.title_bar = tk.Frame(root, bg="#1A1A1A", height=25)
        self.title_bar.pack(fill="x", side="top")
        
        # Title text
        self.title_label = tk.Label(self.title_bar, text="Simple Teleprompter", 
                                   bg="#1A1A1A", fg="white", font=("Arial", 10))
        self.title_label.pack(side="left", padx=10)
        
        # Close button
        self.close_button = tk.Button(self.title_bar, text="×", bg="#1A1A1A", fg="white",
                                    font=("Arial", 14), bd=0, highlightthickness=0,
                                    activebackground="#AA0000", command=self.exit_application)
        self.close_button.pack(side="right", padx=10)
        
        # Bind title bar for moving window
        self.title_bar.bind("<ButtonPress-1>", self.start_move)
        self.title_bar.bind("<ButtonRelease-1>", self.stop_move)
        self.title_bar.bind("<B1-Motion>", self.do_move)
        self.title_label.bind("<ButtonPress-1>", self.start_move)
        self.title_label.bind("<ButtonRelease-1>", self.stop_move)
        self.title_label.bind("<B1-Motion>", self.do_move)
        
        # Create canvas for smooth scrolling
        self.canvas = tk.Canvas(
            root,
            bg="black",
            highlightthickness=0,
            bd=0
        )
        self.canvas.pack(expand=True, fill="both", padx=20, pady=(5, 10))
        
        # Create text frame inside canvas - change to include multiple visible lines
        self.text_frame = tk.Frame(self.canvas, bg="black")
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.text_frame, anchor="nw")
        
        # Create a container for multiple lines
        self.lines_container = tk.Frame(self.text_frame, bg="black")
        self.lines_container.pack(fill="both", expand=True)
        
        # Empty list to hold line label widgets
        self.line_labels = []
        
        # Number of visible lines to create (current + next + buffer)
        self.visible_line_count = 4
        
        # Create label widgets for visible lines
        for i in range(self.visible_line_count):
            color = "white" if i == 0 else "#808080"  # First line white, rest gray
            label = tk.Label(
                self.lines_container,
                text="" if i > 0 else "Press 'O' to open a file",
                font=("Arial", 48),
                fg=color,
                bg="black",
                wraplength=700,
                justify="center"
            )
            label.pack(fill="both", pady=(0, 10))
            self.line_labels.append(label)
        
        # Variables
        self.lines = []
        self.top_line_index = 0  # Index of the top visible line in the script
        self.playing = False
        self.wpm = 100  # Default words per minute
        self.scroll_speed = 1.0  # Pixels per update
        self.scroll_position = 0.0
        self.scroll_update_ms = 16  # ~60fps
        self.x = None
        self.y = None
        self.scroll_animation_id = None
        
        # Add fixed line height variable
        self.fixed_line_height = 120  # Default height for each line
        
        # Keybindings
        self.root.bind("<o>", self.open_file)
        self.root.bind("<O>", self.open_file)
        self.root.bind("<space>", self.toggle_play)
        self.root.bind("<Escape>", self.exit_application)
        self.root.bind("<Up>", self.increase_speed)
        self.root.bind("<Down>", self.decrease_speed)
        self.root.bind("<Left>", self.previous_line)
        self.root.bind("<Right>", self.next_line)
        self.root.bind("<f>", self.toggle_font_size)
        self.root.bind("<F>", self.toggle_font_size)
        self.root.bind("<t>", self.toggle_always_on_top)
        self.root.bind("<T>", self.toggle_always_on_top)
        
        # Bind window resize event
        self.root.bind("<Configure>", self.on_resize)
        
        # Font sizes for toggling
        self.font_sizes = [36, 48, 60, 72]
        self.current_font_size_index = 1  # Start with 48
        
        # Status display
        self.status = tk.Label(
            root,
            text="WPM: 100 | SPACE: Play/Pause | ↑↓: Speed | ←→: Navigate | F: Font | T: TopMost | ESC: Exit",
            font=("Arial", 10),
            fg="gray",
            bg="black"
        )
        self.status.pack(side="bottom", pady=5)

    def start_move(self, event):
        """Begin window drag operation"""
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        """End window drag operation"""
        self.x = None
        self.y = None

    def do_move(self, event):
        """Move window during drag operation"""
        if self.x is not None and self.y is not None:
            deltax = event.x - self.x
            deltay = event.y - self.y
            x = self.root.winfo_x() + deltax
            y = self.root.winfo_y() + deltay
            self.root.geometry(f"+{x}+{y}")

    def on_resize(self, event):
        """Update text wrapping when window is resized"""
        if event.widget == self.root:
            # Update canvas size
            new_width = self.root.winfo_width() - 40
            
            # Update wraplength for all line labels
            for label in self.line_labels:
                label.config(wraplength=new_width)
                
            self.canvas.itemconfig(self.canvas_frame, width=new_width)
            
            # Update the display to reflect changes
            if self.lines:
                self.display_lines()

    def toggle_font_size(self, event=None):
        """Cycle through font sizes"""
        self.current_font_size_index = (self.current_font_size_index + 1) % len(self.font_sizes)
        new_size = self.font_sizes[self.current_font_size_index]
        
        # Update font size for all line labels
        for label in self.line_labels:
            label.config(font=("Arial", new_size))
            # Adjust height parameter based on font size
            label.config(height=2)
        
        # Update the display to reflect changes
        if self.lines:
            self.display_lines()
        
    def toggle_always_on_top(self, event=None):
        """Toggle whether window stays on top"""
        current_state = self.root.attributes("-topmost")
        self.root.attributes("-topmost", not current_state)
        top_status = "ON" if not current_state else "OFF"
        self.status.config(text=f"Always on Top: {top_status} | Press T to toggle")
        # Restore normal status after 2 seconds
        self.root.after(2000, self.update_status)

    def open_file(self, event=None):
        """Open a text file for teleprompter"""
        filename = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("Markdown files", "*.md"), ("All files", "*.*")]
        )
        if filename:
            self.load_file(filename)
    
    def load_file(self, filename):
        """Load content from file"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                # Split by lines, filter out empty lines
                self.lines = [line.strip() for line in content.split('\n') if line.strip()]
                self.top_line_index = 0
                
                # Show first few lines
                if self.lines:
                    self.display_lines()
                else:
                    self.line_labels[0].config(text="No text found in file")
                    for i in range(1, self.visible_line_count):
                        self.line_labels[i].config(text="")
                
                # Update title with filename
                self.title_label.config(text=f"Teleprompter - {os.path.basename(filename)}")
        except Exception as e:
            self.line_labels[0].config(text=f"Error loading file:\n{str(e)}")
            for i in range(1, self.visible_line_count):
                self.line_labels[i].config(text="")
    
    def display_lines(self):
        """Update all visible line labels with current text"""
        if not self.lines:
            self.line_labels[0].config(text="Press 'O' to open a file")
            for i in range(1, self.visible_line_count):
                self.line_labels[i].config(text="")
            return
        
        # Reset scroll position
        self.scroll_position = 0.0
        self.canvas.yview_moveto(0)
        
        # Display each visible line
        for i in range(self.visible_line_count):
            line_index = self.top_line_index + i
            if 0 <= line_index < len(self.lines):
                self.line_labels[i].config(text=self.lines[line_index])
                
                # Ensure consistent height for each line
                self.line_labels[i].config(height=2)
                
                # Set color based on line index (alternating between white and gray)
                # This keeps the color consistent per line as it scrolls
                if line_index % 2 == 0:
                    self.line_labels[i].config(fg="white")
                else:
                    self.line_labels[i].config(fg="#808080")
            else:
                self.line_labels[i].config(text="")
        
        # Update canvas scrollregion
        self.lines_container.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.update_status()
    
    def toggle_play(self, event=None):
        """Play or pause the teleprompter"""
        if not self.lines:
            return
            
        self.playing = not self.playing
        if self.playing:
            # Cancel any existing animation
            if self.scroll_animation_id:
                self.root.after_cancel(self.scroll_animation_id)
            
            # Start smooth scrolling animation
            self.scroll_animation()
        else:
            # Stop animation
            if self.scroll_animation_id:
                self.root.after_cancel(self.scroll_animation_id)
                self.scroll_animation_id = None
                
        self.update_status()
    
    def scroll_animation(self):
        """Smoothly scroll the text upward"""
        if not self.playing:
            return
        
        # Use fixed line height instead of calculating it dynamically
        line_height = self.fixed_line_height
        
        # Adjust scroll speed based on line length and WPM
        if self.top_line_index < len(self.lines):
            words = len(self.lines[self.top_line_index].split())
            # Base speed on current line's word count and WPM
            line_duration = max(60 * words / self.wpm, 2.0)  # Minimum 2 seconds per line
            target_speed = line_height / (line_duration * (1000 / self.scroll_update_ms))
            # Use consistent speed instead of gradual adjustment
            self.scroll_speed = target_speed
        
        # Increment scroll position
        self.scroll_position += self.scroll_speed
        
        # Move the canvas view
        self.canvas.yview_moveto(self.scroll_position / (line_height * self.visible_line_count))
        
        # Check if we need to shift lines
        if self.scroll_position >= line_height:
            # Move to next line
            self.scroll_position = 0
            self.top_line_index += 1
            
            if self.top_line_index < len(self.lines):
                # Update display with new top line
                self.display_lines()
            else:
                # End of script
                self.playing = False
                self.top_line_index = max(0, len(self.lines) - 1)
                self.display_lines()
                self.update_status()
                return
        
        # Schedule the next animation frame
        self.scroll_animation_id = self.root.after(self.scroll_update_ms, self.scroll_animation)

    def next_line(self, event=None):
        """Move to next line"""
        if self.playing:
            # Stop any ongoing animation
            if self.scroll_animation_id:
                self.root.after_cancel(self.scroll_animation_id)
                self.scroll_animation_id = None
            self.playing = False
            
        if self.lines and self.top_line_index < len(self.lines) - 1:
            self.top_line_index += 1
            self.display_lines()
        self.update_status()
    
    def previous_line(self, event=None):
        """Move to previous line"""
        if self.playing:
            # Stop any ongoing animation
            if self.scroll_animation_id:
                self.root.after_cancel(self.scroll_animation_id)
                self.scroll_animation_id = None
            self.playing = False
            
        if self.lines and self.top_line_index > 0:
            self.top_line_index -= 1
            self.display_lines()
        self.update_status()
    
    def increase_speed(self, event=None):
        """Increase WPM"""
        self.wpm += 10
        self.update_status()
    
    def decrease_speed(self, event=None):
        """Decrease WPM"""
        if self.wpm > 10:
            self.wpm -= 10
        self.update_status()
    
    def update_status(self):
        """Update the status bar"""
        status = f"WPM: {self.wpm} | "
        if self.lines:
            status += f"Line: {self.top_line_index + 1}/{len(self.lines)} | "
        status += "▶ PLAYING" if self.playing else "⏸ PAUSED"
        self.status.config(text=status)
    
    def exit_application(self, event=None):
        """Exit the application"""
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Teleprompter(root)
    
    # If file provided as argument, load it
    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
        app.load_file(sys.argv[1])
    
    root.mainloop()