"""Рисование фигур мышью на Canvas."""
import tkinter as tk

class DrawApp:
    """Приложение для рисования кругов мышью."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Рисование фигур")
        self.canvas = tk.Canvas(root, width=500, height=400, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.draw_circle)

    def draw_circle(self, event: tk.Event) -> None:
        """Рисует круг в месте клика."""
        r = 20
        self.canvas.create_oval(
            event.x - r, event.y - r, event.x + r, event.y + r,
            outline="black", fill="lightgreen"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawApp(root)
    root.mainloop()