#!user/bin/python
# encoding:utf-8
value = '哈哈脚本12'
def getByteLength(Str):
    Str = Str.decode("utf8")
    length = len(Str)
    utf8_length = len(Str.encode('utf-8'))
    length = (utf8_length - length) / 2 + length
    return length
print getByteLength(value)
