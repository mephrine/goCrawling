'''
pip install beautifulsoup4

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject= BeautifulSoup(html, "html.parser")

# 전체 가져오기
# print(bsObject)

# 타이틀 가져오기
#print(bsObject.head.title)

# 모든 메타 데이터의 내용 가져오기
for meta in bsObject.head.find_all('meta'):
    print(meta.get('content'))

