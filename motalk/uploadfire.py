#!user/bin/python
#encoding:utf-8
import requests
import json
url = 'http://www.spellthread.com/mo_common_sso/m1/auth/login'
query_args = {
              "useraccount": "8613148874302",
              "userpass": "123456"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(query_args),headers=headers)
result = r.json()

#print result
token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))

url = 'http://dev2.moxian.com:8080/mo_common_fileuploadservice/m1/upload'

files={'file':open("uploadFile.gif", "rb"),
       "userId": 71,
       "fileType": 0,
       "fileClassfycation":0      
       }

r = requests.post(url,file=files)
print r.json()


 