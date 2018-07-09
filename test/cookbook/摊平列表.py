#!/usr/bin/python
# coding: UTF-8
import itertools

a = [[1, 2], [3, 4], [5, 6]]
print list(itertools.chain.from_iterable(a))
print sum(a, [])
print [x for l in a for x in l]
a = [1, 2, [3, 4], [[5, 6], [7], [8]]]
flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
print flatten(a)
