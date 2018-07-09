# !/usr/bin/python 
# -*-coding:utf-8-*- 

import sys 
import json 
import requests 
from login_public import Login 
 
#------------发动态------------------ 
def post(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/post'
    payload ={
                "content": "内容",  #动态内容
                "latitude": 0,      #纬度    
                "longitude": 0,     #经度
                "forwardId": 0,     #转发动态ID
                "type": 0,          #动态可见代码类型 取值范围（0-公开,1-好友,2-指定组员,3-指定好友）
                "active": "y",      #动态状态
                "gids": [0],
                "fids": [0],
                "postResourceVo": [{"resourceValue": "","avatar": 0}]  #动态附件
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, data = json.dumps(payload), headers=headers)
    return r 

#------------点赞------------------ 
def star(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/post/0/star' #数字为动态id数
    payload ={
                "postid": "0",  #动态动态ID
                
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, data = json.dumps(payload), headers=headers)
    return r 

#------------取消赞------------------ 
def unstar(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/post/0/unstar' #数字为动态id数
    payload ={
                "postid": "0",  #动态动态ID
                
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, data = json.dumps(payload), headers=headers)
    return r 

#------------动态详情------------------ 
def postDetil(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/post/2' #数字为动态id数
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, headers=headers)
    return r 

#------------动态修改------------------ 
def postEdit(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/post/2' #数字为动态id数
    payload ={
                "content": "测试修改",   #动态文字
                "latitude": 0,          #纬度
                "longitude": 0,         #经度
                "forwardId": 0,         #转发动态ID
                "type": "PUBLIC",              #动态状态 取值范围 PUBLIC,FRIEND,GROUP,PART
                "active": "y",           #动态状态 取值范围 y,n,d
                "gids": [0],
                "fids": [0],
                "postResourceVo": [{"resourceValue": "","avatar": 0}]       #动态附件       
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url, data = json.dumps(payload), headers=headers)
    return r 

#------------删除动态------------------ 
def postDel(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/post/1' #数字为动态id数
    payload ={
                "postid": "1",  #动态ID
                
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.delete(url, data = json.dumps(payload), headers=headers)
    return r 

#------------草稿箱------------------ 
def draft(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/post/draft' 
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, headers=headers)
    return r 














#------------测试发动态------------------  
def test_post(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = post(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试发动态："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试点赞------------------  
def test_star(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = star(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试点赞："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"    

#------------测试取消赞------------------  
def test_unstar(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = unstar(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试取消赞："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试动态详情------------------  
def test_postDetil(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = postDetil(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试动态详情："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试动态修改------------------  
def test_postEdit(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = postEdit(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试动态修改："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试删除动态------------------  
def test_postDel(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = postDel(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试删除动态："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试草稿箱------------------  
def test_draft(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = draft(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试草稿箱："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   
        
        
        
        
if __name__ == '__main__': 
    test_post() 
    test_star()
    test_unstar()
    test_postDetil()
    test_postEdit()
    test_postDel()
    test_draft()