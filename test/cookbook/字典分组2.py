#!/usr/bin/python
# coding: UTF-8
import collections
from operator import itemgetter
from itertools import groupby

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

def dictListGroupby(dict_list, dict_key, rev=False):
    """按dict_key返回列表字典有序的分组字典,每组的key为dict_key
    @param dict_list: list字典列表
    @param dict_key: 分组的key
    @param rev:bool 是否倒序,Flase为升序,True为降序
    """
    redata = collections.OrderedDict()
    dict_list.sort(key=itemgetter(dict_key), reverse=rev)
    for key, items in groupby(dict_list, key=itemgetter(dict_key)):
        redata[key] = []
        for i in items:
            redata[key].append(i)
    return redata

c = dict(dictListGroupby(rows, 'date', rev=False))
del c['07/01/2012']
print c

