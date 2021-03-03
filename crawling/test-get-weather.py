from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://www.weather.go.kr/weather/forecast/timeseries.jsp")  

soup = BeautifulSoup(html, "lxml") 



table = soup.find("table", class_="forecastNew3")

tr = table.tbody.tr
for t in tr.children:
	if t.name == 'th':
		if t['scope'] == 'colgroup':
			num = int(t['colspan'])

			for i in range(num):
				print(t.get_text(), end = ' ')


tr = tr.next_sibling.next_sibling


print('@시각')
for t in tr.children:
	if t.name == 'td':
		for i in t.contents:
			if i.name =='p':
				print(i.get_text(), end=' ')
print('\n')



tr = tr.next_sibling.next_sibling



print('@날씨') 
for w in tr.children:
	if w.name == 'td' and len(w.contents) > 0:
		print(w['title'], end= ' ')
print('\n')



tr = tr.next_sibling.next_sibling



print('@강수 확률')
for w in tr.children:
	if w.name == 'td' and len(w.contents) > 0:
		print(w.contents[0], end=' ')
print('\n')



tr = tr.next_sibling.next_sibling



print('@강수량') 
for w in tr.children:
	if w.name == 'td' and len(w.contents) > 0:
		num = int(w['colspan'])

		for i in range(num):
			print(w.contents[0].strip(), end=' ')
print('\n')



tr = tr.next_sibling.next_sibling


print('@최저/최고 기온') 
for w in tr.children:
	if w.name == 'td' and len(w.contents) > 0:
		num = int(w['colspan'])

		for i in range(num):
			print(w.contents[0].get_text(), end='/')
			print(w.contents[2].get_text(), end=' ')
print('\n')



tr = tr.next_sibling.next_sibling



print('@기온(℃)')
for w in tr.children:
	if w.name == 'td' and len(w.contents) > 0:
		print(w.contents[0].get_text(), end=' ')
print('\n')



tr = tr.next_sibling.next_sibling



print('@풍향/풍속(m/s)')
for w in tr.children:
	if w.name == 'td' and len(w.contents) > 0:
		print(w['title'], end= ' ')
print('\n')



tr = tr.next_sibling.next_sibling


print('@습도(%)')
for w in tr.children:
	if w.name == 'td' and len(w.contents) > 0:
		print(w.contents[0].get_text(), end=' ')
print('\n')