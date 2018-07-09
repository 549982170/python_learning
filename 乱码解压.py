#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import urllib2
import gzip
import StringIO
url = r'http://wthrcdn.etouch.cn/weather_mini?citykey=101020800'# 101280601 深圳编码号
response = urllib2.urlopen(url)
stream = StringIO.StringIO(response.read())
with gzip.GzipFile(fileobj=stream) as f:            #解压
    data = f.read()
print(data)