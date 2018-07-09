# coding:utf8
'''
Created on 2017-2-8

@author: yizhiwu
'''
from DBUtils.PooledDB import PooledDB
from MySQLdb.cursors import DictCursor
import MySQLdb
import logging

logger = logging.getLogger()

DBCS = {'mysql': MySQLdb, }


class DBPool(object):
    """MYsql连接池"""

    def initPool(self, dbcfg):
        self.config = {}
        self.config = dbcfg
        creator = DBCS.get(dbcfg.get('engine', 'mysql'), MySQLdb)
        self.pool = PooledDB(creator, 5, **dbcfg)

    def connection(self):
        return self.pool.connection()

    def callProc(self, procName):
        try:
            conn = self.connection()
            cursor = conn.cursor()
            count = cursor.execute('call %s' % procName)
            conn.commit()
            cursor.close()
            conn.close()
            if count > 0:
                return True
            return False
        except Exception, err:
            logger.error(err)
            cursor.close()
            conn.close()
            raise err

    def execSql(self, sqlstr):
        '''执行数据库的写操作(插入,修改,删除),自动commit
        @param sqlstr: str 需要执行的sql语句
        '''
        try:
            conn = self.connection()
            cursor = conn.cursor()
            count = cursor.execute(sqlstr)
            conn.commit()
            cursor.close()
            conn.close()
            if count > 0:
                return True
            return False
        except Exception, err:
            logger.error(err)
            cursor.close()
            conn.close()
            raise err

    def execute(self, sqlstrList):
        '''批量处理sql语句并且支持事务回滚,自动commit
        @param sqlstrList: list(str) 需要执行的sql语句list
        '''
        try:
            conn = self.connection()
            cursor = conn.cursor()
            #           conn.autocommit(False)
            for sqlstr in sqlstrList:
                count = cursor.execute(sqlstr)
            conn.commit()
            #           conn.autocommit(True)
            cursor.close()
            conn.close()
            return True
        except Exception, err:
            conn.rollback()
            cursor.close()
            conn.close()
            logger.error(err)
            raise err

    def querySql(self, sqlstr, dictcursor=False):
        '''执行查询并返回所有结果 fetchall'''
        try:
            conn = self.connection()
            if dictcursor:
                cursor = conn.cursor(cursorclass=DictCursor)
            else:
                cursor = conn.cursor()
            cursor.execute(sqlstr)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except Exception, err:
            logger.exception(err)
            cursor.close()
            conn.close()
            raise err

    def querySql2(self, sqlstr, params=None, dictcursor=False):
        '''执行查询并返回所有结果 fetchall'''
        try:
            conn = self.connection()
            if dictcursor:
                cursor = conn.cursor(cursorclass=DictCursor)
            else:
                cursor = conn.cursor()
            cursor.execute(sqlstr, params)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except Exception, err:
            logger.exception(err)
            cursor.close()
            conn.close()
            raise err

    def fetchone(self, sqlstr, dictcursor=False):
        '''获取所有游标对象中的一条数据'''
        try:
            conn = self.connection()
            if dictcursor:
                cursor = conn.cursor(cursorclass=DictCursor)
            else:
                cursor = conn.cursor()
            cursor.execute(sqlstr)
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            return result
        except Exception, err:
            logger.exception(err)
            cursor.close()
            conn.close()
            raise err
