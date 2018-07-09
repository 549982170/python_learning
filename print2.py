#! /usr/bin/env python
#coding=utf-8
#eidt www.jbxue.com
#
import subprocess
import time
import os
ks=int(time.time()) #记录开始时间
ip="192.168.2."

def subping():
    num1=num2=0
    for i in range(1,10):
        ips=ip+str(i)   
        ret=subprocess.call("ping -n 1 -w 1 %s " % ips)
        if ret == 0:
           print (ips,"+++++++++++++Online ")
           num1=num1+1
        else:
           # print (ips,"-------------Offline")
            num2=num2+1 
 
    js=int(time.time())  #记录结束时间
    print("time（秒）:",js-ks,"s")  #打印并计算用的时间，s秒
    print("ON_line:",num1,"    OFF_line:",num2)
 
def osping():
#调用系统的ping命令
    return1=os.system('ping -n 2 -w 1 8.8.8.8')
    if return1:
        print 'ping os ping fail'
    else:
        print 'ping os ping ok'
 
osping()
subping()