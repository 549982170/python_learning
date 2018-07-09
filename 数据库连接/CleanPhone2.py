#!user/bin/python
# -*- coding:gb2312 -*-
import os
import requests
import json
#引入mysql python客户端模块
import MySQLdb
import sys
#dev: http://dev2.moxian.com:8080/mo_common_fileuploadservice/m1/upload
#moxiancn: http://www.moxiancn.com/mo_common_fileuploadservice/m1/upload
#showload: http://www.spellthread.com
while True:
    try:    
        env = raw_input("输入环境：1为dev，2为moxiancn，3为beta：")
        if env == '1':
            url = 'http://dev2.moxian.com:8080/mo_common_sso/m2/auth/login'
            url2 = 'http://dev2.moxian.com:8080/mo_common_user/m2/mobilephone/updatemobilephone'
            url3 = 'http://dev2.moxian.com:8080/mo_common_sso/m2/mobilephone/sendmessage'
            break
        elif env == '2':
            url = 'http://login.moxiancn.com/mo_common_login/m2/auth/login'
            url2 = 'http://sso.moxiancn.com/mo_common_sso/m2/mobilephone/updatemobilephone'
            url3 = 'http://sso.moxiancn.com/mo_common_sso/m2/mobilephone/sendmessage'
            #数据库连接
            conn_1 = MySQLdb.connect(host="172.16.1.29", user="readonly",passwd="dbtest123", db="moxian", charset="utf8")
            conn_2 = MySQLdb.connect(host="172.16.1.29", user="readonly",passwd="dbtest123", db="service", charset="utf8")
            break        
        elif env == '3':
            url = 'http://login.spellthread.com/mo_common_login/m1/auth/login'
            url2 = 'http://sso.spellthread.com:80/mo_common_sso/m1/mobilephone/updatemobilephone'
            url3 = 'http://sso.spellthread.com:80/mo_common_sso/m1/mobilephone/sendmessage'
            #数据库连接
            conn_1 = MySQLdb.connect(host="59.188.11.71", user="readonly",passwd="dbtest123", db="moxian", charset="utf8")
            conn_2 = MySQLdb.connect(host="59.188.11.71", user="readonly",passwd="dbtest123", db="service", charset="utf8")
            break
        else:
            print "Input error!"
    except: pass
        

useraccount = "86"+raw_input("输入需要更新的手机号码：")
#“86”为国家码，如登录为其他地区，则直接修改86即可，这一块就不从数据库取了。
#userpass = raw_input("输入密码：")
phoneNo2 = raw_input("输入需要更改的手机号：")
phoneNo = "86" + phoneNo2
#进行数据库连接
cursor = conn_1.cursor()
#执行sql
sql_1 = "SELECT user_base_password FROM user_user_base_sb WHERE user_base_phone=" + useraccount
#print sql
cursor.execute(sql_1)
#列出数据
records = cursor.fetchall()
for row in records:
    for p in row:
        userpass = p
#print userpass
print "登录密码为：" ,userpass

query_args = {
              "useraccount": useraccount,
              "userpass": userpass,
              "loginAppType":"mobiz"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(query_args),headers=headers)
result = r.json()

#print result
if r.status_code == 200:
    print "登录成功！"
else :
    print "登录失败，请检查登录接口！"

token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
#print token,userId

query_args2 = {
              "countryCode":"86",
              "phoneNo":phoneNo,
              "userId":userId
              }
headers = {'content-type': 'application/json','appType': 'mobiz','userId': userId ,'token': token}
r = requests.post(url3,json.dumps(query_args2),headers=headers)
result = r.json()
#print result

#进行数据库连接
cursor = conn_2.cursor()
#执行sql
sql_2 = "SELECT create_time,verify_record_verify_code FROM sms_verify_record_br WHERE verify_rocord_account = "+ phoneNo2 + " "+"order by create_time desc limit 1"
#print sql
cursor.execute(sql_2)
#列出数据
records = cursor.fetchall()
for row in records:
    for code in row:
        validateCode = code
#print validateCode
#print "接收的验证码为：",validateCode
if r.status_code == 200:
    print "获取验证码成功！"
    print "获取的验证码为：",validateCode
else :
    print "获取验证码失败，请检查获取验证码接口！"
payload ={
           "userId": userId,
           "email": "",
           "validateCode": validateCode,
           "countryCode": "86",
           "phoneNo": phoneNo
}
headers = {'content-type': 'application/json','appType': 'mobiz', 'userId': userId ,'token': token }
r = requests.post(url2, json.dumps(payload), headers=headers)
#print r.json()

if r.status_code == 200:
    print "改绑成功，改绑后的帐号为：",phoneNo2
    print "登录密码为：",userpass
    print "备注：旧的号码可以继续进行注册了！~"
else :
    print "帐号改绑失败！！"
res = r.json()
command = 'pause'
os.system(command) 

if __name__ == "__main__":
    run()
