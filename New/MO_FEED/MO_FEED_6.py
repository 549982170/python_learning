# !/usr/bin/python 
# -*-coding:utf-8-*- 

import sys 
import json 
import requests 
from login_public import Login 
 
#------------新增收藏------------------ 
def favorites(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/favorites'
    payload ={
                "postuuid": "4",  #动态ID,viki写成postid
                "active": "y"     #状态 值y,n,d
             }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, data = json.dumps(payload), headers=headers)
    return r 

#------------删除收藏------------------ 
def favoritesDel(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/favorites/4' #数字为收藏ID
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.delete(url, headers=headers)
    return r 

#------------清空收藏------------------ 
def favoritesDelAll(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/favorites' #数字为收藏ID
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.delete(url, headers=headers)
    return r 

#------------查看收藏动态列表------------------ 
def favoritesList(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/favorites' #数字为收藏ID
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, headers=headers)
    return r 












#------------测试新增收藏------------------  
def test_favorites(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = favorites(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试新增新增收藏："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试删除收藏------------------  
def test_favoritesDel(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = favoritesDel(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试删除收藏："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"

#------------测试清空收藏------------------  
def test_favoritesDelAll(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = favoritesDelAll(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试清空收藏："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------查看收藏动态列表------------------  
def test_favoritesList(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = favoritesList(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试查看收藏动态列表："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  
        
        
        


if __name__ == '__main__': 
    test_favorites()
    test_favoritesDel()
    test_favoritesDelAll()
    test_favoritesList()