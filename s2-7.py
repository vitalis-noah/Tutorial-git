
# s2-7: JSONファイルを扱う:jsonモジュール
#    https://docs.python.jp/3/library/json.html

print('◆テキスト変換')
import json
data = {'Pen':'001','Apple':'002','Pineapple':'003'}

j = json.dumps(data,indent=4)
print(j)

print('\n◆すこし複雑')
data2 = ['abc',1,True,None,{'Pen':'001'}]
j2 = json.dumps(data2,indent=4)
print(j2)

print('\n◆ファイル出力')
data3 = ['PAP',{'Pen':'001','Apple':'002','Pineapple':'003'}]
with open('pap.json',mode='w') as jsonfile:
    json.dump(data3,jsonfile,indent=4)

print('\n◆ファイル入力')
with open('pap.json',mode='r') as jsonfile:
    fdata = json.load(jsonfile)
print(fdata)

