#!user/bin/python
#encoding:utf-8
import requests
import json

url = 'http://dev2.moxian.com:80/mo_talk/m1/gethostlist '
payload = {
          "areaCode": "60",
          "openfireIp": "192.168.0.21",
          "openfireProxyIp": "5222",
          "openfireDomain": "",
          "headUrl": "http://121.201.96.110",
          "serverCode": "002" 
          
            }
headers = {'content-type': 'application/json'}
r = requests.get(url,params=payload,headers=headers)
print r.text
print r.url
res = r.json()

#请求发现只有中国一个服务器？