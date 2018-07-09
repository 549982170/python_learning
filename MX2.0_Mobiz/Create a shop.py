#!user/bin/python
#encoding:utf-8
import requests
import json
url = 'http://www.moxiancn.com/mo_common_sso/m1/auth/login'
query_args = {
              "useraccount": "8613800000065",
              "userpass": "123456"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(query_args),headers=headers)
result = r.json()
# http://www.spellthread.com/  路演环境
# http://dev2.moxian.com:8080  dev环境
#http://www.moxiancn.com       moxiancn环境
#print result

#token = json.loads(result,'utf-8') 
token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
url = 'http://www.moxiancn.com/mo_biz/m1/shop/addshop'
payload ={
             "companyId": "1430122439364",         #公司id
             "name": "新建店铺66",
             "logo": "http://image.spellthread.com/moliao/24721428986180881.gif",                  #logo图片url
             "categoryId":"1",             #行业分类ID
             "longitude": "112.564866",
             "latitude": "22.654879",
             "area": "2322132",
             "detailedAddress": "中深花园",
             "hotline": "@@@@@@@@@",
             "introduce": "测试"
         }

headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.post(url, json.dumps(payload), headers=headers)
print r.json()
res = r.json()
