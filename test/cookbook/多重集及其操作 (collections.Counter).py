#!/usr/bin/python
# coding: UTF-8
import collections

A = collections.Counter([1, 2, 2])
B = collections.Counter([2, 2, 3])
print 'A:', A
print 'B:', B
print 'A | B:', A | B
print 'A & B:', A & B
print 'A + B:', A + B
print 'A - B:', A - B
print 'B - A', B - A

