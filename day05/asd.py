from  bs4 import BeautifulSoup
from matplotlib import font_manager, rc
import requests
import re
import matplotlib.pyplot as plt

res = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(res.content, 'html.parser')

ols = soup.find('ol', class_="list_movieranking")
rankcont = ols.find_all('div', class_='thumb_cont')

ratio = []
labels = []
explode = []

for i in rankcont[:10]:
    title = i.find('a', class_='link_txt').get_text()
    reser = float(re.sub(r'[%^]', '', i.find('span', {'class':'txt_num'}).get_text()))

    labels.append(title)  
    ratio.append(reser)
    explode.append(0.03)
    

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name, size=8)

   
plt.pie(ratio, labels=labels, explode=explode, autopct='%.1f%%')
plt.show()