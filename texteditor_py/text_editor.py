import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

current_theme = {
    "background": "white",
    "foreground": "black",
    "font": "Helvetica 18",
}

def apply_theme():
    text_edit.config(bg=current_theme["background"], fg=current_theme["foreground"], font=current_theme["font"])

def change_theme(theme):
    global current_theme
    current_theme = theme
    apply_theme()

def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"open file:{filepath}")

def save_file():
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"open file:{filepath}")

def create_theme_buttons():
    themes = [
        {"background": "white", "foreground": "black", "font": "Helvetica 18"},
        {"background": "black", "foreground": "white", "font": "Courier 18"},
        {"background": "#0077cc", "foreground": "white", "font": "Arial 16"},
        {"background": "#ffb6c1", "foreground": "#4b0082", "font": "Arial 16"},
        {"background": "#282c34", "foreground": "#abb2bf", "font": "Consolas 18"},
        # Add more themes as needed
    ]

    theme_buttons_frame = tk.Frame(window)
    theme_buttons_frame.grid(row=0, column=2, padx=5, pady=5, sticky="n")

    for i, theme in enumerate(themes):
        theme_button = tk.Button(theme_buttons_frame, text=f"Theme {i+1}", command=lambda t=theme: change_theme(t))
        theme_button.grid(row=i, column=0, pady=2, sticky="ew")

def main():
    global window  # Make window a global variable

    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    global text_edit  
    text_edit = tk.Text(window)
    text_edit.grid(row=0, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="Save", command=save_file)
    open_button = tk.Button(frame, text="Open", command=open_file)

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    create_theme_buttons()

    window.bind("<Control-s>", lambda x: save_file())
    window.bind("<Control-o>", lambda x: open_file())

    apply_theme()

    window.mainloop()

main()
