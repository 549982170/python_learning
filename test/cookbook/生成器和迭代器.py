#!/usr/bin/env python
# encoding:utf8
def gensquares(N):
    for i in range(N):
        yield i**2

for item in gensquares(5):
    print item


def gensquares2(N):
    res = []
    for i in range(N):
        res.append(i*i)
    return res

for item in gensquares2(5):
    print item
