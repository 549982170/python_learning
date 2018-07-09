#!/usr/bin/python
# coding: utf-8
def getRewardDict(item):
    itemDict = {}
    if item:
        itemList = item.split('|')
        for i in itemList:
            j = i.split(',')
            itemDict[j[0]] = j[1]
    return itemDict


a = "11002,500000|10015,5"


c = getRewardDict(a)

print c