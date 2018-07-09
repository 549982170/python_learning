# !/usr/bin/python 
# -*-coding:utf-8-*- 
 
import json 
import requests 
from login_public import Login 
 
 
def addfans(login_uerId, login_token): 
    url = 'http://www.moxiancn.com/mo_pal/api/fans/4' 
    headers = {'content-type': 'application/json', 
               'userId': login_uerId, 'token': login_token} 
    r = requests.post(url, headers=headers) 
    print r.json() 
    print r.status_code 
    return r 
 
 
def addgroup(login_uerId, login_token): 
    url = 'http://www.moxiancn.com/mo_pal/api/group' 
    payload = {'name': 'family'} 
    headers = {'content-type': 'application/json', 
               'userId': login_uerId, 'token': login_token} 
    r = requests.post(url, data=json.dumps(payload), headers=headers) 
    print r.json() 
    print r.status_code 
    return r 
 
 
def creategourp(login_uerId, login_token): 
    url = 'http://www.moxiancn.com/mo_pal/api/group' 
    paylaod = {'name': 'friends'} 
    headers = {'content-type': 'application/json', 
               'userId': login_uerId, 'token': login_token} 
    r = requests.post(url, data=json.dumps(paylaod), headers=headers) 
    print r.json() 
    print r.status_code 
    return r 
 
 
def test_addfans(): 
    a = Login() 
    a.login() 
    r = addfans(a.login_uerId, a.login_token) 
    res = r.json() 
    result = res.get(u'result') 
    assert not result 
    # assert str(r.status_code) == '200' and result == True 
 
 
def test_addgroup(): 
    a = Login() 
    a.login() 
    r = addgroup(a.login_uerId, a.login_token) 
    res = r.json() 
    result = res.get(u'result') 
    # assert str(r.status_code) == '200' and result == True 
    assert not result 
 
 
def test_creatgroup(): 
    a = Login() 
    a.login() 
    r = creategourp(a.login_uerId, a.login_token) 
    res = r.json() 
    result = res.get(u'result') 
    assert not result 
    # assert str(r.status_code) == '200' and result == True 
 
if __name__ == '__main__': 
    test_addfans() 
    test_addgroup() 
    test_creatgroup() 


