import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

# Set window attributes for full screen and always on top
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)

# Create a text box
text_box = tk.Text(root)
text_box.pack(fill=tk.BOTH, expand=True)

try:
    with open('C:\\Users\\User\\Downloads\\Scripts.com.txt', 'r') as file:
        # Read the contents of the file
        file_contents = file.read()

    # Insert file contents into the text box
    text_box.insert(tk.END, file_contents)
except FileNotFoundError:
    messagebox.showerror("Error", "File not found!")

def on_closing():
    # Prevent closing the window immediately
    return "break"

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
