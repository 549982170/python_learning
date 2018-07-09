#!user/bin/python
# -*- coding:gb2312 -*-
import MySQLdb
import sys
while True:
    try:    
        env = raw_input("输入环境：1为moxiancn，2为beta：")
        if env == '1':
            #数据库连接
            conn = MySQLdb.connect(host="172.16.1.29", user="readonly",passwd="dbtest123", db="service", charset="utf8")
            break        
        elif env == '2':
            #数据库连接
            conn = MySQLdb.connect(host="59.188.11.71", user="readonly",passwd="dbtest123", db="service", charset="utf8")
            break
        else:
            print "Input error!"
    except: pass
while True:
    try:  
        phoneNo = raw_input("输入需要知道验证码的手机号：")
        #进行数据库连接
        cursor = conn.cursor()
        #执行sql
        sql = "SELECT create_time,verify_record_verify_code FROM sms_verify_record_br WHERE verify_rocord_account = "+ phoneNo + " "+"order by create_time desc limit 1"
        #print sql
        cursor.execute(sql)
        #列出数据
        records = cursor.fetchall()
        for row in records:
            for code in row:
                validateCode = code
        print "手机号码的验证码为：" ,validateCode
        command = 'pause'
        os.system(command) 
    except: pass