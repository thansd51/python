# def seperate():
#     a = int(input('수 입력'))
#     if a%2 == 0:
#         print("짝수")
#     else:
#         print("홀수")

# seperate()




def addResult(a, b):
    return a+b
# seperate()
print(addResult(3, 5))
ret = addResult(10, 20)
print(ret)


def sum(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum
print(sum(10)) # 1부터 10까지의 합 출력

nums = [1, 1, 1, 2, 2, 3, 2, 3, 2, 3, 3, 3, 1]

# print(nums.count(1))
# print(nums.count(2))
# print(nums.count(3))

set = set(nums)

d1 = {
    'a' : nums.count(1),
    'b' : nums.count(2),
    'c' : nums.count(3)
}


# def max_count(nums):
#     max_count = {}
#     for i in nums:
#         max_count[i] = nums.count(i)
#     return max_count

def max_count(nums):
    counts = {}
    for i in nums:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

counts = max_count(nums)
print(counts) #{1: 4, 2: 4, 3: 5}
print(max(counts.values()))

first = []
maxValue = max(counts.values())
for name, count in counts.items():
    print(name, ":", count)
    if(count == maxValue):
        first.append(count)
print("first : ", first)
# print(counts.items())






# dict = {1: 4, 2: 4, 3: 5}
# print(dict)
# if 1 in dict:
#     print('있음')
# else:
#     print('없음')