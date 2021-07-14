from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req

url = 'https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8'
html = req.get(url) #웹사이트 가져오기
#pprint(html.text)
soup = bs(html.text, 'html.parser') # beautifulsoup로 재DOM\

datas = soup.find('div', {'class' : 'detail_box'})
#pprint(finedust)
details = datas.findAll('dd')
#print(details)

finedust = details[0].find('span', {'class', 'num'})
#pprint(finedust)
ultrafinedust = details[1].find('span', {'class', 'num'})
ozone = details[2].find('span', {'class', 'num'})
#.
print('{0}, {1}, {2}'.format(finedust, ultrafinedust, ozone))
