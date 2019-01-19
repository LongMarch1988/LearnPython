import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # for index ,col in enumerate(header_row):
    # print(index,col)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            curent_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(curent_date, '缺少数据')
        else:
            dates.append(curent_date)
            highs.append(high)
            lows.append(low)
# print(highs)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title("2014年最高/最低气温", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temp', fontsize=17)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
