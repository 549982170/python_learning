#!user/bin/python
#encoding:utf-8
import requests
import json

url = 'http://www.moxiancn.com/mo_common_sso/m1/auth/login'
payload = {
              "useraccount": "8613800000065",
              "userpass": "123456"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,data = json.dumps(payload),headers=headers)
result = r.json()
#print result

token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
#print token,userId
url = 'http://www.moxiancn.com:80/mo_goods/m1/shopgoods/getUpDownNumber'

  
payload ={
                "shopId": "2",

          }
headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.get(url,params=payload, headers=headers)
#print r.url
print r.json()
#print r.text
res = r.json()

