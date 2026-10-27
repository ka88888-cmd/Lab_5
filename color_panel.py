"""Цветная панель: цвет меняется по кнопке."""
import tkinter as tk
from tkinter import colorchooser

class ColorPanelApp:
    """Приложение с панелью и кнопкой смены цвета."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Цветная панель")
        self.panel = tk.Frame(root, width=300, height=200, bg="lightblue")
        self.panel.pack(padx=10, pady=10)
        self.button = tk.Button(root, text="Выбрать цвет", command=self.change_color)
        self.button.pack(pady=5)

    def change_color(self) -> None:
        """Открывает диалог выбора цвета и применяет его к панели."""
        color = colorchooser.askcolor(title="Выберите цвет")[1]
        if color:
            self.panel.config(bg=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPanelApp(root)
    root.mainloop()