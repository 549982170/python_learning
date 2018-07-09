# encoding:utf-8
# usr/bin/python
""""可重入：当一个线程拥有一个锁的使用权后，再次获取锁的使用权时，不会阻塞，会立马得到使用权，则原始锁的话，则不行，会阻塞。"""
import thread
import time

lock = thread.allocate_lock()


def Count(id):
    global num;

    while True:
        lock.acquire()
        if num <= 10:
            print "Thread id is : %s     The num is %s\n" % (id, str(num))
            num = num + 1
        else:
            break
        lock.release()
    else:
        thread.exit_thread()


if __name__ == "__main__":
    num = 1
    thread.start_new_thread(Count, ('A',))
    thread.start_new_thread(Count, ('B',))

    time.sleep(5)
