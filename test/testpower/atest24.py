# !/usr/bin/python
# -*- coding: utf-8 -*-
# x = 4.20
# y = 2.10
# print x+y
# print (x+y) == 6.3
from decimal import Decimal
from decimal import getcontext


def floatAdd(num1, num2, precision=2):
    """高精度相加"""
    getcontext().prec = precision  # 设置精度
    return float(Decimal(str(num1)) + Decimal(str(num2)))


print floatAdd(1.111, 5.4, 4)


new_item = {'val': 1.4}
print new_item['val']
print new_item