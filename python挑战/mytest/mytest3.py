# encoding:utf-8
# usr/bin/python

def f(x, y):
    return x + y


count_list = range(101)
print reduce(f, count_list)

print reduce(f, count_list, 10)

print reduce(lambda x, y: x + y, count_list)
