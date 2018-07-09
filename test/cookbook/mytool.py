#!/usr/bin/python
# coding: UTF-8
import heapq


def maxbylist(num, mylist, mykey=None):
    """求列表中最大的num个值"""
    if mykey is not None:
        return heapq.nlargest(num, list(mylist), key=lambda s: s[mykey])
    else:
        return heapq.nlargest(num, list(mylist))


def minbylist(num, mylist, mykey=None):
    """求列表中最小的num个值"""
    if mykey is not None:
        return heapq.nsmallest(num, list(mylist), key=lambda s: s[mykey])
    else:
        return heapq.nsmallest(num, list(mylist))

def heapqsort(mylist):
    """列表排序"""
    heapq.heapify(list(mylist))
    return mylist
