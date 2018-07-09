#!user/bin/python
#encoding:utf-8
import requests
import json
url = 'http://sso.dev2.moxian.com:80/mo_common_sso/m1/reg/checkphoneno'
payload = {
            "countryCode": "86",
            "phoneNo": "8618998405382",
           }
headers = {'content-type': 'application/json'} 
r = requests.post(url, json.dumps(payload), headers=headers)
print r.json()
res = r.json()