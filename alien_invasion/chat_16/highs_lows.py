import csv
from matplotlib import pyplot as  plt
from datetime import datetime

filname = 'death_valley_2014.csv'
with open(filname, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 获取最高气温
    highs = []
    # 获取最低气温
    lows = []
    # 获取日期
    dates = []
    for row in reader:
        try:
            highs.append(int(row[1]))
            dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
            lows.append(int(row[3]))
        except ValueError:
            pass
        else:
            highs.append(int(row[1]))
            dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
            lows.append(int(row[3]))

print(len(dates))
print(highs)  # 绘制气温表
fig = plt.figure(dpi=128, figsize=(10, 6))
fig.autofmt_xdate()
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
# 设置图形的格式
plt.show()
