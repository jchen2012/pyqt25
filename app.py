import sys

from random import choice
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
QApplication,
QMainWindow,
QPushButton,
)

window_titles = [
"My App",
"Still My App",
"What on earth",
"This is surprising",
"Something went wrong",
]
# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        # self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(800, 600))

        self.button.clicked.connect(self.the_button_was_clicked)
        
        self.windowTitleChanged.connect(self.the_window_title_changed)
                
        # Set the central widget of the Window.
        self.setCentralWidget(self.button)
    
    def the_button_was_clicked(self):
        new_window_title = choice(window_titles)

        print(f"Setting title: {new_window_title}")
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print(f"Window title changed: {window_title}")
        if window_title == "Something went wrong":
            self.button.setDisabled(True)
            
app = QApplication(sys.argv)

# Create a Qt widget, which will be the top window
window = MainWindow()
window.show()

# start the event loop
app.exec()
