import usecsv, re, csv

# apt_201910.csv 파일에서 출력

ap = usecsv.opencsv('day03/apt_201910.csv')
apt = usecsv.switchcsv(ap)

# print(ap[:3])
# # apt_201910.csv 총개수
# print(len(apt))
# print(apt)

# # 시군구 단지명 가격 ==> 6개 출력
# a = [[]]
# for i in apt[:6]:
#     print(i[0], i[4], i[-4])
#     a.append([i[0], i[4], i[-4]])
# print(a)


# 강원도에 120 m3 이상 3억 이하 검색하기 시군구 단지명 가격 출력
list=[['시군구', '단지명', '가격']]
for i in apt:
    try:
        if i[5] >= 120 and i[-4] <= 30000 and re.match('강원', i[0]):
            list.append([i[0], i[4], i[-4]])
    except:
        pass
print(list)

#파일로 출력
# with open('apt11.csv', 'w', newline='') as f:
#     a = csv.writer(f, delimiter=',')
#     a.writerows(list)

# 첫번째 행에 컴퓨터, 노트북, 태블릿
# 두번째 행에 100, 80, 60
# 리스트 형태로 표현

