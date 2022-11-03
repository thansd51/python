from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import pandas as pd
import time
import datetime

from sympy import re

def CoffeBean_store(result):
    wd = webdriver.Chrome("C:\\util\\chromedriver.exe")
    CoffeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
    time.sleep(1)
    for i in range(1, 5): # 매장 수만큼 반복
        wd.get(CoffeBean_URL)
        time.sleep(1) # 웹페이지를 연결하는 동안 1초 대기
        try:
            wd.execute_script("storePop2('%d')" %i)
            time.sleep(1)
            html = wd.page_source
            soupCB = BeautifulSoup(html, 'html.parser')
            store_name_h2 = soupCB.select("div.store_txt > h2")
            store_name = store_name_h2[0].string
            # 매장 이름 출력
            print(i, store_name)
            result.append([store_name])
        except:
            continue
    return
result =[]
CoffeBean_store(result)