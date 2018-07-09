#!user/bin/python
# encoding:utf-8

import re

str1 = 'bzsh_007'
mode = re.compile(r'\d+')
c = mode.findall(str1)
print int(c[-1])

print str(str1)