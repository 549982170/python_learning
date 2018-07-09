#!user/bin/python
#encoding:utf-8
import requests
import json

url = 'http://www.moxiancn.com/mo_common_sso/m1/auth/login'
query_args = {
              "useraccount": "8613133847086",
              "userpass": "123456"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(query_args),headers=headers)
result = r.json()

#print result

token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))

#url = 'http://dev2.moxian.com/mo_biz/m1/merchant/getstep'
#payload = {'content-type': 'application/json',
           #"token":token,
           #"userId":userId
           #}
#headers = {'content-type': 'application/json',"token":token,
           #"userId":userId}
#r = requests.get(url,params=payload,headers=headers)
#print r

#url =  'http://dev2.moxian.com/mo_biz/m1/company/index'+ userId 
#payload = {"userId":userId}
#headers = {'content-type': 'application/json'}
#r = requests.get(url,params=payload)
#print r

url = 'http://www.moxiancn.com/mo_biz/m1/company/update'
payload ={
             "companyId": "1428924535857", #公司id错误
             "companyName": "魔线科技8",
             "companyType": 3,
             "contactNumber": "8613534070424",#接口测试发现电话号码需要加86
             "contactName": "王五",
             "contactEmail": "189348934@qq.com",
             "countryCod": "86",
             "addressDistrict": "222222",
             "addressDetail": "222221212121"
          }
          
headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.put(url, json.dumps(payload), headers=headers)
print r.json()
res = r.json()