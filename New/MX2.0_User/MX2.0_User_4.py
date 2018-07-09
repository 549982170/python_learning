# !/usr/bin/python 
# -*-coding:utf-8-*- 

import sys 
import json 
import requests 
from login_public import Login 
 
#------------新增第三方授权信息------------------ 
def thirdParty(login_uerId, login_token): 
    url = 'http://dev2.moxian.com:80/mo_common_user/m1/thirdParty'  
    payload ={
               "id": 0,      
               "userId": 0,         #用户的魔线id
               "thirdPartyId": 0,   #第三方平台id 
               "thirdPartyName": "",#第三方平台名称 （1：SinaWeibo，2：Facebook，3：Twitter）
               "thirdPartyDb": ""   #第三方平台数据
             }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, data = json.dumps(payload), headers=headers)
    return r 

#------------更新第三方授权信息------------------ 
def thirdPartyUp(login_uerId, login_token): 
    url = 'http://dev2.moxian.com:80/mo_common_user/m1/thirdParty'  
    payload ={
               "id": 0,      
               "userId": 0,         #用户的魔线id
               "thirdPartyId": 0,   #第三方平台id 
               "thirdPartyName": "",#第三方平台名称 （1：SinaWeibo，2：Facebook，3：Twitter）
               "thirdPartyDb": ""   #第三方平台数据
             }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url, data = json.dumps(payload), headers=headers)
    return r 

#------------获取用户所有第三方授权信息------------------ 
def thirdPartyUp(login_uerId, login_token): 
    url = 'http://dev2.moxian.com:80/mo_common_user/m1/thirdParty'  
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, headers=headers)
    return r 

#------------删除一条第三方授权信息记录------------------ 
def thirdPartyDel(login_uerId, login_token): 
    url = 'http://dev2.moxian.com:80/mo_common_user/m1/thirdParty'  
    payload ={
                    "shopId": "12",    
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, headers=headers)
    return r 









#------------测试更新第三方授权信息-------------------  
def test_thirdParty(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = thirdParty(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试更新第三方授权信息："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"    

#------------测试更新第三方授权信息------------------  
def test_thirdPartyUp(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = thirdPartyUp(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试更新第三方授权信息："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n" 

#------------测试获取用户所有第三方授权信息------------------  
def test_thirdPartyGet(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = thirdPartyGet(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试更新第三方授权信息："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  

#------------测试删除一条第三方授权信息记录------------------  
def test_thirdPartyDel(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = thirdPartyDel(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试删除一条第三方授权信息记录："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  









if __name__ == '__main__': 
    test_messageremind()
    test_thirdPartyUp()
    test_thirdPartyGet()
    test_thirdPartyDel()