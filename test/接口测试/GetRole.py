#!/usr/bin/env python
# encoding:utf8
import requests
import json

# url = 'http://127.0.0.1:13001/get_role'
# r = requests.get(url)
# print r.status_code
# print r

# url = 'http://127.0.0.1:13001/get_role'

# 获取角色信息
# http://127.0.0.1:8080/userver/game/get_role?userId=test111&serverId=3&ts=1234561&sign=4d088b550e79f71dfffd15813e704f5b
#  http://127.0.0.1:8080/userver/game/get_role?userId=1550&serverId=13&ts=1234561&sign=11cd0fef4ca373f178953f50d6a6e0da

# 增加金币
# http://127.0.0.1:8080/userver/game/add_coin?userId=test175&serverId=3&ts=1234561&amount=648&os=Android&currency=VDN&orderId=111111&type=web&payTime=1234567&roleId=1243&sign=53b1c9091ce235b25bf20b9b54ff4e8b
# http://127.0.0.1:8080/userver/game/add_coin?userId=1550&serverId=113&ts=1234561&amount=648&os=Android&currency="VDN"&orderId=111111&type=web&payTime=1234567&roleId=1243&sign=ab541ba13509658799dcd9b697e6e9d0

# http://157.119.247.3/userver/game/add_coin?os=ios&ext=1006008&roleId=10002&userId=1001&serverId=30001&amount=100000&currency=VND&orderId=SM20160720102154_185&payTime=1468984915&type=client&sign=36b91050f9149e0959afe9bd4e829c6b

# 查询用户金币数
# http://127.0.0.1:8080/userver/game/get_total_coin?userId=1550&serverId=3&ts=123456&sign=4583ab2b64c227ea6111f6ce854b4bea

# 查询充值订单
# http://127.0.0.1:8080/userver/game/check_add_coin?userId=1550&serverId=1&orderId=111111&ts=1234&sign=fa223d6a72f8e2ecd4c2d0d2539b6fc0
# http://127.0.0.1:8080/userver/game/check_add_coin?userId=1550&serverId=1&orderId=111211&ts=1234&sign=7f757751800c8ebc4ed3a243428469ef

# 获取等级排列
# http://127.0.0.1:8080/userver/game/get_top_level?serverId=3&topCount=10&ts=123456&sign=1f504498dff170b45de7199d51b19cc1

# 发放物品、礼包
# http://127.0.0.1:8080/userver/game/add_package?requestId=12345678&packageId=10010&userId=1550&packageNum=1&ts=1234&serverId=3&sign=620e3c417b9716f01f3f978db306007d

# a5541af4ec926fc11c5c7a3e23d971b4

# 登录
# http://127.0.0.1:8080/userver/user/getToken?token=123&gameId=1&userId=1550&appID=1&channelID=1006

# 越南服
# http://157.119.247.3/userver/game/get_role?userId=1550&serverId=3&ts=1234561&sign=b46d95e8ebdae764d309e4873dbfc980
# http://157.119.247.3/userver/game/get_role?userId=1001&serverId=30001&ts=1467356539&sign=46bae2d6723366aa14cef9396940241b

# http://157.119.247.3/userver/game/check_add_coin?serverId=30001&orderId=ABC_1467689996000_474&ts=1467690139&sign=0c9c278a8defbca044eaab932182e66c

# http://127.0.0.1:8080/userver/game/check_add_coin?serverId=30001&orderId=ABC_1467689996000_474&ts=1467690139&sign=0c9c278a8defbca044eaab932182e66c

# 获取玩家所有信息
# http://127.0.0.1:8080/userver/game/get_playerinfo?uid=1243&serverId=3&ts=1469070662&sign=0900c4b9ec598e6b605ff44ed7c20586
# http://119.29.181.87/userver/game/get_playerinfo?uid=1243&serverId=3&ts=1469070662&sign=0900c4b9ec598e6b605ff44ed7c20586
# http://119.29.181.87/userver/game/get_playerinfo?uid=1754&serverId=10001&ts=1469070662&sign=d167e8e267a01eb3525a958251617cf6
# 119.29.181.87

# 封号/解封 0封号1正常
# http://127.0.0.1:8080/userver/game/get_banCharacter?uid=1243&serverId=3&ts=1469070662&sign=0900c4b9ec598e6b605ff44ed7c20586&status=0
# http://127.0.0.1:8080/userver/game/get_banCharacter?uid=1243&serverId=3&ts=1469070662&sign=0900c4b9ec598e6b605ff44ed7c20586&status=1

# 禁言/解禁 1禁言2解禁
# http://127.0.0.1:8080/userver/game/get_chatMgr?uid=1243&serverId=3&ts=1469070662&sign=0900c4b9ec598e6b605ff44ed7c20586&status=1&donttalktime=10000
# http://127.0.0.1:8080/userver/game/get_chatMgr?uid=1243&serverId=3&ts=1469070662&sign=0900c4b9ec598e6b605ff44ed7c20586&status=2&donttalktime=10000

# 禁言/封号列表
# http://127.0.0.1:8080/userver/game/get_banList?serverId=3&ts=1469070662&sign=213b16cc6b7cc55d2f758c6b8c88df22&type=1
# http://127.0.0.1:8080/userver/game/get_banList?serverId=3&ts=1469070662&sign=4373a96b7c541d747b76ef1fe4b77aab&type=2


# url = 'http://127.0.0.1:13001/get_playerinfo'
# payload = {
#     "uid": "1243",
#     "serverId": "3",
#     "sign": "5bfb2440cb3e3fcd569a382e3843bdb4",
#     "ts": "sss"
# }
#
# headers = {'content-type': 'application/json'}
# r = requests.get(url, data=json.dumps(payload), headers=headers)
# print r.text

url = 'http://127.0.0.1:8080/userver/game/getSvrList'
payload = {
    "channelId": "1001",
    "installId": "",
    "mac": "14772998251103"
}

headers = {'content-type': 'application/json'}
r = requests.post(url, json.dumps(payload), headers=headers)
print r.text
