#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

根据函数名称动态调用
"""


def do_foo():
    print "foo!"


def do_bar():
    print "bar!"


class Print():
    def do_foo(self):
        print "foo!"

    def do_bar(self):
        print "bar!"

    @staticmethod
    def static_foo():
        print "static foo!"

    @staticmethod
    def static_bar():
        print "static bar!"


def main():
    obj = Print()

    func_name = "do_foo"
    static_name = "static_foo"
    eval(func_name)()
    getattr(obj, func_name)()
    getattr(Print, static_name)()

    func_name = "do_bar"
    static_name = "static_bar"
    eval(func_name)()
    getattr(obj, func_name)()
    getattr(Print, static_name)()


if __name__ == '__main__':
    main()



# env.roledefs = {
# 'server1': ['appuser@192.168.11.211:22', ],
#     'server2': ['appuser@119.29.72.22:22', ]
# }
# 密码一致情况下使用
# env.password = 'appuser'


# 密码不一致情况下使用,改用ssh安全性更高
# env.passwords = {
#     'appuser@192.168.11.211:22': 'appuser',
#     'appuser@119.29.72.22:22': 'appuser'
# }
