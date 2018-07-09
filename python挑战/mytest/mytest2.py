# encoding:utf-8
# usr/bin/python

def spam(a, b=[]):
    print(b)
    return b


x = spam(1)
print x
x.append(99)
x.append('Yow!')
print x
print spam(1)
