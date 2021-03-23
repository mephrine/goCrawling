'''
pip install beautifulsoup4
pip3 install psycopg2
'''

#execute sample as below:
# py C:\Users\swjung\git_front_goldnawa\goCrawling\crawling\gold_nawa_crawling.py gold
# py C:\Users\swjung\git_front_goldnawa\goCrawling\crawling\gold_nawa_crawling.py platinum
# py C:\Users\swjung\git_front_goldnawa\goCrawling\crawling\gold_nawa_crawling.py silver

# py C:\Users\swjung\git_front_goldnawa\goCrawling\crawling\gold_nawa_crawling_imsi_push_data.py gold


import psycopg2 # driver 임포트
import sys # 파이썬 실행시 뒤에 파라미터 붙이기 위해 추가
import time # insert 시 너무빨라서 데이터 위아래 안맞아서 sleep 추가하기 위해 import

from urllib.request import urlopen
from bs4 import BeautifulSoup


print("Here is a sample value as below:") 
print("gold") 
print("platinum") 
print("silver") 

input_sys_value = sys.argv[1]

print('The entered parameter value is : ', input_sys_value)

if input_sys_value == "gold":
    input_url = "http://goldgold.co.kr/charts/1_price1.php"
    input_jewelry_type = 'C002001'
    input_gold_purity = 'C003001'
elif input_sys_value == "platinum":
    input_url = "http://goldgold.co.kr/charts/1_price2.php"
    input_jewelry_type = 'C002002'
    input_gold_purity = '' # 순도없음
elif input_sys_value == "silver":
    input_url = "http://goldgold.co.kr/charts/1_price3.php"
    input_jewelry_type = 'C002003'
    input_gold_purity = '' # 순도없음
else:
    quit()


input_gold_currency = 'C001001'
input_country_code = 'C900029'


html = urlopen(input_url)
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
jewelry_type (C002001:금)
gold_date 
gold_purity (C003001:24K)
gold_price_type B
gold_price 살때가격
country_code 029
gold_currency (C001001:원화)
'''


print_code = ''
print_code_value = ''
print_use_yn = ''
print_del_yn = ''


### print value
query = "select code, code_value, use_yn, del_yn from tbl_common_code tcc where code = '" + input_gold_currency + "'"
cur.execute(query)

tbl_common_code_records = cur.fetchall()

for row in tbl_common_code_records:
    print_code = row[0]
    print_code_value = row[1]
    print_use_yn = row[2]
    print_del_yn = row[3]

print('[gold_currency] >> ' , print_code_value , '(' , print_code , ')')
print('[gold_currency] >> ' , 'use_yn : ', print_use_yn)
print('[gold_currency] >> ' , 'del_yn : ', print_del_yn)
print('')



query = "select code, code_value, use_yn, del_yn from tbl_common_code tcc where code = '" + input_jewelry_type + "'"
cur.execute(query)

tbl_common_code_records = cur.fetchall()

for row in tbl_common_code_records:
    print_code = row[0]
    print_code_value = row[1]
    print_use_yn = row[2]
    print_del_yn = row[3]

print('[jewelry_type] >> ' , print_code_value , '(' , print_code , ')')
print('[jewelry_type] >> ' , 'use_yn : ', print_use_yn)
print('[jewelry_type] >> ' , 'del_yn : ', print_del_yn)
print('')



if input_sys_value == "gold":
    query = "select code, code_value, use_yn, del_yn from tbl_common_code tcc where code = '" + input_gold_purity + "'"
    cur.execute(query)

    tbl_common_code_records = cur.fetchall()

    for row in tbl_common_code_records:
        print_code = row[0]
        print_code_value = row[1]
        print_use_yn = row[2]
        print_del_yn = row[3]

    print('[gold_purity] >> ' , print_code_value , '(' , print_code , ')')
    print('[gold_purity] >> ' , 'use_yn : ', print_use_yn)
    print('[gold_purity] >> ' , 'del_yn : ', print_del_yn)
    print('')



query = "select code, code_value, use_yn, del_yn from tbl_common_code tcc where code = '" + input_country_code + "'"
cur.execute(query)

tbl_common_code_records = cur.fetchall()

for row in tbl_common_code_records:
    print_code = row[0]
    print_code_value = row[1]
    print_use_yn = row[2]
    print_del_yn = row[3]

print('[country_code] >> ' , print_code_value , '(' , print_code , ')')
print('[country_code] >> ' , 'use_yn : ', print_use_yn)
print('[country_code] >> ' , 'del_yn : ', print_del_yn)
print('')



print('[input_jewelry_type] >> ' , input_jewelry_type)
print('[input_country_code] >> ' , input_country_code)
print('[input_today] >> ' , input_today)
print('[input_gold_purity] >> ' , input_gold_purity)
print('[input_buy_price] >> ' , input_buy_price)
print('[input_sell_price] >> ' , input_sell_price)
print('[input_gold_currency] >> ' , input_gold_currency)
print('')




SQL = "INSERT INTO" \
    + " tbl_gold_price (jewelry_type, gold_date, gold_purity, gold_price_type, gold_price, country_code, gold_currency)"\
    + " VALUES (%s,%s,%s,%s,%s,%s,%s);"

data = (input_jewelry_type, input_today, input_gold_purity, "B", input_buy_price, input_country_code, input_gold_currency)
cur.execute(SQL, data)
conn.commit()   # 데이터를 변경했다면 반드시 .commit()


SQL = "INSERT INTO" \
    + " tbl_gold_price (jewelry_type, gold_date, gold_purity, gold_price_type, gold_price, country_code, gold_currency)"\
    + " VALUES (%s,%s,%s,%s,%s,%s,%s);"
data = (input_jewelry_type, input_today, input_gold_purity, "S", input_sell_price, input_country_code, input_gold_currency)
cur.execute(SQL, data)
conn.commit()   # 데이터를 변경했다면 반드시 .commit()

cur.close()     # 커서를 닫음 
conn.close()    # 연걸을 종료


