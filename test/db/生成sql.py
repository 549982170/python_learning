#!user/bin/python
# encoding:utf-8
import MySQLdb
import logging
from MySQLdb.cursors import DictCursor

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('mysql.log')
fh.setLevel(logging.DEBUG)
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
# formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)


host = '127.0.0.1'
oport = 3306
ouser = 'root'
opwd = 'root'
db = 'bzsh_2000'  # 变动的数据库前缀
# db = 'bzsh_1000'  # 变动的数据库前缀
conn = MySQLdb.connect(host=host, port=oport, user=ouser, passwd=opwd, charset="utf8")
nconn = MySQLdb.connect(host=host, port=oport, user=ouser, passwd=opwd, charset="utf8", db="bzsh_all")


def querySql(conn, sql, dictcursor=False):
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


def execSql(conn, sql):
    """执行数据库的写操作(插入,修改,删除),自动commit
    @param sql: str 需要执行的sql语句
    """
    try:
        cursor = conn.cursor()
        count = cursor.execute(sql)
        print sql
        conn.commit()
        cursor.close()
        if count > 0:
            return True
        return False
    except Exception, err:
        cursor.close()
        raise err


def changeDB(conn, bdname):
    """"切换数据库
    @conn：数据库连接对象
    @bdname：切换的数据库名称
    """
    try:
        sql = "show databases"
        cursor = querySql(conn, sql)
        for i in cursor:
            if bdname in i:
                conn.select_db(bdname)
                return conn
        return False
    except Exception, err:
        cursor.close()
        raise err

# 好友表（必须初始化）
sql = "select * from tb_character where id not in (select characterId from tb_friend)"
query = querySql(nconn, sql, dictcursor=True)
for i in query:
    serId = str(i['id'])[:1]  # 数据库后缀
    cId = str(i['id'])[1:]  # 旧角色Id
    ncid = i['id']  # 新角色Id
    dbname = db + serId
    oconn = changeDB(conn, dbname)
    sql = "select * from tb_friend where characterId = '%s'" % (cId)
    result = querySql(oconn, sql, dictcursor=True)
    for ca in result:
        sql = 'insert into tb_friend(`characterId`) values("%s")' % (ncid)
        logger.info(sql + ";")

# tb_qingyuan_play,情缘游玩
sql = "select * from tb_character where id not in (select characterId from tb_qingyuan_play)"
query = querySql(nconn, sql, dictcursor=True)
for i in query:
    serId = str(i['id'])[:1]  # 数据库后缀
    cId = str(i['id'])[1:]  # 旧角色Id
    ncid = i['id']  # 新角色Id
    dbname = db + serId
    oconn = changeDB(conn, dbname)
    sql = "select * from tb_qingyuan_play where characterId = '%s'" % (cId)
    result = querySql(oconn, sql, dictcursor=True)
    if not result:
        sql = 'insert into tb_qingyuan_play(`characterId`) values("%s")' % (ncid)
        logger.info(sql + ";")
    for ca in result:
        sql = 'insert into tb_qingyuan_play(`characterId`,`playtask`,`curdate`) values("%s","%s","%s")' % (ncid, ca['playtask'], ca['curdate'])
        logger.info(sql + ";")
