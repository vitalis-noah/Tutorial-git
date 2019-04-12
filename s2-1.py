# Part2 標準ライブラリ

print("◆1 日付と時間:datetimeモジュール")
from datetime import date
sample_today = date.today()
print(sample_today)

sample_date = date(2016, 11, 1)
print(sample_date.year)
print(sample_date.weekday())

print(sample_date.strftime('%Y/%m/%d'))
print(sample_date.strftime('%y/%m/%d'))

#ドキュメントファイルのサンプルより
print(sample_today.strftime("%A %d. %B %Y"))
print('The {1} is {0:%d}, the {2} is {0:%B}.'.format(sample_today, "day", "month"))

from datetime import time
sample_time = time(12, 35, 11)
print(sample_time)
print(sample_time.minute)

#datetimeオブジェクト(p.015)
from datetime import datetime
sample_datetime = datetime.today()
print(sample_datetime)
print(sample_datetime.date())
print(sample_datetime.time())
print(sample_datetime.strftime('%H:%M:%S'))

#timedeltaオブジェクト(p.015)
from datetime import timedelta
sample_date = date(2016,11,1)
sample_timedelta = timedelta(days = 5)
later = sample_date + sample_timedelta
print(later)

new_year = date(2017, 1, 1)
days = new_year - sample_date
print(days)

#メモ
mvtitle = ("マッキントッシュの男","暴力脱獄")
for i in mvtitle:
  print(i)

