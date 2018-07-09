# !/usr/bin/python 
# -*-coding:utf-8-*- 

import sys 
import json 
import requests 
from login_public import Login 
 
#------------添加收货地址------------------ 
def deliveryaddress(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com:80/mo_moxian/m1/deliveryaddress'
    payload ={
               "id": 0,   #地址id
               "userId": login_uerId, #用户id
               "address1": "收货地址1",  #收货地址1
               "address2": "收货地址2",  #收货地址2
               "recipients": "收货人",   #收货人
               "areaCode": "86",   #所在地码
               "areaName": "深圳",  #所在地名称
               "phoneNo": "13800138000", #收货人电话号码
               "postcode": "512123"    #收货地址邮编
             }    
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, data = json.dumps(payload), headers=headers)
    return r 

#------------获取用户所有收货地址------------------ 
def deliGet(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com:80/mo_moxian/m1/deliveryaddress'  
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, headers=headers)
    return r 

#------------删除一个收货地址------------------ 
def deliDel(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com:80/mo_moxian/m1/deliveryaddress' 
    payload ={
                    "addressId": "1", #地址id
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.delete(url, params=payload, headers=headers)
    return r 

#------------编辑收货地址------------------ 
def deliEdit(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com:80/mo_moxian/m1/deliveryaddress' 
    payload ={
                "id": 0,        #地址id
                "address1": "收货地址1",#收货地址1
                "address2": "收货地址2",#收货地址2
                "recipients": "收货人",#收货人
                "areaCode": "86",    #所在地码
                "areaName": "深圳",#所在地名称
                "phoneNo": "18998405382",     #收货人电话号码
                "postcode": "512123",     #收货地址邮编
                "userId":login_uerId
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url, data = json.dumps(payload), headers=headers)
    return r 

#------------设置默认地址------------------ 
def setdefault(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com:80/mo_moxian/m1/deliveryaddress/setdefault' 
    payload ={
                "id": 0,        #地址id
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url, data = json.dumps(payload), headers=headers)
    return r 












#------------测试添加收货地址------------------  
def test_deliveryaddress(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = deliveryaddress(login_uerId, login_token) 
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

#------------测试获取用户所有收货地址------------------  
def test_deliGet(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = deliGet(login_uerId, login_token) 
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

#------------测试删除一个收货地址------------------  
def test_deliDel(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = deliDel(login_uerId, login_token) 
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

#------------测试编辑收货地址------------------  
def test_deliEdit(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = deliEdit(login_uerId, login_token) 
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

#------------测试设置默认地址------------------  
def test_setdefault(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = setdefault(login_uerId, login_token) 
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
    test_deliveryaddress()
    test_deliGet()
    test_deliDel()
    test_deliEdit()
    test_setdefault()
