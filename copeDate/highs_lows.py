# -*- coding: utf8 -*-


import  csv

from pylab import *
from datetime import datetime
from matplotlib import pyplot as plt


mpl.rcParams['font.sans-serif'] = ['SimHei']




# 从文件中获取日期和最高气温
filename = "600410.SH.CSV"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows= [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[2],"%Y-%m-%d")
        dates.append(current_date)

        high = float(row[5])
        highs.append(high)

        low = float(row[6])
        lows.append(low)

    # print(highs)




# 根据数据绘制图形
fig =plt.figure(dpi=300, figsize=(80, 60))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='green')


# 设置图形的格式
plt.title("600410 日均最高、最低价走势图")

plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("价格（元）", fontsize = 16)
plt.tick_params(axis='both', which ='major', labelsize = 16)

# plt.savefig('600410.pdf')
plt.show()

