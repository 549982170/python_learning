#!user/bin/python
# encoding:utf-8
import re
import requests

host = 'http://debug-planning.soovii.com/:5000'  # 环境
url1 = host + '/user/login'  # 登录的url

agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
s = requests.Session()
s.headers.update({'User-Agent': agent})
r = s.get(url1)
html = r.content
r1 = re.compile('content="(.*)"')
csrf_token = re.findall(r1, html)[1]


def myrequest(url, playload, rtype="POST"):
    playload.update({"csrf_token": csrf_token})
    s.headers.update({'X-CSRFToken': csrf_token})
    if rtype == "POST":
        result = s.post(url, data=playload)
    elif rtype == "GET":
        result = s.get(url, data=playload)
    return result


def checkeStatusCode(result, statusCode=200):
    if result.status_code == statusCode:
        return "Test OK"
    return "Test fail"


if __name__ == '__main__':
    # 测试登录
    url = 'http://debug-planning.soovii.com/user/login'
    playload = {
        "username": "wangxin02@soovii.com",
        "password": "123456",
    }
    loging_result = myrequest(url, playload)
    assert loging_result.status_code == 200
    print "logingUrl:", checkeStatusCode(loging_result)

    # 测试修改角色
    url = 'http://debug-planning.soovii.com/character/api/countedit'
    playload = {
        "newName": "叶知秋",
        "EType": "1",
        "eId": "18954,18948,18958,18942"
    }
    countedit_result = myrequest(url, playload)
    assert countedit_result.status_code == 200
    print "counteditUrl:", checkeStatusCode(loging_result)
