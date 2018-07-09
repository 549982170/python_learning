#!user/bin/python
#encoding:utf-8
import threading
import time
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')
d = threading.Thread(name='daemon',target=daemon)
d.setDaemon(True)

def mon_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')
t = threading.Thread(name='non-daemon',target=mon_daemon)

d.start()
t.start()

d.join()
t.join()