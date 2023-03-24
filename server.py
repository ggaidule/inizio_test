import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import requests
import json


class GoogleCustomSearchBar:
    def __init__(self, master):
        self.master = master
        self.master.title("Google Custom Search Bar")

        self.api_key = "AIzaSyA75V6nWkMpMUqROUhEg-HsMhIS6IUWjkM"
        self.cx = "c2d43f76a34aa488e"

        # Create the widgets
        self.query_label = tk.Label(master, text="Search Google:")
        self.query_entry = tk.Entry(master)
        self.search_button = tk.Button(master, text="Search", command=self.search_google)
        self.save_button = tk.Button(master, text="Save Results", command=self.save_results)
        self.search_results_label = tk.Label(master, text="")

        # Add the widgets to the window
        self.query_label.pack()
        self.query_entry.pack()
        self.search_button.pack()
        self.save_button.pack()
        self.search_results_label.pack()

        self.search_results = []

    def search_google(self):
        query = self.query_entry.get()
        url = f"https://www.googleapis.com/customsearch/v1?key={self.api_key}&cx={self.cx}&q={query}&num=10"
        response = requests.get(url)
        self.search_results = json.loads(response.text)['items']
        html = ""
        for result in self.search_results:
            html += f"<div><h3><a href='{result['link']}'>{result['title']}</a></h3><p>{result['snippet']}</p></div>"
        self.search_results_label.config(text=html)

    def save_results(self):
        if not self.search_results:
            tk.messagebox.showerror(title="Error", message="No search results to save.")
            return

        saved_html = ""
        for result in self.search_results:
            saved_html += f"<div><h3><a href='{result['link']}'>{result['title']}</a></h3><p>{result['snippet']}</p></div>"
        save_path = filedialog.asksaveasfilename(defaultextension=".html")
        if save_path:
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(saved_html)
            tk.messagebox.showinfo(title="File saved", message=f"File saved to {save_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GoogleCustomSearchBar(root)
    root.mainloop()
