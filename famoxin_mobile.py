#!/usr/bin/python
# -*- coding:gb2312 -*- 
import time
import requests
import json

agent="Mozilla/5.0 (X11; U; Linux i686 (x86_64); zh-CN; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2"
s = requests.Session()
s.headers.update({'User-Agent': agent})

url = 'http://login.moxian.com/path/login.php?v=1212&t=ios&enter_type=1&_lang_=cs'
query_args1 = {"login_time":"1426582194",
               "login_type":"1",
               "country_num":"0086",
               "user_name":"18998405382",
               "key":"a05901d6d1e0796aa996c409a50a5a6f",
               "mobile_info":"moxian:iphone&1212&f3a7c796828128a9101768b94673feae&8.2&iPhone",
               "user_pwd":"8f38563d476fdbce3142554d0ca75482"
               }

r = s.post(url, data=query_args1)

#key = r.json()["token"]
print r.text



url_2 = 'http://www.moxian.com/api/mx_mobile/index.php?v=1212&t=ios&enter_type=1&_lang_=cs'

query_args2 =  {"mobile_loca":"",
               "all_key":"b5e320aab95ab0342277f902d1b38cb0",
               "func":"system.mobile_addinfo.func",
               "mx_id":"460242",
               "access":0,
               "remote_ip":"192.168.137.134",
               "key":"460242",
               "longitude":"0.000000",
               "latitude":"0.000000",
               "title":"好"}
r = s.post(url_2, data=query_args2)

print r.content