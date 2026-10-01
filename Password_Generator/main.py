import tkinter as tk
import random
import string
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x450")
root.configure(bg="#F4F6F8")
root.resizable(False, False)

# Center window
window_width = 500
window_height = 450

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")


# Heading
heading = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 24, "bold"),
    bg="#F4F6F8",
    fg="#2C3E50"
)

heading.pack(pady=25)


# Length Label
length_label = tk.Label(
    root,
    text="Enter Password Length:",
    font=("Arial", 12, "bold"),
    bg="#F4F6F8",
    fg="#2C3E50"
)

length_label.pack(pady=5)


# Length Entry
length_entry = tk.Entry(
    root,
    width=25,
    font=("Arial", 12),
    justify="center"
)

length_entry.pack(pady=10)


# Password Entry
password_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 13),
    justify="center"
)

password_entry.pack(pady=20)


# Generate Password Function
def generate_password():

    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showwarning(
                "Warning",
                "Password length must be greater than 0."
            )
            return

        if length > 100:
            messagebox.showwarning(
                "Warning",
                "Password length cannot be greater than 100."
            )
            return

        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        password = "".join(
            random.choice(characters)
            for _ in range(length)
        )

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:

        messagebox.showerror(
            "Error",
            "Please enter a valid number."
        )


# Copy Password Function
def copy_password():

    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "Warning",
            "Please generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo(
        "Success",
        "Password copied successfully!"
    )


# Generate Button
generate_button = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 11, "bold"),
    bg="#3498DB",
    fg="white",
    width=20,
    height=2,
    command=generate_password
)

generate_button.pack(pady=10)


# Copy Button
copy_button = tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 11, "bold"),
    bg="#27AE60",
    fg="white",
    width=20,
    height=2,
    command=copy_password
)

copy_button.pack(pady=10)


# Clear Button
def clear_password():

    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial", 11, "bold"),
    bg="#E74C3C",
    fg="white",
    width=20,
    height=2,
    command=clear_password
)

clear_button.pack(pady=10)


root.mainloop()