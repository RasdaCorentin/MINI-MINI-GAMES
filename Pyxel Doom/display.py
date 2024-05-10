import tkinter as tk

class Display:
    def __init__(self):
        self.display_mode = "display_frame"
        root = tk.Tk()
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        root.destroy()