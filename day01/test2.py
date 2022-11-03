# 조건문

a = 2
if(a==1):
    print(1)
else:
    print(2)

if(a==1):
    print(1)
elif(a==2):
    print(2)
else:
    print(3)

x = 3
y = 2
print(x==y)
print(x!=y)

money = 1300
if money >= 1200 and money < 3500:
    print("버스를 탈 수 있다.")
# else:
#     print("버스를 탈 수 없다.")
print(1 in [1, 2, 3 ])
print(x in [1, 2, 3 ])
print(x not in [1, 2, 3])
print("i" not in 'python')

if money < 10 :
    pass
else:
    print('저금')


# 반복문
for i in [1, 2, 3]:
    print(i)
    
for i in (1, 2, 3):
    print(i)

for i in "Hello":
    print(i, end=' ')
print("")
    
# test_list 라는 리스트 생성 one, two, three
# test_list의 값을 반복문을 이용해서 하나씩 출력
# one!, two!, three!
test_list = ['one', 'two', 'three']
# for i in (0, 1, 2):
#     print(test_list[i], end="!")

for i in test_list:
    print(i+"!")

number = 0
for score in [90, 25, 67, 45, 93]:
    number += 1
    if score >= 60:
        print("%d 학생은 합격입니다."%number)
    else:
        print("%d 학생은 불합격입니다."%number)

num = 5
while(num > 0):
    print(num)
    num -= 1

# while 문 이용하고
# num = 10
# 10 9 8 7 --end--
num = 10
while(num > 6):
    print(num, end=' ')
    num -= 1
    if(num==6):
        print("---end---")
# while(num > 0):
#     if(num==6):
#         print("---end---")
#         break
#     print(num, end=' ')
#     num -= 1

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i, end=' ')
print()
for i in range(10):
    print(i, end=' ')

# 100까지 수 중 7의 배수와 합계 출력
print("")
sum = 0
for i in range(101):
    if(i != 0 | i%7 == 0): 
        sum += i
        print(i, end=' ')
print("\nsum:", sum)

# * * *
# * * *
# * * *
print("")
for i in range(3):
    for j in range(3):
        print("*", end=' ')
    print()

print("#####")

i = 0
while i < 5:
    i += 1
    print("*"*i)
