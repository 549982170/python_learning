# !/usr/bin/python 
# -*-coding:utf-8-*- 

import sys 
import json 
import requests 
from login_public import Login 
 
#------------原密码校验方式修改------------------ 
def updateuserpwd(login_uerId, login_token): 
    url = 'http://sso.dev2.moxian.com/mo_common_sso/m1/updateuserpwd'
    payload ={
                "userId": 2,
                "password": "123123",
                "newPassword": "321321"
                      }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, data = json.dumps(payload), headers=headers)
    return r

#------------绑定邮箱发送验证码------------------ 
def sendemail(login_uerId, login_token): 
    url = 'http://sso.dev2.moxian.com/mo_common_sso/m1/email/sendemail'
    payload ={
                "userId": 2,
                "password": "123123",
                "newPassword": "321321"
                      }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, data = json.dumps(payload), headers=headers)
    return r 












#------------测试原密码校验方式修改------------------  
def test_updateuserpwd(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = updateuserpwd(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试原密码校验方式修改："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试绑定邮箱发送验证码------------------  
def test_updateuserpwd(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = updateuserpwd(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试原密码校验方式修改："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   



        
        
        
if __name__ == '__main__': 
    test_updateuserpwd()