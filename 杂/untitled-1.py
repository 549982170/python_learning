#!user/bin/python
#encoding:utf-8


for x in range (0,100):
    x = str(x)
    x = x.zfill(10)
    x = list(x)
    x = map(int, x)
    #print x
    for i in range(0,10):
        #print i
        if all(x[i] == x.count(i)):
            print x



