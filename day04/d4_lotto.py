from  bs4 import BeautifulSoup
import requests

res = requests.get('https://m.dhlottery.co.kr/gameResult.do?method=byWin')
soup = BeautifulSoup(res.content, 'html.parser')

ballNum = soup.find_all('span', class_="ball")
# print(ballNum)

for i in ballNum:
    print(i.get_text(), end='\t')
print()
num = soup.select('#container > div > div.bx_lotto_winnum > span.ball')
for i in num:
    print(i.string, end='\t')
# print(num)
