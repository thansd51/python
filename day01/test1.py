# print("asd")

# a = 0
# print(a)
# print(type(a))
# b = 'hello'
# print(b)
# print(type(b))
# c = "'asdfzzxc'"
# print(c)
# d = "\'as\'"
# print(d)
# print(b+d)
# print(2*3)
# print("2"*3)

# b[1] = "C"
# print(b[0])
# print(b[-1])

# print(b[0:5:2])
# print(b.find("h"))
# find : 없으면 -1
# print(b.index("l"))
# index : 없으면 오류

# bb=','
# print(bb.join("ABCD"))
# cc="a"
# print(cc.join("ABCD"))
# print(b.upper())
# D="ASD"
# print(D.lower())

# dd="           py       "
# print(dd.lstrip())
# print(dd.rstrip())
# print(dd.strip())

# aa = "Now is aa bb cc"
# print(aa.split())

# #리스트(list)
# l = list()
# print(1, type(l))

# lst = [1, 2, 3]
# print(type(lst))

# 리스트 l2 ==> 1부터 11까지로 이루어진 리스트 l2 생성
# l2 = list()
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# # print(l2[0])
# print(lst)
# print(len(lst))
# # l2의 마지막 값 출력
# print(lst[len(lst)-1]) # l2에서 마지막 원소(L2의 길이 -1)
# # L2의 첫번째 값을 99로 수정
# lst[0] = 99
# print(lst)
# lst[1] = [1, 2, 3]
# print(lst)
print(len(lst))
# lst[2] = '문자'
# print(lst)

# lst.append(999)
# print(lst)
# lst.remove(5)
# print(lst)

# # 1, 2, 3 이루어진 a1 리스트 생성
# a1 = [1, 2, 3]
# # 'life', 'is', 'to', 'short' 이루어진 b1 리스트 생성
# # bb1 = "life is to short"
# # print(bb1.split())
# b1 = ['life', 'is', 'to', 'short']
# # 1, 2, 'life', 'is' 이루어진 c1 리스트 생성
# c1 = [1, 2, 'life', 'is']
# # 1, 2, (3, 4), ('life', 'is') 이루어진 d1 리스트 생성
# d1 = [1, 2, [3, 4], ['life', 'is']]

# # d1의 첫번째 값 출력
# print(d1)

# print(d1[0])
# print(d1[3][0])
# print(d1[0:3])
# d1.insert(2, "aa")
# d1.append('dd')
# print(d1)
# print(len(d1))
# d1.pop()
# print(d1)

# a2 = [2, 1, 0, 2, 3, 2, 4, 2]
# print(a2.count(2))

# 튜플(tuple)
t = tuple()
print(t, type(t))
t1 = (1, 2, 3)
print(t1, type(t1))
print(t1[0], t1[0:2])
print(t1 + t1)
t4 = (1, 2, (3, 4), ('life', 'is'))
print(t4)

#dict
d = dict()
print(d, type(d))
d1 = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
print(d1, type(d1))
print(d1)
#print(d1['d']) 오류 발생 키 값에 d 없음
d1['c'] = 33
print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())

print(type(d1.keys()))
print(type(d1.values()))
print(type(d1.items()))

print("type list", type(list(d1.keys())))
print(list(d1.keys()))

# name은 Hong, phone은 010111122222, birth는 0814로 이루어진 dict
dict = {
    'name' : 'Hong',
    'phone' : '01011112222',
    'birth' : '0814'
}
print(dict)
# dict에 key 값이 1, value 가 'a' 추가
dict[1] = 'a'
print(dict) 
# dict에 key 값이 pet, value 가 'dog' 추가
dict['pet'] = 'dog'
print(dict)
# key가 pet의 value값 출력
print(dict['pet'])
# dict key값만 출력
print(dict.keys())
# dict.keys()를 리스트 형태로 출력
# print(list(dict.keys()))

lst = list(dict.keys())
print(lst)
del dict[1]
print(dict)
dict.clear()
print(dict)

# set - 중복을 허용 x
s1 = {1, 2, 3, 4, 4, 4, 4, 4}
print(s1, type(s1))
s2 = set([1, 2, 3, 4, 5, 4, 2, 2])
print(s2, type(s2))
print(s1 & s2)
print(s1 | s2)
print(s2.difference(s1))

# list, tuple, dict, set

