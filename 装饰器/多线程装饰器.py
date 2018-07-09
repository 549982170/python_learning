# encoding:utf-8
# usr/bin/python
import time
import hashlib
import pickle
import threading
from functools import wraps

lock_dict = {}


class MyThread(threading.Thread):
    def __init__(self, func, args=None, kwargs=None):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.key = hashlib.sha1(pickle.dumps((self.func.func_name,))).hexdigest()
        self.result = None

    @property
    def lock(self):
        lock = lock_dict.get(self.key)
        if not lock:
            lock = threading.RLock()
            lock_dict[self.key] = lock
        return lock

    def run(self):
        """"重写start方法,加锁,逻辑处理异常抛出异常,这里可以拓展结果返回"""
        try:
            if self.lock.acquire():
                self.result = self.func(*self.args)
        except:
            raise
        finally:
            self.lock.release()

    def get_result(self):
        try:
            return self.result  # 获取时候需要t.join(), 不然主线程比子线程跑的快,会拿不到结果
        except:
            raise


def thread_function(function):
    """多线程路由函数独立锁（函数名作为唯一识别,保证函数线程安全）"""

    @wraps(function)
    def run(*args, **kwargs):
        try:
            t = MyThread(function, args=args, kwargs=kwargs)
            t.start()
        except:
            raise

    return run


def thread_lock(function):
    """多线程路由函数独立锁（函数名作为唯一识别,保证函数线程安全）"""

    @wraps(function)
    def run(*args, **kwargs):
        try:
            key = hashlib.sha1(pickle.dumps((function.func_name,))).hexdigest()
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


a = 0


@thread_function
def test1(j, k=1):
    global a
    print "handle a{}".format(a)
    time.sleep(5)
    print "finsh a{}".format(a)
    a += 1


b = 0


@thread_lock
def test2(j, k=1):
    global b
    print "handle b{}".format(b)
    time.sleep(5)
    print "finsh b{}".format(b)
    b += 1

c = 0

@thread_function
def test_xc():
    global c
    print "handle test{}".format(c)
    f = open("test.txt", "a")
    f.write("test_dxc" + '\n')
    time.sleep(5)
    f.close()
    print "finsh test{}".format(c)
    c += 1


def run1():
    print "req a"
    for ca in range(10):
        t = threading.Thread(target=test1, args=(1,), kwargs={"k": 2})  # 异步处理数据避免阻塞
        t.start()
    print "rep a"


def run2():
    print "req b"
    for ca in range(10):
        t = threading.Thread(target=test2, args=(1,), kwargs={"k": 2})  # 异步处理数据避免阻塞
        t.start()
    print "rep b"


def run3():
    print "req test"
    for ca in range(10):
        t = threading.Thread(target=test_xc)  # 异步处理数据避免阻塞
        t.start()
    print "rep test"


if __name__ == "__main__":
    run1()
    # run2()
    # run3()
