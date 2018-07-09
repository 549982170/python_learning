#!user/bin/python
#encoding:utf-8
import requests
import json
url = 'http://www.spellthread.com/mo_common_sso/m1/auth/login'
query_args = {
              "useraccount": "8613500000000",
              "userpass": "123456"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(query_args),headers=headers)
result = r.json()

#print result

#token = json.loads(result,'utf-8') 
token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
print token
print userId
url = 'http://www.spellthread.com/mo_biz/m1/merchantqualify/updatecompanyqualify'
payload ={
             "id": "1",                     #资质ID
             "companyId": "1428561071715",  #公司ID
             "companyType": 3,
             "checkStatus": "2",
             "idCard": "420800197012204531",
             "idCardFrontPath": "http://image.dev2.moxian.com/moliao/11291428631093856.png",
             "idCardBehindPath": "http://image.dev2.moxian.com/moliao/11291428631093856.png",
             "phoneNo": "8615915343022",
             "realName": "张三",
             "qualificationPath": "http://image.dev2.moxian.com/moliao/11291428631093856.png"
           }

headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.put(url,data=json.dumps(payload), headers=headers)
print r.json()
res = r.json()
print r.url
