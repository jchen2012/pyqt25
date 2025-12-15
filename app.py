import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        self.setFixedSize(QSize(400, 300))

# Set the central widget of the

app = QApplication(sys.argv)

# Create a Qt widget, which will be the top window
window = MainWindow()
window.show()

# start the event loop
app.exec()
