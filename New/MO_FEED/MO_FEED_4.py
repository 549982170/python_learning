# !/usr/bin/python 
# -*-coding:utf-8-*- 

import sys 
import json 
import requests 
from login_public import Login 
 
#------------提交举报------------------ 
def report(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/report'
    payload ={
                 "type": "EROTICISM",       #状态 值EROTICISM,CHEAT,ABUSES,ADVERTISEMENT,POLITICAL,TORT 
                 "postuuid": "2",           #动态ID，viki错误写成postid
                 "content": "测试提交举报"       #内容,viki错误写成comment
              } 
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url, data = json.dumps(payload), headers=headers)
    return r 

#------------删除举报------------------ 
def reportDel(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/report/2'   #数字为举报ID
    payload ={
                     "reportId": "2",       #举报ID，与开发环境Swagger UI提交方式不符
              }     
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.delete(url, data = json.dumps(payload), headers=headers)
    return r 

#------------举报详情------------------ 
def findone(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/report/2/findone'   #数字为举报ID   
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, headers=headers)
    return r 

#------------动态所有举报------------------ 
def reportAll(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/report/2'   #数字为举报ID   
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, headers=headers)
    return r 













#------------测试提交举报------------------  
def test_report(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = report(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试提交举报："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试删除举报------------------  
def test_reportDel(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = reportDel(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试删除举报："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"

#------------测试举报详情------------------  
def test_findone(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = findone(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试举报详情："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"

#------------测试动态所有举报------------------  
def test_reportAll(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = reportAll(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试动态所有举报："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"
        


if __name__ == '__main__': 
    test_report()
    test_reportDel()
    test_findone()
    test_reportAll()