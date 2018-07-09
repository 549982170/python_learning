
#!/usr/bin/env python
# -*- coding:utf8 -*-

import urllib2

req = urllib2.Request("http://www.baidu.com/")
res = urllib2.urlopen(req)
html = res.read()
res.close()

html = unicode(html, "gb2312").encode("utf8")
print html