#!user/bin/python
# -*- coding:gb2312 -*-

import requests
import os

agent="Mozilla/5.0 (X11; U; Linux i686 (x86_64); zh-CN; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2"
s = requests.Session()
s.headers.update({'User-Agent': agent})
while True:
    url = 'http://127.0.0.1:8000/add/'
    a = raw_input("������һ������")
    b = raw_input("��������һ������")
    payload = {
                 'a': a,
                 'b': b,
    
            }
    r = s.get(url, params=payload)
    print u"�������ĺ��ǣ�"+r.text
    command = 'pause'
    os.system(command) 