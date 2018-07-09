#!/usr/bin/env python
# coding:utf8
# Created on 2016-5-19
# @author: yi.zhiwu
import os
import shutil
import time
import datetime
import sys

f_path = sys.argv[1]
t_path = sys.argv[2]
f_path = (f_path[:-1] if f_path[-1] == '/' else f_path)
t_path = (t_path[:-1] if t_path[-1] == '/' else t_path)


def cp_file():
    # 把第一个参数目录下的文件复制到第二个参数，包含2016-05-16的则创建目录剪切操作，复制目录树
    for root, dirs, files in os.walk(f_path):
        for f in files:
            fp = os.path.join(root, f)
            oldname = str(f)  # 旧文件名
            includename = "basic_"
            if oldname.count(includename) >= 1:  # 过滤掉必须包含basic的文件才操作
                i = "-"
                small_path = root.replace(f_path, '').replace("\\", "").replace("/", "")
                if oldname.count(i) >= 2:
                    d_name = oldname[-10:].replace("-", "")
                    d_path = os.path.join(t_path, small_path, d_name)
                    if not os.path.exists(d_path):
                        os.makedirs(d_path)
                    # 文件名更改
                    oldnamefile = os.path.join(d_path, oldname)
                    tmp = "." + str(oldname).split('.')[-1]
                    newname = oldname.replace(tmp, '')
                    newnamefile = os.path.join(d_path, newname)
                    # 重复文件删除,防止文件已经存在shutil.move报错
                    if os.path.exists(newnamefile):
                        os.remove(newnamefile)
                    # 剪切文件
                    shutil.move(fp, d_path)
                    # 去掉文件后面的日期
                    os.renames(oldnamefile, newnamefile)
                    print "Transfer yesterday's files success:" + fp

                else:
                    d_name = time.strftime("%Y%m%d", time.localtime(time.time()))
                    d_path = os.path.join(t_path, small_path, d_name)
                    if not os.path.exists(d_path):
                        os.makedirs(d_path)
                    outfile = os.path.join(d_path, f)
                    shutil.copy(fp, outfile)
                    print "Transfer today's files success:" + fp


def clean():
    i = "-"  # 文件标识
    for root, dirs, files in os.walk(t_path):
        r_path = root.replace(t_path, '').replace("\\", "/").split('/')[-1]  # 获取最后一层目录名字
        if (not files) and (not dirs):  # 删除空目录
            shutil.rmtree(root, True)
            print "Remove empty directories success:" + root
        for f in files:
            j = str(f)
            if len(r_path) == 8:  # 日期目录
                try:
                    d_years = r_path[:4]
                    d_month = r_path[4:6]
                    d_day = r_path[-2:]
                    str_date = d_years + '-' + d_month + '-' + d_day
                    f_date = datetime.datetime.strptime(str_date, "%Y-%m-%d").date()  # 文件夹名称转化为日期对象
                    today_time = (datetime.datetime.now()).date()  # 今天前日期
                    # 不需删除前段时间的动态文件，文件转移时已重命名
                    # yes_time = (datetime.datetime.now() + datetime.timedelta(days=-1)).date()  # 昨天日期
                    # if f_date == yes_time:  # 昨天的日志文件夹里面把动态生成的日志删除
                    #     if j.count(i) != 2:
                    #         fp = os.path.join(root, f)
                    #         os.remove(fp)  # 删除前一天的动态日志
                    #         print "Remove  yesterday's file success:" + fp
                    if (today_time - f_date).days > 15:  # 清除15天前文件目录
                        shutil.rmtree(root, True)
                        print "Delete the directory 15 days ago success:" + root
                except IOError, e:
                    print e
                else:
                    pass


if __name__ == '__main__':
    cp_file()
    clean()
