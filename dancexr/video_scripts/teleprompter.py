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
        self.root.geometry("1280x300+20+20")  # Default size and position
        self.root.minsize(400, 200)  # Minimum window size
        
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
        
        # Configure the main display area
        self.text_display = tk.Label(
            root, 
            text="Press 'O' to open a file",
            font=("Arial", 48),
            fg="white",
            bg="black",
            wraplength=700,  # Will be updated on resize
            justify="center"
        )
        self.text_display.pack(expand=True, fill="both", padx=20, pady=(5, 20))
        
        # Variables
        self.lines = []
        self.current_line = 0
        self.playing = False
        self.wpm = 100  # Default words per minute
        self.words_per_line = 0
        self.x = None
        self.y = None
        
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
        # Only update if the window size changed (not other configure events)
        if event.widget == self.root:
            # Leave some padding
            new_width = self.root.winfo_width() - 40
            self.text_display.config(wraplength=new_width)
            
    def toggle_font_size(self, event=None):
        """Cycle through font sizes"""
        self.current_font_size_index = (self.current_font_size_index + 1) % len(self.font_sizes)
        new_size = self.font_sizes[self.current_font_size_index]
        self.text_display.config(font=("Arial", new_size))
        
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
                self.current_line = 0
                
                # Estimate words per line
                total_words = sum(len(line.split()) for line in self.lines)
                if self.lines:
                    self.words_per_line = total_words / len(self.lines)
                
                # Show first line
                if self.lines:
                    self.display_current_line()
                else:
                    self.text_display.config(text="No text found in file")
                
                # Update title with filename
                self.title_label.config(text=f"Teleprompter - {os.path.basename(filename)}")
        except Exception as e:
            self.text_display.config(text=f"Error loading file:\n{str(e)}")
    
    def display_current_line(self):
        """Show the current line in the display"""
        if 0 <= self.current_line < len(self.lines):
            self.text_display.config(text=self.lines[self.current_line])
        self.update_status()
    
    def toggle_play(self, event=None):
        """Play or pause the teleprompter"""
        if not self.lines:
            return
            
        self.playing = not self.playing
        if self.playing:
            threading.Thread(target=self.play_lines, daemon=True).start()
        self.update_status()
    
    def play_lines(self):
        """Auto-advance through lines based on WPM"""
        while self.playing and self.current_line < len(self.lines):
            # Calculate delay based on words in current line and WPM
            line = self.lines[self.current_line]
            words = len(line.split())
            if words == 0:
                words = 1
                
            # Calculate seconds to display based on WPM
            wait_time = (words / self.wpm) * 60
            
            # Minimum time of 1 second per line
            wait_time = max(wait_time, 1)
            
            time.sleep(wait_time)
            
            if not self.playing:
                break
                
            self.current_line += 1
            if self.current_line < len(self.lines):
                self.root.after(0, self.display_current_line)
            else:
                self.playing = False
                self.update_status()
    
    def next_line(self, event=None):
        """Move to next line"""
        if self.lines and self.current_line < len(self.lines) - 1:
            self.current_line += 1
            self.display_current_line()
    
    def previous_line(self, event=None):
        """Move to previous line"""
        if self.lines and self.current_line > 0:
            self.current_line -= 1
            self.display_current_line()
    
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
            status += f"Line: {self.current_line + 1}/{len(self.lines)} | "
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