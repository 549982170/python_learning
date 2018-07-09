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
#print result

token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
#print token,userId
url = 'http://www.moxiancn.com/mo_goods/m1/shopgoodsgroup/addgoodstogroup'
#好友id30，35
  
payload ={
           "oldGroupId": "3",#旧的分组id
           "newGroupId": "2",#新的分组id
           "shopId": 2,#店铺id
           "goodsidArray": "13,12,11" #商品id数组，格式为[1222,1234,14456]
          }
headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.put(url,data=json.dumps(payload), headers=headers)
#print r.url
print r.json()
res = r.json()
#传shopId为空报错