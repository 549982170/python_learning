#!user/bin/python
# encoding:utf-8
import json

x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
# print a(10), b(10)

# x = 10
# c = lambda y, x=x: x + y
# x = 20
# d = lambda y, x=x: x + y
#
# print a(10), b(10)

funcs = [lambda x, n=n: x + n for n in range(5)]
for f in funcs:
    print f(0)

# print funcs
