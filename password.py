import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_and_display():
    try:
        length = int(length_entry.get())
        if length > 0:
            password = generate_password(length)
            result_label.config(text=f"Generated Password: {password}")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a positive integer for password length.")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid integer for password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and pack widgets
length_label = ttk.Label(root, text="Enter the desired length of the password:")
length_label.pack(pady=10)

length_entry = ttk.Entry(root)
length_entry.pack(pady=10)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password_and_display)
generate_button.pack(pady=20)

result_label = ttk.Label(root, text="")
result_label.pack()

# Run the main loop
root.mainloop()
