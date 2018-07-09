#!user/bin/python
# encoding:utf-8
from operator import itemgetter

# 方法一
csv1 = [{"name": "b", "num": 3}, {"name": "a", "num": 1}, {"name": "c", "num": 2}, {"name": "d", "num": 3}]

csv1.sort(key=itemgetter('num', 'name'), reverse=True)
print csv1

# 方法二
csv2 = [{"name": "b", "num": 3}, {"name": "a", "num": 1}, {"name": "c", "num": 2}, {"name": "d", "num": 3}, {"num": 3},
        {"name": "a"}]


def sortKeyFun(x):
    xList = ["num", "name"]
    return tuple(x.get(ca) for ca in xList)


csv2.sort(key=sortKeyFun, reverse=True)
print csv2

# 方法三
csv3 = [{"name": "b", "num": 3}, {"name": "a", "num": 1}, {"name": "c", "num": 2}, {"name": "d", "num": 3}, {"num": 3},
        {"name": "a"}]


def mysortedByKeyList(dictList, keyList):
    dictList.sort(key=lambda x: tuple(x.get(ca) for ca in keyList), reverse=True)
    return dictList


keyList = ["num", "name"]
print mysortedByKeyList(csv3, keyList)
