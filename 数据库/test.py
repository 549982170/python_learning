#!user/bin/python
# -*- coding:gb2312 -*-
import MySQLdb

conn_1 = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="bash_uat", charset="utf8")
cursor = conn_1.cursor()
sql_1 = "select v.mastername, t1.totalMoney from (select channelId,sum(money) as totalMoneyfrom bash_uat.tb_vip_buy where buydate>='2016-05-05 00:00:01' and buydate<='2016-05-05 23:59:59' group by channelId) as t1LEFT JOIN gameadmin_uat.channel_view v on t1.channelId=v.channelID order by t1.totalMoney desc ;"
cursor.execute(sql_1)
records = cursor.fetchall()
print records