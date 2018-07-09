#!user/bin/python
# encoding:utf-8
from  functools import partial


def spam(a, b, c, d):
    print a, b, c, d


s1 = partial(spam, 1)
s2 = partial(spam, d=42)

s1(2, 3, 4)
s2(1, 2, 3)
