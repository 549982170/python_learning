#!/user/bin/python
#test the variable threading.enumerate()
import threading
import time
def worker():
    print "test"
    time.sleep(2)
threads = [ ]
for i in xrange(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
for item in threading.enumerate():
    print item
print
for item in threads:
    print item
