#!user/bin/python
# encoding:utf-8


def fact(n):  # 递归,会栈溢出
    if n == 1:
        return 1
    return n * fact(n - 1)


# print fact(100)


def fact(n):  # 尾递归,一个栈不溢出
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print fact_iter(5, 1)

print fact(100)
