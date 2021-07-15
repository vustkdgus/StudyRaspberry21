# QT Designer 연동 소스
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/mainWindow01.ui', self)

        #ui
        self.BtnStart.clicked.connect(self.btnStart_Clicked)
        self.BtnStop.clicked.connect(self.btnStop_Clicked)
    
    def btnStart_Clicked(self):
        print('시작했습니다!!')
        self.LblResult.setText('시작했습니다')

    def btnStop_Clicked(self):
        print('종료했습니다')
        self.LblResult.setText('종료했습니다')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())