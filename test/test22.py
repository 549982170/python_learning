#!user/bin/python
# encoding:utf-8
from gevent import monkey;
import time

monkey.patch_socket()
import gevent


def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        # gevent.sleep(0)


t1 = time.time()
g1 = gevent.spawn(f, 500000)
g2 = gevent.spawn(f, 500000)
g3 = gevent.spawn(f, 500000)
g1.join()
g2.join()
g3.join()
print time.time() - t1
