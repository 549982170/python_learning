#!user/bin/python
# -*- coding:gb2312 -*-
import MySQLdb
import sys
while True:
    try:    
        env = raw_input("���뻷����1Ϊmoxiancn��2Ϊbeta��")
        if env == '1':
            #���ݿ�����
            conn = MySQLdb.connect(host="172.16.1.29", user="readonly",passwd="dbtest123", db="service", charset="utf8")
            break        
        elif env == '2':
            #���ݿ�����
            conn = MySQLdb.connect(host="59.188.11.71", user="readonly",passwd="dbtest123", db="service", charset="utf8")
            break
        else:
            print "Input error!"
    except: pass
while True:
    try:  
        phoneNo = raw_input("������Ҫ֪����֤����ֻ��ţ�")
        #�������ݿ�����
        cursor = conn.cursor()
        #ִ��sql
        sql = "SELECT create_time,verify_record_verify_code FROM sms_verify_record_br WHERE verify_rocord_account = "+ phoneNo + " "+"order by create_time desc limit 1"
        #print sql
        cursor.execute(sql)
        #�г�����
        records = cursor.fetchall()
        for row in records:
            for code in row:
                validateCode = code
        print "�ֻ��������֤��Ϊ��" ,validateCode
        command = 'pause'
        os.system(command) 
    except: pass