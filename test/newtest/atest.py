#!/usr/bin/python
# coding: UTF-8
import hashlib

def md5(ss):
    m = hashlib.md5()
    m.update(ss)
    return m.hexdigest()

a = "zengweiji"
b = "123456"

c = a+b

print md5(c)