#!user/bin/python
#encoding:utf-8
import requests
import json
url = 'http://www.spellthread.com/mo_common_sso/m1/auth/login'
query_args = {
              "useraccount": "8613542501471",
              "userpass": "123456"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(query_args),headers=headers)
result = r.json()

print result
token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
url = 'http://www.moxiancn.com/mo_talk/m1/gethostlist'
payload ={
                 "areaCode": "60", #国家地区码
                 "openfireIp": "192.168.0.21", #Openfire IP
                 "openfireProxyIp": "5222",#OpenFire代理端口
                  "openfireDomain": "",#openfire domain
                 "headUrl": "http://121.201.96.110", #访问IP
                 "serverCode": "002" #节点code
                      }

headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.get(url,params=payload,headers=headers)
print r.json()
res = r.json()
