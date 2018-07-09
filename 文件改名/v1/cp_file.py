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
            i = "-"
            j = str(f)
            small_path = root.replace(f_path, '').replace("\\", "").replace("/", "")
            if j.count(i) >= 2:
                d_name = j[-10:].replace("-", "")
                d_path = os.path.join(t_path, small_path, d_name)
                if not os.path.exists(d_path):
                    os.makedirs(d_path)
                try:
                    shutil.move(fp, d_path)
                    print "转移昨天的日志文件到目录：" + fp
                except:
                    print "文件已存在：" + fp
            else:
                d_name = time.strftime("%Y%m%d", time.localtime(time.time()))
                d_path = os.path.join(t_path, small_path, d_name)
                if not os.path.exists(d_path):
                    os.makedirs(d_path)
                outfile = os.path.join(d_path, f)
                shutil.copy(fp, outfile)
                print "复制今天的日志文件：" + fp


def clean():
    i = "-"  # 文件标识
    for root, dirs, files in os.walk(t_path):
        r_path = root.replace(t_path, '').replace("\\", "/").split('/')[-1]  # 获取最后一层目录名字
        if (not files) and (not dirs):  # 删除空目录
            shutil.rmtree(root, True)
            print "删除空目录：" + root
        for f in files:
            j = str(f)
            if len(r_path) == 8:  # 日期目录
                try:
                    d_years = r_path[:4]
                    d_month = r_path[4:6]
                    d_day = r_path[-2:]
                    str_date = d_years + '-' + d_month + '-' + d_day
                    f_date = datetime.datetime.strptime(str_date, "%Y-%m-%d").date()  # 文件夹名称转化为日期对象
                    yes_time = (datetime.datetime.now() + datetime.timedelta(days=-1)).date()  # 昨天日期
                    today_time = (datetime.datetime.now()).date()  # 今天前日期
                    if f_date == yes_time:  # 昨天的日志文件夹里面把动态生成的日志删除
                        if j.count(i) != 2:
                            fp = os.path.join(root, f)
                            os.remove(fp)  # 删除前一天的动态日志
                            print "删除文件：" + fp
                    if (today_time - f_date).days > 15:  # 清除15天前文件目录
                        shutil.rmtree(root, True)
                        print "删除15天前的目录：" + root
                except IOError, e:
                    print e
                else:
                    pass


if __name__ == '__main__':
    cp_file()
    clean()
