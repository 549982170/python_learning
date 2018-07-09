#!user/bin/python
#encoding:utf-8
import requests
import json
url = 'http://sso.moxiancn.com/mo_common_sso/m1/reg/moxian'
payload = {
              "phoneNo": "",
              "birthday": "864748800",
              "birthdayViableType":0,
              "nickName":"",
              "countryCode":"123",
              "captcha":"3774",
              "sexType":"0",
              "password":"123456"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(payload),headers=headers)
result = r.json()
print r.json()
res = r.json()
