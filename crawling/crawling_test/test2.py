
# https://webnautes.tistory.com/779

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.python.org/about")
bsObject= BeautifulSoup(html, "html.parser")

#print (bsObject.head.find("meta", {"name":"description"}))

#print(bsObject.head.find("meta",{"name":"description"}).get("content"))

# 모든 링크의 텍스트와 주소 가져오기
# a 태그로 둘러싸인 텍스트와 a 태그의 href 속성을 출력합니다.
for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))
