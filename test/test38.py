#!user/bin/python
# encoding:utf-8
import datetime


def get_between_days(startdate, endint):
    """获取时间差
    @param startdate: date对象开始时间
    @param endint: int对象20160907结束时间,系统时间作为刷新"""
    endint = str(endint) + " " + "05:00"
    enddate = datetime.datetime.strptime(endint, '%Y%m%d %H:%M')
    return (startdate-enddate).days


print get_between_days(datetime.datetime.now(), 20161123)
