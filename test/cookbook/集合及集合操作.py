#!/usr/bin/python
# coding: UTF-8
A = {1, 2, 3, 3}
print u'并集A', A
B = {3, 4, 5, 6, 7}
print u'并集B', B
print u'并集', A | B  # 并集
print u'交集', A & B  # 交集
print u'求差集', A - B  # 求差集
print u'求差集', B - A  # 求差集
print u'对称差集', A ^ B  # 对称差集
