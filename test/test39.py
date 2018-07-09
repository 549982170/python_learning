#!user/bin/python
# encoding:utf-8
import datetime


def chanceListToStr(mylist):
    """把列表转为1，2，3形式
    @param mylist：list传入的列表"""
    return ','.join([str(i) for i in mylist])

print chanceListToStr(['1',2,3])
