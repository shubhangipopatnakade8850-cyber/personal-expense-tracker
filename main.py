#import tkinter for creating GUI apps
import tkinter as tk
from tkinter import filedialog, messagebox

#main Window code
root = tk.Tk()
root.title("✨ Smart Text Editor")
root.geometry("900x600")
root.config(bg="#2b2b2b")

current_file = None

# ---------------- TEXT AREA ----------------
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Consolas", 12),
    bg="#1e1e1e",
    fg="white",
    insertbackground="white"
)
text.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

# Scrollbar
scroll = tk.Scrollbar(root, command=text.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
text.config(yscrollcommand=scroll.set)

# ---------------- STATUS BAR ----------------
status = tk.Label(root, text="Words: 0 | Lines: 0", bg="#333", fg="white", anchor="e")
status.pack(fill=tk.X, side=tk.BOTTOM)

def update_status(event=None):
    content = text.get("1.0", tk.END)
    words = len(content.split())
    lines = content.count("\n")
    status.config(text=f"Words: {words} | Lines: {lines}")

text.bind("<KeyRelease>", update_status)

# ---------------- FUNCTIONS ----------------
def new_file():
    global current_file
    text.delete("1.0", tk.END)
    current_file = None
    root.title("✨ New File")

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(filetypes=[("Text File", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())
        current_file = file_path
        root.title(f"📄 {file_path}")

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(text.get("1.0", tk.END))
        messagebox.showinfo("Saved", "File saved successfully!")
    else:
        save_as()

def save_as():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        current_file = file_path
        save_file()

# --------- EDIT FUNCTIONS ----------
def cut(): text.event_generate("<<Cut>>")
def copy(): text.event_generate("<<Copy>>")
def paste(): text.event_generate("<<Paste>>")
def clear(): text.delete("1.0", tk.END)

# --------- VIEW FUNCTION ----------
dark_mode = True
def toggle_theme():
    global dark_mode
    if dark_mode:
        text.config(bg="white", fg="black", insertbackground="black")
    else:
        text.config(bg="#1e1e1e", fg="white", insertbackground="white")
    dark_mode = not dark_mode

# --------- ABOUT WINDOW ----------
def about():
    win = tk.Toplevel(root)
    win.title("About")
    win.geometry("450x350")
    win.config(bg="#1e1e1e")

    tk.Label(win, text="✨ Smart Text Editor",
             bg="#1e1e1e", fg="white",
             font=("Helvetica", 14, "bold")).pack(pady=10)

    tk.Label(win, text="Made by SHUBHANGI POPAT NAKADE",
             bg="#1e1e1e", fg="#00ffcc").pack()

    tk.Label(win,
             text="Designed not just to write — but to empower.\n\n"
                  "Behind every achievement is a simple beginning.\n"
                  "This space is yours to capture ideas, solve problems, and create something meaningful.\n\n"
                  "Don’t wait for inspiration.\n\nCreate it. ✨",
             bg="#1e1e1e", fg="white",
             wraplength=380, justify="center").pack(pady=15)

    tk.Button(win, text="Close", command=win.destroy).pack(pady=10)

# ---------------- MENU ----------------
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New (Ctrl+N)", command=new_file)
file_menu.add_command(label="Open (Ctrl+O)", command=open_file)
file_menu.add_command(label="Save (Ctrl+S)", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Clear", command=clear)

view_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Toggle Dark/Light Mode", command=toggle_theme)

help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# ---------------- SHORTCUT KEYS ----------------
root.bind("<Control-n>", lambda e: new_file())
root.bind("<Control-o>", lambda e: open_file())
root.bind("<Control-s>", lambda e: save_file())

# Run app
root.mainloop()