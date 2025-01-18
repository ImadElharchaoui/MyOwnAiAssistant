import json
from tkinter import *
from tkinter import filedialog, messagebox

def add_entry(entry_type, name, path):
    with open("Data.json", "r") as file:
        data = json.load(file)

    if entry_type not in data:
        data[entry_type] = {}

    data[entry_type][name] = {"name": name, "path": path}

    with open("Data.json", "w") as file:
        json.dump(data, file, indent=4)

    messagebox.showinfo("Success", f"{entry_type.capitalize()} '{name}' added successfully!")

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        path_entry.delete(0, END)
        path_entry.insert(0, file_path)

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        path_entry.delete(0, END)
        path_entry.insert(0, folder_path)

def submit():
    entry_type = entry_type_var.get()
    name = name_entry.get()
    path = path_entry.get()

    if not name or not path:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    add_entry(entry_type, name, path)

# Create the GUI
root = Tk()
root.title("Add Entry")

entry_type_var = StringVar(value="games")

Label(root, text="Entry Type:").grid(row=0, column=0, padx=10, pady=10)
Radiobutton(root, text="Game", variable=entry_type_var, value="games").grid(row=0, column=1)
Radiobutton(root, text="Folder", variable=entry_type_var, value="folders").grid(row=0, column=2)

Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=10)
name_entry = Entry(root)
name_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

Label(root, text="Path:").grid(row=2, column=0, padx=10, pady=10)
path_entry = Entry(root)
path_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

Button(root, text="Browse File", command=browse_file).grid(row=3, column=1, padx=10, pady=10)
Button(root, text="Browse Folder", command=browse_folder).grid(row=3, column=2, padx=10, pady=10)

Button(root, text="Submit", command=submit).grid(row=4, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
