# coding:utf-8
# !/user/bin/python
a = 3
b = 5


def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        temp = a % b
        a = b
        b = temp

    return a


print gcd(a, b)
