#!user/bin/python
#encoding:utf-8
import requests
import json
#dev: http://dev2.moxian.com:8080/mo_common_fileuploadservice/m1/upload
#moxiancn: http://www.moxiancn.com/mo_common_fileuploadservice/m1/upload
#showload: http://www.spellthread.com
url = 'http://www.spellthread.com/mo_common_sso/m1/auth/login'
query_args = {
              "useraccount": "8618998405382",
              "userpass": "123456"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(query_args),headers=headers)
result = r.json()

print result

token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
print token,userId
url = 'http://www.spellthread.com/mo_common_user/m1/mobilephone/updatemobilephone'
payload ={
           "userId": userId,
           "email": "",
           "validateCode": "",
           "countryCode": "86",
           "phoneNo": "8613800000017"
}
headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.post(url, json.dumps(payload), headers=headers)
print r.json()
res = r.json()
