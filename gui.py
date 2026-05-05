import tkinter as tk
from tkinter import messagebox
from quotes import get_random_quote, save_history, load_history

class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор случайных цитат")

        self.quote_label = tk.Label(root, text="", wraplength=300, font=("Arial", 12))
        self.quote_label.pack(pady=10)

        self.generate_btn = tk.Button(root, text="Сгенерировать цитату", command=self.generate_quote)
        self.generate_btn.pack(pady=5)

        self.history_listbox = tk.Listbox(root, width=60, height=10)
        self.history_listbox.pack(pady=10)

        self.filter_frame = tk.Frame(root)
        self.filter_frame.pack(pady=5)

        self.author_var = tk.StringVar()
        self.theme_var = tk.StringVar()

        tk.Entry(self.filter_frame, textvariable=self.author_var, width=20).grid(row=0, column=0, padx=5)
        tk.Entry(self.filter_frame, textvariable=self.theme_var, width=20).grid(row=0, column=1, padx=5)
        tk.Button(self.filter_frame, text="Фильтровать", command=self.filter_history).grid(row=0, column=2, padx=5)

        self.load_history()

    def generate_quote(self):
        quote = get_random_quote()
        self.quote_label.config(text=f'"{quote["text"]}"\n— {quote["author"]}')
        save_history(quote)
        self.load_history()

    def load_history(self):
        self.history_listbox.delete(0, tk.END)
        for q in load_history():
            self.history_listbox.insert(tk.END, f'"{q["text"]}" — {q["author"]}')

    def filter_history(self):
        author = self.author_var.get().strip()
        theme = self.theme_var.get().strip()
        history = load_history()
        filtered = [q for q in history if (not author or q["author"].lower() == author.lower()) and (not theme or q["theme"].lower() == theme.lower())]
        self.history_listbox.delete(0, tk.END)
        for q in filtered:
            self.history_listbox.insert(tk.END, f'"{q["text"]}" — {q["author"]}')
