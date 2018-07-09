#!user/bin/python
# encoding:utf-8
import os
path = 'D:\mytongdao\Debug.win32'  # 文件夹路径
for root, dirs, files in os.walk(path):
    for f in files:
        # print f
        fp = os.path.join(root, f)
        postfix = str(fp).split('.')[-1]  # 文件名后缀
        if postfix == 'exe':
            print f