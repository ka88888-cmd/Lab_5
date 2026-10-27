"""Приложение PyQt5 с таблицей."""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class TableWindow(QMainWindow):
    """Окно с таблицей."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQt5 Таблица")
        self.resize(400, 300)
        central = QWidget()
        layout = QVBoxLayout()
        self.table = QTableWidget(3, 2)
        self.table.setHorizontalHeaderLabels(["Имя", "Возраст"])
        data = [("Анна", "25"), ("Иван", "30"), ("Ольга", "22")]
        for row, (name, age) in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(age))
        layout.addWidget(self.table)
        central.setLayout(layout)
        self.setCentralWidget(central)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableWindow()
    window.show()
    sys.exit(app.exec_())