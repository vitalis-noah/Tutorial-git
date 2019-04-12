# s2-8:オブジェクトの直列化：pickleモジュール
#    https://docs.python.jp/3/library/pickle.html

print('◆オブジェクトの保存')
import pickle
serialize_data = {'Pen':'001','Apple':'002','Pineapple':'003'}
with open('pickle_test.dump','wb') as f:
#   pickle.dump(data, f) ※誤植:data→serialize_data
    pickle.dump(serialize_data, f)
print('>>> pickle_test.dump に出力しました.')    
#exit()

print('\n◆オブジェクトの復元')
import pickle
with open('pickle_test.dump','rb') as f:
    deserialize_data = pickle.load(f)

print(deserialize_data)
