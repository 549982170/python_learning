#!/usr/bin/python
# -*- coding:gb2312 -*-

import os
import time

case = raw_input("输入1建立wifi；输入2关闭wifi：")



if case == '1':
    command = 'netsh wlan set hostednetwork mode=allow ssid=test_wifi key=test123456' 
    os.system(command) 
    command = 'netsh wlan start hostednetwork' 
    os.system(command) 
    command = 'exit' 
    os.system(command) 
    print "The wifi setup OK!"

if  case == '2':
    command = 'netsh wlan set hostednetwork mode=disallow'
    os.system(command) 
    command = 'exit' 
    print "The wifi turn off OK!"

else:  
    command = 'exit' 
    print "Input Error!~"

print time.ctime()

