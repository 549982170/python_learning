from math import sqrt


def prime(n):
    s = sqrt(n+1)
    L = range(1, 101)
    i = 1;
    ret = []
    while i < s and i < len(L):
        ret.append(L[i])
        L = filter(lambda x: x%L[i]!=0, L)


    return ret
    
li = prime(100)
print ' '.join('%s' % d for d in li)