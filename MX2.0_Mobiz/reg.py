#!user/bin/python
#encoding:utf-8
import requests
import json
url = 'http://sso.dev2.moxian.com:80/mo_common_sso/m1/reg/moxian'
payload = {
            "nickName": "测试175",
            "password": "123456",
            "sexType": 0,
            "captcha": "3007",
            "phoneNo": "8618998405382",
            "birthday": "1432021802",
            "birthdayViableType": 0,
            "countryCode": "86",
            "city": "深圳",
            "isAdminItype": 0,
            "isMobizItype": 0,
            "isMopalItype": 0
}

headers = {'content-type': 'application/json'} 

r = requests.post(url, json.dumps(payload), headers=headers)
print r.json()
res = r.json()
