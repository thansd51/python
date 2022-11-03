from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"

res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

text = soup.select_one('#exchangeList > li.on > a.head.usd > div')
print(text)

value = text.select_one('span.value').string
print(value)

txt1 = soup.select_one('div.head_info')
print(txt1)
print(txt1.select('span')[0].string)

txt2 = txt1.select('span')
for i in txt2:
    print(i.string)
print(txt2)
print('-'*30)
# 가격
for i in txt2[:2]:
    print(i.string, end="")
print()
# 상승 하락
updown = txt1.select('span.blind')[1].string
print(updown)