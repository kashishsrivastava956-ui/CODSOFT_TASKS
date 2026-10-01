
import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("450x550")
root.configure(bg="#F4F6F8")
root.resizable(False, False)

# Variables
num1 = ""
num2 = ""
operator = ""

# Display
display = tk.Entry(
    root,
    font=("Arial", 24, "bold"),
    justify="right",
    bd=8,
    relief="sunken",
    width=20
)
display.grid(row=0, column=0, columnspan=4, padx=20, pady=25)

# Button click function
def button_click(value):
    display.insert(tk.END, value)

# Clear function
def clear():
    display.delete(0, tk.END)

# Calculate function
def calculate():
    expression = display.get()

    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        clear()
    except:
        messagebox.showerror("Error", "Invalid calculation.")
        clear()

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3)
]

for text, row, column in buttons:
    if text == "=":
        command = calculate
        bg = "#27AE60"
    else:
        command = lambda value=text: button_click(value)
        bg = "#3498DB"

    tk.Button(
        root,
        text=text,
        command=command,
        font=("Arial", 18, "bold"),
        width=6,
        height=2,
        bg=bg,
        fg="white"
    ).grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )

# Clear button
tk.Button(
    root,
    text="CLEAR",
    command=clear,
    font=("Arial", 16, "bold"),
    width=28,
    height=2,
    bg="#E74C3C",
    fg="white"
).grid(
    row=5,
    column=0,
    columnspan=4,
    padx=10,
    pady=15
)

root.mainloop()
