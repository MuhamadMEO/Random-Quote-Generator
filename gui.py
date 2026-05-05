import tkinter as tk
from tkinter import messagebox
from quotes import get_random_quote, save_history, load_history

class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор случайных цитат")
        self.root.geometry("500x500")

        # Поле для отображения текущей цитаты
        self.quote_label = tk.Label(
            root, 
            text="", 
            wraplength=450, 
            font=("Arial", 12, "italic"), 
            justify="center"
        )
        self.quote_label.pack(pady=20)

        # Кнопка генерации
        self.generate_btn = tk.Button(
            root, 
            text="Сгенерировать цитату", 
            font=("Arial", 12), 
            command=self.generate_quote
        )
        self.generate_btn.pack(pady=10)

        # Фрейм для фильтрации
        self.filter_frame = tk.Frame(root)
        self.filter_frame.pack(pady=10)

        tk.Label(self.filter_frame, text="Автор:").grid(row=0, column=0, padx=5)
        self.author_var = tk.StringVar()
        tk.Entry(self.filter_frame, textvariable=self.author_var, width=20).grid(row=0, column=1, padx=5)

        tk.Label(self.filter_frame, text="Тема:").grid(row=0, column=2, padx=5)
        self.theme_var = tk.StringVar()
        tk.Entry(self.filter_frame, textvariable=self.theme_var, width=20).grid(row=0, column=3, padx=5)

        tk.Button(
            self.filter_frame, 
            text="Фильтровать", 
            command=self.filter_history
        ).grid(row=0, column=4, padx=5)

        # Список для истории
        self.history_listbox = tk.Listbox(root, width=60, height=12)
        self.Вот полный код файла `gui.py` с учётом всех исправлений, объединения функций в `quotes.py` и добавления точки входа.

Файл `quotes.py` должен находиться в той же папке.

### gui.py
