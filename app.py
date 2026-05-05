import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os

class QuoteGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Quote Generator")
        self.root.geometry("600x500")

        # Загрузка данных
        self.quotes = self.load_quotes()
        self.history = self.load_history()

        self.setup_ui()

    def load_quotes(self):
        if os.path.exists('quotes.json'):
            with open('quotes.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def load_history(self):
        if os.path.exists('history.json'):
            with open('history.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_history(self):
        with open('history.json', 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)

    def setup_ui(self):
        # Основной фрейм
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Кнопка генерации
        generate_btn = ttk.Button(main_frame, text="Сгенерировать цитату", command=self.generate_quote)
        generate_btn.grid(row=0, column=0, pady=10)

        # Отображение цитаты
        self.quote_text = tk.Text(main_frame, height=4, wrap=tk.WORD, font=('Arial', 12))
        self.quote_text.grid(row=1, column=0, pady=10, sticky=(tk.W, tk.E))

        # Фильтры
        filter_frame = ttk.LabelFrame(main_frame, text="Фильтры", padding="10")
        filter_frame.grid(row=2, column=0, pady=10, sticky=(tk.W, tk.E))

        ttk.Label(filter_frame, text="Автор:").grid(row=0, column=0)
        self.author_filter = ttk.Combobox(filter_frame, state="readonly")
        self.author_filter.grid(row=0, column=1, padx=5)
        self.author_filter.bind('<<ComboboxSelected>>', self.apply_filters)

        ttk.Label(filter_frame, text="Тема:").grid(row=0, column=2, padx=(20, 5))
        self.topic_filter = ttk.Combobox(filter_frame, state="readonly")
        self.topic_filter.grid(row=0, column=3, padx=5)
        self.topic_filter.bind('<<ComboboxSelected>>', self.apply_filters)

        # История
        history_frame = ttk.LabelFrame(main_frame, text="История цитат", padding="10")
        history_frame.grid(row=3, column=0, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        columns = ('text', 'author', 'topic')
        self.history_tree = ttk.Treeview(history_frame, columns=columns, show='headings', height=8)
        self.history_tree.heading('text', text='Цитата')
        self.history_tree.heading('author', text='Автор')
        self.history_tree.heading('topic', text='Тема')
        self.history_tree.column('text', width=300)
        self.history_tree.column('author', width=150)
        self.history_tree.column('topic', width=150)

        scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, command=self.history_tree.yview)
        self.history_tree.configure(yscrollcommand=scrollbar.set)

        self.history_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Обновление фильтров
        self.update_filters()
        self.refresh_history()

    def update_filters(self):
        authors = sorted(set(q['author'] for q in self.quotes))
        topics = sorted(set(q['topic'] for q in self.quotes))

        self.author_filter['values'] = [''] + authors
        self.topic_filter['values'] = [''] + topics

    def generate_quote(self):
        if not self.quotes:
            messagebox.showwarning("Предупреждение", "Список цитат пуст!")
            return

        quote = random.choice(self.quotes)
        self.history.append(quote)
        self.save_history()

        self.quote_text.delete(1.0, tk.END)
        self.quote_text.insert(1.0, f"{quote['text']}\n\n— {quote['author']} ({quote['topic']})")

        self.refresh_history()

    def apply_filters(self, event=None):
        author = self.author_filter.get()
        topic = self.topic_filter.get()

        filtered = self.history
        if author:
            filtered = [q for q in filtered if q['author'] == author]
        if topic:
            filtered = [q for q in filtered if q['topic'] == topic]

        self.refresh_history(filtered)

    def refresh_history(self, data=None):
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)

        display_data = data if data is not None else self.history
        for quote in display_data:
            self.history_tree.insert('', 'end', values=(quote['text'], quote['author'], quote['topic']))

if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteGenerator(root)
    root.mainloop()
