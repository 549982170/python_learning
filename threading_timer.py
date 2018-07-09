#!user/bin/python
#encoding:utf-8
import threading
import time
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def delayed():
    logging.debug('worker running')
    return

t1 = threading.Timer(3,delayed)
t1.setName('t1')
t2 = threading.Timer(3,delayed)
t2.setName('t2')

print time.ctime(time.time())
logging.debug('staring timers')
t1.start()
t2.start()

print time.ctime(time.time())
logging.debug('waiting before canceling %s',t2.getName())
time.sleep(2)
print time.ctime(time.time())
logging.debug('canceling %s',t2.getName())
print time.ctime(time.time())
t2.cancel()
print time.ctime(time.time())
logging.debug('done')
