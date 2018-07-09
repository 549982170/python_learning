#!user/bin/python
# encoding:utf-8
import datetime

no = datetime.datetime.now()
n2 = datetime.timedelta(seconds=-120)

print no+n2
