#!user/bin/python
# -*- coding:gb2312 -*-
import os
import requests
import json
#dev: http://dev2.moxian.com:8080/mo_common_fileuploadservice/m1/upload
#moxiancn: http://www.moxiancn.com/mo_common_fileuploadservice/m1/upload
#showload: http://www.spellthread.com
while True:
    try:    
        env = raw_input("输入环境：1为dev，2为moxiancn，3为beta：")
        if env == '1':
            url = 'http://dev2.moxian.com:8080/mo_common_sso/m1/auth/login'
            url2 = 'http://dev2.moxian.com:8080/mo_common_user/m1/mobilephone/updatemobilephone'
            break
        elif env == '2':
            url = 'http://login.moxiancn.com/mo_common_login/m1/auth/login'
            url2 = 'http://sso.moxiancn.com/mo_common_sso/m1/mobilephone/updatemobilephone'
            break        
        elif env == '3':
            url = 'http://login.spellthread.com/mo_common_login/m1/auth/login'
            url2 = 'http://sso.spellthread.com:80/mo_common_sso/m1/mobilephone/updatemobilephone'
            break
        else:
            print "Input error!"
    except: pass
        

useraccount = "86"+raw_input("输入需要更新的手机号码：")
userpass = raw_input("输入密码：")
phoneNo = "86"+raw_input("输入需要更改的手机号：")

query_args = {
              "useraccount": useraccount,
              "userpass": userpass,
              "loginAppType":"moxian"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(query_args),headers=headers)
result = r.json()

print result

token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
#print token,userId

payload ={
           "userId": userId,
           "email": "",
           "validateCode": "",
           "countryCode": "86",
           "phoneNo": phoneNo
}
headers = {'content-type': 'application/json', 'userId': userId ,'token': token }
r = requests.post(url2, json.dumps(payload), headers=headers)
print r.json()
print r.status_code
res = r.json()
command = 'pause'
os.system(command) 

if __name__ == "__main__":
    run()
