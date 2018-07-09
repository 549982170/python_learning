#!user/bin/python
# encoding:utf-8
import requests
import json

# U8支付回调
# url = 'http://127.0.0.1:8080/zodiacU8/pay/ipayios/payCallback'
# payload = {
#     "transdata": 10561,
#     "signtype": 40012,
#     "sign": 1469070662,
#     "u8ChannelID": 1001
# }
# headers = {'content-type': 'application/json'}
# r = requests.get(url, params=payload, headers=headers)
# print r.text

# game回调
url = 'http://127.0.0.1:23001/payCallback'
payload = {
    "orderID": 1063679123647365121,
    "userID": 1569,
    "channelID": 1001,
    "currency": 'RMB',
    "money": 25,
    "sign": 'a0b2d863372ec968198abe96c23e6612'
}
headers = {'content-type': 'application/json'}
r = requests.get(url, params=payload, headers=headers)
print r.text
