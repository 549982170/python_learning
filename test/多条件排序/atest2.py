#!user/bin/python
# encoding:utf-8
from itertools import product
from itertools import combinations

l = [1, 2, 3]
# print list(product(l, l))
c = (str(ca[0])+str(ca[1]) for ca in product(l, repeat=2))
print list(c)
# print list(product(l, repeat=4))
#
# print list(combinations([1, 2, 3, 4, 5], 3))
