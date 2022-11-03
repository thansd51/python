from bs4 import BeautifulSoup
import urllib.request as req


url = 'https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC'

res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

# print(soup)

txt1 = soup.select('#mw-content-text > div > ul > li a')
# li >  b > a(li 하위 a 접근)
# 후손 : li a
# 자식 : li > b  
#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > a
#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li
#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a
#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > a

print(txt1)

for i in txt1:
    print(i.string)