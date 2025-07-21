import tkinter as tk
from tkinter import messagebox
import re

# Function to validate the password
def validate_password():
    password = entry.get()
    if len(password) < 8 or len(password) > 16:
        messagebox.showerror("Invalid", "Password length must be between 8 and 16.")
    elif not re.search("[a-z]", password):
        messagebox.showerror("Invalid", "Password must contain at least one lowercase letter.")
    elif not re.search("[A-Z]", password):
        messagebox.showerror("Invalid", "Password must contain at least one uppercase letter.")
    elif not re.search("[0-9]", password):
        messagebox.showerror("Invalid", "Password must contain at least one digit.")
    elif not re.search("[@#$&_]", password):
        messagebox.showerror("Invalid", "Password must contain at least one special character (@, #, $, &, _).")
    elif re.search(r"\s", password):
        messagebox.showerror("Invalid", "Password must not contain spaces.")
    else:
        messagebox.showinfo("Valid", "This is a valid password.")

# Create the GUI window
root = tk.Tk()
root.title("Password Validator")
root.geometry("350x200")
root.resizable(False, False)

# Label
label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=10)

# Entry box
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack()

# Validate button
btn = tk.Button(root, text="Validate", command=validate_password, font=("Arial", 12), bg="lightblue")
btn.pack(pady=20)

# Run the GUI loop
root.mainloop()
