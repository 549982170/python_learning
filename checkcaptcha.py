#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests


def run():
    url = 'http://dev2.moxian.com:8080/moxian_com_user/m1/forget/sendforgetcaptcha'
    payload = {"code": "648831","type": 3,"mobile": "","email": "test2@126.com"}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
          
    print r.json()
    res = r.json()
    
      
if __name__ == '__main__':
    run()
    