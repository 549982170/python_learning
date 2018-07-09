#!/usr/bin/env python
# encoding:utf-8
import os
import os.path
import sys
import shutil

path = sys.argv[1]
small_path = (path[:-1] if path[-1] == '/' else path)
for root, dirs, files in os.walk(path):
    for f in files:
        fp = os.path.join(root, f)
        postfix = "." + str(fp).split('.')[-1]
        filename = str(f).replace(postfix, "") + postfix + ".1"
        path = str(root).replace("\\", "/")
        outfile = os.path.join(path, filename).replace("\\", "/")
        i = ".1"  # 忽略包含该字符的文件名的文件
        j = ".py"
        l = "-"
        k = str(outfile)
        if k.count(i) >= 2 or k.count(j) >= 1 or k.count(l) >= 2:
            print k, "is already exists"
        else:
            shutil.copy(fp, outfile)
            print outfile
