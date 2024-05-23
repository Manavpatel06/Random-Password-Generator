import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip


def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return

    complexity = complexity_var.get()

    characters = ''
    if chars_var.get():
        characters += string.ascii_letters
    if nums_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=password)


def copy_to_clipboard():
    password = password_label.cget("text")
    pyperclip.copy(password)
    messagebox.showinfo("Info", "Password copied to clipboard!")


root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

complexity_label = tk.Label(root, text="Complexity:")
complexity_label.grid(row=1, column=0, padx=10, pady=10)
complexity_var = tk.StringVar()
complexity_var.set("Medium")
complexity_menu = tk.OptionMenu(root, complexity_var, "Low", "Medium", "High")
complexity_menu.grid(row=1, column=1, padx=10, pady=10)

chars_var = tk.BooleanVar()
chars_check = tk.Checkbutton(root, text="Include Letters", variable=chars_var)
chars_check.grid(row=2, column=0, padx=10, pady=5, sticky="w")

nums_var = tk.BooleanVar()
nums_check = tk.Checkbutton(root, text="Include Numbers", variable=nums_var)
nums_check.grid(row=3, column=0, padx=10, pady=5, sticky="w")

symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_check.grid(row=4, column=0, padx=10, pady=5, sticky="w")

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, columnspan=2, padx=10, pady=10)

password_label = tk.Label(root, text="")
password_label.grid(row=6, columnspan=2, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=7, columnspan=2, padx=10, pady=10)

root.mainloop()
