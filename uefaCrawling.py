from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import re

path = "C:/util/chromedriver.exe"
driver = wd.Chrome(path)
driver.get('https://sports.news.naver.com/wfootball/index') # 가져올 URL주소

# 기록/순위
record = driver.find_element(By.XPATH, '//*[@id="_sports_lnb_menu"]/div/ul[1]/li[5]/ul/li[5]/a')
record.click()
time.sleep(4)

# 시즌 선택
seasonList = driver.find_element(By.XPATH, '//*[@id="_currentYearButton"]/em')
seasonList.click()
inputSeason = input('선택할 시즌(09-10 ~ 22-23): ')
select = int(inputSeason[3:5])

count = len(driver.find_elements(By.CSS_SELECTOR, '#_yearList > li'))+1
seasonNum = int(re.sub(r'[^0-9]', '', driver.find_element(By.CSS_SELECTOR, '#content > div.record_sub_title.with_combo_box > h4 > span').text)[4:6])+1
list = []

for i in range(1, count):
    season = driver.find_element(By.CSS_SELECTOR, '#_yearList > li:nth-child(%d) > button' %i) #1~14
    seasonNum-=1
    if seasonNum == select:
        season.click()

# 리그별 데이터 출력
for i in range(1, 6):
    league = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/ul/li[%d]/a' %i)
    league.click()
    time.sleep(0.3)

    team_info = driver.find_elements(By.CSS_SELECTOR, '#wfootballTeamRecordBody > table > tbody > tr')
    leagues = driver.find_element(By.CSS_SELECTOR, '#content > div.record_tab > ul > li.selected > a > span > span.title').text
    print(leagues, ':')
    time.sleep(0.3)

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

# 데이터 저장
df = pd.DataFrame(list, columns=('순위', '팀', '승점', '승', '무', '패', 'UCL'))

df.to_csv('result.csv', encoding='utf-8-sig', mode='w', index=False)

# 데이터 시각화
read = pd.read_csv('result.csv')

font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

top = read[read['순위'] <= 6]

ax = top['승점'].plot(kind='barh', figsize=(10,30), legend=True, fontsize=14)
ax.set_yticklabels(top['팀'], fontsize=8)
plt.show()



