from  bs4 import BeautifulSoup
import requests

codes = ['252670', '251340']
datas = []

for code in codes:
    url = 'https://finance.naver.com/item/main.naver?code='+code
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    title = soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').get_text()
    price = soup.select_one('#chart_area > div.rate_info > div > p.no_today > em > span').get_text()

    datas.append([title, price])
print(datas)
