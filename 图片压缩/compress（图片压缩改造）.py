#!/usr/bin/env python
from PIL import Image
import os
import os.path
import sys

path = sys.argv[1]
small_path = (path[:-1] if path[-1] == '/' else path) + '_small'
if not os.path.exists(small_path):
    os.mkdir(small_path)
# print small_path
for root, dirs, files in os.walk(path):
    for f in files:
        # print root, "\n", dirs, "\n", files, "\n"
        fp = os.path.join(root, f)
        img = Image.open(fp)
        w, h = img.size
        print small_path + "/" + root
        if not os.path.exists(small_path + "/" + str(root).replace(path, "")):
            os.makedirs(small_path + "/" + str(root).replace(path, ""))
        img.resize((w / 2, h / 2)).save(
            os.path.join(str(small_path + "/" + str(root).replace(path, "")).replace("\\", "/"), f), "JPEG")
    # print fp
