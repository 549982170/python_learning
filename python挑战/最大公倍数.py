# coding:utf-8
# !/user/bin/python
a = 3
b = 5


def test(a, b):
    num = a * b
    for ca in range(2, num + 1):
        if ca % a == 0 and ca % b == 0:
            return ca


print test(a, b)
