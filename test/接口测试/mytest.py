#!/usr/bin/env python
# encoding:utf8
import requests
import json
import base64

s = '4bcdf239307c48a792d41a92522b8a44:28fb691399fc4b3e8115b03de10d7595'
_url = "http://t-home.api.soovii.com/"

Authorization = "Basic" + " " + base64.b64encode(s.encode("utf-8"))
url = _url + "oauth/token"
payload = {
    "username": "wangxin02@soovii.com",
    "password": "123456",
    "scope": "common",
    "grant_type": "password"
}
headers = {'Authorization': Authorization}
r = requests.post(url, data=payload, headers=headers)
result = json.loads(r.text)
print r.text

Authorization = result.get("token_type") + " " + result.get("access_token")

url = _url + "api/employee/detail"
headers = {'Authorization': Authorization}
r = requests.get(url, headers=headers)
result = json.loads(r.text)
print r.text


