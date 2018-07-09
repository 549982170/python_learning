#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json




      
def run():
      url = 'http://debug.moxian.com/user/mobile/send_reg_msg?v=1213&t=ios&enter_type=1&_lang_=cs'
      payload = {"countryCode": "86", "phoneNo": "8613800138000"}
      headers = {'content-type': 'application/json'}
      r = requests.post(url, data=json.dumps(payload), headers=headers)
      
      print r.json()
      res = r.json()
      
      
      

if __name__ == '__main__':
      run()     
            