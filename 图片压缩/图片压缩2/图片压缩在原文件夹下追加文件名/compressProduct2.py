#!/usr/bin/env python
# encoding:utf-8
"""图片压缩，执行python compressProduct.py + 图片文件夹名，在该文件夹下生成追加_thumb文件名称图片"""
from PIL import Image
import os
import os.path
import sys
path = sys.argv[1]
small_path = (path[:-1] if path[-1] == '/' else path)
for root, dirs, files in os.walk(path):
    for f in files:
        # print f
        fp = os.path.join(root, f)
        # print fp
        img = Image.open(fp)
        postfix = "."+str(fp).split('.')[-1]
        # print postfix
        filename = str(f).replace(postfix, "")+"_thumb"+postfix
        # print filename
        path = str(root).replace("\\", "/")
        # print path
        outfile = os.path.join(path, filename).replace("\\", "/")
        i = "_thumb"
        j = str(outfile)
        if j.count(i) >= 2:
            print f, "is already exists"
        else:
            img.resize((200, 200)).save(outfile, "JPEG")
            print outfile
