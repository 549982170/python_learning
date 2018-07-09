# encoding:utf-8
# usr/bin/python

def apply_async(func, callback=None, *args):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


apply_async(add, print_result, (2, 3))
