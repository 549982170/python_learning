# -*- coding: utf-8 -*-
# !/usr/bin/python
a = 2


def formatDigit(num, digit=0):
    """字符串格式化位数"""
    if isinstance(num, int):
        return ("%0" + str(digit) + "d") % num
    return None

我 = "11"
print 我

print formatDigit(a)
