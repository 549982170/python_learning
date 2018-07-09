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

#token = json.loads(result,'utf-8') 
token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
url = 'http://dev2.moxian.com:80/mo_biz/m1/shop/updateshop'
payload ={
             "id": "85",     #店铺主键ID
             "name": "食品店主店12",
             "longitude": "112.564866",
             "latitude": "22.654879",
             "area": "2322132",
             "detailedAddress": "深圳市岗厦中深大厦2305",
             "hotline": "110755-7560811",
             "introduce": "肉松饼店",
             "takeoutHotline": "110755-7560811",
             "reservationHotline": "110755-7560811",
             "businessHoursBegin": "1427795234",
             "businessHoursEnd": "1427795234",
             "serve": "WIFI",
             "personalityUrl": "www.baidu.com"#店铺地址不能带http://开头
          }

headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.put(url,json.dumps(payload) , headers=headers)
print r.json()
res = r.json()
