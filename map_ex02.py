import folium
import io
import sys
from PyQt5 import QtWidgets, QtWebEngineWidgets

app = QtWidgets.QApplication(sys.argv) # QT 원품 생성

m = folium.Map(location=[35.1175, 129.0903], zoom_start=12) ## folium 앱 생성

data = io.BytesIO() # byte로 변환
m.savae(data, close_file=False) # 앱 데이터 저장

win = QtWebEngineWidgets.QWebEngineView() ## Qt5 웹엔진 생성
win.setHtml(data.getvalue().decode()) ## 바이너리 맵데이터를 HTML로 재변환
win.resize(800, 600) # 윈폼 사이즈
win.show()

sys.exit(app.exec_())