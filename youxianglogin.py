#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
#import time
#t1 = time.time()

#for i in range(1000):

      
def run():
      url = 'http://dev2.moxian.com/moxian_com_user/m1/login'
      payload = {"account": "827875010@qq.com","password": "123456"}
      headers = {'content-type': 'application/json'}
      r = requests.post(url, data=json.dumps(payload), headers=headers)
      
      print r.json()
      res = r.json()
      
      


if __name__ == '__main__':
      run()     
#t2 = time.time()

#print "\n",t2 -t1 
