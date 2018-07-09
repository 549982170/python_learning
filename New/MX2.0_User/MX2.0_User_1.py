# !/usr/bin/python 
# -*-coding:utf-8-*- 

import sys 
import json 
import requests 
from login_public import Login 
 
#------------获取个人资料------------------ 
def userprofile(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/userprofile'
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, headers=headers)
    return r 

#------------编辑昵称------------------ 
def baseinfo_Name(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/userprofile/baseinfo'
    payload ={
                "nickName": "编辑昵称",   #用户昵称
                "areaCode": "",
                "birthday": "",
                "birthdayViableType": 0,
                "lastDailyMood": "",
                "tags": "",
                "homeTown": "",
                "favoritePlace": "",
                "school": "",
                "major": "",
                "expertise": "",
                "type": 0,     #类型 (1修改昵称2所在地3生日4隐藏生日5每日心情6标签7家乡8出没地9学校专业10专长11地理位置是否可见)
                "userId": 0,
                "locationVisibility": 0
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url,data = json.dumps(payload), headers=headers)
    return r 

#------------编辑所在地------------------ 
def baseinfo_Area(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/userprofile/baseinfo'
    payload ={
                "nickName": "编辑昵称",   
                "areaCode": "深圳",        #所在地
                "birthday": "",
                "birthdayViableType": 0,
                "lastDailyMood": "",
                "tags": "",
                "homeTown": "",
                "favoritePlace": "",
                "school": "",
                "major": "",
                "expertise": "",
                "type": 0,     #类型 (1修改昵称2所在地3生日4隐藏生日5每日心情6标签7家乡8出没地9学校专业10专长11地理位置是否可见)
                "userId": login_uerId,
                "locationVisibility": 0
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url,data = json.dumps(payload), headers=headers)
    return r 

#------------编辑生日------------------ 
def baseinfo_Birthday(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/userprofile/baseinfo'
    payload ={
                "nickName": "编辑昵称",   
                "areaCode": "深圳",        
                "birthday": "1432029552",         #生日
                "birthdayViableType": 0,
                "lastDailyMood": "",
                "tags": "",
                "homeTown": "",
                "favoritePlace": "",
                "school": "",
                "major": "",
                "expertise": "",
                "type": 0,     #类型 (1修改昵称2所在地3生日4隐藏生日5每日心情6标签7家乡8出没地9学校专业10专长11地理位置是否可见)
                "userId": login_uerId,
                "locationVisibility": 0
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url,data = json.dumps(payload), headers=headers)
    return r 

#------------编辑生日------------------ 
def baseinfo_BirType(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/userprofile/baseinfo'
    payload ={
                "nickName": "编辑昵称",   
                "areaCode": "深圳",        
                "birthday": "1432029552",         
                "birthdayViableType": 0,  #隐藏年龄 （0 不隐藏 1 隐藏）
                "lastDailyMood": "",
                "tags": "",
                "homeTown": "",
                "favoritePlace": "",
                "school": "",
                "major": "",
                "expertise": "",
                "type": 0,     #类型 (1修改昵称2所在地3生日4隐藏生日5每日心情6标签7家乡8出没地9学校专业10专长11地理位置是否可见)
                "userId": login_uerId,
                "locationVisibility": 0
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url,data = json.dumps(payload), headers=headers)
    return r 

#------------编辑每日心情------------------ 
def baseinfo_Mood(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/userprofile/baseinfo'
    payload ={
                "nickName": "编辑昵称",   
                "areaCode": "深圳",        
                "birthday": "1432029552",         
                "birthdayViableType": 0,  
                "lastDailyMood": "今天是个美好的一天！",    #每日心情
                "tags": "",
                "homeTown": "",
                "favoritePlace": "",
                "school": "",
                "major": "",
                "expertise": "",
                "type": 0,     #类型 (1修改昵称2所在地3生日4隐藏生日5每日心情6标签7家乡8出没地9学校专业10专长11地理位置是否可见)
                "userId": login_uerId,
                "locationVisibility": 0
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url,data = json.dumps(payload), headers=headers)
    return r 

#------------获取系统标签列表------------------ 
def systemtagsinfo(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/userprofile/systemtagsinfo'
    payload ={
                "countryCode": "86",   #电话区号
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url,params=payload, headers=headers)
    return r 

#------------设置标签------------------ 
def baseinfoSet(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/userprofile/baseinfo'
    payload ={
                "countryCode": "86",   #电话区号
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url,data = json.dumps(payload), headers=headers)
    return r 

#------------编辑家乡------------------ 
def HomeTown(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/userprofile/baseinfo'
    payload ={
                "homeTown": "三水",   #家乡
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url,data = json.dumps(payload), headers=headers)
    return r 

#------------编辑出没地------------------ 
def favoritePlace(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/userprofile/baseinfo'
    payload ={
                "favoritePlace": "三水",   #出没地
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url,data = json.dumps(payload), headers=headers)
    return r 

#------------编辑学校------------------ 
def school(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/userprofile/baseinfo'
    payload ={
                "type": "9",   #类型 (1 修改昵称 2 所在地 3 生日 4 隐藏生日 5 每日心情 6 标签 7 家乡 8 出没地 9 学校 专业 10 专长)
                "school": "哈尔滨佛教大学",   #学校
                "expertise": "打杂",   #专业
                "userId": login_uerId,   #用户id
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url,data = json.dumps(payload), headers=headers)
    return r 

#------------编辑专长------------------ 
def major(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/userprofile/baseinfo'
    payload ={
                "type": "10",   #类型 (1 修改昵称 2 所在地 3 生日 4 隐藏生日 5 每日心情 6 标签 7 家乡 8 出没地 9 学校 专业 10 专长)
                "major": "专长",   #专长
                "userId": login_uerId,   #用户id
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url,data = json.dumps(payload), headers=headers)
    return r 

#------------编辑设置地理位置可见------------------ 
def Visibility(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/userprofile/baseinfo'
    payload ={
                "type": "11",   #类型 (1 修改昵称 2 所在地 3 生日 4 隐藏生日 5 每日心情 6 标签 7 家乡 8 出没地 9 学校 专业 10 专长 11 地理位置是否可见)
                "locationVisibility": "0",   #地理位置是否可见 0 可见 1不可见
                "userId": login_uerId,   #用户id
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.put(url,data = json.dumps(payload), headers=headers)
    return r 

#------------上传头像------------------ 
def uploadavatar(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/avatar/uploadavatar'
    payload ={
                "avatarId": "1",   #头像id
                "avatarPath": "0",   #上传成功后的路径
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url,data = json.dumps(payload), headers=headers)
    return r 

#------------获取头像列表------------------ 
def getavatar(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/avatar/getavatar'
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.get(url, headers=headers)
    return r 

#------------设置为头像头像------------------ 
def setavatar(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/avatar/setavatar'
    payload ={
                "avatarId": "1",   #头像id
                "userId": login_uerId,   #用户Id
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url,data = json.dumps(payload), headers=headers)
    return r 

#------------设置删除头像------------------ 
def delete(login_uerId, login_token): 
    url = 'http://moxian.dev2.moxian.com/mo_moxian/m1/avatar/delete'
    payload ={
                "avatarId": "1",   #头像id
              }
    headers = {'content-type': 'application/json', 'userId': login_uerId ,'token': login_token }
    r = requests.post(url,data = json.dumps(payload), headers=headers)
    return r 














#------------测试获取个人资料------------------  
def test_userprofile(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = userprofile(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试获取个人资料："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"    

#-----------------测试编辑昵称-----------------------  
def test_baseinfo_Name(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = baseinfo_Name(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试编辑昵称："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"    

#------------测试编辑所在地------------------  
def test_baseinfo_Area(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = baseinfo_Area(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试编辑所在地："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"    

#------------测试编辑生日------------------  
def test_baseinfo_Birthday(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = baseinfo_Birthday(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试编辑生日："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试隐藏年龄------------------  
def test_baseinfo_BirType(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = baseinfo_BirType(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试隐藏年龄："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试编辑每日心情-----------------  
def test_baseinfo_Mood(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = baseinfo_Mood(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试编辑每日心情："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试获取系统标签列表-----------------  
def test_systemtagsinfo(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = systemtagsinfo(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试获取系统标签列表："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试设置标签-----------------  
def test_baseinfoSet(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = baseinfoSet(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试设置标签："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试编辑家乡-----------------  
def test_HomeTown(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = HomeTown(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试编辑家乡："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试编辑出没地-----------------  
def test_favoritePlace(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = favoritePlace(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试编辑出没地："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试编辑学校-----------------  
def test_school(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = school(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试编辑学校："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试编辑专长-----------------  
def test_major(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = major(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试编辑专长："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试设置地理位置可见-----------------  
def test_Visibility(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = Visibility(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试设置地理位置可见："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试上传头像-----------------  
def test_uploadavatar(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = uploadavatar(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试上传头像："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试获取头像列表-----------------  
def test_getavatar(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = getavatar(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试获取头像列表："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试设置为头像-----------------  
def test_setavatar(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = setavatar(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试获取头像列表："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   

#------------测试删除头像-----------------  
def test_delete(): 
    a = Login
    login_uerId = a.login("login_uerId") 
    login_token = a.login("login_token")   #uerId不变，token改变，故可以请求两次
    r = delete(login_uerId, login_token) 
    res = r.json() 
    result = res.get(u'result') 
    #assert str(r.status_code) == '200' and result == False    断言正确性
    print "测试获取头像列表："    
    print r.json()
    #print r.json() 
    #print r.status_code
    if str(r.status_code) == '200' and result == True:
        print sys._getframe().f_code.co_name + "-------------is OK!\n"
    else:
        print sys._getframe().f_code.co_name + "-------------is Error!\n"   













    
 
if __name__ == '__main__': 
    test_userprofile() 
    test_baseinfo_Name()
    test_baseinfo_Area()
    test_baseinfo_Birthday()
    test_baseinfo_BirType()
    test_baseinfo_Mood()
    test_systemtagsinfo()
    test_baseinfoSet()
    test_HomeTown()
    test_favoritePlace()
    test_school()
    test_major()
    test_Visibility()
    test_uploadavatar()
    test_getavatar()
    test_setavatar()
    test_delete()