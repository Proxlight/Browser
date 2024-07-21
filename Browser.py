import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkhtmlview import HTMLLabel

# Initialize the main window
root = ctk.CTk()
root.title("CustomTkinter Browser")
root.geometry("800x600")

# Function to navigate to the URL entered in the entry widget
def navigate():
    url = url_entry.get()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    web_label.set_html('<h1>Loading...</h1>')
    web_label.set_url(url)

# Function to go back to the previous page
def go_back():
    try:
        web_label.web.navigate_back()
    except Exception as e:
        print(f"Error: {e}")

# Function to go forward to the next page
def go_forward():
    try:
        web_label.web.navigate_forward()
    except Exception as e:
        print(f"Error: {e}")

# Create the URL entry widget
url_entry = ctk.CTkEntry(root, width=600, placeholder_text="Enter URL here")
url_entry.pack(pady=10)

# Create a frame for navigation buttons
nav_frame = ctk.CTkFrame(root)
nav_frame.pack(pady=10)

# Create the navigation buttons
back_button = ctk.CTkButton(nav_frame, text="Back", command=go_back)
back_button.pack(side=tk.LEFT, padx=10)

forward_button = ctk.CTkButton(nav_frame, text="Forward", command=go_forward)
forward_button.pack(side=tk.LEFT, padx=10)

go_button = ctk.CTkButton(nav_frame, text="Go", command=navigate)
go_button.pack(side=tk.LEFT, padx=10)

# Create the HTML label to display web content
web_label = HTMLLabel(root, html='<h1>Welcome to CustomTkinter Browser!</h1>')
web_label.pack(fill=tk.BOTH, expand=True)

# Start the main event loop
root.mainloop()
