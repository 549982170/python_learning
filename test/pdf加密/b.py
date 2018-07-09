# coding:utf-8
# !/user/bin/python
import PythonMagick
im = PythonMagick.Image('files.pdf')
im.write("file_img%d.png")