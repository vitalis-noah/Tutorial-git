
# s2-6 csvファイルを扱う: csvモジュール (p.020)
#    https://docs.python.jp/3/library/csv.html

# csvファイルを読み込む
import csv
with open('test.csv',encoding='utf-8', newline='') as csvfile:
    reader_test = csv.reader(csvfile)
    for row in reader_test:
        print(row)

# csvファイルに追加する
data = ['0004','山田次郎','03-333-3333','jiro@ddd.co.jp']
with open('test.csv','a', encoding='utf-8', newline='') as csvfile:
    writer_test = csv.writer(csvfile)
    writer_test.writerow(data)

# 辞書を使った読込
with open('test.csv',encoding='utf-8', newline='') as csvfile:
    dict_test = csv.DictReader(csvfile)
    for row in dict_test:
        print(row)



