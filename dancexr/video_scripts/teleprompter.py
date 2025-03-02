import tkinter as tk
import time
import threading
import sys
import os

class Teleprompter:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Teleprompter")
        self.root.configure(bg="black")
        self.root.attributes("-fullscreen", True)  # Start in fullscreen
        
        # Configure the main display area
        self.text_display = tk.Label(
            root, 
            text="Press 'O' to open a file",
            font=("Arial", 48),
            fg="white",
            bg="black",
            wraplength=root.winfo_screenwidth() - 100,
            justify="center"
        )
        self.text_display.pack(expand=True, fill="both", padx=50, pady=50)
        
        # Variables
        self.lines = []
        self.current_line = 0
        self.playing = False
        self.wpm = 100  # Default words per minute
        self.words_per_line = 0
        
        # Keybindings
        self.root.bind("<o>", self.open_file)
        self.root.bind("<O>", self.open_file)
        self.root.bind("<space>", self.toggle_play)
        self.root.bind("<Escape>", self.exit_application)
        self.root.bind("<Up>", self.increase_speed)
        self.root.bind("<Down>", self.decrease_speed)
        self.root.bind("<Left>", self.previous_line)
        self.root.bind("<Right>", self.next_line)
        
        # Status display
        self.status = tk.Label(
            root,
            text="WPM: 100 | SPACE: Play/Pause | ↑↓: Speed | ←→: Navigate | ESC: Exit | O: Open File",
            font=("Arial", 12),
            fg="gray",
            bg="black"
        )
        self.status.pack(side="bottom", pady=10)

    def open_file(self, event=None):
        """Open a text file for teleprompter"""
        filename = tk.filedialog.askopenfilename(
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
                self.root.title(f"Teleprompter - {os.path.basename(filename)}")
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
            # Use either line-specific word count or average words per line
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