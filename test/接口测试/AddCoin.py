#!/usr/bin/env python
# encoding:utf8
import requests
import json

# url = 'http://127.0.0.1:13001/get_role'
# r = requests.get(url)
# print r.status_code
# print r

url = 'http://103.216.120.161:13003/get_banCharacter'
payload = {
    "uid": 10561,
    "serverId": 40012,
    "ts": 1469070662,
    "sign": "9310121a530266b3c310e5b3ce568374",
    "status": 0
}

# url = 'http://127.0.0.1:13001/get_banCharacter'
# payload = {
#     "uid": 1550,
#     "serverId": 1,
#     "ts": 1469070662,
#     "sign": "8b6c01169410ba8da676d6f086cd1d50",
#     "status": 0
# }

headers = {'content-type': 'application/json'}
r = requests.get(url, data=json.dumps(payload), headers=headers)
print r.json()
