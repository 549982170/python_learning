#!user/bin/python
#encoding:utf-8
import requests
import json
motype = 'mobiz'
user = '8618126274558'
pwd = '111111'

def getToken(user,pwd):
    url = 'http://login.moxiancn.com/mo_common_login/m2/auth/login'
    query_args = {
                  "useraccount": user,#帐号
                  "userpass": pwd,          #密码 
                  "loginAppType":motype
                  }
    headers = {'content-type': 'application/json'}
    r = requests.post(url,json.dumps(query_args),headers=headers)
    result = r.json()
    token = result.get(u'data').get(u'token')
    token = str(token)
    userId = str(result.get(u'data').get(u'userId'))
    return (token,userId)

#获取公司ID
token,userId = getToken(user,pwd)
#print u'用户的ID：',userId
#print u'登录的token：',token
url = 'http://mobiz.moxiancn.com/mo_biz/m2/role'
headers = {'content-type': 'application/json', 'userId': userId ,'token': token ,'appType': motype}
r = requests.get(url , headers=headers)
result = r.json()
companyId = str(result.get(u'data').get(u'companyId'))
#print u'公司ID:', companyId

#获取店铺列表
token,userId = getToken(user,pwd)
#print u'用户的ID：',userId
#print u'登录的token：',token
url = 'http://mobiz.moxiancn.com/mo_biz/m2/companies/index'
headers = {'content-type': 'application/json', 'userId': userId ,'token': token ,'appType': motype}
r = requests.get(url , headers=headers)
result = r.text
#print u'店铺列表:\n', result
#取第一个店铺ID，转换为字典
json_dict = json.loads(result) 
#遍历方式找数据，严重消耗性能
#for i in range(0,len(json_dict.get('data').get('shopList'))):   
    #shopId  = json_dict.get('data').get('shopList')[0].get('id')
#取全部店铺名字
#for i in json_dict.get('data').get('shopList'):   
    #shopName  = i.get('shopName')
    #print shopName
shopId  = str(json_dict.get('data').get('shopList')[0].get('id'))
#print shopId




#--------------------------------------------------------------------------
#测试导出粉丝报表
token,userId = getToken(user,pwd)
url = 'http://report.moxiancn.com/mo_report/m2/mobizReports/companies/'+companyId+'/shops/'+shopId+'/outputs/fans'
payload ={
            "companyId": companyId,
            "shopId":shopId,
            "email":"549982170@qq.com",
            "beginDate":"1419660110",
            "endDate":"1442197110"
            
          }


headers = {'content-type': 'application/json', 'userId': userId ,'token': token,'appType': motype}
r = requests.get(url,params = payload,headers=headers)
result = r.json()
result_msg = result.get(u'result')
print u'导出粉丝报表:\n',r.text
if str(r.status_code) == '200' and result_msg == True:
    print "Test pass!\n"
else:
    print "Test fail!\n" 
    
    
#--------------------------------------------------------------------------
#测试导出线下报表
token,userId = getToken(user,pwd)
url = 'http://report.moxiancn.com/mo_report/m2/mobizReports/companies/'+companyId+'/shops/'+shopId+'/outputs/consumers/stores'
payload ={
            "companyId": companyId,
            "shopId":shopId,
            "email":"549982170@qq.com",
            "beginDate":"1419660110",
            "endDate":"1442197110"
            
          }


headers = {'content-type': 'application/json', 'userId': userId ,'token': token,'appType': motype}
r = requests.get(url,params = payload,headers=headers)
result = r.json()
result_msg = result.get(u'result')
print u'导出线下报表:\n',r.text
if str(r.status_code) == '200' and result_msg == True:
    print "Test pass!\n"
else:
    print "Test fail!\n" 
    
    
    
#--------------------------------------------------------------------------
#测试导出线上报表
token,userId = getToken(user,pwd)
url = 'http://report.moxiancn.com/mo_report/m2/mobizReports/companies/'+companyId+'/shops/'+shopId+'/outputs/consumers/notwork/orders'
payload ={
            "companyId": companyId,
            "shopId":shopId,
            "email":"549982170@qq.com",
            "beginDate":"1419660110",
            "endDate":"1442197110"
            
          }


headers = {'content-type': 'application/json', 'userId': userId ,'token': token,'appType': motype}
r = requests.get(url,params = payload,headers=headers)
result = r.json()
result_msg = result.get(u'result')
print u'导出线上报表:\n',r.text
if str(r.status_code) == '200' and result_msg == True:
    print "Test pass!\n"
else:
    print "Test fail!\n" 
    
    
#--------------------------------------------------------------------------
#测试导出优惠券报表
token,userId = getToken(user,pwd)
url = 'http://report.moxiancn.com/mo_report/m2/mobizReports/companies/'+companyId+'/shops/'+shopId+'/outputs/coupons'
payload ={
            "companyId": companyId,
            "shopId":shopId,
            "email":"549982170@qq.com",
            "beginDate":"1419660110",
            "endDate":"1442197110"
            
          }


headers = {'content-type': 'application/json', 'userId': userId ,'token': token,'appType': motype}
r = requests.get(url,params = payload,headers=headers)
result = r.json()
result_msg = result.get(u'result')
print u'导出优惠券报表:\n',r.text
if str(r.status_code) == '200' and result_msg == True:
    print "Test pass!\n"
else:
    print "Test fail!\n" 




#--------------------------------------------------------------------------
#测试导出积分报表
token,userId = getToken(user,pwd)
url = 'http://report.moxiancn.com/mo_report/m2/mobizReports/companies/'+companyId+'/shops/'+shopId+'/outputs/points'
payload ={
            "companyId": companyId,
            "shopId":shopId,
            "email":"549982170@qq.com",
            "beginDate":"1419660110",
            "endDate":"1442197110"
            
          }


headers = {'content-type': 'application/json', 'userId': userId ,'token': token,'appType': motype}
r = requests.get(url,params = payload,headers=headers)
result = r.json()
result_msg = result.get(u'result')
print u'导出积分报表:\n',r.text
if str(r.status_code) == '200' and result_msg == True:
    print "Test pass!\n"
else:
    print "Test fail!\n" 