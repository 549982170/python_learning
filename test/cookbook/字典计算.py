#!/usr/bin/env python
# encoding:utf8
from operator import itemgetter

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# print zip(prices.values(), prices.keys())

min_price = min(zip(prices.values(), prices.keys()))
# print min_price
max_price = max(zip(prices.values(), prices.keys()))
# print max_price
prices_sorted = sorted(zip(prices.values(), prices.keys()))
# print prices_sorted

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_lfname = sorted(rows, key=itemgetter('uid'))
# print(rows_by_lfname)


def sortedDictList(dict_list, dict_key, rev=False):
    """列表字典按字典里面的某个key来排序
    @param dict_list: list字典列表
    @param dict_key: str字典里面的某个key
    @param rev:bool 是否倒序,Flase为生序,True为降序
    """
    return sorted(dict_list, key=itemgetter(dict_key), reverse=rev)

def minDictList(dict_list, dict_key):
    """列表字典最小的字典
    @param dict_list: list字典列表
    @param dict_key: str字典里面的某个key
    @param rev:bool 是否倒序,Flase为生序,True为降序
    """
    return min(dict_list, key=itemgetter(dict_key))

def maxDictList(dict_list, dict_key):
    """列表字典最大的字典
    @param dict_list: list字典列表
    @param dict_key: str字典里面的某个key
    @param rev:bool 是否倒序,Flase为生序,True为降序
    """
    return max(dict_list, key=itemgetter(dict_key))

print sortedDictList(rows, "uid")
print minDictList(rows, "uid")
print maxDictList(rows, "uid")
