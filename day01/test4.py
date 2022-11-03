import re

text = "<title>지금은 문자열 연습입니다.</title>"

#1. 0~7 사이 추출
print(text[0:7])
#2. "문"이 있으면 위치값 출력
print(text.find("문"))
print(text.index("문"))
#3. "파" 있으면 위치값 출력 없으면 -1 출력
print(text.find("파"))
#4. 없으면 오류
# print(text.index("파"))

text1 = "<title>지금은 문자열 연습입니다.</title>"
text2 = ";"
#1. text1 공백제거하고 text2 연결
print(text1.strip()+text2)
#2. text1 왼쪽공백제거하고 text2 연결
print(text1.lstrip()+text2)
#3. text1 오른쪽공백제거하고 text2 연결
print(text1.rstrip()+text2)
#4. text1 <title>을 <div>로 바꾸기
print(text1.replace("title", "div"))

text3 = ('111<head>안녕하세요</head>22')
body = re.search('<head.*/head>', text3)
print(body)
body = body.group()
print(body)

# [0-9], [a-z]
# ab*c : abc, abbc, abbbc
# *(0이상), +(1이상), ?(0이상 1이하)
print("--------------------------")
text4 = ("<head>안녕하세요...<title>지금은 문자열 연습입니다.</title></head>")
# search 사용 : <title>지금은 문자열 연습입니다.</title>
body = re.search("<t.*e>", text4)
print(body.group())

body = re.sub('<.*?>', '', text4)
print(body)