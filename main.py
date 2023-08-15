import tkinter as tk
from tkinter import ttk
from tkinterhtml import HtmlFrame
import threading
import webbrowser
import os

class OnScreenKeyboard:
    def __init__(self, root):
        self.root = root
        self.root.title("On-Screen Keyboard")

        self.text_var = tk.StringVar()
        self.text_entry = tk.Entry(root, textvariable=self.text_var, font=("Arial", 20))
        self.text_entry.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

        self.webview_thread = threading.Thread(target=self.run_webview)
        self.webview_thread.start()

    def run_webview(self):
        html_path = os.path.abspath("index.html")
        webbrowser.open(f"file://{html_path}", new=0)

def main():
    root = tk.Tk()
    app = OnScreenKeyboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
