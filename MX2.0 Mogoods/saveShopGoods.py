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
url = 'http://www.moxiancn.com:80/mo_goods/m1/shopgoods/saveShopGoods'
time1 = time.time()+10000
time2 = time.time()+100000000
  
payload ={
                "shopId": "2",
                "goodsId": "3",
                "companyId": "1430122439364",
                "goodsName": "测试商品1",
                "goodsType": "1",     #商品类型 1-商品 ，2-优惠券
                "goodsSummary": "商品介绍大卡司双人奶茶套餐，不限时段通用，免费WIFI，（商品介绍）",#商品简介
                "goodsDetail": "在2.14号之前，在深圳大卡司各分店均可享用双人奶茶套餐，欢迎使用。",
                "goodsStock": "100",          #商品库存
                "goodsGroupId": "2",         #商品分组Id
                "goodsUpTime": time1,   #上架时间 秒时间戳
                "goodsDownTime": time2, #下架时间 秒时间戳
                "goodsRule": "• 有用。• 不兑现、不找零。• 团购用户不可同时享受商家其他优惠。• 不兑现、不找零。• 团购用户不可同时享受商家其他优惠。",#商品使用规则
                "goodsStartTime": time1,#商品有效开始时间 秒时间戳
                "goodsEndTime": time2,#下架时间 秒时间戳
                "isRecommend": 1, #是否商家推荐 1-推荐，0-不推荐
                "goodsBuyMax": 0,#商品限购数 0-不限购
                "goodsPictureJson": "[{'url':'1231231','price':10,'goodsTempletId':'','isAssemble':1},{'url':'1231231','price':10,'goodsTempletId':'','isAssemble':1}]",
                                  #商品图片数组 [{'url':'1231231', --图片地址 'price':10, --图片数字 'goodsTempletId':1, --图片模板Id 'isAssemble':1 --是否图片数字组合 1-是否则不是}, 
                                  #{'url':'4444','price':10,'goodsTempletId':,'isAssemble':0},{'url':'555','price':10,'goodsTempletId':,'isAssemble':1}]                
                "price": 1,          #商品兑换价格 商品类型为商品（goodsType=1）时 必填
                "sendMethod": "100",     #商品发货方式 商品类型为商品（goodsType=1）时 必填
                "postage": "0",    #商品发货运费 商品类型为商品（goodsType=1）时 必填
                "couponType": 1,   #优惠券类型 商品类型为商品（goodsType=2）时 必填 1-现金券，2-折扣券
                "isSpecial": 1,      #是否有促销 1-有促销否则没有促销
                "specialPrice": 10,     #商品促销价 isSpecial=1 时 必填
                "specialStartTime": time1,   #商品促销开始时间 isSpecial=1 时 必填 秒间戳
                "specialEndTime": time2,     #商品促销结束时间 isSpecial=1 时 必填 秒间戳
                "specialBuyMax": 100,                     #商品促销限购 isSpecial=1 时 必填
                "goodsCategoryId": "1" ,   #商品分类Id
                "goodsCategoryName": "1",   #商品分类名称
                "primePrice": 100,         #商品原价格 商品类型为商品（goodsType=1）时 必填
                "couponPrice": 9.88,   #折扣金额 商品类型为商品（goodsType=2）时 必填
                "currency":"￥"     #货币类型 美元-$ ,人民币-￥
          }
headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.post(url,data=json.dumps(payload), headers=headers)
#print r.url
print r.json()
#print r.text
res = r.json()

