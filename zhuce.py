#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import json
import requests
import string


#prefix = '8613682'


      
def run():
      #seq = random.randint(1,900000)
      #number = '{0},{1:06d}'.format(prefix,seq)
      nname = random.sample(string.letters,6)
      url = 'http://www.moxiancn.com/moxian_com_user/m1/reg'
      payload = {"nickName": "kun123", "password": "123456", "sexType": 0, 
                 "captcha": "215208", "phoneNo": "8613800138002", 
                 "birthday": 662695805, "birthdayViableType": 0, 
                 "countryCode": "86", "city": "", "latitude": 0, "longitude": 0}
      headers = {'content-type': 'application/json'}
      r = requests.post(url, data=json.dumps(payload), headers=headers)
      
      print r.json()
      res = r.json()
           
     
      
      
      
if __name__ == '__main__':
      run()

