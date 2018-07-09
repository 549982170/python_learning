# !/usr/bin/python 
# -*-coding:utf-8-*- 

import sys 
import json 
import requests 
from login_public import Login 
 
#------------发布评论------------------ 
def comment(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/comment'
    payload ={
                 "postuuid": "2",       #动态ID
                 "replyComment": 0,     #viki没写？
                 "content": "评论",     #内容
                 "status":"NORMAL",     #状态 值（NORMAL, UNNORMAL）
                 "userId":login_uerId  #用户ID
              } 
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, data = json.dumps(payload), headers=headers)
    return r 

#------------删除评论------------------ 
def commentDel(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/comment/1'   #数字为评论ID
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.delete(url, headers=headers)
    return r 

#------------评论详情------------------ 
def findone(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/comment/1/findone' #数字为评论ID
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, headers=headers)
    return r 

#------------动态所有评论------------------ 
def commentAll(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/comment/1' #数字为动态ID
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, headers=headers)
    return r 









#------------测试发布评论------------------  
def test_comment(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = comment(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试发布评论："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   
        
#------------测试删除评论------------------  
def test_commentDel(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = commentDel(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试删除评论："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  

#------------测试评论详情------------------  
def test_findone(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = findone(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试评论详情："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  

#------------动态所有评论------------------  
def test_commentAll(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = commentAll(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试动态所有评论："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  


        
        
if __name__ == '__main__': 
    test_comment()
    test_commentDel()
    test_findone()
    test_commentAll()