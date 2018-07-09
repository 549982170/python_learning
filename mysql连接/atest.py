#!/usr/bin/python
# coding: UTF-8
import MySQLdb
from MySQLdb.cursors import DictCursor
import datetime
import logging

# ----------------数据库配置------------------
host = '192.168.3.211'
port = 3306
user = 'test'
pwd = 'sooviitest'
db = 'soovii_productionplanning_db_t'  # 变动的数据库前缀
conn = MySQLdb.connect(host=host, port=port, user=user, passwd=pwd, db=db, charset="utf8")

# 日志模块
import logging

# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('sql.log')
fh.setLevel(logging.DEBUG)
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter()
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)


def querySql(sql, dictcursor=False):
    """执行查询并返回所有结果 fetchall"""
    try:
        if dictcursor:
            cursor = conn.cursor(cursorclass=DictCursor)
        else:
            cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Exception, err:
        cursor.close()
        raise err


def execSql(sql):
    """执行数据库的写操作(插入,修改,删除),自动commit
    @param sql: str 需要执行的sql语句
    """
    try:
        cursor = conn.cursor()
        count = cursor.execute(sql)
        conn.commit()
        cursor.close()
        if count > 0:
            return True
        return False
    except Exception, err:
        cursor.close()
        raise err


sql = "select * from pm_attendance_record"
result = querySql(sql, True)
logger.info("start")
for ca in result:
    print ca
logger.info("end")
print "finish"