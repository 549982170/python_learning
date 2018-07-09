#!/usr/bin/env python
# coding:utf8


petlevel = 122
prange = [1, 10, 25, 50, 100, 150, 200, 300]
factor = [x for x in prange if x <= petlevel][-1:][0]
print factor