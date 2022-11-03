from email import header
import requests
from bs4 import BeautifulSoup
import pandas as pd

header = {'User-Agent': 'Mozilla/5.0'}

req = requests.get('https://www.melon.com/chart/index.htm', headers=header)
soup = BeautifulSoup(req.content, 'html.parser')
# print(soup)
# 순위, 곡명, 가수, 앨범

tbody = soup.select_one('#frm > div > table > tbody')
chart =[]

for i in tbody.select('tr'):
     tds = i.select('td')
     rank = tds[1].get_text()
     title = tds[5].select_one('span > a').get_text()
     singer = tds[5].select_one('div.ellipsis.rank02 > a').get_text()
     album = tds[6].select_one('div.ellipsis.rank03 > a').get_text()
     
     chart.append([rank, title, singer, album])
print(chart)

df = pd.DataFrame(chart, columns=('순위', '곡명', '가수', '앨범'))
print(df)

df.to_csv('day06/melonChart.csv', encoding='utf-8-sig', mode = 'w', index=False)