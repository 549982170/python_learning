#!/usr/bin/python
# coding: UTF-8
a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print c
