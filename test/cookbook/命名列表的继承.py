#!/usr/bin/python
# coding: UTF-8
import collections


class Point(collections.namedtuple('PointBase', ['x', 'y'])):
    __slots__ = ()

    def __add__(self, other):
        return Point(x=self.x + other.x, y=self.y + other.y)


p = Point(x=1.0, y=2.0)
q = Point(x=2.0, y=3.0)
print p + q
