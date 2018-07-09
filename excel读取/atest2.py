#!/usr/bin/python
# coding: UTF-8
import execjs
import urllib
import urllib2


class NetIn(object):
    def __init__(self):
        self.loginUrl = "http://202.113.112.30/0.htm"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        }
        self.values = {
            'DDDDD': "",
            'upass': "",
            'R1': "0",
            'R2': "1",
            'para': "00",
            '0MKKey': "123456",
            'v6ip': ""
        }

    def jiaMiPasswd(self):
        print "请输入您的密码"
        passwd = raw_input()
        jiaMiPasswd = execjs.compile(open(r"a41.js").read().decode("utf-8")).call('bingo', passwd)  # 这里a41.js已经移动到当前目录了
        return jiaMiPasswd


if __name__ == "__main__":
    netIn = NetIn()
    print "请输入您的账号："
    uname = raw_input()
    netIn.values['DDDDD'] = uname
    netIn.values['upass'] = netIn.jiaMiPasswd()
    postdata = urllib.urlencode(netIn.values)
    request = urllib2.Request(netIn.loginUrl, postdata, netIn.headers)
    response = urllib2.urlopen(request)
    print response.read().decode('gbk')  # 最后将页面信息打印出来查看是否成功登陆
