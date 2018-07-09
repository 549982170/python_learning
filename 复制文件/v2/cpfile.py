#!/usr/bin/env python
# encoding:utf8
# Created on 2016-6-14
# @author: yi.zhiwu

import shutil
import sys
import json
import os
import re
import commands

# 从appSvr01复制
svrSrc = "appSvr01"
# 忽略的文件夹列表
ignoreFolderList = ['b_log', 'errlog', 'log']
# 需要处理的文件名
alterFile = ['config.json', '1_startmaster.sh', '2_startdbfront.sh', '3_startgate.sh', '4_startgame1.sh',
             '4_startgame2.sh', '4_startgame3.sh', '4_startgame4.sh', '4_startgame5.sh', '4_startgame6.sh',
             '4_startgame7.sh', '4_startgame8.sh', '5_startnet.sh', '6_startadmin.sh', 'master' + svrSrc[-2:] + '.py',
             'start.sh', 'stop.sh', 'svr' + svrSrc[-2:] + '.py']
b_blog = ""


def run():
    f_path = sys.argv[1]
    f_path = (f_path[:-1] if f_path[-1] == '/' else f_path)
    srvId = sys.argv[2]  # 分服Id
    if int(srvId) < 10:
        srvId = "0" + str(srvId)
    else:
        srvId = str(srvId)
    nameList = []
    for filename in os.listdir(f_path):
        if "appSvr" in filename:
            nameList.append(int(filename[-2:]))
    if nameList:
        svrNo = max(nameList) + 1  # 新服号
        if svrNo <= 20:
            if svrNo < 10:
                next_filename = "appSvr0" + str(svrNo)
                nsvrNo = "0" + str(svrNo)
            else:
                next_filename = "appSvr" + str(svrNo)
                nsvrNo = str(svrNo)
            # 测试
            # svrNo = "06"
            # next_filename = "appSvr06"

            appSvrPath = os.path.join(f_path, svrSrc)  # 从appSvr01复制文件
            new_folder = os.path.join(f_path, next_filename)
            # 创建新服文件夹和新服下日志文件夹
            if not os.path.exists(new_folder):
                os.mkdir(new_folder)  # 创建新服文件夹
                print u'创建' + next_filename + u'文件夹成功'
            for i in ignoreFolderList:
                log_folder = os.path.join(new_folder, i)  # 创建新服日志文件夹
                if not os.path.exists(log_folder):
                    os.mkdir(log_folder)
                    print u'创建' + i + u'文件夹成功'
            if cp_file(appSvrPath, next_filename, srvId, nsvrNo):
                print "Copy file success"
            else:
                print "Copy file fail"
        else:
            print u'创建分服超过20个'
    else:
        print u'该目录没有appSvr01'


def cp_file(appSvrPath, next_filename, srvId, nsvrNo):
    for root, dirs, files in os.walk(appSvrPath):
        if root.replace("/", "\\").split("\\")[-1] in ignoreFolderList:
            continue  # 过滤日志文件夹
        for f in files:
            if ".pyc" in f[-4:]:
                continue  # 过滤.pyc文件
            new_path = root.replace(svrSrc, next_filename)  # 目标路径生成
            fp = os.path.join(root, f)  # 复制来源文件
            tp = os.path.join(new_path, f)  # 复制目标文件
            # 创建新服目录文件夹
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            if not alter_file(srvId, nsvrNo, f, fp, tp, new_path):  # 筛选需要修改的文件,没修进行保存则进行复制
                shutil.copy(fp, tp)
    return True


def alter_file(srvId, nsvrNo, f, fp, tp, new_path):
    if f in alterFile:
        osvrpy = 'svr' + svrSrc[-2:] + '.py'  # svr**.py 旧文件名
        nsvrpy = 'svr' + nsvrNo + '.py'  # svr**.py 新文件名字
        omasterpy = 'master' + svrSrc[-2:] + '.py'  # master01.py 旧文件名
        nmasterpy = 'master' + nsvrNo + '.py'  # master01.py 新文件名字
        if f == 'config.json':
            with open(fp, 'r') as conff:
                config = json.load(conff)
                config['master']['rootport'] = int("110" + nsvrNo)
                config['master']['webport'] = int("120" + nsvrNo)
                config['servers']['net']['netport'] = int("140" + nsvrNo)
                config['servers']['gate']['rootport'] = int("100" + nsvrNo)
                config['servers']['net']['remoteport'][0]['rootport'] = int("100" + nsvrNo)
                config['servers']['gate']['serverId'] = str(srvId)
                config['servers']['admin']['remoteport'][0]['rootport'] = int("100" + nsvrNo)
                config['servers']['admin']['webport'] = int("130" + nsvrNo)
                config['servers']['game1']['remoteport'][0]['rootport'] = int("100" + nsvrNo)
                config['servers']['game2']['remoteport'][0]['rootport'] = int("100" + nsvrNo)
                config['servers']['game3']['remoteport'][0]['rootport'] = int("100" + nsvrNo)
                config['servers']['game4']['remoteport'][0]['rootport'] = int("100" + nsvrNo)
                config['servers']['game5']['remoteport'][0]['rootport'] = int("100" + nsvrNo)
                config['servers']['game6']['remoteport'][0]['rootport'] = int("100" + nsvrNo)
                config['servers']['game7']['remoteport'][0]['rootport'] = int("100" + nsvrNo)
                config['servers']['game8']['remoteport'][0]['rootport'] = int("100" + nsvrNo)
                config['db']['main']['db'] = "bzsh_0" + nsvrNo
                config['memcached']['hostname'] = "app" + nsvrNo
                config['memcached']['urls'] = ["127.0.0.1:112" + nsvrNo]
                config['redis']['port'] = "63" + nsvrNo
                json.dump(config, open(tp, 'w'), indent=4)
                return True  # 一次行修改完成config.json
        elif f == osvrpy:
            tp = os.path.join(new_path, nsvrpy)
        elif f == omasterpy:
            tp = os.path.join(new_path, nmasterpy)
        # 所有文件alterFile列表里面文件内容把svr**.py改为新svr**.py保存到tp路径
        with open(fp, 'r') as myfile:
            with open(tp, 'w') as tfile:
                data = myfile.read()
                # 把alterFile列表的文件内容的svr**.py和master**.py向上+1更新
                data = re.sub(osvrpy, nsvrpy, data)
                data = re.sub(omasterpy, nmasterpy, data)
                tfile.write(data)
        return True  # 已重新写入文件
    return False  # 未写入文件，直接复制


if __name__ == '__main__':
    print u'执行方式:python cpfile.py /data/appsystems + 分服Id（例：python cpfile.py /data/appsystems 6'
    run()
