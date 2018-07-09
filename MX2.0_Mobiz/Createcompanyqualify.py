#!user/bin/python
#encoding:utf-8
import requests
import json
url = 'http://dev2.moxian.com/mo_common_sso/m1/auth/login'
query_args = {
              "useraccount": "8618998405382",
              "userpass": "123456"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(query_args),headers=headers)
result = r.json()

#print result

#token = json.loads(result,'utf-8') 
token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
url = 'http://dev2.moxian.com:8080/mo_biz/m1/merchantqualify/createcompanyqualify'
payload ={
             "companyId": "1428561071715",
             "companyType": 3,
             "checkStatus": "1",
             "idCard": "420800197012204530",
             "idCardFrontPath": "http://image.dev2.moxian.com/moliao/11291428631093856.png",
             "idCardBehindPath": "http://image.dev2.moxian.com/moliao/11291428631093856.png",
             "phoneNo": "15915343022",   #号码不能加86
             "realName":"张三",
             "qualificationPath": "http://image.dev2.moxian.com/moliao/11291428631093856.png"
          }

headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.post(url, json.dumps(payload), headers=headers)
print r.json()
res = r.json()
