#!/usr/bin/env python
# encoding:utf8
t = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 1, 2, 1, 6, 6, 6, 6, 6, 6, 6, 6]
d = {}
for i in set(t):
    d[i] = t.count(i)
t = sorted(d.iteritems(), key=lambda x: x[1], reverse=True)
print t