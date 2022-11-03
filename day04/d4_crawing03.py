from  bs4 import BeautifulSoup
import re
import requests

r = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")
txt = r.text # 텍스트 형식으로 데이터 추출

bin = r.content # binary 형식으로 데이터 추출
# print(bin)

print('-'*30)

html = """
<ul>
<li><a href="hoge.html">hoge</li>
<li><a href="https://example.com/fuga">fuga*</li>
<li><a href="https://example.com/foo">foo*</li>
<li><a href="shttps://example.com/foobbb">foobbb*</li>
<li><a href="http://example.com/aaa">aaa</li>
"""

# https로 시작하는 것 출력

soup = BeautifulSoup(html, 'html.parser')

# txt = soup.select('li')
# for i in txt:
#     print(i.find('https'))
# print(txt)

list = soup.find_all(href=re.compile(r'https://')) # https 있는 모든거 출력
print(list)
print('-'*30)

list1 = soup.find_all(href=re.compile(r'^https://')) # https 있는 시작하는
print(list1)
print('-'*30)

for i in list1:
    print(i.attrs['href'])