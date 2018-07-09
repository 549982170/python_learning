#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json




      
def run():
      url = 'http://www.moxiancn.com:80/moxian_com_user/m1/reg/checkphoneno'
      payload = {"countryCode": "86", "phoneNo": "8613800138000"}
      headers = {'content-type': 'application/json'}
      r = requests.post(url, data=json.dumps(payload), headers=headers)
      
      print r.json()
      res = r.json()
      
      
      

if __name__ == '__main__':
      run()     
            