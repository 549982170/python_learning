#!/usr/bin/env python
# encoding:utf8
# Created on 2016-6-14
# @author: yi.zhiwu
import os
import shutil
import json
import sys

f_path = sys.argv[1]
f_path = (f_path[:-1] if f_path[-1] == '/' else f_path)

svrSrc = "appSvr01"  # 从appSvr01复制
ignoreFolderList = ['b_log', 'errlog', 'log']  # 忽略的文件夹列表
alterFile = ['config.json', '1_startmaster.sh', '2_startdbfront.sh', '3_startgate.sh', '4_startgame1.sh',
             '4_startgame2.sh', '4_startgame3.sh', '4_startgame4.sh', '4_startgame5.sh', '4_startgame6.sh',
             '4_startgame7.sh', '4_startgame8.sh', '5_startnet.sh', '6_startadmin.sh', 'master01.py', 'start.sh',
             'stop.sh', 'stopservice.py', 'svr01.py']  # 需要处理的文件名


def cp_file():
    nameList = []
    for filename in os.listdir(f_path):
        if "appSvr" in filename:
            nameList.append(int(filename[-2:]))
    if nameList:
        svrNo = str(max(nameList) + 1)  # 新服号
        if svrNo <= 20:
            if svrNo < 10:
                next_filename = "appSvr0" + svrNo
            else:
                next_filename = "appSvr" + svrNo
            # 测试
            next_filename = "appSvr06"
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
                    if not alter_file(f, svrNo, fp, tp):  # 筛选需要修改的文件,没修进行保存则进行复制
                        shutil.copy(fp, tp)
            print "Copy file seccess"
        else:
            print u'创建分服超过20个'
    else:
        print u'该目录没有appSvr01'


def alter_file(f, svrNo, fp, tp):
    if f in alterFile:
        if f == 'config.json':
            with open(fp, 'r') as conff:
                config = json.load(conff)
                config['master']['rootport'] = "110" + svrNo
                config['master']['webport'] = "120" + svrNo
                config['servers']['webport'] = "120" + svrNo
                print config
        return True
    return False


if __name__ == '__main__':
    cp_file()
