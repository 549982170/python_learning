#!/usr/bin/env python
# encoding:utf-8

def test(list1, list2):
    l = []
    for a in list1:
        if a in list2 and a not in l:
            l.append(a)
    return l


l1 = ['a', 'b', 'c', 'f']
l2 = ['d', 'b', 'c', 'a']
L = test(l1, l2)

print L
