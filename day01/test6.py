import codecs
import re

f = codecs.open('friends101.txt', 'r', 'utf-8')
script101 = f.read()
print(script101[:100])

lines = re.findall(r'Monica:.+',script101)
print(lines[:3])
print(type(lines))

# script101 에서 All:
all = re.findall(r"All.+", script101)
print(all[:5])

# All 에서 마지막 출력
print(all[-1])
print(len(all))

char = re.compile(r"[A-Z][a-z]+:")

names = re.findall(char, script101)
print(names)
print(len(names))

set = set(names)
print(set)
print(len(set))

# 등장인물 이름이 7자 이상인 사람 출력
for i in set:
    if len(i) > 7:
        print(i)

character = list(set)
print(character)
print("--------------------------------")
# character에서 : 제거해서 출력

character_list =[]
for i in character:
    ch = re.sub(":","", i)
    print(ch, end=' ')
print(ch)

print("--------------------------------")

for i in character:
    character_list += [i[:-1]]
print(character_list)

print("--------------------------------")

for i in character:
    character_list.append(re.sub(":","", i))
print(character_list)

ch = 'Scene:'
ch = re.sub(':', '', ch)
print(ch)

a = '제 이메일 주소는 greate@naver.com'
a+= ' 오늘은 today@naver.com 내일은 apple@gmail.com life@abc.co.kr 라는 메일을 사용합니다.'
print(a)

char = re.compile(r"[a-z]*@[a-z.]*")
names = re.findall(char, a)
print(names)

words = ['apple', 'cat', 'brave', 'drama', 'asise', 'blow', 'coat', 'above']

list = []
for i in words:
    list += re.findall(r'[a][a-z]+', i)
print(list)

for i in words:
    m = re.search(r'[a][a-z]+', i) # search는 찾고자 하는 단어가 중간에 있어도 찾음
    if m:
        print(m.group())
print("------------------------------")
for i in words:
    # m = re.match(r'[a][a-z]+', i) # match는 찾고자 하는 단어가 처음에 있어야 찾음
    m = re.match(r'a\D+', i) # \d(숫자) \D(숫자가 아닌)
    if m:
        print(m.group())

exam1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2022년입니다.'

print(re.findall(r'\d.+년', exam1)) # ['91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2022년']
print(re.findall(r'\d.+?년', exam1)) # ['91년', '97년', '2022년'] > .+? 에서 ?(0이상 1이하)로 '년' 출력
print(re.findall(r'\d+.년', exam1)) # ['91년', '97년', '2022년']
print(re.findall(r'\d+년', exam1))