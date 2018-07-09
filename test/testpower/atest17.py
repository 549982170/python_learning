#!user/bin/python
# encoding:utf-8
a = ('1', '2', '3')
b = "'%s'" % a.__repr__()
print(b.__repr__())