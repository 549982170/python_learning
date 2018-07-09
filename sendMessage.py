#!user/bin/python
#encoding:utf-8

import time
import requests
agent="Mozilla/5.0 (X11; U; Linux i686 (x86_64); zh-CN; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2"
s = requests.Session()
s.headers.update({'User-Agent': agent})

print time.ctime()
url = 'http://moxian.com/user/ajax/firstlogin'
query_args = {
     'login_type': '1',
     'user_name': '18998405382',
     'user_pwd': '8f38563d476fdbce3142554d0ca75482',
     'keeplogin': 'off',
     "country_num": "86"
}

r = s.post(url, data=query_args)
print r.json()
code = r.json()['data']

url = 'http://moxian.com/user/ajax/secondlogin'
query_args = {
     'login_type': '1',
     'user_name': '18998405382',
     'keeplogin': 'off',
     'verify_code': code,
     'redirect_url': 'true',
     "country_num": "86"
}
r = s.post(url, data=query_args)
print r.json()
print r.cookies

url = 'http://moxian.com/main/gateway.php'
query_args = {
      "type": "add_info",
      "desc[]": "test",
      "type_id": "0",
      "tags[]": "la_2677",
      "pics[]":"http://img.juhe.cn/joke/201412/19/DDE51B6C09E1557D6542627755901308.gif",
      "info_local": ""
}
r = s.post(url, data=query_args)
print r.content

print time.ctime()
print "The message is OK" 