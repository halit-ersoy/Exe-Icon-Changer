import tkinter as tk
from tkinter import filedialog
import shutil


def select_file():
    selected_file = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])
    if selected_file:
        entry_path.delete(0, tk.END)
        entry_path.insert(tk.END, selected_file)


def select_icon():
    selected_icon = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])
    if selected_icon:
        entry_icon.delete(0, tk.END)
        entry_icon.insert(tk.END, selected_icon)


def change_icon():
    exe_path = entry_path.get()
    icon_path = entry_icon.get()

    if not exe_path or not icon_path:
        status_label.config(text="Please select both EXE file and icon file.", fg="red")
        return

    try:
        # Load the icon file
        with open(icon_path, 'rb') as icon_file:
            icon_data = icon_file.read()

        # Create a copy of the exe file with the icon changed
        new_exe_path = filedialog.asksaveasfilename(defaultextension=".exe", filetypes=[("Executable files", "*.exe")],
                                                    title="Save As")
        if new_exe_path:
            shutil.copyfile(exe_path, new_exe_path)
            # Update the icon of the copied executable
            with open(new_exe_path, 'r+b') as exe_file:
                exe_file.seek(0)
                exe_file.write(icon_data)
            status_label.config(text="Icon changed successfully. New file saved at: " + new_exe_path, fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")


# GUI
root = tk.Tk()
root.title("EXE Icon Changer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Select the EXE file you want to change the icon of:").grid(row=0, column=0, sticky="w")
entry_path = tk.Entry(frame, width=50)
entry_path.grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Browse", command=select_file).grid(row=1, column=1, padx=5)

tk.Label(frame, text="Select the icon file you want to use:").grid(row=2, column=0, sticky="w")
entry_icon = tk.Entry(frame, width=50)
entry_icon.grid(row=3, column=0, padx=5, pady=5)
tk.Button(frame, text="Browse", command=select_icon).grid(row=3, column=1, padx=5)

tk.Button(frame, text="Change Icon", command=change_icon).grid(row=4, columnspan=2, pady=10)

status_label = tk.Label(root, text="", fg="black")
status_label.pack()

root.mainloop()
