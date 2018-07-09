#!/usr/bin/env python
# encoding:utf8
def d1(func):
    def t1(*args, **kwargs):
        print "d1"
        func(*args)
    return t1

def t2(url):
    def d1(func):
        def t1(*args, **kwargs):
            print "t2", url
            func(*args, **kwargs)
        return t1
    return d1

@t2("/standardization/<sid>")
@d1
def test():
    print "test1"

def test2():
    print "test2"

def myroute(mode,url,test2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            mode(url)
            test2()
            func(*args, **kwargs)
        return wrapper
    return decorator

def mode(url):
    print url

url = "/standardization/<sid>"

@myroute(mode,url,test2)
def test3():
    print "tets3"


test()
print "------"
test3()