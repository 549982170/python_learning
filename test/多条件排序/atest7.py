#!/usr/bin/env python
# coding: utf-8
# 以同步的方式获取URL：

import getPage


def processPage(page):
    print page


def logError(error):
    print error


def finishProcessing(value):
    print "Shutting down..."
    exit(0)


url = "http://google.com"
try:
    page = getPage(url)
    processPage(page)
except Error, e:
    logError(error)
finally:
    finishProcessing()
# 以异步的方式获取URL：

from twisted.internet import reactor
import getPage


def processPage(page):
    print page
    finishProcessing()


def logError(error):
    print error
    finishProcessing()


def finishProcessing(value):
    print "Shutting down..."
    reactor.stop()


url = "http://google.com"
# getPage takes: url,
# success callback, error callback
getPage(url, processPage, logError)

reactor.run()
