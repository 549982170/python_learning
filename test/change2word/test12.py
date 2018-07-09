#!/usr/bin/python
# coding: UTF-8
import datetime


def test(st, et):
    t1 = datetime.datetime.strptime(st, "%H:%M:%S")
    t2 = datetime.datetime.strptime(et, "%H:%M:%S")
    return int((t2 - t1).total_seconds())


st = "00:00:00"
et = "00:00:10"
print test(st, et)
