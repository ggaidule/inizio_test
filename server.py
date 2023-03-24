import tkinter as tk
from tkinter import filedialog
import requests
import json

# Replace YOUR_API_KEY with your actual API key
apiKey = "AIzaSyA75V6nWkMpMUqROUhEg-HsMhIS6IUWjkM"
cx = "c2d43f76a34aa488e"

def search_google():
    query = query_entry.get()
    url = f"https://www.googleapis.com/customsearch/v1?key={apiKey}&cx={cx}&q={query}&num=10"
    response = requests.get(url)
    results = json.loads(response.text)['items']
    html = ""
    for result in results:
        html += f"<div><h3><a href='{result['link']}'>{result['title']}</a></h3><p>{result['snippet']}</p></div>"
    search_results_label.config(text=html)
    save_file(html)

def save_file(html):
    save_path = filedialog.asksaveasfilename(defaultextension=".html")
    if save_path:
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(html)

# Create the GUI window
window = tk.Tk()
window.title("Google Custom Search Bar")

# Create the widgets
query_label = tk.Label(window, text="Search Google:")
query_entry = tk.Entry(window)
search_button = tk.Button(window, text="Search", command=search_google)
search_results_label = tk.Label(window)

# Add the widgets to the window
query_label.pack()
query_entry.pack()
search_button.pack()
search_results_label.pack()

# Start the main event loop
window.mainloop()
