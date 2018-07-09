#!/usr/bin/env python
# encoding:utf-8
"""图片压缩，执行python compressProduct.py + 图片文件夹名，在该文件夹下生成追加_thumb文件名称图片"""
from PIL import Image
from PIL.Image import EXTENT
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
        if img.size[0] > img.size[1]:
            offset = int(img.size[0]-img.size[1])/2
            img = img.transform((img.size[1], img.size[1]), EXTENT, (offset, 0, int(img.size[0]-offset), img.size[1]))
        else:
            offset = int(img.size[1]-img.size[0])/2
            img = img.transform((img.size[0], img.size[0]), EXTENT, (0, offset, img.size[0], (img.size[1]-offset)))
        img.thumbnail((200, 200))

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
            img.save(outfile, "JPEG")
            print outfile
