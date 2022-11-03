f=open('c:/새파일.txt', 'w')
print(f)
f.close()

f=open('c:/새파일.txt', 'w')
for i in range(1, 6):
    data = '%d번째 줄입니다. \n' %i
    f.write(data)
f.close()

f=open('c:/새파일.txt', 'a')
for i in range(6, 11):
    data = '%d번째 줄입니다. \n' %i
    f.write(data)
f.close()

f=open('c:/새파일.txt', 'r')
line = f.readline()
print(line)
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

f=open('c:/새파일.txt', 'r')
lines = f.readlines()
print(lines)
f.close()

f=open('c:/새파일.txt', 'r')
data = f.read()
print(data)
f.close()

with open('c:/새파일.txt', 'w') as f:
    f.write('aa bb cc')
#data = f.read() - with open은 f가 close된 상태
