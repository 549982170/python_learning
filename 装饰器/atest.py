# encoding:utf-8
# usr/bin/python
# -*- coding: utf-8 -*-
import threading
import time
import pickle

from functools import wraps

lock_dict = {}

def thread_lock(function):
    """多线程路由函数独立锁（函数名+函数结点作为唯一识别,保证函数线程安全）"""

    @wraps(function)
    def run(*args, **kwargs):
        try:
            key = pickle.dumps((function.func_name,))
            lock = lock_dict.get(key)
            if not lock:
                lock = threading.RLock()
                lock_dict[key] = lock
            if lock.acquire():
                function(*args, **kwargs)
        except:
            raise
        finally:
            lock.release()

    return run

@thread_lock
def test_xc():
    # mutex.acquire()  # 取得锁
    f = open("test.txt", "a")
    f.write("test_dxc" + '\n')
    time.sleep(1)

    f.close()
    # mutex.release()  # 释放锁


if __name__ == '__main__':
    # mutex = threading.Lock()  # 创建锁
    for i in xrange(5):
        t = threading.Thread(target=test_xc)
        t.start()


