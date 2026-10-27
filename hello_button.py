"""Окно с кнопкой «Привет»."""
import tkinter as tk
from tkinter import messagebox

class HelloApp:
    """Приложение с кнопкой, показывающей приветствие."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Привет")
        self.button = tk.Button(root, text="Привет", command=self.say_hello)
        self.button.pack(padx=20, pady=20)

    def say_hello(self) -> None:
        """Показывает сообщение."""
        messagebox.showinfo("Привет", "Привет, мир!")

if __name__ == "__main__":
    root = tk.Tk()
    app = HelloApp(root)
    root.mainloop()