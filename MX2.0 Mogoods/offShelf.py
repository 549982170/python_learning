#!user/bin/python
#encoding:utf-8
import requests
import json
import time
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
#print token,userId
url = 'http://www.moxiancn.com:80/mo_goods/m1/managergoods/offShelf'
#好友id30，35
time1 = time.time()
time2 = time.time()+10000
  
payload ={
           #"userId": 1, # 用户ID 
           "shopId": "2",#商铺ID，必填
           #"merchantId": "1",#商家ID 可以不填
           "goodsId": "27", # 商品ID，必填
           "goodsUpTime": time1,# 上架时间
           "goodsDownTime": time2 # 下架时间，下架时间必须大于上架时间          
          }
headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.post(url,data=json.dumps(payload), headers=headers)
#print r.url
print r.json()
#print r.text
res = r.json()
#传shopId为空报错
