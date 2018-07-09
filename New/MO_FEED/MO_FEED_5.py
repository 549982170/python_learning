# !/usr/bin/python 
# -*-coding:utf-8-*- 

import sys 
import json 
import requests 
from login_public import Login 
 
#------------新增推送信息------------------ 
def postinfo(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/postinfo'
    payload ={
                "postuuid": "2",                #动态ID,viki写成postid
                "user": login_uerId,            #用户ID，viki写成userid
                "content": "测试新增推送信息",         #内容，viki写成comment
                "type": "STAR",                #状态 值TRANSPOND,COMMENT,STAR
                "active": "y",                  #状态 值y,n,d
                "avatarUrl": ""                 #viki没有写？
             }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, data = json.dumps(payload), headers=headers)
    return r 

#------------删除动态推送信息------------------ 
def postinfoDel(login_uerId, login_token): 
    url = 'http://dev2.moxian.com:80/mo_moment/api/postinfo/2'
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.delete(url, headers=headers)
    return r 

#------------删除用户推送信息------------------ 
def postinfoDelUser(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/postinfo'
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.delete(url, headers=headers)
    return r 

#------------推送信息详情------------------ 
def findone(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/postinfo/2/findone' #数字为推送信息ID
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, headers=headers)
    return r 

#------------动态所有推送信息------------------ 
def postinfoAll(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/postinfo/2' #数字为动态ID
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, headers=headers)
    return r 

#------------用户所有推送信息------------------ 
def postinfoUser(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/postinfo' #数字为动态ID
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, headers=headers)
    return r 











#------------测试新增推送信息------------------  
def test_postinfo(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = postinfo(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试新增推送信息："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试删除动态推送信息------------------  
def test_postinfoDel(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = postinfoDel(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试删除动态推送信息："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试删除用户推送信息------------------  
def test_postinfoDelUser(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = postinfoDelUser(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试删除动态推送信息："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"

#------------测试推送信息详情------------------  
def test_findone(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = findone(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试推送信息详情："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   
        
#------------测试动态所有推送信息------------------  
def test_postinfoAll(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = postinfoAll(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试动态所有推送信息："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试用户所有推送信息------------------  
def test_postinfoUser(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = postinfoUser(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试动态所有推送信息："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   
        
 
 
 
        
if __name__ == '__main__': 
    test_postinfo()
    test_postinfoDel()
    test_postinfoDelUser()
    test_findone()
    test_postinfoAll()
    test_postinfoUser()