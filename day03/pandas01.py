import pandas as pd
import re

df = pd.read_csv('day03/apt_201910.csv', encoding='cp949', thousands=',')
# print(len(df))
# print(df.shape)
# print(df.head())
# print(df.tail())

# # 면적이 200보다 큰 거 출력
# print(df.면적>130)
print(df[df.면적> 200])
print(df.단지명)        

# 면적이 130 넘고 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적 > 130) & (df.가격 < 20000)])

# 면적이 130 넘거나 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적 > 130) | (df.가격 < 20000)])

# 단지명(아파트)과 가격만 10번째까지 출력
# df.loc[행조건, 열의 조건]
print(df.loc[:10, ['단지명', '가격']])

# 면적이 130 이상인 단지명, 가격, 면적 출력
print(df.loc[:, ['단지명', '가격', '면적']][df.면적 > 130])

# 9억원을 초과하는 가격으로 거래된 단지명(아파트)의 가격만 출력
print(df.가격[df.가격 > 90000])

# 9억원을 초과하는 가격으로 거래된 단지명(아파트), 가격만 출력
print(df.loc[:, ['단지명', '가격']][df.가격 > 90000])

dfAsc = df.sort_values(by='가격', ascending=False)
print(dfAsc.가격)
print('-'*20)

# 단가 = 가격 / 면적
# df.단가 df['단가']은 같지만 없는 컬럼을 생성할 때는 df['단가']만 가능
df['단가'] = df.가격 / df.면적
# 시군구, 면적, 단가 를 10개 출력
print(df.loc[:10, ['시군구', '면적', '단가']])
print(df.loc[:10, ('시군구', '면적', '단가')])

# 시군구(지역)에 강릉이 들어간 자료만 출력
# print(re.match('강릉', df[df.시군구]))
print(df[df.시군구.str.find('강릉') > -1])
local_are = df[df.시군구.str.find('강릉') > -1]
print(local_are)
# print(df[df.시군구])

# 강릉이 들어간 시군구, 가격, 단가 출력
print(local_are.loc[:10, ['시군구', '가격', '단가']])




