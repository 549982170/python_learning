#!/usr/bin/python
# coding: UTF-8
import datetime


def test(year):
    return datetime.datetime.strptime(str(year), "%Y").day


year = 2013
# print test(year)



import calendar


def getsec(year):
    all_days = 0
    for i in range(1, 13):
        all_days = calendar.monthrange(int(year), i)[1] + all_days
    return all_days


year = "2013"
print getsec(year)
