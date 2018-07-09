# encoding:utf-8
# usr/bin/python
from functools import partial
import math


def spam(a, b, c, d):
    return a, b, c, d


s1 = partial(spam, 1)  # a = 1
print s1(2, 3, 4)

print s1(4, 5, 6)

s2 = partial(spam, d=42)  # d = 42

print s2(1, 2, 3)

print s2(4, 5, 5)

s3 = partial(spam, 1, 2, d=42)  # a = 1, b = 2, d = 42

print s3(3)

print s3(4)

points = [(1, 2), (3, 4), (5, 6), (7, 8)]


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

pt = (4, 3)
points.sort(key=partial(distance,pt))
print points