#!user/bin/python
#encoding:utf-8
import threading
def sayhello():
    print "hello world"
    global t #Notice:use global variable!
    t = threading.Timer(5.0,sayhello)
    t.start()
t = threading.Timer(5.0,sayhello)
t.start()
