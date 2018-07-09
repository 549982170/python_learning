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
#行业分类
#token = json.loads(result,'utf-8') 
token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
url = 'http://dev2.moxian.com:8080/mo_biz/m1/industryCategory/getCategoryByPrId'
payload ={
             "pId": 3,              #父几点Id，不传默认为0-一级节点
             "countryCode": "cn"    #国家码，不传默认为cn-中国
          }

headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.get(url, params=payload, headers=headers)
print r.json()
res = r.json()
