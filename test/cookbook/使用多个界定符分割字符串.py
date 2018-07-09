#!/usr/bin/python
# coding: UTF-8
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
# print re.split(r'[;,\s]\s*', line)

fields = re.split(r'(;|,|\s)\s*', line)
# print fields

# 列表值相加
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]
c = [v + d for v, d in zip(list1, list2)]
# print c
