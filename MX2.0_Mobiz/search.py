#!user/bin/python
#encoding:utf-8
import requests
import json
url = 'http://www.moxiancn.com/mo_common_sso/m1/auth/login'
query_args = {
              "useraccount": "8613800138076",
              "userpass": "123456"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(query_args),headers=headers)
result = r.json()

#print result

#token = json.loads(result,'utf-8') 
token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
print userId
url = 'http://www.moxiancn.com/mo_biz/m1/company/search'
payload ={
            "companyId": 1428924535857
          }

headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.get(url, params=payload, headers=headers)
print r.json()
res = r.json()
