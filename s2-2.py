
# s2-2 カレンダー:calendarモジュール (p.016)

# memo:ファイル名や変数に、予約語は使わないこと
import calendar
sample_calendar = \
    calendar.TextCalendar(calendar.SUNDAY)
print(sample_calendar.prmonth(2016,11,2,2))


# 指定月の１日の曜日と、月の日数
from datetime import datetime
sample_datetime = datetime.today()
print(sample_datetime)
range = calendar.monthrange( \
    sample_datetime.year, sample_datetime.month)
print(range)


# うるう年判定
print(calendar.isleap(2016))
print(calendar.isleap(2017))
print(calendar.isleap(datetime.today().year))

#今月のカレンダー
from datetime import date
#print(date.today())
print(sample_calendar.prmonth(date.today().year, \
                              date.today().month, \
                              2, 2))
# format文を使い、短い文章化すること、失敗。理由不明.
#print(sample_calendar.prmonth('{0:%Y},{0:%m},2,2'.format(date.today())))
#print(sample_calendar.prmonth(2019,2,2,2))
#print('{0:%Y},{0:%m},2,2'.format(date.today()))
#print(sample_calendar.prmonth('{0:%Y},{0:%m},2,2'.format(date.today())))                             

