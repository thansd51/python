from unittest import result
import requests as req
from  bs4 import BeautifulSoup
import pandas as pd

res = req.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')
# res = req.get('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=108')
soup = BeautifulSoup(res.content, 'html.parser')

tbody = soup.select_one('tbody')

list=[]
for i in tbody.select('tr'):
    tds = i.select('td')
    local = tds[0].string
    temp = tds[6].string
    humidity = tds[-4].string

    list.append([local, temp, humidity])
print(list)

df = pd.DataFrame(list, columns=('지역', '온도', '습도'))
print(df)

df.to_csv('weather.csv', encoding='cp949', mode = 'w', index= True)

# with open('weather.csv', 'w') as file:
#     file.write('point, temp, num \n')
#     for item in list:
#         row = ','.join(item)
#         file.write(row+'\n')

# df1 = pd.read_csv('weathers.csv', index_col='point', encoding='euc-kr')
# print(df1)

# find 방법
# table = soup.find('table', {'class' : 'table-col'})
# # # print(table)

# for i in table.find_all('tr'):
#     tds = i.find_all('td')
#     if len(tds) > 0:
#         local = tds[0].string
#         temp = tds[6].string
#         humidity = tds[-4].string

#     list.append([local, temp, humidity])
# print(list)