#!/usr/bin/python
# coding: UTF,8
import datetime


def test(t):

    d ="%02d-%02d-%02d %02d:%02d:%02d" % (int(t["year"]), int(t["month"]), int(t["day"]), int(t["hour"]), int(t["minute"]), int(t["second"]))
    return d


t = {'year': '2013', 'month': '9', 'day': '30', 'hour': '16', 'minute': '45', 'second': '2'}
print test(t)
