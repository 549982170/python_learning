# !/usr/bin/python 
# -*-coding:utf-8-*- 

import sys 
import json 
import requests 
from login_public import Login 
 
#------------加关注------------------ 
def addFans(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/fans'
    payload ={
             "id":"14"
             }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, params=payload, headers=headers)
    return r 

#------------取消关注------------------
def delFans(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/fans'
    payload ={
             "id":"14"
             }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.delete(url, params=payload, headers=headers)
    return r 

#------------关注商家------------------
def addMerchant(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/fans/merchant'
    payload ={
             "id":"1"
             }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, params=payload, headers=headers)
    return r 

#------------取消关注商家------------------
def delMerchant(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/fans/merchant'
    payload ={
             "id":"1"
             }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.delete(url, params=payload, headers=headers)
    return r 

#------------修改备注------------------
def remark(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/fans/remark'
    payload ={
             "content": "修改备注",
             "userId": 1
             }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url,data = json.dumps(payload), headers=headers)
    return r 

#------------用户消息屏蔽------------------
def notify(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/fans/remark'
    payload ={
             "friendId": 2,
             "notity": "false"
             }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url,data = json.dumps(payload), headers=headers)
    return r 

#------------屏蔽消息修改------------------
def notifyEdit(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/fans/remark'
    payload ={
             "friendId": 2,
             "notity": "true"
             }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url,data = json.dumps(payload), headers=headers)
    return r 













#------------测试加关注------------------  
def test_addFans(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = addFans(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试加关注："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"    

#------------测试取消关注------------------
def test_delFans(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = delFans(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试取消关注："     
    print r.json()
    #print r.json() 
    #print r.status_code     
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"

#------------测试关注商家------------------
def test_addMerchant(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = addMerchant(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试关注商家："     
    print r.json()
    #print r.json() 
    #print r.status_code     
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"

#------------测试取消关注商家------------------
def test_delMerchant(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = delMerchant(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试取消关注商家：" 
    print r.json()
    #print r.json() 
    #print r.status_code     
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"

#------------测试修改备注------------------
def test_remark(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = remark(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试修改备注：" 
    print r.json()
    #print r.json() 
    #print r.status_code     
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"

#------------测试用户消息屏蔽------------------
def test_notify(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = notify(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试用户消息屏蔽：" 
    print r.json()
    #print r.json() 
    #print r.status_code     
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"

#------------屏蔽消息修改------------------
def test_notifyEdit(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = notifyEdit(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试屏蔽消息修改：" 
    print r.json()
    #print r.json() 
    #print r.status_code     
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"

    
 
if __name__ == '__main__': 
    test_addFans() 
    test_delFans() 
    test_addMerchant()
    test_delMerchant()
    test_remark()
    test_notify()
    test_notifyEdit()