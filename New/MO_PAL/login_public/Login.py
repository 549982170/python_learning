# !/usr/bin/python 
# -*-coding:utf-8-*- 
 
import json 
import requests 

def login(x):
    url = 'http://www.moxiancn.com/mo_common_sso/m1/auth/login'
    query_args = {
                      "useraccount": "8613800138000",
                      "userpass": "123456"
                 }
    headers = {'content-type': 'application/json'}
    r = requests.post(url,json.dumps(query_args),headers=headers)
    result = r.json()
#    print r.json()   
    login_token = result.get(u'data').get(u'token')
    login_uerId = str(result.get(u'data').get(u'userId'))    
    if x == "login_uerId"  :  
        return login_uerId
    if x == "login_token":
        return login_token
if __name__ == '__main__': 
    login(x)