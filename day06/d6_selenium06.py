from xml.dom.minidom import Document
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import pandas as pd
import time

path = "C:\\util\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(path, options=options)
driver.implicitly_wait(2)
driver.get('https://www.youtube.com/c/paikscuisine/videos')

all_videos=driver.find_elements(By.ID, 'dismissible')
body_tag = driver.find_element(By.TAG_NAME, 'body')
# print(body_tag)
body_tag.send_keys(Keys.END) # 스크롤이 1번 진행

# 화면 길이 확인
# document.documentElement.scrollHeight: 화면길이 
# print(driver.execute_script('return document.documentElement.scrollHeight'))

while True:
    last_height = driver.execute_script('return document.documentElement.scrollHeight')

    for i in range(10):
        body_tag.send_keys(Keys.END)
        time.sleep(1)
    new_height = driver.execute_script('return document.documentElement.scrollHeight')

    if last_height == new_height:
        print('종료')
        break
    print('='*100)