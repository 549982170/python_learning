#!/usr/bin/python
# coding: UTF-8
g = (x ** 2 for x in xrange(10))
print next(g)
print next(g)
print next(g)
print next(g)
print sum(x ** 3 for x in xrange(10))
print sum(x ** 3 for x in xrange(10) if x % 3 == 1)