#!/usr/bin/python
# coding: utf-8
import sys
import datetime

# a = (('10', '11'),)
# print '10' in a[0]

a = '2016-06-18 20:00:00'
b = '2016-06-14 15:39:27'
c = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
d = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')
# print (c-d).total_seconds()
