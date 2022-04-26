# 파이썬으로 웹을 크롤링 하기 위한 필수 라이브러리 중 하나인 BeautifulSoup을 설치 한다.
# pip3 install beautifulsoup4

from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex"

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser", from_encoding='euc-kr')

name_nation = soup.select('h3.h_lst > span.blind')
name_price = soup.select('span.value')

i = 0
for c_list in soup :
    try:
        print(i+1, name_nation[i].text, name_price[i].text)
        i = i + 1
    except IndexError :
        pass