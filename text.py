import re
a = "this is my re module test"
obj = re.search(r'.*is',a)
print obj
obj.group()
print re.findall(r'.*is',a)
