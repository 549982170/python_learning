#!user/bin/python
#encoding:utf-8
import requests
import json
import urllib,urllib2
url = 'http://w5.m41s.com/index.php'
query_args = {
              "m": "user",
              "f": "123456",
              "referer":"L2luZGV4LnBocD9tPW15JmY9YnVnJnR5cGU9b3BlbmVkQnk="
              }

Body ={
            "account": "yi.zhiwu",
            "password":"20140811",
            "keepLogin[]":"on",
            "referer":"/index.php?m=my&f=bug&type=openedBy"
          }

agent="Mozilla/5.0 (X11; U; Linux i686 (x86_64); zh-CN; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2"
s = requests.Session()
s.headers.update({'User-Agent': agent})

url2 = requests.get(url, params = query_args).url  #拼链接
#print url2
r = s.post(url2, data = Body)
r = urllib2.urlopen(url2)
print r

