import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store contacts
FILE_NAME = "contacts.json"

# Load contacts
def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return {}
    return {}

# Save contacts
def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Warning", "Name and phone number are required.")
        return

    if name in contacts:
        messagebox.showwarning("Warning", "Contact already exists.")
        return

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    save_contacts()
    clear_entries()
    display_contacts()
    messagebox.showinfo("Success", "Contact added successfully.")

# View contacts
def display_contacts(data=None):
    contact_list.delete(0, tk.END)

    if data is None:
        data = contacts

    for name, details in data.items():
        contact_list.insert(
            tk.END,
            f"{name}  |  {details['phone']}"
        )

# Search contact
def search_contact():
    search_text = search_entry.get().strip().lower()

    if not search_text:
        display_contacts()
        return

    results = {}

    for name, details in contacts.items():
        if (search_text in name.lower() or
                search_text in details["phone"].lower()):
            results[name] = details

    display_contacts(results)

# Select contact
def select_contact(event):
    selected = contact_list.curselection()

    if not selected:
        return

    item = contact_list.get(selected[0])
    name = item.split("  |  ")[0]

    if name in contacts:
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)

        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contacts[name]["phone"])

        email_entry.delete(0, tk.END)
        email_entry.insert(0, contacts[name]["email"])

        address_entry.delete(0, tk.END)
        address_entry.insert(0, contacts[name]["address"])

# Update contact
def update_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Warning", "Name and phone number are required.")
        return

    if name not in contacts:
        messagebox.showwarning("Warning", "Contact not found.")
        return

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    save_contacts()
    clear_entries()
    display_contacts()
    messagebox.showinfo("Success", "Contact updated successfully.")

# Delete contact
def delete_contact():
    name = name_entry.get().strip()

    if not name:
        messagebox.showwarning("Warning", "Select a contact first.")
        return

    if name not in contacts:
        messagebox.showwarning("Warning", "Contact not found.")
        return

    confirm = messagebox.askyesno(
        "Delete Contact",
        f"Are you sure you want to delete {name}?"
    )

    if confirm:
        del contacts[name]
        save_contacts()
        clear_entries()
        display_contacts()
        messagebox.showinfo("Success", "Contact deleted successfully.")

# Clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("750x600")
root.configure(bg="#F4F6F8")
root.resizable(False, False)

contacts = load_contacts()

# Heading
heading = tk.Label(
    root,
    text="CONTACT BOOK",
    font=("Arial", 24, "bold"),
    bg="#F4F6F8",
    fg="#2C3E50"
)
heading.pack(pady=15)

# Input frame
input_frame = tk.Frame(
    root,
    bg="white",
    padx=20,
    pady=15
)
input_frame.pack(padx=30, fill="x")

# Name
tk.Label(
    input_frame,
    text="Name:",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=0, column=0, sticky="w", pady=5)

name_entry = tk.Entry(
    input_frame,
    font=("Arial", 11),
    width=35
)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Phone
tk.Label(
    input_frame,
    text="Phone:",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=1, column=0, sticky="w", pady=5)

phone_entry = tk.Entry(
    input_frame,
    font=("Arial", 11),
    width=35
)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

# Email
tk.Label(
    input_frame,
    text="Email:",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=2, column=0, sticky="w", pady=5)

email_entry = tk.Entry(
    input_frame,
    font=("Arial", 11),
    width=35
)
email_entry.grid(row=2, column=1, padx=10, pady=5)

# Address
tk.Label(
    input_frame,
    text="Address:",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=3, column=0, sticky="w", pady=5)

address_entry = tk.Entry(
    input_frame,
    font=("Arial", 11),
    width=35
)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#F4F6F8")
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Add Contact",
    command=add_contact,
    width=14,
    bg="#27AE60",
    fg="white",
    font=("Arial", 10, "bold")
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Update",
    command=update_contact,
    width=14,
    bg="#2980B9",
    fg="white",
    font=("Arial", 10, "bold")
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Delete",
    command=delete_contact,
    width=14,
    bg="#E74C3C",
    fg="white",
    font=("Arial", 10, "bold")
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Clear",
    command=clear_entries,
    width=14,
    bg="#7F8C8D",
    fg="white",
    font=("Arial", 10, "bold")
).grid(row=0, column=3, padx=5)

# Search section
search_frame = tk.Frame(root, bg="#F4F6F8")
search_frame.pack(pady=5)

tk.Label(
    search_frame,
    text="Search:",
    font=("Arial", 11, "bold"),
    bg="#F4F6F8"
).pack(side="left", padx=5)

search_entry = tk.Entry(
    search_frame,
    font=("Arial", 11),
    width=35
)
search_entry.pack(side="left", padx=5)

tk.Button(
    search_frame,
    text="Search",
    command=search_contact,
    width=10,
    bg="#8E44AD",
    fg="white",
    font=("Arial", 10, "bold")
).pack(side="left", padx=5)

tk.Button(
    search_frame,
    text="Show All",
    command=display_contacts,
    width=10,
    bg="#34495E",
    fg="white",
    font=("Arial", 10, "bold")
).pack(side="left", padx=5)

# Contact list
list_frame = tk.Frame(root, bg="white")
list_frame.pack(padx=30, pady=10, fill="both", expand=True)

tk.Label(
    list_frame,
    text="Saved Contacts",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="#2C3E50"
).pack(pady=8)

contact_list = tk.Listbox(
    list_frame,
    font=("Arial", 11),
    width=75,
    height=10
)
contact_list.pack(padx=10, pady=5)

contact_list.bind("<<ListboxSelect>>", select_contact)

# Display saved contacts
display_contacts()

root.mainloop()