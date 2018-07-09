# encoding:utf-8
# usr/bin/python

def apply_async(func, args, callback):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


print apply_async(add, (2, 3), callback=print_result)
