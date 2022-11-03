from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import re

path = "C:\\util\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(2)
driver.get('https://www.melon.com/chart/index.htm')

# 순위, 곡명, 가수, 앨범

# XPATH = //*[@id="frm"]/div/table/tbody
tbody = driver.find_element(By.XPATH, '//*[@id="frm"]/div/table/tbody')
trs = tbody.find_elements(By.TAG_NAME, 'tr')

chart =[]

for i in trs:
    rank = i.find_element(By.CLASS_NAME, 'rank').text
    title = i.find_element(By.CLASS_NAME, 'wrap_song_info').find_element(By.TAG_NAME, 'a').text
    singer = i.find_element(By.CSS_SELECTOR, 'div.rank02').find_element(By.TAG_NAME, 'a').text
    album = i.find_element(By.CSS_SELECTOR, 'div.rank03').find_element(By.TAG_NAME, 'a').text
    like = i.find_element(By.CLASS_NAME, 'like').find_element(By.CLASS_NAME, 'cnt').text 
    like = re.sub(',', '', like)
    
    chart.append([rank, title, singer, album, like])
print(chart)

df = pd.DataFrame(chart, columns=('순위', '곡명', '가수', '앨범', '좋아요'))
print(df)

df.to_csv('day06/melonChartSelenium.csv', encoding='utf-8-sig', mode = 'w', index=False)