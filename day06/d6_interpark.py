from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import pandas as pd


path = "C:\\util\\chromedriver.exe"
driver = wd.Chrome(path)
time.sleep(1)
driver.get('http://tour.interpark.com/?mbn=tour&mln=tour_tour')

search = driver.find_element(By.ID, 'SearchGNBText')
search.send_keys('제주도')
seartBtn = driver.execute_script('searchBarModule.ClickForSearch()')

time.sleep(2)
#app > div > div:nth-child(1) > div.resultAtc > div.contentsZone > div.panelZone > div.searchAllBox.domesticHotel.col1 > div > button
moreBtn = driver.find_element(By.CSS_SELECTOR, 'div.searchAllBox.domesticHotel.col1 > div > button')
moreBtn.click()
time.sleep(1)
list = []

for i in range(1, 11):
    page = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[3]/div[2]/div[3]/ul/li[%d]' %i)
    page.click()
    
    time.sleep(1)

    item = driver.find_elements(By.CSS_SELECTOR, '#boxList > li')
    
    for i in item:
        try:
        # title = i.find_element(By.CLASS_NAME, 'infoTitle').text
        # price = i.find_element(By.XPATH, '//*[@id="boxList"]/li/div/div[2]/div[2]/div[2]/div/p[1]/strong').text
        # score = i.find_element(By.XPATH, '//*[@id="boxList"]/li/div/div[2]/div[3]/div[2]/p[1]').text.split('평점')[1]
            title = i.find_element(By.TAG_NAME, 'h5').text
            price = i.find_element(By.TAG_NAME, 'strong').text
            score = i.find_element(By.CSS_SELECTOR, 'div.productInfo > div:nth-child(3) > div:nth-child(2) > p.info').text.split('평점')[1]
        #div.productInfo > div:nth-child(3) > div:nth-child(2) > p:nth-child(1)
    
            list.append([title, price, score])
            print(title, price, score, sep=' | ')
            print('-'*100)
        except:
            print(i.text)
            continue
print(list)
print(len(list))

df = pd.DataFrame(list, columns=('호텔명', '가격', '평점'))

# df.to_csv('day06/hotel.csv', encoding='utf-8-sig', mode='w', index=True)




