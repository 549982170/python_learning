#!user/bin/python
#encoding:utf-8
import requests
import json
url = 'http://httpbin.org/post'
headers = {'content-type': 'application/json'}
r = requests.post(url,headers=headers)
print r.json()