#!user/bin/python
# encoding:utf-8
import json
import re
a = "1 日 男兵宿舍 内 714	众人自拍"
print a.replace(" ", "").replace("\t", "").replace("\n", "").strip()




import re

pattern = re.compile(r'\S')
result = list(ca for ca in pattern.finditer(a))
print result