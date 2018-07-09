# coding:utf-8
# !/user/bin/python
L = [0, 1, 2, 3]
L.sort()
length = L.__len__()
m = length / 2

if length % 2 == 0:
    print (L[m - 1] + L[m]) / 2.0
else:
    print L[m]

L = [0, 1, 2, 3]
m = len(L)
L.sort()
if (m % 2) != 0:
    print L[(m - 1) / 2]
else:
    print (L[m / 2] + L[m / 2 - 1]) / 2.0


def fun(*p):
    new_p = sorted(p)
    n = len(new_p)
    if (n % 2 == 0):
        a = int(n / 2)
        b = 0.5 * (new_p[a - 1] + new_p[a])
        return '%.1f' % b
    else:
        a = int((n - 1) / 2)
        return new_p[a]


print (fun(*L))
