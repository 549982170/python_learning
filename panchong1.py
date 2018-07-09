import urllib2
html = urllib2.urlopen('http://www.baidu.com').read()
print 'size is ',html