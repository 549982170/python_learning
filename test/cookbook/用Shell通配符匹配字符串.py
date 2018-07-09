#!/usr/bin/python
# coding: UTF-8
from fnmatch import fnmatch, fnmatchcase

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
print [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
