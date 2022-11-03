import pandas as pd

# survey.csv 읽어서 위에서 5개 출력

df_read = pd.read_csv('day03/survey.csv', encoding='utf-8')
print(df_read[:5])
print(df_read.head())
# 평균
print(df_read.mean())
# 수입의 평균
print(df_read.income.mean())
# 수입의 평균(반올림해서 소수점 1자리)
print(round(df_read.income.mean(), 1))
print(df_read.income.sum())
#수입의 중앙값
print(df_read.income.median())
print(df_read.income.describe())
print(df_read.sex.value_counts())