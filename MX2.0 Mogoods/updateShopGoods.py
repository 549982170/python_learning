#!user/bin/python
#encoding:utf-8
import requests
import json
import time
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
url = 'http://www.moxiancn.com:80/mo_goods/m1/shopgoods/updateShopGoods'
#print time.time()
time1 = time.time()
time2 = time.time()+10000  
payload ={
                "shopId": "2",
                "goodsId": "27",
                "goodsName": "测试122315",
                "goodsType": 1,
                "goodsSummary": "商品介绍大卡司双人奶茶套餐，不限时段通用，免费WIFI，（商品介绍）",
                "goodsDetail": "在2.14号之前，在深圳大卡司各分店均可享用双人奶茶套餐，欢迎使用。",
                "goodsStock": 10,
                "goodsGroupId": 2,
                "goodsUpTime": time1,
                "goodsDownTime": time2,
                "goodsRule": "• 有效期：2014.8.19-2015.2.14 • 使用规则：无需预约，消费高峰时可能需要排队。• 可叠加使用。• 不兑现、不找零。• 团购用户不可同时享受商家其他优惠。• 不兑现、不找零。• 团购用户不可同时享受商家其他优惠。",
                "goodsStartTime": time1,
                "goodsEndTime": time2,
                "isRecommend": 1,
                "goodsBuyMax": 0,
                "goodsPictureJson": "[{'url':'1231231','price':10,'goodsTempletId':'','isAssemble':1},{'url':'1231231','price':10,'goodsTempletId':'','isAssemble':1}]",
                "price": 1,
                "sendMethod": "100",
                "postage": 0,
                "couponType": 1,
                "isSpecial": 1,
                "specialPrice": 10,
                "specialStartTime": time1,
                "specialEndTime": time2,
                "specialBuyMax": 100,
                "goodsCategoryId": "1",
                "goodsCategoryName": "1",
                "primePrice": 100,
                "couponPrice": 9.88,
                "currency":"￥"
          }
headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.put(url,data=json.dumps(payload), headers=headers)
#print r.url
print r.json()
#print r.text
res = r.json()

