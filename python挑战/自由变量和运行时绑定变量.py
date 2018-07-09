# encoding:utf-8
# usr/bin/python
x = 10
a = lambda y, x=x: x + y

x = 20
b = lambda y, x=x: x + y

print a(10)
print b(10)

j = 10


def c(k, j=j):
    return k + j


j = 20


def d(k, j=j):
    return k + j


print c(10)
print d(10)

funcs = [lambda x, n=n: x + n for n in range(5)]
for f in funcs:
    print(f(0))
