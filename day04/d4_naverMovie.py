from  bs4 import BeautifulSoup
import re
import requests

r = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")
html = r.text # 텍스트 형식으로 데이터 추출

soup = BeautifulSoup(html, 'html.parser')
movie_rank = soup.find_all('div', class_='tit3')
movie_rank1 = soup.select('div.tit3')

print(soup)

for i in movie_rank:
    print(i.get_text().strip())

print('-'*30)
for i in range(len(movie_rank)):
    print((i+1), '위 :', movie_rank[i].get_text().strip())  

# list = soup.find_all(href=re.compile(r'^/movie/bi/mi/basic.naver?')) 
# print(list)

# for i in list:
#     print(i.attrs['href'])

