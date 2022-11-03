from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import pandas as pd

path = "C:\\util\\chromedriver.exe"
driver = wd.Chrome(path)
time.sleep(1)
driver.get('https://sports.news.naver.com/wfootball/index')

record = driver.find_element(By.XPATH, '//*[@id="_sports_lnb_menu"]/div/ul[1]/li[5]/ul/li[5]/a')
record.click()

time.sleep(2)

list = []

for i in range(1, 6):
    league = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/ul/li[%d]/a' %i)
    league.click()
    time.sleep(1)

    team_info = driver.find_elements(By.CSS_SELECTOR, '#wfootballTeamRecordBody > table > tbody > tr')
    leagues = driver.find_element(By.CSS_SELECTOR, '#content > div.record_tab > ul > li.selected > a > span > span.title').text
    print(leagues, ':')
    time.sleep(1)

    for i in team_info:
        try:
            rank = i.find_element(By.TAG_NAME, 'strong').text
            team = i.find_element(By.CLASS_NAME, 'name').text
            score = i.find_element(By.CSS_SELECTOR, 'td.selected > div > span').text
            win = i.find_element(By.CSS_SELECTOR, 'td:nth-child(5) > div > span').text
            tie = i.find_element(By.CSS_SELECTOR, 'td:nth-child(6) > div > span').text
            defeat = i.find_element(By.CSS_SELECTOR, 'td:nth-child(7) > div > span').text
            champs = i.find_element(By.CSS_SELECTOR, 'td > div > span').text
            
            list.append([rank, team, score, win, tie, defeat, champs])
            print('순위: '+rank, '팀: '+team, '승점: '+score, '승: '+win, '무: '+tie, '패: '+defeat, champs, sep=' | ')
            print('-'*100)
        except:
            continue
print(list)

df = pd.DataFrame(list, columns=('순위', '팀', '승점', '승', '무', '패', 'UCL'))

df.to_csv('day06/uefa.csv', encoding='utf-8-sig', mode='w', index=False)




