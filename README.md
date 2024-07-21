# CustomTkinter GUI Browser

A simple yet beautiful GUI browser built using Python and customtkinter. This browser includes a navigation bar for entering URLs, back and forward buttons, and a display area for the web pages.

## Features

- **CustomTkinter UI**: A modern, customizable look and feel.
- **Navigation**: Includes back, forward, and URL entry functionalities.
- **HTML Rendering**: Displays web content using `tkhtmlview`.

## Requirements

- Python 3.6 or higher
- `customtkinter`
- `tkhtmlview`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/customtkinter-browser.git
    cd customtkinter-browser
    ```

2. Install the required packages:

    ```bash
    pip install customtkinter tkhtmlview
    ```

## Usage

Run the following command to start the browser:

```bash
python browser.py
```

## Code Overview

### Importing Libraries

We start by importing the necessary libraries.

```python
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkhtmlview import HTMLLabel
```

### Setting Up the Main Window

Initialize the main application window.

```python
root = ctk.CTk()
root.title("CustomTkinter Browser")
root.geometry("800x600")
```

### Navigation Functions

Define functions to handle URL navigation, back, and forward actions.

```python
def navigate():
    url = url_entry.get()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    web_label.set_html('<h1>Loading...</h1>')
    web_label.set_url(url)

def go_back():
    try:
        web_label.web.navigate_back()
    except Exception as e:
        print(f"Error: {e}")

def go_forward():
    try:
        web_label.web.navigate_forward()
    except Exception as e:
        print(f"Error: {e}")
```

### Building the User Interface

Create the entry widget for the URL, navigation buttons, and the HTML label for displaying web content.

```python
url_entry = ctk.CTkEntry(root, width=600, placeholder_text="Enter URL here")
url_entry.pack(pady=10)

nav_frame = ctk.CTkFrame(root)
nav_frame.pack(pady=10)

back_button = ctk.CTkButton(nav_frame, text="Back", command=go_back)
back_button.pack(side=tk.LEFT, padx=10)

forward_button = ctk.CTkButton(nav_frame, text="Forward", command=go_forward)
forward_button.pack(side=tk.LEFT, padx=10)

go_button = ctk.CTkButton(nav_frame, text="Go", command=navigate)
go_button.pack(side=tk.LEFT, padx=10)

web_label = HTMLLabel(root, html='<h1>Welcome to CustomTkinter Browser!</h1>')
web_label.pack(fill=tk.BOTH, expand=True)
```

### Running the Application

Start the main event loop to run the application.

```python
root.mainloop()
```

## Contributing

We welcome contributions! Please fork this repository and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- **Pratyush Mishra** - Proxlight(https://github.com/Proxlight)
