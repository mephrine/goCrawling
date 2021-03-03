# https://webnautes.tistory.com/691

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Get Kyobo Bookstore's bestseller website
html = urlopen('http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf')
bsObject = BeautifulSoup(html, "html.parser")

# The detailed web page of book is extracted and save in the list.
book_page_urls = []
for cover in bsObject.find_all('div', {'class':'detail'}):
    link = cover.select('a')[0].get('href')
    book_page_urls.append(link)
    #print(link)

# Extract necessary data from meta information.
# Author information that is not in the meta information was imported.
for index, book_page_url in enumerate(book_page_urls):
    html = urlopen(book_page_url)
    bsObject = BeautifulSoup(html, "html.parser")
    title = bsObject.find('meta', {'property':'eg:itemName'}).get('content')
    author = bsObject.select('span.name a')[0].text
    image = bsObject.find('meta', {'property':'eg:itemImage'}).get('content')
    url = bsObject.find('meta', {'property':'eg:itemUrl'}).get('content')
    originalPrice = bsObject.find('meta', {'property': 'eg:originalPrice'}).get('content')
    salePrice = bsObject.find('meta', {'property':'eg:salePrice'}).get('content')

    print(index+1)
    print(title)
    print(author)
    print(image)
    print(url)
    print(originalPrice)
    print(salePrice)


