import pandas as pd
import csv
import re

from sympy import li

# popSeoul = pd.read_csv('c:/test/popSeoul.csv', encoding='utf-8')
# print(popSeoul)

f= open('c:/test/popSeoul.csv', 'r')
reader = csv.reader(f)
# print(reader)
list =[]

# for i in reader:
#     list.append(i)
# print(list)

# 숫자만 읽어와서 ,를 제거하고 float 형태로 변환하여 list 추가
# 문자 상태 그대로

for i in reader:
    temp = []
    for j in i:
        if re.search('\d', j):
            # temp.append(j) #,를 제거하고 float 형태로 변환
            temp.append(float(re.sub(",","", j)))
        else:
            temp.append(j)
    list.append(temp)
print(list) # [['Gu', 'Korean', 'Foreigner', 'Senior'], ['Total', 9740398.0, 285529.0, 1468146.0], ['Jongrogu', 151767.0, 11093.0, 27394.0]]

# '구', '한국인', '외국인', '외국인 비율(%) = 외국인/(한국인+외국인)*100' i[2]/(i[1]+i[2])*100
ko_fo = [['구', '한국인', '외국인', ' 외국인 비율(%)']]
for i in list:
    try:
        foreign = round(i[2]/(i[1]+i[2])*100, 1)
        if foreign > 5:
            ko_fo.append([i[0], i[1], i[2], foreign])
    except:
        pass
print(ko_fo)

