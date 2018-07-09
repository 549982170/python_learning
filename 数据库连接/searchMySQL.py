# coding=utf-8
  
#引入mysql python客户端模块
import MySQLdb
import sys
#进行数据库连接
conn_1 = MySQLdb.connect(host="172.16.1.29", user="readonly",passwd="dbtest123", db="moxian", charset="utf8")
cursor = conn_1.cursor()
#执行sql
phoneNo = "8613800000073"
sql_1 = "SELECT user_base_password FROM user_user_base_sb WHERE user_base_phone="+ phoneNo
cursor.execute(sql_1)
#列出数据
records = cursor.fetchall()
for row in records:
    for r in row:
        validateCode = r
print validateCode 