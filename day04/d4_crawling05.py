from nbformat import write
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

res = requests.get("https://finance.naver.com/")
html = res.content 

soup = BeautifulSoup(html, 'html.parser')
# print(soup)

a = soup.select('#container > div.aside > div > div.aside_area.aside_popular > table > tbody')
# for i in a:
#     print(i.get_text())

tbody =soup.select_one('#container > div.aside > div > div.aside_area.aside_popular > table > tbody')

trs = tbody.select('tr')
print(trs)
datas = []
for i in trs:
    name = i.select_one('th > a').get_text()
    cur_price = i.select_one('td').get_text()
    ch_direction = i.select_one('td > img')['alt']
    ch_updown = i.select_one('td > span').get_text().strip()
    
    datas.append([name, cur_price, ch_direction, ch_updown])
print(datas)

write_wb =Workbook()
write_ws = write_wb.create_sheet('결과')

for i in datas:
    write_ws.append(i)

write_wb.save(r'financeWork.xls')

