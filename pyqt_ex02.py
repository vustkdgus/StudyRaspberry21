## QT5 user window class ex
import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)

# button = QPushButton("Click me")
# button.show()
# label = QLabel("Hello QT5!")
# label.show()
win = MyWindow()
win.show()

app.exec_()