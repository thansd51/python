from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

res = req.urlopen(url)
print(res)

soup = BeautifulSoup(res, 'html.parser')

# 기상청 육상 중기예보: title만 출력
# title = soup.title
title = soup.find('title').string
print(title)

wf = soup.find('wf').string
print(wf)