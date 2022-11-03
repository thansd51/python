import requests as req
from  bs4 import BeautifulSoup
import urllib.request
import pandas as pd

# codes = ['1', '2', '3', '4', '5']
# result = []

# for code in codes:
#     url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo='+code+'&sido=&gugun=&store='
#     res = req.get(url)
#     soup = BeautifulSoup(res.content, 'html.parser')
    
          
        
        
#  local = soup.select('#contents > div.content > fieldset > div.tableType01 > table > tbody > tr > td.noline.center_t')
#     store = soup.select('#contents > div.content > fieldset > div.tableType01 > table > tbody > tr > td.center_t')
#     address = soup.select('#contents > div.content > fieldset > div.tableType01 > table > tbody > tr > td.center_t > a')
#     # phone = soup.select('')

#     # print(local)
#     print(store)
#     # print(address)
# 

# 함수 방법
def hollys_store(result):
    for page in range(1, 6):
        url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store='%page

        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        tag_tbody = soup.select_one('tbody')
        
        for store in tag_tbody.select('tr'):
            tds = store.select('td')
            store_sido = tds[0].string
            store_name = tds[1].string
            store_address = tds[3].string
            store_phone = tds[-1].string
            result.append([store_sido, store_name, store_address, store_phone])
    return
result = []
hollys_store(result)
# print(result)
hollys_df = pd.DataFrame(result, columns=('store', 'sido-gu', 'address', 'phone'))
print(hollys_df)

hollys_df.to_csv('hollys.csv', encoding='cp949', mode = 'w', index= True)