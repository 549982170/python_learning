#!/usr/bin/python
# coding: UTF-8
import MySQLdb
from MySQLdb.cursors import DictCursor
import datetime
import logging

# ----------------数据库配置------------------
host = '10.0.0.81'
port = 3306
user = 'root'
pwd = 'hj34$%yzw175'
db = 'bzsh_40008'  # 变动的数据库前缀
# -------------- 测试-------------
# host = '127.0.0.1'
# port = 3306
# user = 'root'
# pwd = 'root'
# db = 'bzsh_40008'  # 变动的数据库前缀

conn = MySQLdb.connect(host=host, port=port, user=user, passwd=pwd, db=db, charset="utf8")

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


sql = "select * from tb_limitdraw where activityId =40001"
result = querySql(sql, True)
logger.info("start")
for ca in result:
    characterId = ca['characterId']
    drawtime = datetime.datetime.now()
    drawcount = ca['drawcount']
    floatNum = ca['floatNum']
    oldscore = int(ca['score'])
    rewardList = ca['rewardList']
    updateTime = datetime.datetime.now()
    sql = "select * from tb_limitdraw where activityId =40002 and characterId = '%s'" % (characterId)
    result2 = querySql(sql, True)
    if result2:
        newscore = int(result2[0]['score'])
        totalscore = oldscore + newscore
        sql = "update tb_limitdraw set score=%s where activityId =40002 and characterId = '%s'" % (
            totalscore, characterId)
        logger.info(sql + ';')
        # print sql + ";"

    else:
        newid = int(str(characterId) + "40002")
        mytype = 2
        sql = "insert into tb_limitdraw(id,characterId,`type`,drawtime,drawcount,floatNum,score,rewardList,updateTime,activityId) " \
              "values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
              % (newid, characterId, mytype, drawtime, drawcount, floatNum, oldscore, rewardList, updateTime, 40002)
        logger.info(sql + ';')
        # print sql + ";"
logger.info("end")
print "finish"