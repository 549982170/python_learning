#!/usr/bin/python
# coding: UTF-8
from itertools import islice


def n_grams(a, n):
    z = (islice(a, i, None) for i in range(n))
    return zip(*z)


a = [1, 2, 3, 4, 5, 6]
print n_grams(a, 3)
print n_grams(a, 2)
print n_grams(a, 4)
