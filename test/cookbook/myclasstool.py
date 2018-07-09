#!/usr/bin/python
# coding: UTF-8
from collections import deque


class mydeque:
    def __init__(self, lenth):
        self.mylist = []
        self.q = deque(maxlen=lenth)

    def myappend(self, num):
        """返回固定长度的列表，清除最旧一个"""
        self.q.append(num)
        return self.q

    def mypop(self, num):
        self.q.pop(num)
        return self.q

    def mypopleft(self):
        self.q.popleft()
        return self.q


