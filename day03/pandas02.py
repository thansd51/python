import pandas as pd
#'name': 'Mark', 'Jane', 'aaa', 'rr',
# 'age' : 33, 44, 55, 11,
# 'score' : 91.2, 88.5, 55.6, 88.9
data = {
    'name': ['Mark', 'Jane', 'aaa', 'rr'],
    'age' : [33, 44, 55, 11],
    'score' : [91.2, 88.5, 55.6, 88.9]
}
#data를 데이터프레임으로 생성
df = pd.DataFrame(data)
print(df)
print(type(df))
print(df.sum())
print(df.mean())

data_dic = {
    'year' : [2018, 2019, 2020, 2021, 2022],
    'age' : [350, 400, 1050, 2000, 1000]
}
# 데이터프레임으로
df2 = pd.DataFrame(data_dic)
print(df2)

df3 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]], index=['중간고사', '기말고사'], columns=['1반', '2반', '3반'])
print(df3)

df4 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]])
df4.columns = ['A', 'B', 'C']
df4.index = [11, 22]
print(df4)

print(df3.sum())
print(df3.mean())
# 1반의 합계 출력
print(df3['1반'].sum())
print(df3['1반'].mean())

# df5를 df5.cvs 내보내기
# df3.to_csv('df3.csv', encoding='utf-8', header='False')
# df_read = pd.read_csv('df3.csv', encoding='utf-8')
# print(df_read)