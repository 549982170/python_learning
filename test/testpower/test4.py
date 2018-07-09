#!/usr/bin/python
# coding: UTF-8
a = u"x"
print a.isalpha()  # 是否为字母
print a.isdigit()
print a.startswith(('x', 'yz'))
print a.endswith(('x', 'yz'))
def startswith(Str, startTuple):
    """是否为startTuple字母开头"""
    return Str.startswith(startTuple)

startTuple = ("x", "y")
print startswith(a, startTuple)