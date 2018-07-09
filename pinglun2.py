#!user/bin/python
#encoding:utf-8

import time
import requests
agent="Mozilla/5.0 (X11; U; Linux i686 (x86_64); zh-CN; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2"
s = requests.Session()
s.headers.update({'User-Agent': agent})

print time.ctime()
username = raw_input("username:")
password = raw_input("password:")

url = 'http://www.yl1001.com/CheckUserAjax.php?ajaxformflag=1'
query_args_1 = {"uname" : username,
              "password": password,
              "per_login_type" : "0"
              }

r = s.post(url, data=query_args_1)
print r.json()
MD5 = r.json()['pwd']

print time.ctime()

#-------get checkcode-------



#----------------------------



#----------------------------





url2 = 'http://www.job1001.com/webdev/position_new/index.php?&mode=ajax&doaction=xinzhi_ajax&detail=reply&position=php'
query_args_2 = {
      "bcontents" : "ok",
      "code" : code,
      "article_id" : "6551426240154573",
      "content" : "ok",
      "group_id" : "0",
      "group_id" : "102424",
      "cks" : MD5,
      "ajaxformflag" : "1"
}
r = s.post(url2, data=query_args_2)
print r.content


print time.ctime()
print "The message is OK" 