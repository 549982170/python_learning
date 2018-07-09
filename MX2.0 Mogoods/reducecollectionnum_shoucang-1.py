#!user/bin/python
#encoding:utf-8
import requests
import json
url = 'http://www.moxiancn.com/mo_common_sso/m1/auth/login'
query_args = {
              "useraccount": "8613800000065",
              "userpass": "123456"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(query_args),headers=headers)
result = r.json()
#print result

token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
#print token,userId
url = 'http://www.moxiancn.com:80/mo_goods/m1/shopgoodsdynamic/shopgoodsdynamic/reducecollectionnum'
#好友id30，35
payload ={
          "shopId": 2,
          "goodsId": 11
          }
headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.put(url, data = json.dumps(payload), headers=headers)
print r.json()
res = r.json()
