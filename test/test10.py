#!/usr/bin/python
# coding: utf-8
# dict = {1: 2, 'a': 'b', 'hello': 'world'}
# for j, k in dict.items():
#     print j, k
import datetime, time

# c = 1465280789
#
# conv_day = datetime.datetime.utcfromtimestamp(c)
# print conv_day


now = datetime.datetime.now().date()
deltaDate = now + datetime.timedelta(days=-1)
nowdate = deltaDate
if nowdate == datetime.datetime.now().date():
    print nowdate

else:
    print "ss"