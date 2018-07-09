#!user/bin/python
#encoding:utf-8
import requests
import json
user = raw_input("输入帐号：")
pwd = raw_input("输入密码：")
black = raw_input("输入需要移除黑名单的好友ID：")
url = 'http://login.moxiancn.com/mo_common_login/m1/auth/login'
query_args = {
              "useraccount": '86'+str(user),
              "userpass": pwd
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(query_args),headers=headers)
result = r.json()
#token = json.loads(result,'utf-8') 
token = result.get(u'data').get(u'token')
#print token
userId = str(result.get(u'data').get(u'userId'))
#print token
print u'我当前的ID：' + userId
print result
url = 'http://pal.moxiancn.com:80/mo_pal/api/fans/black/'+str(black)
headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.delete(url, headers=headers)
#print r.url
print r.json()
res = r.json()

