from selenium import webdriver as wd
from bs4 import BeautifulSoup
import pandas as pd
import re
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import matplotlib as mpl
import matplotlib.pyplot as plt

path = "C:\\util\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://www.youtube.com/c/paikscuisine/videos')

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

all_videos = soup.find_all(id='dismissible')

datas = []

# 제목, 재생시간, 조회수
for video in all_videos:
    title = video.find(id='video-title').text
    playTime = video.find('span', class_='style-scope ytd-thumbnail-overlay-time-status-renderer').text.strip()
    view = video.find('span', {'class': 'style-scope ytd-grid-video-renderer'}).text
    
    datas.append([title, playTime, view])

# print(datas)

# DataFrame 형태로 변환하여 제목, 재생시간, 조회수
# youtube.csv

df = pd.DataFrame(datas, columns=('제목', '재생시간', '조회수'))
# print(df)

# df.to_csv('youtube.csv', encoding='utf-8-sig', mode = 'w', index=True)

dict ={
		'10만' : 0,
		'50만' : 0,
		'100만' : 0
	}

# df1 = pd.read_csv('day05/youtube.csv', encoding='utf-8-sig')

# for i in df.loc[:, '조회수']:
# 	numbers = re.findall(r'\d.*\d', i)
	
# 	for num in numbers:

# 		if (float(num) >= 100):
# 			dict['100만'] += 1
# 		if (float(num) >= 50):
# 			dict['50만'] += 1
# 		if (float(num) >= 10):
# 			dict['10만'] += 1
		
# print(dict)

# 방법
dict_youtube = {
	'100만' : 0,
	'50만' : 0,
	'10만' : 0
}
for item in datas:
	item = float(str(item).split('조회수')[1].split('만회')[0].strip())
	# print(item)
	if item >= 100:
		dict_youtube['100만'] += 1
	if item >= 50:
		dict_youtube['50만'] += 1
	if item >= 10:
		dict_youtube['10만'] += 1
print(dict_youtube)

# 그래프 그리기
# 한글
font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()

mpl.rc('font', family=font_name)
figure = plt.figure()
axes = figure.add_subplot(111)
axes.pie(dict_youtube.values(), labels=dict_youtube.keys(), autopct='%.1f%%')
plt.show()




