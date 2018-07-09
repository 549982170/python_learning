#!/usr/bin/env python
# coding: utf-8

from twisted.internet import defer, reactor
from pprint import pprint


def cback1(result):
    raise Exception('cback1')


def cerr1(failure):
    print 'cerr1: %s' % str(failure)


def cback2(result):
    return 'succ cback2'


def cerr2(failure):
    print 'cerr2: %s' % str(failure)


d = defer.Deferred()
d.addCallbacks(callback=cback1, errback=cerr1)
d.addCallbacks(callback=cback2, errback=cerr2)
d.addCallback(callback=lambda ign: pprint('cback3'))

# 执行回调函数序列
d.callback('run')

# # 退出事件循环
# reactor.callLater(2, reactor.stop)
# reactor.run()
