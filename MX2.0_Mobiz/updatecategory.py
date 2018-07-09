#!user/bin/python
#encoding:utf-8
import requests
import json
url = 'http://dev2.moxian.com/mo_common_sso/m1/auth/login'
query_args = {
              "useraccount": "8613534070424",
              "userpass": "123456"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(query_args),headers=headers)
result = r.json()

#print result

#token = json.loads(result,'utf-8') 
token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
url = 'http://dev2.moxian.com:80/mo_biz/m1/shop/updatecategory'
payload ={
             "shopId":85,
             "categoryId": 2,  #行业分类ID
          }

headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.get(url, params=payload, headers=headers)
print r.json()
res = r.json()
