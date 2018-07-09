# coding:utf-8
#!/user/bin/python
'''
Created on 2017年10月9日
@author: yizhiwu
人员签到模块测试
'''
import json
from mytest.util import myrequest

# 人员签到
url = "/api/signin"
playload = {
    "projectid": 462,
    "personnelId":109,
    "signintype":2,
    "location":"116.407526,39.90403"
    
}

result = myrequest(url, playload=playload, data_type="json")
print result.json()


# 人员绑定
url = "/api/personnelbinding"
playload = {
    "openId":"da457125dsaffaf545785",
    "idcard":"123",
    "phone":13148817565
}
# result = myrequest(url, playload=playload, data_type="json")
# print result.json()

# 人员签到项目列表
url = "/api/getprojectInfo"
playload = {
    "openId":"da457125dsaffaf54578",
}
# result = myrequest(url, playload=playload, data_type="json")
# print result.json()

# 人员签到项目列表
url = "/api/getsinginInfo"
playload = {
    "projectid":1,
    "personnelid":109,
    
    
}
# result = myrequest(url, playload=playload, data_type="json")
# print result.json()


