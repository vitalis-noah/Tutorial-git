# s2-9: SQLiteデータベースを使う: sqlite3モジュール
#     https://docs.python.jp/3/library/sqlite3.html

#[Pythonの型: SQLiteの型]
#     bytes : BLOB
#     int   : INTEGER
#     float : REAL
#     str   : TEXT
#     None  : NULL

import sqlite3

#DBファイル作成・接続
con =sqlite3.connect('physique.db', isolation_level=None)
#cursorオブジェクト取得
c = con.cursor()

#スキーマ生成
c.execute("create table personal(id text, name text, \
        height integer, weight real)")

#データ追加
c.execute("insert into personal values( \
        '001','Yamada Taro',173,62.5)")
c.execute("insert into personal values( \
        '002','Tanaka Hanako',163,53.1)")
c.execute("insert into personal values( \
        '003','Suzuki Saburo',180,75.8)")

#データ表示
for row in c.execute("Select * from personal"):
    print(row)

#DB切断
con.close()
