#!/user/bin/python
#creat a daemon
#encoding��utf-8
import threading
import time
def worker():
    time.sleep(3)
    print "worke"
t = threading.Thread(target=worker)
t.setDaemon(True)
t.start()
print "����"