"""Прогрессбар с кнопкой запуска."""
import tkinter as tk
from tkinter import ttk

class ProgressApp:
    """Приложение с прогрессбаром."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Прогрессбар")
        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(padx=10, pady=10)
        self.button = tk.Button(root, text="Запустить", command=self.start)
        self.button.pack(pady=5)
        self.value = 0

    def start(self) -> None:
        """Запускает заполнение прогрессбара."""
        self.value = 0
        self.progress["value"] = 0
        self.update()

    def update(self) -> None:
        """Увеличивает прогресс, пока не достигнет 100."""
        if self.value < 100:
            self.value += 5
            self.progress["value"] = self.value
            self.root.after(100, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgressApp(root)
    root.mainloop()