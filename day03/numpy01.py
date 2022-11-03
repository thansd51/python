import numpy as np

a = np.array([[2, 3], [5, 2]])
print(a)

d = np.array([2, 3, 4, 5, 6])
print(d)

print(d.shape)
e = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(e.shape)

print(np.zeros((2, 10)))
print(np.ones((2, 10)))
print(np.arange(2, 10)) #2 이상 10 미만 원소로 구성된 1차원 배열

a = np.ones((2,3))
print(a)
b = np.transpose(a)
print(b)

arr1 = np.array(([2, 3, 4], [6, 7, 8]))
arr2 = np.array(([12, 13, 14], [26, 27, 28]))

print(arr1+arr2)

d = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6, 7], [5, 6, 7, 8, 9, 9]])
print(d)
print(type(d))
d_list = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6, 7], [5, 6, 7, 8, 9, 9]]
d_list[2] = 0
print(d_list)
d[:2]=0
print(d)

print(np.arange(10))