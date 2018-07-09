#!/usr/bin/python
# coding: UTF-8
a = [1, 2, 3, 4, 5, 6]
b = zip(*([iter(a)] * 2))
print b
print "--------"
group_adjacent = lambda a, k: zip(*([iter(a)] * k))
print group_adjacent(a, 3)
print group_adjacent(a, 2)
print group_adjacent(a, 1)
print zip(a[::2], a[1::2])
print zip(a[::3], a[1::3], a[2::3])
group_adjacent = lambda a, k: zip(*(a[i::k] for i in range(k)))
print "--------"
print group_adjacent(a, 3)
print group_adjacent(a, 1)
