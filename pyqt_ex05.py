# QT Designer 연동 소스
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from naverSearch import *
import webbrowser

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/naverSearch.ui', self)

        #ui signal(control event)
        self.btnSearch.clicked.connect(self.btnSearch_clicked)
        self.tblResult.itemSelectionChanged.connect(self.tblResult_Selected)
        self.txtSearchWord.returnPressed.connect(self.btnSearch_clicked)

    def tblResult_Selected(self):
        selected = self.tblResult.currentRow()
        url = self.tblResult.item(selected, 1).text()
        # QMessageBox.about(self, 'URL', url)
        webbrowser.open(url)

    def makeTable(self, result):
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(2)
        self.tblResult.setRowCount(len(result))

        self.tblResult.setHorizontalHeaderLabels(['기사제목', '뉴스링크'])

        n = 0
        for post in result:
            titile = post['title'].replace('&lt;', '<').replace('&gt;', '>').replace('<b>', '').replace('</b>', '').replace('&quot;', "'")
            self.tblResult.setItem(n, 0, QTableWidgetItem(post['title']))
            self.tblResult.setItem(n, 1, QTableWidgetItem(post['originallink']))
            n += 1

        self.tblResult.setColumnWidth(0, 400)
        self.tblResult.setColumnWidth(1, 300)
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def btnSearch_clicked(self):

        api = naverSearch()
        jsonResult = []
        sNode = 'news'
        search_word = self.txtSearchWord.text()
        display = 100

        if len(search_word) == 0:
            QMessageBox.about(self, 'popup', '검색어를 입력하세요')
            return

        # naver api search
        jsonSearch = api.getNaverSearchResult(sNode, search_word, 1, display)
        jsonResult = jsonSearch['items']
        print(len(jsonResult))
        self.stsResult.showMessage('검색결과 : {0}개'.format(len(jsonResult)))
        #print(jsonSearch)
        #model = QtGui.QStandardItemModel()
        #self.lsvResult.setModel(model)

        #for post in jsonResult:
        #   item = QtGui.QStandardItem(post['title'])
        #  model.appendRow(item)
        self.makeTable(jsonResult)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())