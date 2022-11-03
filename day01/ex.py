import pandas as pd

#1
str = '20201231Thursday'
year = str[:4]
print(year)
mmdd = str[4:8]
print(mmdd)
day = str[8:]
print(day)

#2
a = ['쓰', '레', '기', '통']
a.reverse()
print(a) #['통', '기', '레', '쓰']

#3
dic = {
    'year': 2020,
    'mm': 12,
    'dd': 31,
    'day': 'Thursday',
    'weather': 'snow' 
}
print(dic.keys())
print(dic.values())

#5
for i in range(1, 6):
    for j in range(1, i+1):
        print('*', end=' ')
    print()

#6 
def avg(*args):
    x=0
    for i in args:
        x += i

    return x/len(args)

print(avg(5, 3, 12, 9))
print(avg(2.4, 3.2, 7.3))
print(avg(10, 5))

#7
df = pd.DataFrame([
    [500, 450, 520, 610],
    [690, 700, 820, 900],
    [1100, 1030, 1200, 1380],
    [1500, 1650, 1700, 1850],
    [1990, 2020, 2300, 2420],
    [1020, 1600, 2200, 2550]
], index=['2015', '2016', '2017', '2018', '2019', '2020'], columns=['1분기', '2분기', '3분기', '4분기'])
print(df)

df.to_csv('c:/test/df.csv', header='False')