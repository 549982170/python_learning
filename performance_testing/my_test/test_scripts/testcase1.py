# coding:utf-8
# !/user/bin/python
from util import myrequest

'''
Created on 2017年10月9日
@author: yizhiwu
性能测试用例1
'''


class Transaction(object):
    def __init__(self):
        pass

    def run(self):
        url = "/api/getprojectInfo"
        playload = {
            "openId": "da457125dsaffaf54578",
        }
        result = myrequest(url, playload=playload, data_type="json")
        print result.json()


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
