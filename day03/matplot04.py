import matplotlib.pyplot as plt
import pandas as pd

# color = ['b', 'orange', 'green', 'red', 'purple', 'brown']
# xLabel = ['first', 'second', 'third', 'fourth']
 
df = pd.DataFrame([
    [500, 450, 520, 610],
    [690, 700, 820, 900],
    [1100, 1030, 1200, 1380],
    [1500, 1650, 1700, 1850],
    [1990, 2020, 2300, 2420],
    [1020, 1600, 2200, 2550]
], index=['2015', '2016', '2017', '2018', '2019', '2020'], columns=['first', 'second', 'third', 'fourth'])

plt.xlabel('Quarters')
plt.ylabel('sales')
plt.title('2015~2020 Quarterly sales')
# plt.legend(['2015', '2016', '2017', '2018', '2019', '2020'])
df = df.transpose()
df.plot()
plt.show()

# print(df[2:3])