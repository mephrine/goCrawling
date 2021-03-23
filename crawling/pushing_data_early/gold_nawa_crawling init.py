'''
pip install beautifulsoup4
pip3 install psycopg2

'''

import psycopg2 # driver 임포트

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://goldgold.co.kr/charts/1_price1.php?&page=1")
bsObject = BeautifulSoup(html, "html.parser")

so_many_tables = bsObject.body.table

tbl_buy = []
tbl_sell = []

input_day_1 = ''
input_day_2 = ''
input_day_3 = ''
input_day_4 = ''
input_day_5 = ''
input_day_6 = ''
input_day_7 = ''
input_buy_price_1 = ''
input_buy_price_2 = ''
input_buy_price_3 = ''
input_buy_price_4 = ''
input_buy_price_5 = ''
input_buy_price_6 = ''
input_buy_price_7 = ''
input_sell_price_1 = ''
input_sell_price_2 = ''
input_sell_price_3 = ''
input_sell_price_4 = ''
input_sell_price_5 = ''
input_sell_price_6 = ''
input_sell_price_7 = ''

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
        input_day_1 = text_tr('td')[1].text        # 첫번쨰날짜
        input_day_2 = text_tr('td')[2].text        # 
        input_day_3 = text_tr('td')[3].text        # 
        input_day_4 = text_tr('td')[4].text        # 
        input_day_5 = text_tr('td')[5].text        # 
        input_day_6 = text_tr('td')[6].text        # 
        input_day_7 = text_tr('td')[7].text        # 
    if index == 9:
        input_buy_price_1 = text_tr('td')[1].text    # 첫번쨰살때가격
        input_buy_price_2 = text_tr('td')[2].text    # 
        input_buy_price_3 = text_tr('td')[3].text    # 
        input_buy_price_4 = text_tr('td')[4].text    # 
        input_buy_price_5 = text_tr('td')[5].text    # 
        input_buy_price_6 = text_tr('td')[6].text    # 
        input_buy_price_7 = text_tr('td')[7].text    # 

# 팔때
for index, text_tr in enumerate(tbl_sell):
    if index == 5:
        input_sell_price_1 = text_tr('td')[1].text    # 팔때가격
        input_sell_price_2 = text_tr('td')[2].text    # 
        input_sell_price_3 = text_tr('td')[3].text    # 
        input_sell_price_4 = text_tr('td')[4].text    # 
        input_sell_price_5 = text_tr('td')[5].text    # 
        input_sell_price_6 = text_tr('td')[6].text    # 
        input_sell_price_7 = text_tr('td')[7].text    # 
    
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


SQL_BUY = "INSERT INTO" \
    + " tbl_gold_price (jewelry_type, gold_date, gold_purity, gold_price_type, gold_price, country_code, gold_currency)"\
    + " VALUES (%s,%s,%s,%s,%s,%s,%s);"

SQL_SELL = "INSERT INTO" \
    + " tbl_gold_price (jewelry_type, gold_date, gold_purity, gold_price_type, gold_price, country_code, gold_currency)"\
    + " VALUES (%s,%s,%s,%s,%s,%s,%s);"


data = ("001", input_day_1, "24K", "B", input_buy_price_1, "029", "001")
cur.execute(SQL_BUY, data)
data = ("001", input_day_1, "24K", "S", input_sell_price_1, "029", "001")
cur.execute(SQL_SELL, data)

data = ("001", input_day_2, "24K", "B", input_buy_price_2, "029", "001")
cur.execute(SQL_BUY, data)
data = ("001", input_day_2, "24K", "S", input_sell_price_2, "029", "001")
cur.execute(SQL_SELL, data)

data = ("001", input_day_3, "24K", "B", input_buy_price_3, "029", "001")
cur.execute(SQL_BUY, data)
data = ("001", input_day_3, "24K", "S", input_sell_price_3, "029", "001")
cur.execute(SQL_SELL, data)

data = ("001", input_day_4, "24K", "B", input_buy_price_4, "029", "001")
cur.execute(SQL_BUY, data)
data = ("001", input_day_4, "24K", "S", input_sell_price_4, "029", "001")
cur.execute(SQL_SELL, data)

data = ("001", input_day_5, "24K", "B", input_buy_price_5, "029", "001")
cur.execute(SQL_BUY, data)
data = ("001", input_day_5, "24K", "S", input_sell_price_5, "029", "001")
cur.execute(SQL_SELL, data)

data = ("001", input_day_6, "24K", "B", input_buy_price_6, "029", "001")
cur.execute(SQL_BUY, data)
data = ("001", input_day_6, "24K", "S", input_sell_price_6, "029", "001")
cur.execute(SQL_SELL, data)

data = ("001", input_day_7, "24K", "B", input_buy_price_7, "029", "001")
cur.execute(SQL_BUY, data)
data = ("001", input_day_7, "24K", "S", input_sell_price_7, "029", "001")
cur.execute(SQL_SELL, data)

conn.commit()   # 데이터를 변경했다면 반드시 .commit()
cur.close()     # 커서를 닫음 
conn.close()    # 연걸을 종료


