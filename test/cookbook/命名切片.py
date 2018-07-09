#!/usr/bin/python
# coding: UTF-8
a = [0, 1, 2, 3, 4, 5]
# 内置函数slice(stop) slice(start, stop[, step])
LASTTHREE = slice(-3, None)
print LASTTHREE
print a[LASTTHREE]
