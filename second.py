import string
import random
import tkinter as tk
from tkinter import messagebox
import pyperclip

# Function to generate password
def generate_password():
    length = length_var.get()

    if length < 4:
        messagebox.showerror("Error", "Password length must be at least 4.")
        return

    characters = ""
    if use_uppercase.get():
        characters += string.ascii_uppercase
    if use_lowercase.get():
        characters += string.ascii_lowercase
    if use_digits.get():
        characters += string.digits
    if use_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character set.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

# GUI setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x400")
root.config(bg="#1e1e1e")

# Header
tk.Label(root, text="🔐 Password Generator", font=("Helvetica", 18), fg="white", bg="#1e1e1e").pack(pady=20)

# Password display
password_entry = tk.Entry(root, font=("Helvetica", 14), width=25, bd=2)
password_entry.pack(pady=10)

# Length input
length_frame = tk.Frame(root, bg="#1e1e1e")
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length:", fg="white", bg="#1e1e1e").pack(side=tk.LEFT)
length_var = tk.IntVar(value=12)
tk.Spinbox(length_frame, from_=4, to=64, textvariable=length_var, width=5).pack(side=tk.LEFT, padx=10)

# Options
use_uppercase = tk.BooleanVar(value=True)
use_lowercase = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=False)

options_frame = tk.Frame(root, bg="#1e1e1e")
options_frame.pack(pady=10)

tk.Checkbutton(options_frame, text="Uppercase", variable=use_uppercase, fg="white", bg="#1e1e1e", selectcolor="#2e2e2e").grid(row=0, column=0, sticky="w")
tk.Checkbutton(options_frame, text="Lowercase", variable=use_lowercase, fg="white", bg="#1e1e1e", selectcolor="#2e2e2e").grid(row=1, column=0, sticky="w")
tk.Checkbutton(options_frame, text="Digits", variable=use_digits, fg="white", bg="#1e1e1e", selectcolor="#2e2e2e").grid(row=2, column=0, sticky="w")
tk.Checkbutton(options_frame, text="Symbols", variable=use_symbols, fg="white", bg="#1e1e1e", selectcolor="#2e2e2e").grid(row=3, column=0, sticky="w")

# Buttons
tk.Button(root, text="Generate Password", command=generate_password, bg="#27ae60", fg="white", width=20).pack(pady=10)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2980b9", fg="white", width=20).pack(pady=5)

# Run
root.mainloop()
