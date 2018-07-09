#!user/bin/python
# encoding:utf-8

from twisted.internet import reactor, defer


def getDummyData(x):
    """
    创建一个 Deferred 对象，并返回这个对象
    """
    d = defer.Deferred()
    # 2 秒钟后执行 Deferred 回调函数序列，把 x * 3 作为参数传递给回调序列中的第一个函数
    # reactor.callLater 是一个定时延迟调用的方法
    reactor.callLater(2, d.callback, x * 3)
    return d


def printData(result):
    """
    打印结果
    """
    print result


d = getDummyData(3)

# 添加回调函数到回调函数序列中
d.addCallback(printData)

# 4 秒钟后停止 reactor 循环（退出进程）
reactor.callLater(4, reactor.stop)

# 开始 Twisted reactor 事件循环
reactor.run()
