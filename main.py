import tkinter as tk
from tkinter import messagebox
import pyshorteners

# Initialise pyshorteners
tiny = pyshorteners.Shortener()


# Functions
# Shorten
def shorten():
    try:
        long_url = url_entry.get()
        short_url = tiny.tinyurl.short(long_url)
        shortened_url_entry.delete(0, "end")
        shortened_url_entry.insert(0, short_url)
    except:
        tk.messagebox.showerror("Error", "Invalid URL")


# Copy to clipboard
def copy():
    url = shortened_url_entry.get()
    if url:
        window.clipboard_append(url)
        window.update()


# Clear
def clear():
    url_entry.delete(0, "end")
    shortened_url_entry.delete(0, "end")


# Window
window = tk.Tk()
window.title("URL Shortener")

# Labels
# Enter your URL label
enter_url = tk.Label(window, text="Enter your URL:")
enter_url.grid(row=0, column=0, padx=5, pady=10)
# Shortened URL label
shortened_url = tk.Label(window, text="Shortened URL:")
shortened_url.grid(row=2, column=0, padx=5, pady=10)

# Entries
# URL entry
url_entry = tk.Entry(window)
url_entry.grid(row=0, column=1, padx=5, pady=10)
# Shortened URL entry
shortened_url_entry = tk.Entry(window)
shortened_url_entry.grid(row=2, column=1, padx=5, pady=10)

# Buttons
# Shorten button
shorten_button = tk.Button(window, text="Shorten", command=shorten)
shorten_button.grid(row=0, column=2, padx=5, pady=10)
# Copy to clipboard
copy_to_clipboard_button = tk.Button(window, text="Copy to Clipboard", command=copy)
copy_to_clipboard_button.grid(row=2, column=2, padx=5, pady=10)
# Clear button
clear_button = tk.Button(window, text="Clear", command=clear)
clear_button.grid(row=3, column=1, padx=5, pady=10)

# Main loop
window.mainloop()
