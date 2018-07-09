# !/usr/bin/python 
# -*-coding:utf-8-*- 

import sys 
import json 
import requests 
from login_public import Login 
 
#------------通讯录搜索------------------ 
def phones(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/fans/phones'
    payload ={   
                 "phones": '["8613472858302"]'

              }    
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url,data = json.dumps(payload),headers=headers)    #接口文档写了用get请求
    return r 

#------------附近搜索------------------ 
def nearbyPeople(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/fans/nearby/people'
    payload ={   
                  "x": 0,             #经度
                  "y": 0,             #纬度
                  "gender": 0,        #性别
                  "visibility": "false",  
                  "createTime": "",
                  "updateTime": "",
                  "active": ""        #是否可见   
              }
    query_args = {
                  "page": "1",        #页码
                  "size": "10"        #记录数
                  }    
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url,data = json.dumps(payload),params = query_args,headers = headers)    
    return r 

#------------精确查找------------------ 
def users(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/fans/users'
    payload ={   
                 "condition":"14"

              }    
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url,params=payload,headers=headers)    
    return r 

#------------个人首页------------------ 
def homePage(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/fans/' + login_uerId
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url,headers=headers)    
    return r 

#------------保存位置------------------ 
def location(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/fans/location'
    payload ={
              "x": 0,      #经度
              "y": 0,      #纬度
              "gender": 0, 
              "visibility": "false",
              "active": "True" #是否可见
              }    
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url,data = json.dumps(payload),headers=headers)    
    return r 

#------------删除位置------------------ 
def delLocation(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/fans'
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.delete(url,headers=headers)    
    return r 













#------------测试通讯录搜索------------------  
def test_phones(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = phones(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试通讯录搜索："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  

#------------测试附近搜索------------------  
def test_nearbyPeople(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = nearbyPeople(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试附近搜索："    
    print r.json()
    #print r.url
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  
       
#------------测试精确查找------------------  
def test_users(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = users(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试精确查找："    
    print r.json()
    #print r.url
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"         
        
#------------测试个人首页------------------  
def test_homePage(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = homePage(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试个人首页："    
    print r.json()
    #print r.url
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"         
        
#------------测试个保存位置------------------  
def test_location(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = location(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试个保存位置："    
    print r.json()
    #print r.url
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"     

#------------测试删除位置------------------  
def test_delLocation(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = delLocation(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试删除位置："    
    print r.json()
    #print r.url
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"    





if __name__ == '__main__': 
    test_phones()
    test_nearbyPeople()
    test_users()
    test_homePage()
    test_location()
    test_delLocation()