#!/usr/bin/python
# coding: UTF-8
import time
import sys
from functools import wraps
from inspect import getmembers


def memo(fun):
    cache = {}

    @wraps(fun)
    def wrap(*arg):
        if arg not in cache:
            cache[arg] = fun(*arg)
        return cache[arg]

    return wrap


@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i - 1) + fib(i - 2)

@memo
def fib2(i):
    if i < 2:
        return 1
    return fib(i - 1) + fib(i - 2)

t1 = time.time()
fib(1)
t2 = time.time()
print t2 - t1
t3 = time.time()
fib(1)
t4 = time.time()
print t4 - t3

t5 = time.time()
fib2(1)
t6 = time.time()
print t6 - t5
