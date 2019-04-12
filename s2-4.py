# s2-4 ハッシュ:hashlibモジュール
#     https://docs.python.jp/3/library/hashlib.html

import hashlib
hash_md5 = hashlib.md5()
hash_md5.update(b'NikkeiBP')
print(hash_md5.hexdigest())
print(hashlib.md5(b'NikkeiBP').hexdigest())

hash_sha256 = hashlib.sha256()
hash_sha256.update(b'NikkeiBP')
print(hash_sha256.hexdigest())

update_test = hashlib.sha256()
update_test.update(b'Nikkei')
update_test.update(b'BP')
print(update_test.hexdigest())

