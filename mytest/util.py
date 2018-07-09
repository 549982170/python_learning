# coding:utf-8
#!/user/bin/python
'''
Created on 2017年9月15日
@author: yizhiwu
'''
import re
import requests
import json

# 配置
host = "http://d-planning.soovii.com:5000"
username = "wangxin02@soovii.com"
password = "123456",


login_url = host + '/user/login'  # 登录
agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
s = requests.Session()
s.headers.update({'User-Agent': agent})
r = s.get(login_url)
html = r.content
r1 = re.compile('content="(.*)"')
csrf_token = re.findall(r1, html)[1]


def myrequest(req_url, playload, data_type="", rtype="POST" ):
    url = host + req_url
    playload.update({"csrf_token": csrf_token})
    s.headers.update({'X-CSRFToken': csrf_token})
    if data_type == "json":
        playload = json.dumps(playload)
    if rtype == "POST":
        result = s.post(url, data=playload)
    elif rtype == "GET":
        result = s.get(url, data=playload)
    print "req:", playload
    return result


def loging_user(username, password):
    url = "/user/login"
    playload = {"username":username, "password":password}
    loging_result = myrequest(url, playload)
    print loging_result
    
    
# 登录
loging_user(username, password)

