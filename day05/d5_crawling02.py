from  bs4 import BeautifulSoup
import requests


res = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(res.content, 'html.parser')

# print(soup)
datas = []

title = soup.select('#mainContent > div > div.box_ranking > ol > li > div > div.thumb_cont > strong > a')
score = soup.select('#mainContent > div > div.box_ranking > ol > li > div > div.thumb_cont > span.txt_append > span')[:2]
p = soup.select('#mainContent > div > div.box_ranking > ol > li > div > div.thumb_cont > span.txt_append > span')[1:2]

# print(title)
print(score)
# print(p)




# 다른 방법

ols = soup.find('ol', class_="list_movieranking")
rankcont = ols.find_all('div', class_='thumb_cont')
print(rankcont)

for i in rankcont:
    title = i.find('a', class_='link_txt').get_text()
    rank = i.find('span', class_='txt_grade').get_text()
    # reser = i.find('a', class_='txt_num').get_text()
    reser = i.find('span', {'class':'txt_num'}).get_text()
    print('제목: ' + title)
    print('평점: ' + rank)
    print('예매율: ' + reser)
    print()

