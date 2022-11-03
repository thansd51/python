import pymysql
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib


dbURL="127.0.0.1"
dbPort=3306
dbUser = "root"
dbPass = "1234"
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass, db='bigdb', charset='utf8', use_unicode=True, 
cursorclass=pymysql.cursors.DictCursor) # 컬럼명 불러오기

# 부산의 날씨
select_data = "select * from forecast where city='부산' order by tmef desc"
cur = conn.cursor()
cur.execute(select_data)
result = cur.fetchall()

df = pd.DataFrame(result)
print(df)

font_path = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)

# 그래프 변경
plt.plot(pd.to_numeric((df['tmn'])), label='최저기온')
plt.plot(pd.to_numeric((df['tmx'])), label='최고기온')

plt.legend()
plt.show()



