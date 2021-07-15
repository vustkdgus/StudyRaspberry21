## QT5 user window class ex
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# declare window class
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My QT5 Window") # 제목표시줄
        self.setGeometry(80, 80, 600, 300) # x, y, width, height
        self.setWindowIcon(QIcon('./image/chart.png'))

        #label add
        self.label = QLabel('message', self)
        self.label.move(10, 10)
        self.label.setGeometry(10, 10, 300, 20)

        #button add
        self.btn = QPushButton('click', self)
        self.btn.move(10, 50)

        #signal add
        self.btn.clicked.connect(self.btn_clicked)

# button click signal(event)
def btn_clicked(self):
    self.label.clear()
    self.label.setText("message: button click!!")

app = QApplication(sys.argv)

win = MyWindow()
win.show()
app.exec_()