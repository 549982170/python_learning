#!user/bin/python
#encoding:utf-8

import threading

mutex = threading.Lock()
 
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        global mutex
        if mutex.acquire():
            for x in range (0,10):
                x = str(x)
                x = x.zfill(10)
                x= list(x)
                print x
        mutex.release()

if __name__ == "__main__":
    for i in range(0, 2):
        my_thread = MyThread()
        my_thread.start()
