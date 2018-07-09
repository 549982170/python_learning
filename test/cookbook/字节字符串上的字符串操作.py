#!/usr/bin/python
# coding: UTF-8
data = b'Hello World'
print data[0:5]
print data.startswith(b'Hello')
print data.split()
print data.replace(b'Hello', b'Hello Cruel')

# 字节数组
data = bytearray(b'Hello World')
print data[0:5]
print data.startswith(b'Hello')
print data.split()
print data.replace(b'Hello', b'Hello Cruel')
