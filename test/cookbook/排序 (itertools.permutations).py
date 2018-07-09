#!/usr/bin/python
# coding: UTF-8
import itertools

for p in itertools.permutations([1, 2, 3, 4]):
    # print p
    print ''.join(str(x) for x in p)