#!user/bin/python
# encoding:utf-8

queryResult = (20000, 20001)


def checkargs(func):
    """检查输出不存在的输入分服"""

    def call_it(*args, **kwargs):
        svrList = []
        for ca in queryResult:
            svrList.append(str(ca))
        for a_svr in args:
            if a_svr and a_svr not in svrList:
                print "The service id does not exist in 'tb_server':"
        func(*args)

    return call_it

flag = False
def createSvr(*args):
    print '1'
    global queryResult, flag
    queryResult = (20000, 20001, 20002)
    # flag = True
    run_redis('20002')


@checkargs
def run_redis(*args):
    for ca in queryResult:
        s_name = str(ca)
        if args:  # 有传入特定分服时只执行分服
            if s_name not in args:
                continue
        if not flag:
            if True:
                print "not do"
                continue
        print "do"


if __name__ == '__main__':
    createSvr()
