'''
pip install beautifulsoup4
pip3 install psycopg2

'''

import psycopg2 # driver 임포트

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://goldgold.co.kr/charts/1_price1.php")
bsObject = BeautifulSoup(html, "html.parser")

so_many_tables = bsObject.body.table

tbl_buy = []
tbl_sell = []

input_today = ''
input_buy_price = ''
input_sell_price = ''

# table 안에 table 구조에서 꺼내기
for index, text_tr in enumerate(so_many_tables):
    #print(index, text_tr)
    if index == 13: 
        tbl_buy = text_tr.table     # 살때가격 테이블
    if index == 17:
        tbl_sell = text_tr.table    # 팔때가격 테이블


# 살때
for index, text_tr in enumerate(tbl_buy):
    if index == 5:
        input_today = text_tr('td')[7].text    # 오늘날짜
    if index == 9:
        input_buy_price = text_tr('td')[7].text    # 살때가격


# 팔때
for index, text_tr in enumerate(tbl_sell):
    if index == 5:
        input_sell_price = text_tr('td')[7].text    # 팔때가격
    #if index == 9:
        #print(text_tr('td')[7].text)    # 18k가격
    #if index == 13:
        #print(text_tr('td')[7].text)    # 14k가격

# 순금이 24k 입니다.



# DB Connect
# conn = psycopg2.connect("host=localhost dbname=test user=postgres password=pwtest port=5432")
conn = psycopg2.connect(host='210.0.47.232', dbname='goldnawa', user='goldnawa', password='goldnawa!', port='5432') # db에 접속
cur = conn.cursor() # 커서를 생성한다


# data 입력
'''
jewelry_type (001:금)
gold_date 
gold_purity 24K
gold_price_type B
gold_price 살때가격
country_code 999
gold_currency 001 원화
'''


SQL = "INSERT INTO" \
    + " tbl_gold_price (jewelry_type, gold_date, gold_purity, gold_price_type, gold_price, country_code, gold_currency)"\
    + " VALUES (%s,%s,%s,%s,%s,%s,%s);"

data = ("001", input_today, "24K", "B", input_buy_price, "999", "001")
cur.execute(SQL, data)

SQL = "INSERT INTO" \
    + " tbl_gold_price (jewelry_type, gold_date, gold_purity, gold_price_type, gold_price, country_code, gold_currency)"\
    + " VALUES (%s,%s,%s,%s,%s,%s,%s);"
data = ("001", input_today, "24K", "S", input_sell_price, "999", "001")
cur.execute(SQL, data)

conn.commit()   # 데이터를 변경했다면 반드시 .commit()
cur.close()     # 커서를 닫음 
conn.close()    # 연걸을 종료


