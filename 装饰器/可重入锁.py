# encoding:utf-8
# usr/bin/python
import threading
import time

lock = threading.RLock()


def CountNum(id):
    global num

    lock.acquire()

    if num <= 10:
        print "Thread id is : %s     The num is %s\n" % (id, str(num))
        num = num + 1
        CountNum(id)

    lock.release()


if __name__ == "__main__":
    num = 1
    t1 = threading.Thread(target=CountNum, args=('A'))

    t1.start()

    time.sleep(5)
