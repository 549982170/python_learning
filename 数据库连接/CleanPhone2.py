#!user/bin/python
# -*- coding:gb2312 -*-
import os
import requests
import json
#����mysql python�ͻ���ģ��
import MySQLdb
import sys
#dev: http://dev2.moxian.com:8080/mo_common_fileuploadservice/m1/upload
#moxiancn: http://www.moxiancn.com/mo_common_fileuploadservice/m1/upload
#showload: http://www.spellthread.com
while True:
    try:    
        env = raw_input("���뻷����1Ϊdev��2Ϊmoxiancn��3Ϊbeta��")
        if env == '1':
            url = 'http://dev2.moxian.com:8080/mo_common_sso/m2/auth/login'
            url2 = 'http://dev2.moxian.com:8080/mo_common_user/m2/mobilephone/updatemobilephone'
            url3 = 'http://dev2.moxian.com:8080/mo_common_sso/m2/mobilephone/sendmessage'
            break
        elif env == '2':
            url = 'http://login.moxiancn.com/mo_common_login/m2/auth/login'
            url2 = 'http://sso.moxiancn.com/mo_common_sso/m2/mobilephone/updatemobilephone'
            url3 = 'http://sso.moxiancn.com/mo_common_sso/m2/mobilephone/sendmessage'
            #���ݿ�����
            conn_1 = MySQLdb.connect(host="172.16.1.29", user="readonly",passwd="dbtest123", db="moxian", charset="utf8")
            conn_2 = MySQLdb.connect(host="172.16.1.29", user="readonly",passwd="dbtest123", db="service", charset="utf8")
            break        
        elif env == '3':
            url = 'http://login.spellthread.com/mo_common_login/m1/auth/login'
            url2 = 'http://sso.spellthread.com:80/mo_common_sso/m1/mobilephone/updatemobilephone'
            url3 = 'http://sso.spellthread.com:80/mo_common_sso/m1/mobilephone/sendmessage'
            #���ݿ�����
            conn_1 = MySQLdb.connect(host="59.188.11.71", user="readonly",passwd="dbtest123", db="moxian", charset="utf8")
            conn_2 = MySQLdb.connect(host="59.188.11.71", user="readonly",passwd="dbtest123", db="service", charset="utf8")
            break
        else:
            print "Input error!"
    except: pass
        

useraccount = "86"+raw_input("������Ҫ���µ��ֻ����룺")
#��86��Ϊ�����룬���¼Ϊ������������ֱ���޸�86���ɣ���һ��Ͳ������ݿ�ȡ�ˡ�
#userpass = raw_input("�������룺")
phoneNo2 = raw_input("������Ҫ���ĵ��ֻ��ţ�")
phoneNo = "86" + phoneNo2
#�������ݿ�����
cursor = conn_1.cursor()
#ִ��sql
sql_1 = "SELECT user_base_password FROM user_user_base_sb WHERE user_base_phone=" + useraccount
#print sql
cursor.execute(sql_1)
#�г�����
records = cursor.fetchall()
for row in records:
    for p in row:
        userpass = p
#print userpass
print "��¼����Ϊ��" ,userpass

query_args = {
              "useraccount": useraccount,
              "userpass": userpass,
              "loginAppType":"mobiz"
              }
headers = {'content-type': 'application/json'}
r = requests.post(url,json.dumps(query_args),headers=headers)
result = r.json()

#print result
if r.status_code == 200:
    print "��¼�ɹ���"
else :
    print "��¼ʧ�ܣ������¼�ӿڣ�"

token = result.get(u'data').get(u'token')
userId = str(result.get(u'data').get(u'userId'))
#print token,userId

query_args2 = {
              "countryCode":"86",
              "phoneNo":phoneNo,
              "userId":userId
              }
headers = {'content-type': 'application/json','appType': 'mobiz','userId': userId ,'token': token}
r = requests.post(url3,json.dumps(query_args2),headers=headers)
result = r.json()
#print result

#�������ݿ�����
cursor = conn_2.cursor()
#ִ��sql
sql_2 = "SELECT create_time,verify_record_verify_code FROM sms_verify_record_br WHERE verify_rocord_account = "+ phoneNo2 + " "+"order by create_time desc limit 1"
#print sql
cursor.execute(sql_2)
#�г�����
records = cursor.fetchall()
for row in records:
    for code in row:
        validateCode = code
#print validateCode
#print "���յ���֤��Ϊ��",validateCode
if r.status_code == 200:
    print "��ȡ��֤��ɹ���"
    print "��ȡ����֤��Ϊ��",validateCode
else :
    print "��ȡ��֤��ʧ�ܣ������ȡ��֤��ӿڣ�"
payload ={
           "userId": userId,
           "email": "",
           "validateCode": validateCode,
           "countryCode": "86",
           "phoneNo": phoneNo
}
headers = {'content-type': 'application/json','appType': 'mobiz', 'userId': userId ,'token': token }
r = requests.post(url2, json.dumps(payload), headers=headers)
#print r.json()

if r.status_code == 200:
    print "�İ�ɹ����İ����ʺ�Ϊ��",phoneNo2
    print "��¼����Ϊ��",userpass
    print "��ע���ɵĺ�����Լ�������ע���ˣ�~"
else :
    print "�ʺŸİ�ʧ�ܣ���"
res = r.json()
command = 'pause'
os.system(command) 

if __name__ == "__main__":
    run()
