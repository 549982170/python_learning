#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json

def run():
      url = 'http://dev2.moxian.com:8080/mo_auth/m1/auth/login'
      payload = {
            "useraccount": "peny@mail.com",
            "userpass": "111111"
          }
      headers = {'content-type': 'application/json'}
      r = requests.post(url, data=json.dumps(payload), headers=headers)
      
      print r.json()
      res = r.json()
      
       
      

if __name__ == '__main__':
      run()     
            