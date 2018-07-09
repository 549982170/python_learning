# !/usr/bin/python 
# -*-coding:utf-8-*- 

import sys 
import json 
import requests 
from login_public import Login 
 
#------------动态列表------------------ 
def postList(login_uerId, login_token): 
    url = 'http://www.moxiancn.com:80/mo_moment/api/post'
    payload ={
                "begin": "1",  #接口viki有错，没有这个
                "end": "2"     #接口viki有错，没有这个    
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, params=payload, headers=headers)
    return r 











#------------测试动态列表------------------  
def test_postList(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = postList(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试动态列表："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   
        




        
        
if __name__ == '__main__': 
    test_postList() 