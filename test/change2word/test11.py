#!/usr/bin/python
# coding: UTF-8
from time import time

t = time()
mylistlist = ['a', 'b', 'is', 'python', 'jason', 'hello', 'hill', 'with', 'phone', 'test',
              'dfdf', 'apple', 'pddf', 'ind', 'basic', 'none', 'baecr', 'var', 'bana', 'dd', 'wrd']
mylistlist = dict.fromkeys(mylistlist, True)
print mylistlist
myfilter = []
for i in range(1000000):
    for find in ['is', 'hat', 'new', 'list', 'old', '.']:
        if find not in mylistlist:
            myfilter.append(find)
print "total run time:"
print time() - t
