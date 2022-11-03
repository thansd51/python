from  bs4 import BeautifulSoup
import requests

r = requests.get("https://sports.news.naver.com/wfootball/record/index?category=primera&league=650&tab=player")
html = r.text # 텍스트 형식으로 데이터 추출

soup = BeautifulSoup(html, 'html.parser')
# print(soup)
num = soup.select('#wfootballPlayerRecordBody > table > tbody > tr > td.num')
align_l = soup.select('#wfootballPlayerRecordBody > table > tbody > tr > td.align_l')
# print(txt)
for i in num:
    print(i.get_text())

for i in align_l:
    print(i.get_text().strip())

list = []
for i in range(len(align_l)):
    print(align_l[i].get_text().strip())
print(list)


# txt = soup.select('#wfootballPlayerRecordBody > table > tbody > tr')

# for i in txt:
#     print(i.get_text().strip())

# for i in range(len(txt)):
#     print((i+1), '위 :', txt[i].get_text().strip())