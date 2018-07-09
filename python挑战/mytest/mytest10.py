# encoding:utf-8
# usr/bin/python
import hashlib


def md5(ss):
    m = hashlib.md5()
    m.update(ss)
    return m.hexdigest()

ss = "yihai" + "soovii123"
print md5(ss)
