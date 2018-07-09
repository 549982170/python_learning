#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json

def run():
      url = 'http://dev2.moxian.com/moxian_com_user/m1/forget/sendforgetcaptcha'
      payload = {"type":"3","email":"827875010@qq.com"}
      headers = {'content-type': 'application/json'}
      r = requests.post(url, data=json.dumps(payload), headers=headers)
      
      print r.json()
      res = r.json()
      
       
      

if __name__ == '__main__':
      run()     
            