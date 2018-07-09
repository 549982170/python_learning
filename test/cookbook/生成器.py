#!/usr/bin/env python
# encoding:utf8
import time
t1 = time.time()
print sum([i for i in xrange(100000000)])
print time.time() - t1

t2 = time.time()
print sum(i for i in xrange(100000000))
print time.time() - t2


