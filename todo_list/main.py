import tkinter as tk
from tkinter import messagebox
import json

# Main window
root = tk.Tk()

root.title("To-Do List Manager")
root.geometry("800x600")
root.configure(bg="#F4F6F8")
root.resizable(False, False)

# Center the window
window_width = 800
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")


# ---------------- HEADING ----------------

heading = tk.Label(
    root,
    text="To-Do List Manager",
    font=("Arial", 20, "bold"),
    bg="#F4F6F8",
    fg="#2C3E50"
)

heading.pack(pady=20)


# ---------------- TASK FRAME ----------------

task_frame = tk.Frame(
    root,
    bg="#F4F6F8"
)

task_frame.pack(pady=10)


# Task Label
task_label = tk.Label(
    task_frame,
    text="Task:",
    font=("Arial", 12, "bold"),
    bg="#F4F6F8"
)

task_label.pack(side="left", padx=5)


# Task Entry
task_entry = tk.Entry(
    task_frame,
    width=30,
    font=("Arial", 12)
)

task_entry.pack(side="left", padx=5)


# ---------------- TASK LIST ----------------

list_frame = tk.Frame(root)

list_frame.pack(pady=15)


task_listbox = tk.Listbox(
    list_frame,
    width=55,
    height=15,
    font=("Arial", 12),
    selectbackground="#4CAF50",
    selectforeground="white"
)

task_listbox.pack(side="left")


# Scrollbar
scrollbar = tk.Scrollbar(
    list_frame,
    orient="vertical"
)

scrollbar.pack(side="right", fill="y")

task_listbox.config(
    yscrollcommand=scrollbar.set
)

scrollbar.config(
    command=task_listbox.yview
)


# ---------------- COUNTER ----------------

counter = tk.Label(
    root,
    text="Total Tasks : 0",
    font=("Arial", 12, "bold"),
    bg="#F4F6F8",
    fg="#2C3E50"
)

counter.pack(pady=5)


# Update Counter
def update_counter():
    total = task_listbox.size()

    counter.config(
        text=f"Total Tasks : {total}"
    )


# ---------------- ADD TASK ----------------

def add_task():

    task = task_entry.get().strip()

    if task != "":
        task_listbox.insert(tk.END, task)

        task_entry.delete(0, tk.END)

        update_counter()

        save_tasks()

    else:
        messagebox.showwarning(
            "Warning",
            "Please enter a task."
        )


# Add Button
add_button = tk.Button(
    task_frame,
    text="Add Task",
    font=("Arial", 10, "bold"),
    bg="#4CAF50",
    fg="white",
    command=add_task
)

add_button.pack(side="left", padx=5)


# ---------------- DELETE TASK ----------------

def delete_task():

    selected_task = task_listbox.curselection()

    if selected_task:

        task_listbox.delete(selected_task)

        update_counter()

        save_tasks()

    else:

        messagebox.showwarning(
            "Warning",
            "Please select a task."
        )


# Delete Button
delete_button = tk.Button(
    task_frame,
    text="Delete Task",
    font=("Arial", 10, "bold"),
    bg="#E74C3C",
    fg="white",
    command=delete_task
)

delete_button.pack(side="left", padx=5)


# ---------------- UPDATE TASK ----------------

def update_task():

    selected_task = task_listbox.curselection()

    if selected_task:

        new_task = task_entry.get().strip()

        if new_task != "":

            task_listbox.delete(selected_task)

            task_listbox.insert(
                selected_task[0],
                new_task
            )

            task_entry.delete(0, tk.END)

            save_tasks()

        else:

            messagebox.showwarning(
                "Warning",
                "Please enter a new task."
            )

    else:

        messagebox.showwarning(
            "Warning",
            "Please select a task."
        )


# Update Button
update_button = tk.Button(
    task_frame,
    text="Update Task",
    font=("Arial", 10, "bold"),
    bg="#3498DB",
    fg="white",
    command=update_task
)

update_button.pack(side="left", padx=5)


# ---------------- MARK COMPLETE ----------------

def mark_complete():

    selected_task = task_listbox.curselection()

    if selected_task:

        task = task_listbox.get(selected_task)

        if not task.startswith("✔ "):

            task_listbox.delete(selected_task)

            task_listbox.insert(
                selected_task[0],
                "✔ " + task
            )

            save_tasks()

    else:

        messagebox.showwarning(
            "Warning",
            "Please select a task."
        )


# Complete Button
complete_button = tk.Button(
    task_frame,
    text="Complete",
    font=("Arial", 10, "bold"),
    bg="#27AE60",
    fg="white",
    command=mark_complete
)

complete_button.pack(side="left", padx=5)


# ---------------- SAVE TASKS ----------------

def save_tasks():

    tasks = task_listbox.get(0, tk.END)

    with open("tasks.json", "w") as file:

        json.dump(list(tasks), file, indent=4)


# ---------------- LOAD TASKS ----------------

def load_tasks():

    try:

        with open("tasks.json", "r") as file:

            tasks = json.load(file)

            for task in tasks:

                task_listbox.insert(
                    tk.END,
                    task
                )

        update_counter()

    except FileNotFoundError:

        pass

    except json.JSONDecodeError:

        messagebox.showwarning(
            "Warning",
            "tasks.json file is corrupted."
        )


# ---------------- CLEAR ALL ----------------

def clear_all():

    if task_listbox.size() == 0:

        messagebox.showinfo(
            "Information",
            "There are no tasks to clear."
        )

        return

    confirm = messagebox.askyesno(
        "Clear All",
        "Are you sure you want to delete all tasks?"
    )

    if confirm:

        task_listbox.delete(0, tk.END)

        update_counter()

        save_tasks()


# Clear All Button
clear_button = tk.Button(
    task_frame,
    text="Clear All",
    font=("Arial", 10, "bold"),
    bg="#E67E22",
    fg="white",
    command=clear_all
)

clear_button.pack(side="left", padx=5)


# ---------------- LOAD SAVED TASKS ----------------

load_tasks()


# ---------------- RUN APPLICATION ----------------

root.mainloop()