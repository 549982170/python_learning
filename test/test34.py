#!user/bin/python
# encoding:utf-8

import functools

def foo(a, b=5):
    print a + b

foo(1)

foo(1, 6)

foo2 = functools.partial(foo, b=4)
foo2(4)