# !/usr/bin/python 
# -*-coding:utf-8-*- 

import sys 
import json 
import requests 
from login_public import Login 
 
#------------添加收货地址------------------ 
def messageremind(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/messageremind'  
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, headers=headers)
    return r 

#------------设置消息提醒------------------ 
def messageremind_(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/messageremind' 
    payload ={
                "isRemindOpen": 0, #是否开启 0 否 1 是
                "disturb": 0,      #免打扰是否开启 0 否 1 是
                "startTime": 0,    #免打扰开启开始时间 (单位 时间戳)
                "endTime": 0,      #免打扰开启结束时间 (单位 时间戳 )
                "sound": 0,        #声音是否开启 0 否 1 是
                "appType": 0,      
                "vibration": 0,     #震动是否开启 0 否 1 是
                "userId":""
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url, data = json.dumps(payload), headers=headers)
    return r 












#------------测试添加收货地址------------------  
def test_messageremind(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = messageremind(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试添加收货地址："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"    

#------------测试设置消息提醒------------------  
def test_messageremind_(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = messageremind_(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试添加收货地址："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"    






if __name__ == '__main__': 
    test_messageremind()
    test_messageremind_()