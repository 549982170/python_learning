#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json




      
def run():
      url = 'http://dev2.moxian.com:8080/moxian_com_user/m1/forget/resetpassword'
      payload = {"code":"1363","newpassword": "123456","param": "86-13534070424"}
      headers = {'content-type': 'application/json'}
      r = requests.post(url, data=json.dumps(payload), headers=headers)
      
      print r.json()
      res = r.json()
      
      


if __name__ == '__main__':
      run()     
            