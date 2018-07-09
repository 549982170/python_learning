#!/usr/bin/env python
# encoding:utf-8
import time

with open("./test/1.txt", 'a') as f:
    t1 = time.time()
    s = "[2016-05-13-20-52-14],basic_equiplist,zoneid=1,playerId=1325,accName=1001-sun003,nickname=申曼文,level=79," \
        "type=3,goodsId=26001,num=1,leftNum=1,time=1463143934,date=20160513,pf=1001"
    for i in range(0, 200000):
        time.sleep(0.001)
        f.write(s + '\n')
    t2 = time.time()
    f.write(u'运行时间：' + str(t2 - t1) + u'秒')
