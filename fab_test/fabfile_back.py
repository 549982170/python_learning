#!/usr/bin/env python
# coding:utf8
# Created on 2016-5-21
# @author: yi.zhiwu

import json
from time import sleep
from fabric.api import env, roles, run, execute, cd, run, env, hosts
from dbpool import DBPool

# 数据库配置
config = json.load(open('config.json', 'r'))
adminPool = DBPool()
adminPool.initPool(config['admin'])
CONFIG_DB_NAME = config['admin']['db']

queryResult = adminPool.querySql("select * from tb_server", True)
hot_list = {}
# hot_list = {"1": ['appuser@119.29.72.22:22']}
role = []
for ca in queryResult:
    service_id = str(ca['id']) + str(ca['tcpPort'])[-2:]
    hot_list[service_id] = ["appuser@" + ca['hostIP'] + ':22']
    role.append(service_id)

env.roledefs = hot_list

env.password = 'appuser'  # 服务器统一密码

# env.password = 'zcjoy@1709'  # 服务器统一密码


def server_stop(svr_no):  # 停止服务
    with cd('/data/appsystems/appSvr' + svr_no):
        run(stop())


def server_start(svr_no):  # 开启服务
    with cd('/data/appsystems/appSvr' + svr_no):
        run(start())


def mem_start(svr_no):  # 开启memcache
    with cd('/data/appsystems/shell'):
        run(m_start(svr_no))


def redis_start(svr_no):  # 开启memcache
    with cd('/data/appsystems/shell'):
        run(r_start(svr_no))


def stop():
    return "./stop.sh"


def kill(pid):
    return 'kill -9' + ' ' + pid


def start():
    return "./start.sh"


def m_start(svr_no):
    return "./mem" + svr_no + ".sh"


def r_start(svr_no):
    return "./redis" + svr_no + ".sh"


@roles(role)
def kill_pname(pname):  # 根据进程名杀进程
    pid = run("ps aux|grep " + pname + " |grep -v grep |awk '{print $2}'")
    run(kill(pid))


# --------------------服务器运行操作----------------

@roles(role)
def run_stopsvr():  # 关闭服务服务器
    for i in range(1, 5):
        svr_no = "0" + str(i)
        try:
            server_stop(svr_no)  # 取最后一位为服务器号，类似tcpPort，webPort，memPort一样规则
        except:
            pass

            # for i in role:
            #     svr_no = i[-2:]
            #     try:
            #         server_stop(svr_no)  # 取最后一位为服务器号，类似tcpPort，webPort，memPort一样规则
            #     except:
            #         pass
            # sleep(200)


@roles(role)
def run_starsvr():  # 启动服务服务器
    for i in range(1, 5):
        svr_no = "0" + str(i)
        try:
            server_start(svr_no)  # 取最后一位为服务器号，类似tcpPort，webPort，memPort一样规则
        except:
            pass

            # for i in role:
            #     svr_no = i[-2:]
            #     try:
            #         server_start(svr_no)  # 取最后一位为服务器号，类似tcpPort，webPort，memPort一样规则
            #     except:
            #         pass


@roles(role)
def kill_mem():  # 杀memcache
    kill_pname('mem')  # 杀进程


@roles(role)
def kill_redis():  # 杀memcache
    kill_pname('redis')  # 杀进程


@roles(role)
def run_mem():  # 杀memcache
    for i in range(1, 5):
        svr_no = "0" + str(i)
        try:
            mem_start(svr_no)  # 取最后一位为服务器号，类似tcpPort，webPort，memPort一样规则
        except:
            pass

            # for i in role:
            #     svr_no = i[-2:]
            #     try:
            #         mem_start(svr_no)  # 取最后一位为服务器号，类似tcpPort，webPort，memPort一样规则
            #     except:
            #         pass


@roles(role)
def run_redis():  # 重启memcache

    for i in range(1, 5):
        svr_no = "0" + str(i)
        try:
            redis_start(svr_no)  # 取最后一位为服务器号，类似tcpPort，webPort，memPort一样规则
        except:
            pass

            # for i in role:
            #     svr_no = i[-2:]
            #     try:
            #         redis_start(svr_no)  # 取最后一位为服务器号，类似tcpPort，webPort，memPort一样规则
            #     except:
            #         pass


if __name__ == '__main__':
    pass
