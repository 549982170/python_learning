#!user/bin/python
#encoding:utf-8

import urllib2
import json
from urllib import urlretrieve  

url = 'http://japi.juhe.cn/joke/img/text.from?key=e2b1d4fbaf2f02a49d331355c6792f42&page=1&pagesize=9'
result = urllib2.urlopen(url).read()
result = json.loads(result)  #把返回的json当字典处理
x=1
for i in result.get('result').get('data'): 
    PicUrl = i.get('url')
    #print PicUrl
    
    urlretrieve(PicUrl,'f://123//%s.gif' % x, )   
    x+=1
