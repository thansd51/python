from  bs4 import BeautifulSoup
import re
import requests

res = requests.get('https://news.daum.net/economic/')
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)

links = soup.select('a[href]')
print(links)

for i in links:
    if re.search('https://v.\w', i['href']): #. 임의의 문자 1개 # \w 숫자와문자 # + 1회 이상
        print(i)         

print('-'*30)

lis = soup.find_all(href=re.compile(r'https://v.\w'))

for i in lis:
    print(i.get_text().strip())
