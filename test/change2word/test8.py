#!/usr/bin/python
# coding:utf-8
import re
content = open('distutils.cfg').read()
#Window下用记事本打开配置文件并修改保存后，编码为UNICODE或UTF-8的文件的文件头
#会被相应的加上\xff\xfe（\xff\xfe）或\xef\xbb\xbf，然后再传递给ConfigParser解析的时候会出错
#，因此解析之前，先替换掉
content = re.sub(r"\xfe\xff","", content)
content = re.sub(r"\xff\xfe","", content)
content = re.sub(r"\xef\xbb\xbf","", content)
open('distutils.cfg', 'w').write(content)