# !/usr/bin/python 
# -*-coding:utf-8-*- 

import sys 
import json 
import requests 
from login_public import Login 
 
#------------创建群组------------------ 
def addGroup(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/group'
    payload ={   
                  "name": "创建群组"    #组名不能重复
              }    
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url,data = json.dumps(payload),headers=headers)    #接口文档写了用get请求
    return r 

#------------删除群组------------------ 
def delGroup(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/group/1'  #后面的数字为组id   
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.delete(url,headers=headers)    
    return r 

#------------编辑组名------------------ 
def editGroup(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/group/1'  #后面的数字为组id
    payload ={   
                  "name": "创建群组2"             #组名不能重复
              }    
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url,data = json.dumps(payload),headers=headers)   
    return r 

#------------查询组好友列表------------------ 
def searchGroup(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/group/1/friends'  #里面的数字为组id  
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url,headers=headers)    
    return r 

#------------添加成员------------------ 
def addFriends(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/group/1/addFriends'  #里面的数字为组id  
    payload ={   
                      "fids": "[0]"            #好友id数组
              }    
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url,data = json.dumps(payload),headers=headers)    
    return r 

#------------删除成员------------------ 
def delFriends(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/group/1/removeFriends'  #里面的数字为组id  
    payload ={   
                      "fids": "[0]"            #好友id数组
              }    
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url,data = json.dumps(payload),headers=headers)   
    return r 

#------------组列表------------------ 
def groupList(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/group'      
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url,headers=headers)    
    return r 

#------------未加组好友------------------ 
def notingroup(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_pal/api/group/1/notincurrentfriends' #里面的数字为组id,接口文档没有写“1”数值       
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url,headers=headers)    
    return r 









#------------测试创建群组------------------  
def test_addGroup(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = addGroup(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试创建群组："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  

#------------测试删除群组------------------  
def test_delGroup(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = delGroup(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试删除群组："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  

#------------测试编辑组名------------------  
def test_editGroup(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = editGroup(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试编辑组名："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  

#------------测试查询组好友列表------------------  
def test_searchGroup(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = searchGroup(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试查询组好友列表："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  

#------------测试添加成员------------------  
def test_addFriends(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = addFriends(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试添加成员："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  

#------------测试删除成员------------------  
def test_delFriends(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = delFriends(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试删除成员："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  

#------------测试组列表------------------  
def test_groupList(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = groupList(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试组列表："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  
#------------未加组好友------------------  
def test_notingroup(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = notingroup(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试未加组好友："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"  




if __name__ == '__main__': 
    test_addGroup()
    test_delGroup()
    test_editGroup()
    test_searchGroup()
    test_addFriends()
    test_delFriends()
    test_groupList()
    test_notingroup()