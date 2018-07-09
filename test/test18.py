#!/usr/bin/env python
# coding:utf8
import urllib2
import json

# url = "http://192.168.11.211:13002/reloadConfig"
# req = urllib2.Request(url=url)
# response = urllib2.urlopen(req)
# rspResult = response.read()
# response.close()
# if json.loads(rspResult).get('result') == 1:
#     print (url + " " + "reload success")

import time
import sys


def progress(percent, bar_length):
    hashes = '#' * int(percent / 5000.0 * bar_length)
    spaces = ' ' * (bar_length - len(hashes))
    sys.stdout.write("\rPercent: [%s] %0.2f%%" % (hashes + spaces, percent/50.0))
    sys.stdout.flush()
    time.sleep(1)


progress(2500, 100)
