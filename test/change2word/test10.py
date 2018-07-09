#!/usr/bin/python
# coding: UTF-8
from collections import defaultdict

a = {"1": "n", "s1": "n1", "s2": "n2"}

b = {"1": "n3"}
c = defaultdict(list)
dictMerged = dict(a, **dict(b, **c))
# print dictMerged

# print '\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)])
