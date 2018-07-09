#!user/bin/python
#encoding:utf-8
import requests
import json
url = 'http://login.moxiancn.com/mo_common_login/m1/auth/login'
payload = {
              "useraccount": "8618126274558",
              "userpass": "123456"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,data = json.dumps(payload),headers=headers)
result = r.json()
token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
print token,userId

path = u'F://123//1.gif'
#print path
files = {'file': open(path, 'rb'),
         "userId": userId,  
         "fileType":"0",
         "fileClassfycation":"0"         
         }
url = 'http://file.moxiancn.com/mo_common_fileuploadservice/m1/upload'
#payload ={
           #"userId": userId,  
           #"fileType":"0",
           #"fileClassfycation":"0"
          #}

headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.post(url, files = files, headers=headers)
print r.json()