#!user/bin/python
# encoding:utf-8

d = {'a': 7, 'c': 4, 'b': 3, 'd': 4, 'f': 6, 'e': 1}
result = []
keys = sorted(d, key=lambda k: d[k], reverse=1)
print keys
