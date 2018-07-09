#!user/bin/python
import threading
#import time
def worker():
    """thread worker function"""
    print 'Worker'
#    time.sleep(2)
    return
threads = [ ]
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()