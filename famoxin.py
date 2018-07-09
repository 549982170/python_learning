#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json


def run():
      url = 'http://www.moxian.com/api/mx_mobile/index.php'
      payload = {"all_key":"b5e320aab95ab0342277f902d1b38cb0",
                 "title":"[爱你][爱你][爱你]",
                 "mobile_loca":"广东省深圳市福田区彩田路1996号",
                 "remote_ip":"10.0.2.15",
                 "link":"",
                 "mx_id":460242,
                 "class":"0",
                 "longitude":114.074586,
                 "func":"system.mobile_addinfo.func",
                 "latitude":22.537558,
                 "access":0,
                 "key":"460242"
                 }

      headers = {'content-type': 'application/json'}
      r = requests.post(url, data=json.dumps(payload), headers=headers)
      
      print r.json()
      res = r.json()
      print "The error is" ,requests.codes.ok
      
      
      

if __name__ == '__main__':
      run()     
            

