
#s2-3 データ圧縮 zlib / gzip (p.016)
#    https://docs.python.jp/3/library/archiving.html

#zlib
print('① zlib')
sample_data = b'a' * 100000
print(len(sample_data))

import zlib
compress_data = zlib.compress(sample_data)
print(len(compress_data))
print(sample_data == compress_data)

decompress_data = zlib.decompress(compress_data)
print(len(decompress_data))
print(sample_data == decompress_data)

#gzip
print('② gzip')
import gzip
sample_data = b'a' * 100000
with gzip.open('cfile.gz', 'wb') as f:
    f.write(sample_data)

with gzip.open('cfile.gz', 'rb') as f:
    cfile_data = f.read()

print(sample_data == cfile_data)
