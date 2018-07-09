#!user/bin/python
# encoding:utf-8
import datetime
from time import gmtime



def countage(dateStr):
    dateObj = datetime.datetime.strptime(dateStr, "%Y-%m-%d %H:%M:%S")
    d = dateObj.day
    m = dateObj.month
    y = dateObj.year
    a = gmtime()
    # difference in day
    dd = a[2] - d
    # difference in month
    dm = a[1] - m
    # difference in year
    dy = a[0] - y
    # checks if difference in day is negative
    if dd < 0:
        dd = dd + 30
        dm = dm - 1
        # checks if difference in month is negative when difference in day is also negative
        if dm < 0:
            dm = dm + 12
            dy = dy - 1
    # checks if difference in month is negative when difference in day is positive
    if dm < 0:
        dm = dm + 12
        dy = dy - 1
    return dy


countage("2016-07-5 10:15:07")
