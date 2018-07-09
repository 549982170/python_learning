# coding=utf-8

import MySQLdb
from DBUtils.PooledDB import PooledDB


def connect(sql, kwargs):
    pool = PooledDB(MySQLdb, 5, **kwargs)
    db = pool.connection()
    cur = db.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    checkContent = 'd538ecf8-8f94-11e6-87ce-14187740b71a'

    '''

    sqlOne = 'select * from ftrack.social_event'
    cur.execute(sqlOne)
    res = cur.fetchall()
    #print res
    '''

    '''
    sqlOne = 'select * from ftrack.show'
    cur.execute(sqlOne)
    res = cur.fetchall()
    for i in res:
        for j in i:
            if checkContent == j:
                print i
    '''

    newList = ['select * from ftrack.%s' % i[0] for i in res]
    count = 0
    for i in newList:
        count += 1
        print count
        print i
        if 'social' in i:
            continue
        cur.execute(i)
        res = cur.fetchall()
        for j in res:
            # print j
            for z in j:
                if checkContent in str(z):
                    print j
                    print "end search"

    '''
    newList = [ 'describe ftrack.%s;' % i[0] for i in res ]
    print len(newList)
    for i in newList:
        print i
        cur.execute(i)
        res = cur.fetchall()
        print res
    '''

    cur.close()  # or del cur
    db.close()  # or del db

    return res


if __name__ == '__main__':
    # 192.168.3.211 影视协作测试数据库
    '''
    kwargs = {
        'db':'soovii_productionplanning_db',
        'host':'192.168.3.211',
        'port':3306,
        'user':'root',
        'passwd':'root'
    }
    '''

    # ftrack

    kwargs = {
        'db': 'ftrack',
        'host': '192.168.3.210',
        'port': 3306,
        'user': 'root',
        'passwd': 'root'
    }

    sql = 'show tables'

    tuples = connect(sql, kwargs)
